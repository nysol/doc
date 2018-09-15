
.. _common_param:

共通パラメータ
=======================
処理メソッドで指定できるパラメータには、概ね共通した意味で用いられるものが多い。
ただし、メソッドによっては全く異なる意味として実装されているケースもあるので注意されたい。
:numref:`common_param_table` に一覧を示し、続いてその内容について詳述する。

  .. csv-table:: 入力データ例:mcmdが扱う表構造データ
    :header-rows: 1
    :name: common_param_table

    キーワード,内容
    :ref:`i= m=<common_param_i>`,                         入力データの指定
    :ref:`o= u=<common_param_o>`,                         出力データの指定
    :ref:`f=<common_param_f>`,                            入出力項目名の指定
    :ref:`k=<common_param_k>`,                            キー項目名
    :ref:`s=<common_param_s>`,                            並べ替え項目名
    :ref:`q=<common_param_q>`,                            自動並べ替えの無効化
    :ref:`a=<common_param_a>`,                            追加項目名
    :ref:`nfn=<common_param_nfn>`,                        入出力データの1行目を項目名ヘッダとみなさない
    :ref:`nfno=<common_param_nfno>`,                      項目名ヘッダを出力しない
    :ref:`x=<common_param_x>`,                            項目番号による指定
    :ref:`precision=<common_param_precision>`,            有効桁数の変更設定
    :ref:`tmpPath=<common_param_tmpPath>`,                作業ファイル格納パス名
    :ref:`delim=<common_param_delim>`,                    ベクトル型データの区切り文字
    :ref:`bufcount=<common_param_bufcount>`,              キー単位処理のバッファ数
    :ref:`assert_diffSize=<common_param_assert_diffSize>`,入出力件数が異なればwarningを出す
    :ref:`assert_nullkey=<common_param_assert_nullkey>`,  キー項目のNULL値にwarningを出す
    :ref:`assert_nullin=<common_param_assert_nullin>`,    入力項目のNULL値にwarningを出す
    :ref:`assert_nullout=<common_param_assert_nullout>`,  出力項目のNULL値にwarningを出す

.. _common_param_i:

i= m= : 入力データの指定
------------------------------
入力データを指定するパラメータ( ``i=`` と ``m=`` )には、
CSVファイル名、Pythonリスト、処理フローオブジェクトを指定できる。
中には ``mnewrand`` のように入力データを必要としないメソッドもあるが、
``i=`` はほとんどのメソッドで利用できるパラメータであり、
``m=`` は ``mjoin`` など参照データを利用するメソッドにおいて利用される。
いずれの形式であっても、全行で同数の項目数を持っていなければエラーとなる。
``i=`` が省略された時には標準入力からデータを読み込む。
この機能があるために、パイプラインによる接続が可能となる。
例えば、 :numref:`common_param_i_stdin` では、 ``msum`` で ``i=`` を指定していないが、
これは ``mcut`` の結果がパイプラインを介して標準入力としてCSVデータが入力されるためである。

  .. code-block:: python
    :linenos:
    :caption: i=を省いた場合は標準入力から読み込む
    :name: common_param_i_stdin

    import nysol.mcmd as nm
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ]

    f=nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount")
    print(f.run())
    # [['A', '15600'], ['B', '2400']]


入力データの複数指定
'''''''''''''''''''''''''

入力データを複数指定することもでき、その場合は、それらのデータが全て併合される。
これは、実行時に ``m2cat`` を自動的に付加することによって実現している。
さらに入力側に接続されたメソッドからの標準入力も併合対象になる。
複数指定したいずれのデータも項目名が同一でなければならない。
サンプルコードを :numref:`common_param_i_multi` に示す。

.. code-block:: python
  :linenos:
  :caption: i=に複数データを指定する例
  :name: common_param_i_multi

  import nysol.mcmd as nm

  dat=[
  ["customer","amount"],
  ["A",100],
  ["B",300],
  ]

  # datを3つのCSVファイルに出力
  nm.m2cat(i=dat,o="dat1.csv").run()
  nm.m2cat(i=dat,o="dat2.csv").run()
  nm.m2cat(i=dat,o="dat3.csv").run()

  # Pythonリストを複数利用する場合の一つの方法は、Python上で統合した上でmcut nfni=Trueを指定して読み込む
  dat1=dat2=dat3=dat[1:] # 項目名ヘッダを省いたPythonリスト
  f=None
  f <<= nm.mcut(f="0:customer,1:amount",i=(dat1+dat2+dat3),nfni=True)
  f <<= nm.msum(k="customer",f="amount")
  print(f.run())
  # [['A', '300'], ['B', '900']]

  # CSVファイルを複数指定する例
  f=None
  f <<= nm.mcut(f="customer,amount",i=["dat1.csv","dat2.csv","dat3.csv"])
  f <<= nm.msum(k="customer",f="amount")
  print(f.run())
  # [['A', '300'], ['B', '900']]

  # 処理フローオブジェクトを複数指定することも可能(ここでは簡単のため同じデータdatを使っている)
  f1=nm.mcut(f="customer,amount",i=dat)
  f2=nm.mcut(f="customer,amount",i=dat)
  f3=nm.mcut(f="customer,amount",i=dat)
  f=nm.msum(k="customer",f="amount",i=[f1,f2,f3])
  print(f.run())
  # [['A', '300'], ['B', '900']]

  # Pythonリスト、CSV、処理フローオブジェクトを混在させることも可能
  f=nm.msum(k="customer",f="amount",i=[dat,f1,"dat1.csv"])
  print(f.run())
  # [['A', '300'], ['B', '900']]

  # mcutからの標準入力も併合可能
  f=None
  f=nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount",i=["dat1.csv",dat])
  print(f.run())
  # [['A', '300'], ['B', '900']]

.. _common_param_o:

o= u= : 出力データの指定
------------------------------
出力データを指定するパラメータ( ``o=`` と ``u=`` )には、
CSVファイル名、Pythonリストを指定できる。
中には ``msep`` のように ``o=`` を指定しないメソッドもあるが、
``o=`` はほとんどのメソッドで利用できるパラメータであり、
``u=`` は ``mselstr`` など行を選択するメソッドにおいて、
条件にアンマッチの行を出力するデータとして用いられる。
``o=`` が省略された時には標準出力にデータを書き込む。
この機能があるために、パイプラインによる接続が可能となる。
例えば、 :numref:`common_param_o_stdout` では、 ``mcut`` で ``o=`` を指定していないが、
これは ``mcut`` の結果がパイプラインを介して標準出力としてCSVデータが ``msum`` に出力されるためである。

  .. code-block:: python
    :linenos:
    :caption: i=を省いた場合は標準入力から読み込む
    :name: common_param_o_stdout

    import nysol.mcmd as nm
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ]

    f=nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount")
    print(f.run())
    # [['A', '15600'], ['B', '2400']]


:numref:`common_param_o_exp` に利用例をいくつか示す。
CSVファイルに出力するには、 ``o=`` にファイル名を与えればよい。
リストに出力する時は、 ``o=`` に空のリストを与えればよい。
ただし、追記になるので、リストが空でなければ追記されていく。
さらに、項目数などフォーマットが異なっていても追記できるので、扱いには注意が必要である。

  .. code-block:: python
    :linenos:
    :caption: o=の利用例
    :name: common_param_o_exp

    import nysol.mcmd as nm

    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ]
    # o=に空のリストを与えると、そこに結果が出力(追記)される。ただし、項目名は出力されない。
    result=[]
    nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount",o=result).run()
    print(result)
    # [['A', '5200'], ['B', '800']]

    # 追記なので、同じことをもう一度すると、上の結果に追記される。
    nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount",o=result).run()
    print(result)
    # [['A', '5200'], ['B', '800'], ['A', '5200'], ['B', '800']]

    # さらに、項目数が異なっていても追記してしまうので、扱いには注意が必要である。
    nm.mcut(f="customer,date,amount",i=dat).msum(k="customer",f="amount",o=result).run()
    print(result)
    # [['A', '5200'], ['B', '800'], ['A', '5200'], ['B', '800'], ['A', '20180101', '5200'], ['B', '20180101', '800']]

    # o=を省略すると、結果をリストで返す。追記とはならない。
    result=nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount").run()
    print(result)
    # [['A', '5200'], ['B', '800']]

    # o=に文字列を与えるとCSVファイル名とみなし、ファイル出力される。項目名も出力される。
    nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount",o="result.csv").run()
    print(result)
    # result.csvの内容
    # customer%0,amount
    # A,5200
    # B,800

.. _common_param_f:

f= : 入出力項目名の指定
------------------------------
処理対象となる入力項目名の指定をおこなう。
例えば、mcut においては「選択される項目名」、
magg においては 「集計される項目名」、
mjoin においては「結合される項目名」を指定する。
また複数の項目名は、 ``f="a,b,c"`` のようにカンマで区切って指定する。
さらに、mcut、msum、mjoinのように指定された項目毎に出力項目名を指定できるメソッドもある。
出力項目名は、 ``f="a:A,b:B"`` のように、入力項目名の後にコロンで区切って指定する。
出力項目名が省略されたときは、入力項目名と同じ項目名が利用される。
その利用例を :numref:`common_param_f_exp` に示す。

  .. code-block:: python
    :linenos:
    :caption: f=の利用例
    :name: common_param_f_exp

    import nysol.mcmd as nm
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ]
    # msumの集計項目の名称をamountからtotalに変更して実行。
    result=nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount:total",o="result.csv").run()
    # result.csvの内容
    # customer%0,total
    # A,5200
    # B,800

.. _common_param_k:

k= : キー項目の指定
------------------------------
キー項目を指定する(複数項目指定可)。
キー項目とは、集計の単位として指定したり、またファイルの結合時に2ファイル間の共通項目として指定する項目である。
例えば、msum では、同一キーごとに合計処理をおこなう(集計キーブレイク処理)。
また mjoin では、2 つのデータファイルについて、キー項目の大小を見比べて結合処理を実施する(結合キーブレイク処理)。
k=パラメータが指定されたとき、多くのメソッドでは、その項目を文字列昇順で並べ替えた上で、
それぞれの処理を実行する。
並べ替え処理は、実行時に自動追加される(「 :doc:`autoadd` 」節参照)。
ただし、入力データがk=で指定した項目で既に並べ変わっている時は、並べ替えは実行されない(必要ない)。
また、mhashsum メソッドのように、アルゴリズムの性質から ``k=`` を指定しても
並べ替えを行わない例外的なメソッドもある。
なおキーブレイク処理については、 :ref:`後述<common_keybreak>` するが、
項目の並べ替えが頻繁に発生するとパフォーマンスの低下を招くため、
キーブレイク処理の内容と必要性を理解した上で、並べ替えの回数を少なくするスクリプトを記述することが望ましい。
:numref:`common_param_k_exp` に集計キーブレイク処理の例としてmsumを、
そして結合キーブレイク処理の例として mjoinの例を示す。
なお、出力されたCSVデータの項目ヘッダの%に続く特殊記号の意味は「 :doc:`項目名ヘッダー<field>`  」の節を参照されたい。

  .. code-block:: python
    :linenos:
    :caption: k=の利用例
    :name: common_param_k_exp

    import nysol.mcmd as nm

    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800]
    ]

    cust=[
    ["customer","gender","age"],
    ["A","female",49],
    ["B","male",25]
    ]

    # 集計キーブレイク処理の例
    # customer別にamountを合計する処理。
    # バックでcustomer項目が並べ替えられてからamount項目の合計処理が行われる。
    nm.msum(k="customer",f="amount",i=dat,o="result.csv").run()
    # customer%0,date,amount
    # A,20180101,5200
    # B,20180101,800


    # 結合キーブレイク処理の例
    # customer項目をキーにgender,age項目を結合する処理。
    # バックでdatとcustの両データがcustomer項目で並べ替えられてから結合処理が行われる。
    nm.mjoin(k="customer",m=cust,f="gender,age",i=dat,o="result.csv").run()
    # customer%0,date,amount,gender,age
    # A,20180101,5200,female,49
    # B,20180101,800,male,25

.. _common_keybreak:

キーブレイク処理
''''''''''''''''''''''
**キーブレイク処理** とは、その項目が並べ換わっていることを前提として、
同一のキー項目値毎に一定の処理を行う処理方式のことを言う。
キーブレイク処理は大きく分けて 2 つの処理に分けられる。
一つは集計のためのキーブレイク処理 (「 **集計キーブレイク処理** 」と呼ぶ) で、
他方は結合のためのキーブレイク処理 (「 **結合キーブレイク処理** 」と呼ぶ) である。
mjoin、mcommon のようにメソッド名に「join」もしくは「common」を含むメソッドが結合キーブレイク処理を、
それ以外の k=パラメータを指定できるメソッドの多くは集計キーブレイク処理を行っていると考えてよい。

たとえば集計キーブレイク処理を行う msum メソッドでは、キー項目の値の変化を検知することで、
同一キー毎に合計処理を実行する。
そのためには事前にキー項目で行を並べ替える(文字列昇順)必要があるので、
合計処理を行う前に、並べ替え処理が実行される(自動追加されるのでユーザは並べ替えを気にする必要はない)。

結合キーブレイク処理はもう少し複雑で、たとえば mjoin メソッドは、2 つのデータについて、
キー項目の大小を見比べる。
キー項目が小さいデータは読み進め、キー項目値が同じであれば結合処理を実施する。
この ようにキー項目値の大小比較をしているため、結合のためのキーブレイク処理においては、
事前に 2 つのデータともキー項目で並べ替えられていることが前提となる。
そのため mjoin は、 ``i=`` と ``m=`` で指定されたデータをそれぞれキー項目で並べ替える。
また、mrjoin のような数値範囲による結合キーブレイク処理においては、数値昇順で並べ替えを行う。

キーブレイク処理を伴うメソッドでは、k=で項目を指定するだけで、
裏で並べ替えをの要否を判断し、必要な場合は並べ替えを実行してくれる。
そのため、ユーザは原則としての並べ替えを意識する必要はない。
ただ並べ替え処理が不要になったわけではなく、
各メソッドが内部的に並べ替え処理を行っているという点に注意が必要である。
スクリプトの構成によっては、並 替え処理が頻繁に発生し、パフォーマンス低下の原因となる。
このことを示す例を :numref:`common_keybreak_exp` に示している。
この例では、datに2つの表(custとinvoice)を結合し、``customer`` 別に ``amount`` を合計する処理である。
そして、2つのmjoinの順序を入れ替えるだけで、ソートの回数が1回減ることを示している。

  .. code-block:: python
    :linenos:
    :caption: k=の利用例
    :name: common_keybreak_exp

    import os
    import nysol.mcmd as nm

    dat=[
    ["customer","invoice"],
    ["A","01001"],
    ["A","01005"],
    ["B","01003"],
    ["B","01010"]
    ]

    invoice=[
    ["invoice","amount"],
    ["01001",1800],
    ["01005",200],
    ["01003",100],
    ["01010",800]
    ]

    cust=[
    ["customer","gender","age"],
    ["A","female",49],
    ["B","male",25]
    ]

    # この順番で処理すると、裏でソートが3回実行されることになる。
    f=None
    f <<= nm.mjoin(k="customer",m=cust,f="gender,age",i=dat)
    f <<= nm.mjoin(k="invoice",m=invoice,f="amount")
    f <<= nm.msum(k="customer",f="amount",o="result.csv")
    f.run()
    # result.csvの内容
    # customer%0,invoice,gender,age,amount
    # A,01005,female,49,2000
    # B,01010,male,25,900

    # mjoinを入れ替えると、msumでcustomer順に並べ替える必要がなくなり、ソートは2回に減る。
    f=None
    f <<= nm.mjoin(k="invoice",m=invoice,f="amount",i=dat)
    f <<= nm.mjoin(k="customer",m=cust,f="gender,age")
    f <<= nm.msum(k="customer",f="amount",o="result.csv")
    f.run()
    # result.csvの内容
    # customer%0,date,amount,gender,age
    # A,20180101,5200,female,49
    # B,20180101,800,male,25

:numref:`common_keybreak_exp` の例は、実行順を入れ替えるだけでパフォーマンスを改善できることを示すものである。
処理フロー全体を調べれば、このような改善(最適化)は自動的に行える可能性があるが、
現在のところ実装はされておらず、将来の課題としたい。

.. _common_param_s:

s= : 並べ替え項目の指定
------------------------------
maccum などいくつかのメソッドは、行(レコード)の順序が処理結果に影響を与える。
s=パラメータを指定すると、そのメソッドの実行前に指定の項目で行を並べ替え処理を実行する。
項目の並べ替え方法(並び順)は、数値/文字列、昇順/降順の組み合わせで 4 通り指定できる。
指定方法は、項目名 のあと % に続けて n と r を以下の通り組み合わせる。

* 文字列昇順: s=項目名 (% 指定なし)
* 文字列逆順: s=項目名%r
* 数値昇順: s=項目名%n
* 数値降順: s=項目名%nr

なお、k=とs=の両方を指定した場合は、k=の項目を優先して並べる。
また、並べ替え項目を複数指定することも可能である。
:numref:`common_param_s_exp` にs=の利用例を示している。
なお、出力されたCSVデータの項目ヘッダの%に続く特殊記号の意味は「 :doc:`項目名ヘッダー<field>`  」の節を参照されたい。

  .. code-block:: python
    :linenos:
    :caption: s=の利用例
    :name: common_param_s_exp

    import nysol.mcmd as nm

    dat=[
    ["customer","receiptNo","val"],
    ["A","1",1],
    ["B","2",2],
    ["A","10",3],
    ["B","9",4]
    ]

    # receiptNoを文字列昇順に並べて累計を計算する。
    nm.maccum(s="receiptNo",f="val:accum",i=dat,o="result.csv").run()
    # result.csvの内容
    # customer,receiptNo%0,val,accum
    # A,1,1,1
    # A,10,3,4
    # B,2,2,6
    # B,9,4,10

    # receiptNoを数値昇順に並べるとaccumの結果も変わってくる。
    nm.maccum(s="receiptNo%n",f="val:accum",i=dat,o="result.csv").run()
    # result.csvの内容
    # customer,receiptNo%0n,val,accum
    # A,1,1,1
    # B,2,2,3
    # B,9,4,7
    # A,10,3,10

    # k=も指定すると、その項目(customer)が優先して並べ替えられる。
    nm.maccum(k="customer",s="receiptNo",f="val:accum",i=dat,o="result.csv").run()
    # result.csvの内容
    # customer%0,receiptNo%1,val,accum
    # A,1,1,1
    # A,10,3,4
    # B,2,2,2
    # B,9,4,6

**対象メソッド**

:doc:`maccum<methods/maccum>` ,
:doc:`mbest<methods/mbest>` ,
:doc:`mmvavg<methods/mmvavg>` ,
:doc:`mnumber<methods/mnumber>` ,
:doc:`mslide<methods/mslide>` など

.. _common_param_q:

q= : 自動並べ替えの無効化
------------------------------
k=で指定した項目による自動並べ替えを無効にしたい場合にこのオプションを用いる。
またs=が必要なメソッドでq=を指定するとs=を省略可能となる。
s=を指定したとしてもソートは実行されない。
:numref:`common_param_q_exp` に利用例を示す。
k=で指定された ``customer`` 項目の値に変化のあった時に集計(合計)がおこなわれるため、
入力データの1行目、2,3行目、そして4行目の3ブロックが集計単位となる。

  .. code-block:: python
    :linenos:
    :caption: q=の利用例
    :name: common_param_q_exp

    import nysol.mcmd as nm

    dat=[
    ["customer","quantity"],
    ["A",1],
    ["B",2],
    ["B",3],
    ["A",4]
    ]

    # q=Trueを指定すると、自動ソーティングは実行されず、入力データの順序でキーブレイク集計(合計)が計算される。
    nm.msum(q=True,k="customer",f="quantity",i=dat,o="result.csv").run()
    # result.csvの内容
    # customer,quantity
    # A,1
    # B,5
    # A,4

.. _common_param_a:

a= : 追加項目の指定
------------------------------
新たに項目を追加するようなメソッドにおいて、その項目名を指定する。
多くのメソッドは、追加する項目は一つであるため、ここで指定する項目名も一つであることが多い。
中には、 :doc:`mcombi<methods/mcombi>` や :doc:`msetstr<methods/msetstr>`
のように複数の項目を出力するものもあるが、
その際はカンマで区切って複数の項目名を指定する。
:numref:`common_param_a_exp` に利用例を示す。

  .. code-block:: python
    :linenos:
    :caption: a=の利用例
    :name: common_param_a_exp

    import nysol.mcmd as nm

    dat=[
    ["customer","quantity","amount"],
    ["A",1,100],
    ["B",2,50],
    ["B",3,200],
    ["A",4,99]
    ]

    # quantityとamountを掛け算した結果を total 項目として追加している。
    nm.mcal(c='${quantity}*${amount}',a="total",i=dat,o="result.csv").run()
    # result.csvの内容
    # customer,quantity,amount,total
    # A,1,100,100
    # B,2,50,100
    # B,3,200,600
    # A,4,99,396

    # 本日の日付と曜日を全行にセットし、date と dow の2項目を追加出力している。
    nm.msetstr(v="20180913,thursday",a="date,dow",i=dat,o="result.csv").run()
    # result.csvの内容
    # customer,quantity,amount,date,dow
    # A,1,100,20180913,thursday
    # B,2,50,20180913,thursday
    # B,3,200,20180913,thursday
    # A,4,99,20180913,thursday


.. _common_param_nfn:

nfn= : 1行目を項目名ヘッダとみなさない
---------------------------------------------------------
このオプションを指定すると入力データの 1 行目を項目名行とみなさず、
また出力データにも項目名を出力しない。
主に1行目に項目名がないデータの場合に利用される。
このオプションを指定すると項目指定で項目名は利用できないので項目番号指定をすることになる。
項目番号は 0 から始まる整数で指定することに注意する。
項目番号の指定方法の詳細は「 :doc:`field` 」を参照されたい。
また、自動ソートの機能は全く働かなくなるため、
:ref:`k=<common_param_k>` や :ref:`s=<common_param_s>` を必要とするメソッドの実行においては、
実行前に明示的に :doc:`msortf<methods/msortf>` でソーティングを実行する必要がある。
自動ソートは、項目名ヘッダにその情報を記録しており、その情報が使えなくなるからである。
よって、k=やs=を必要とするメソッドを明示的にソーティングせずに実行すれば、
:ref:`q=True<common_param_q>` を指定して実行した結果と同等になる。
:numref:`common_param_nfn_exp` に利用例を示す。

  .. code-block:: python
    :linenos:
    :caption: nfn=の利用例
    :name: common_param_nfn_exp

    import nysol.mcmd as nm

    dat=[
    ["A",1,100],
    ["B",2,50],
    ["B",3,200],
    ["A",4,99]
    ]

    # 入力データに項目名ヘッダのないので、nfn=Trueを指定し、項目を番号で指定している。
    nm.mcut(nfn=True,f="0,2",i=dat).msum(nfn=True,k="0",f="1",o="result.csv").run()
    # result.csvの内容
    # A,100
    # B,250
    # A,99

.. _common_param_nfno:

nfno= : 項目名ヘッダを出力しない
-----------------------------------
このオプションを指定すると出力データに項目名行を出力しない。
:ref:`nfn=True<common_param_nfn>` とは違い、
i=やm=で指定される入力データは項目名ヘッダを伴うデータであることを前提としており、
:ref:`f=<common_param_f>` や :ref:`k=<common_param_k>` などによる項目の指定は項目名で行う。
よって、自動ソートも機能する。
ただし、 ``f=iName:oName`` のように出力項目名を指定しても無効になる。
出力を処理メソッドで接続していった場合、それ以降は自動ソートは無効になる。
ちなみに、入力側のみ項目名ヘッダを想定しない ``nfni=True`` は
:doc:`mcut<methods/mcut>` でのみ利用可能なオプションである。
:numref:`common_param_nfno_exp` に ``nfno=True`` の利用例を示す。

  .. code-block:: python
    :linenos:
    :caption: nfno=の利用例
    :name: common_param_nfno_exp

    import nysol.mcmd as nm

    dat=[
    ["customer","amount"],
    ["A",100],
    ["B",50],
    ["B",200],
    ["A",99]
    ]

    # 入力項目は名前で指定するが、出力には項目名ヘッダは出力されない。
    nm.msum(nfno=True,k="customer",f="amount",i=dat,o="result.csv").run()
    # A,199
    # B,250

.. _common_param_x:

x= : 項目番号による指定
------------------------------
項目名ヘッダを伴う入力データに対して項目番号によって項目を指定したい場合にこのオプションを用いる。
コロンで区切って出力項目名を指定することも可能である。
また項目名ヘッダを伴うために自動ソートも機能する。
:numref:`common_param_x_exp` に利用例を示す。

  .. code-block:: python
    :linenos:
    :caption: x=の利用例
    :name: common_param_x_exp

    import nysol.mcmd as nm

    dat=[
    ["customer","amount"],
    ["A",100],
    ["B",50],
    ["B",200],
    ["A",99]
    ]

    # 0番目(customer)項目をキーに1番目項目(amount)の合計を計算する。
    nm.msum(x=True,k="0",f="1",i=dat,o="result.csv").run()
    # result.csvの内容 (項目名ヘッダのソーティング情報も正しく出力される)
    # customer%0,amount
    # A,199
    # B,250

    # 出力項目名の変更も可能で、集計項目を total に変更している。
    nm.msum(x=True,k="0",f="1:total",i=dat,o="result.csv").run()
    # result.csvの内容
    # customer%0,total
    # A,199
    # B,250

.. _common_param_precision:

precision=
------------------------------
浮動小数点を扱うメソッド(msumやmavgなど)の内部で、結果をテキストで出力する際に、
C 言語におけるsprintfの書式 "%. ``有効桁数`` g" を用いている。
この書式は、データの桁数と指定した ``有効桁数`` によって、
標準標記 (整数部.小数部: ex. 123.456) と、
指数表記 (仮数部 e± 指数部: ex. 1.23456e+02) を切り替える。
切り替えの基準であるが、データを指数表記で表したときに、指数部が指定の有効桁数を超えるか、
もしくは-5 以下の場合 (すなわち、小数点以下に 0 が 4 つ以上続く場合) に指数表記を採用する。
``有効桁数`` は 1から16 の整数が指定可能で、デフォルトは 10 である。
n < 1 の場合は n = 1 にセットされ、n > 16 の場合は n = 16 にセットされる。
また、環境変数 KG_Precision を設定することでも有効桁数を変更できる。
ただし、環境変数を変更すると、それ 以降に実行するコマンド全てに反映されることに注意する。
:numref:`common_param_precision_exp` に利用例を示す。
id=1 は指数表現で 1.2345678e+08 であり、指数部が有効桁数 6 を超えているので指数表記となり、
仮数部の有効桁数が 6 となっている。
id=2 は指数表現で 1.23456789e+03 であり、指数部が有効桁数 7 を超えていないので標準標記 となり、
整数部 + 小数部の桁数が 6 となっている。
id=4 は指数表現で 1.23456789e-04 であり、指数部が-4 未満では ないので標準標記となり、
有効桁数が 6 となっている。
id=5 は指数表現で 1.23456789e-05 であり、指数部が-4 未満 となるため指数表記となり、
仮数部の有効桁数が 6 となっている。

また、環境変数を ``KG_Precision='2'`` で指定して実行した例では、
mcalの出力結果項目でない ``val`` 項目も有効桁数が2桁になっている。
これは、Pythonリスト ``dat`` の ``val`` 項目の値がPythonの浮動小数点で入力されており、
それをテキストに変換する時にも環境変数の有効桁数の設定が影響するためである。
なお、この変換は、実行時に自動追加される :ref:`readlist <autoadd_io>` メソッドが行っている。

  .. code-block:: python
    :linenos:
    :caption: precision=の利用例
    :name: common_param_precision_exp

    import nysol.mcmd as nm

    dat=[
    ["id","val"],
    [1,123456789],
    [2,1234.56789],
    [3,0.123456789],
    [4,0.000123456789],
    [5,0.0000123456789]
    ]

    # val項目の内容を有効桁数6桁で表示する。
    nm.mcal(c="${val}", a="result", precision=6, i=dat, o="result.csv").run()
    # result.csvの内容
    # id,val,result
    # 1,123456789,1.23457e+08
    # 2,1234.56789,1234.57
    # 3,0.123456789,0.123457
    # 4,0.000123456789,0.000123457
    # 5,1.23456789e-05,1.23457e-05

    # 環境変数で有効桁数2桁に設定した場合の例。
    os.environ['KG_Precision'] = '2' 
    nm.mcal(c="${val}", a="result", i=dat, o="result.csv").run()
    # result.csvの内容
    # id,val,result
    # 1,1.2e+08,1.2e+08
    # 2,1.2e+03,1200
    # 3,0.12,0.12
    # 4,0.00012,0.00012
    # 5,1.2e-05,1.2e-05

.. _common_param_tmpPath:

tmpPath=
------------------------------
処理メソッドが内部で用いる作業ファイルを格納するディレクトリ名を指定する。
例えば、msortf は巨大なデータについては分割ソートを用いるが、その一時ファイルとして保存される。
それ以外にも、キー項目の単位が大きくなった場合、キーブレイク処理で一時ファイルが用いられることもある。
また、 処理フローが分岐する際に自動挿入される :doc:`mfifo<methods/mfifo>` の内部バッファでも
一時ファイルが用いられることがある。
一時ファイルの出力ディレクトリは、指定がなければデフォルトとして/tmp が用いられる。
一時ファイルを格納するディレクトリは読み書き可能な状態で存在する必要がある。
一時ファイルは、必ず ``__KGTMP`` から始まるファイル名が用いられる。

作業ファイルは、正常に終了すれば (エラー終了も含めて mcmd のコントロール下で正常に終了するという意味) 
削除されるが、不測の事態(例えば、バグ終了の場合)には、消されず残る場合がある。
データ量によっては、非常に多くの作業ファイルが生成される可能性があり (100 万ファイル以上!!)、
その場合は、次に一時ファイルを利用する処理メソッドの動作が極端に遅くなる可能性がある(
100万ファイルあるディレクトリを ``ls`` したときの遅さを想像してみればよい)。
現在のところ、これらの不要ファイ ルの自動消去 (ガベージコレクション) の機能は実装しておらず、
定期的に作業パスのファイルを確認しておくべきである。
なお、/tmpディレクトリは、一般的にはosを再起動すればクリアされる。

また、環境変数 KG_Tmp_Path を設定することで、作業ディレクトリを変更できる。
ただし、環境変数を変更すると、それ以降に実行する処理メソッド全てに反映されることに注意する。
:numref:`common_param_tmpPath_exp` に利用例を示す。

  .. code-block:: python
    :linenos:
    :caption: tmpPath=の利用例
    :name: common_param_tmpPath_exp

    import nysol.mcmd as nm
    # カレントパスのtmp以下に一時ファイルが作られる。
    # 処理が正常に終了すれば、全ての一時ファイルは自動的に消去される。
    nm.msum(k="customer",f="amount",i=dat,tmpPath="./tmp").run()

    # 同じことは、環境変数を設定することでも可能である。
    os.environ['KG_Tmp_Path'] = './tmp' 
    nm.msum(k="customer",f="amount",i=dat).run()

.. _common_param_delim:

delim= : ベクトル型データの区切り文字
--------------------------------------------
:doc:`mvcount<methods/mvcount>` などの処理メソッドが扱うベクトル型データについて、要素の区切り文字を指定する。
デフォルトは半角スペースである。
CSV の区切り文字であるカンマを指定することもできるが、ベクトルの区切り文字と区別するために
ベクトル全体がダブルクオーテーションで囲われる。
:numref:`common_param_delim_exp` に利用例を示す。

  .. code-block:: python
    :linenos:
    :caption: delim=の利用例
    :name: common_param_delim_exp

    import nysol.mcmd as nm

    dat=[
    ["vec"],
    ["b:a:c"],
    ["x:p"]
    ]

    # val項目の内容を有効桁数6桁で表示する。
    nm.mvsort(vf="vec",delim=":",i=dat,o="result.csv").run()
    os.system("cat result.csv")
    # result.csvの内容
    # vec
    # a:b:c
    # p:x

    # delim を指定していないので b:a:c や x:p は一つの要素として解釈される。
    nm.mvsort(vf="vec",i=dat,o="rsult.csv").run()
    os.system("cat result.csv")
    # result.csvの内容
    # vec
    # a:b:c
    # p:x

    dat=[
    ["vec1","vec2"],
    ["a","b"],
    ["p","q"]
    ]
    # 区切り文字をカンマにした場合は、ベクトル全体がダブルクオーテーションで囲われることで CSV の区切り文字との区別がつけられる。
    nm.mvcat(vf="vec1,vec2", a="vec3", delim=",", i=dat, o="result.csv").run()
    os.system("cat result.csv")
    # vec3
    # "a,b"
    # "p,q"

.. _common_param_bufcount:

bufcount= : キー単位処理のバッファ数
-----------------------------------------------
:doc:`mbucket<methods/mbucket>` , :doc:`mnjoin<methods/mnjoin>` , :doc:`mshare<methods/mshare>` など、
キーブレイク処理において、データを複数パス走査する必要のあるコマンドにおいて利用する内部バッファの数
(ブロック数) を指定する。
一つのバッファは 4MB で、デフォルトでは 10 ブロック (40MB) である。
データがバッファに収まらない場合は一時ファイルに書き出されるため、
キーのサイズが非常に大きい場合は、メモリに余裕があれば、
このパラメータを調整することで処理速度の向上が期待できる。
:numref:`common_param_bufcount_exp` に利用例を示す。

  .. code-block:: python
    :linenos:
    :caption: bufcount=の利用例
    :name: common_param_bufcount_exp

    import nysol.mcmd as nm
    # 参照ファイルのキーサイズが 80MB(4MB × 20) 以内であれば、一時ファイルは使われない。
    nm.mnjoin(k="id", m=ref, f="name", i=dat, o="result.csv", bufcount=20).run()

.. _common_param_assert_diffSize:

assert_diffSize= : 入出力件数が異なればwarningを出す
----------------------------------------------------------------
このパラメータを指定すると、指定した処理メソッドの入力ファイルと出力ファイルの件数の比較を行い、
入力ファイルと出力ファイルの件数 が異なる場合に、「#WARNING# ; the number of lines is different」
というメッセージを表示する。

例えば、mjoin(参照ファイルの項目結合)を利用する際に、
入力ファイルのキー項目(k=パラメータで指定する項目)と
参照ファイルのキー項目(K=パラメータで指定する項目)が
完全に一致しているかどうかを確認したい場合を想定してみよう。
mjoin で 外部結合で NULL 値を出力する ``n=True`` オプションを指定しない場合は、
入力ファイルと参 照ファイルで共通のキー項目のみが結合され、
一致しないキー項目の値は除外される為、入力データと出力データの件数が異なってくる。
その際、 ``assert_diffSize=True`` を指定しておくと、入力ファイルと出力ファイルの件数の比較を行い、
入力ファイルと出力ファイルの件数が異なる場合にwarningを出してくれる。
そのため入力ファイルと参照ファイルのキー項目が完全に一致していないことを確認することができる。
:numref:`common_param_diffSize_exp` にそのような例を示す。

  .. code-block:: python
    :linenos:
    :caption: assert_diffSize=の利用例
    :name: common_param_diffSize_exp

    import nysol.mcmd as nm

    dat=[
    ["item","date","price"],
    ["A","20081201",100],
    ["A","20081213",98],
    ["B","20081002",400],
    ["B","20081209",450],
    ["C","20081201",100]
    ]
    ref=[
    ["item","cost"],
    ["A",50],
    ["B",300],
    ["E",200]
    ]

    # datにrefのcost項目を結合する。しかしdatのキーであるCがref側には無いため、出力が1件少なくなりwarningがでる。
    nm.mjoin(assert_diffSize=True,k="item",f="cost",m=ref,i=dat,o="result.csv").run()
    #WARNING# ; the number of lines is different; 2018/09/13 15:57:49
    os.system("cat result.csv")
    # result.csvの内容
    # item%0,date,price,cost
    # A,20081201,100,50
    # A,20081213,98,50
    # B,20081002,400,300
    # B,20081209,450,300

.. _common_param_assert_nullkey:

assert_nullkey= : キー項目のNULL値にwarningを出す
------------------------------------------------------------
このパラメータを指定すると、キー項目 (k=または K=パラメータで指定する項目)にNULL値が
含まれているかどうかのチェックを行い、NULL 値が含まれていた場合に、
「#WARNING# ; exist NULL in key filed」という メッセージを表示する。
:numref:`common_param_nullkey_exp` に例を示す。

  .. code-block:: python
    :linenos:
    :caption: assert_nullkey=の利用例
    :name: common_param_nullkey_exp

    import nysol.mcmd as nm

    dat=[
    ["item","price"],
    ["A",100],
    [None,98],
    ["B",400],
    ["B",450],
    ["C",100]
    ]

    # 集計キーitemの2行目にnull値があるので、警告を出してくれている。
    nm.msum(assert_nullkey=True,k="item",f="price",i=dat,o="result.csv").run()
    #WARNING# ; exist NULL in key filed; 2018/09/13 16:07:30
    os.system("cat result.csv")
    # result.csvの内容
    # item%0,price
    # ,98
    # A,100
    # B,850
    # C,100

.. _common_param_assert_nullin:

assert_nullin= : 入力項目のNULL値にwarningを出す
-----------------------------------------------------
このパラメータを指定すると、f=またはvf=で指定された入力項目にNULL値が含まれているかどうかのチェックを行い、
NULL 値が含まれていた場合に、「#WARNING# ; exist NULL in input data」というメッセージを表示する。
f=などのパラメータで指定していない項目にNULL値があっても警告は出さない。
:numref:`common_param_nullin_exp` に例を示す。

  .. code-block:: python
    :linenos:
    :caption: assert_nullin=の利用例
    :name: common_param_nullin_exp

    import nysol.mcmd as nm

    dat=[
    ["item","price"],
    ["A",100],
    ["A",None],
    ["B",400],
    ["B",450],
    ["C",100]
    ]

    # 集計項目priceの2行目にnull値があるので、警告を出してくれている。
    # msumではnull値は無視して合計処理を行うので結果は問題ない。
    nm.msum(assert_nullin=True,k="item",f="price",i=dat,o="result.csv").run()
    #WARNING# ; exist NULL in input data; 2018/09/13 16:12:25
    os.system("cat result.csv")
    # result.csvの内容
    # item%0,price
    # A,100
    # B,850
    # C,100

.. _common_param_assert_nullout:

assert_nullout= : 出力項目のNULL値にwarningを出す
------------------------------------------------------------------
このパラメータを指定すると、出力項目に NULL 値が含まれているかどうかのチェックを行い、
NULL 値が含まれ ていた場合に、「#WARNING# ; exist NULL in output data」というメッセージを表示する。
ただし、計算項目など、入力データがそのまま出力されるものについてはチェックを行わない。
:numref:`common_param_nullout_exp` に例を示す。

  .. code-block:: python
    :linenos:
    :caption: assert_nullout=の利用例
    :name: common_param_nullout_exp

    import nysol.mcmd as nm

    dat=[
    ["item","date","quantity"],
    ["A","20180801",10],
    ["A","20180805",12],
    ["B","20180701",3],
    ["B","20180822",44],
    ["B","20180901",25]
    ]

    # 集計項目priceの2行目にnull値があるので、警告を出してくれている。
    nm.mslide(assert_nullout=True,k="item",s="date",f="quantity:nextQtty",i=dat,o="result.csv",n=True).run()
    #WARNING# ; exist NULL in output data; 2018/09/13 16:24:16
    os.system("cat result.csv")
    # result.csvの内容
    # item%0,date%1,quantity,nextQtty
    # A,20180801,10,12
    # A,20180805,12,
    # B,20180701,3,44
    # B,20180822,44,25
    # B,20180901,25,




