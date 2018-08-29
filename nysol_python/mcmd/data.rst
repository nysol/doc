
データ
=========================

mcmdが扱えるデータは、 :numref:`data_table` に示されるような項目名ヘッダー付きの表構造データである。
mcmdが提供する処理メソッドの多くは、 ``i=`` で入力データを指定し、 ``o=`` で出力データを指定する。
これらのパラメータに指定できる表構造データは、現在のところ、CSVデータファイル名もしくはPython Listsのいずれかである。
入力については、処理フローオブジェクトも指定できるが、それはデータフローの接続のためであり、
詳しくは :doc:`別節<flow>` にて解説している。

  .. csv-table:: 入力データ例:mcmdが扱う表構造データ
    :name: data_table

    customer,date,amount
    A,20180101,5200
    B,20180101,800
    B,20180112,3500
    A,20180105,2000
    B,20180107,4000

 
リスト(Python Lists)
---------------------
:numref:`data_list` は :numref:`data_table` をリストで表現したPythonコードである。
二重リストになっており、最初の要素は項目名ヘッダーで、続いてデータが1行を1要素として格納されている。
行あたりの項目数は全行で同じでなければならない。
また、項目名ヘッダーには特殊な規則があり :ref:`後で詳しく解説<項目名ヘッダー>` する。

  .. code-block:: python
    :linenos:
    :caption: リストによる表構造データの表現
    :name: data_list

    >>> dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

細かな変換はreadlist,writelistを使う

入力の変換
'''''''''''''''
mcmdは内部では全てのデータをテキストのバイトストリームとして扱うため、
Python Listsを入力データとして指定した場合、変換操作が加わることになる [#f1]_ 。
mcmdで入力データとして扱い可能なデータ型は、文字列、数値(int,float,bool)であり、
特殊な値としてNone,nan,infも扱うことができる。
いずれもmcmd内部では文字列に変換されるが、その変換規則は表 :numref:`data_inTypeConv` に示す通りで、
実際のPythonコードとその実行結果を :numref:`data_inTypeConvCode` に示す。
なお、コード中の ``mread`` メソッドは、``i=`` で指定された内容をそのまま出力するメソッドである。

  .. csv-table:: Pythonのデータ型のmcmdデータへの変換規則と変換例
    :name: data_inTypeConv

    Pythonデータ型/値,変換前,変換後
    string,\'abc\'       ,\'abc\'
    int   ,12            ,\'12\'
    float ,0.123         ,\'0.123\'
    nan   ,float(\'nan\'),\'\' (空文字)
    inf   ,float(\'inf\'),\'\' (空文字)
    -inf  ,float(\'inf\'),\'\' (空文字)
    True  ,True          ,\'1\'
    False ,False         ,\'0\'
    None  ,None          ,\'\' (空文字)

  .. code-block:: python
    :linenos:
    :caption: Pythonデータ型の変換例
    :name: data_inTypeConvCode

    >>> import nysol.mcmd as nm
    >>> dat=[
    ["str","int","float","nan","inf","-inf","True","False","None"],
    ["A",10,0.123,float("nan"),float("inf"),float("-inf"),True,False,None]
    ]
    >>> nm.mread(i=dat).run()
    ['A', '10', '0.123', '', '', '', '1', '0', '']


出力の変換
'''''''''''''''
出力も入力と同様に、mcmdの内部で処理されるテキストのバイトストリームデータを
Pythonの各種型に変換する必要が出てくる。
特に何も指定しなければ、全て文字列として出力される。
それら文字列を他のデータ型に変換したければ、``writelist`` メソッドを用いればよい。
このメソッドは、項目単位で出力するデータ型を指定できる。
変換可能なデータ型は、str,int,float,boolであり、strは 空文字に、その他の型は ``None`` に変換される。
出力時の変換規則は表 :numref:`data_outTypeConv` に示す通りで、
実際のPythonコードとその実行結果を :numref:`data_outTypeConvCode` に示す。

  .. csv-table:: mcmdの出力データのPythonのデータ型への変換規則
    :name: data_outTypeConv

    Pythonデータ型,変換前,変換後
    string,\'abc\'       ,\'abc\'
    int   ,\'12\'        ,12
    float ,\'0.123\'     ,0.123
    bool  ,\'1\'         ,True
    bool  ,\'0\'         ,False
    string,\'\' (空文字) ,""
    int   ,\'\' (空文字) ,None
    float ,\'\' (空文字) ,None
    bool  ,\'\' (空文字) ,None

  .. code-block:: python
    :linenos:
    :caption: mcmdの出力のPythonデータ型への変換例
    :name: data_outTypeConvCode

    >>> import nysol.mcmd as nm
    >>> dat=[
    ["str","int","float","zero","nonzero","null"],
    ["A",10,0.123,0,1,""]
    ]
    >>> nm.mread(i=dat).run() # writelistを用いなければ、全ての項目は文字列として出力される
    ['A', '10', '0.12', '0', '1', '']
    >>> nm.mread(i=dat).writelist(dtype="str:str,int:int,float:float,zero:bool,nonzero:bool,null:int").run()
    ['A', 10, 0.12, False, True, None]

CSV
-------------------
CSV(Comma Separated Values)フォーマットとは、 :numref:`data/csv` に例示されるような値をカンマで区切った表構造データである。
CSVは表構造データのフォーマットのデファクトスタンダードであり、
アプリケーションプログラム間でのデータ交換用フォーマットとして 広く利用されている。

  .. code-block:: python
    :caption: CSVデータ
    :name: data_csv

    itemID,itemName,class,price
    0899781,bread,food,128
    8879674,orange juice,drink,98
    3244565,cheese,food,350
    6711298,bowl,tableware,168

mcmdでCSVファイルの指定は、 ``i="filename.csv"`` のように、ファイル名を文字列で与える。
``i=`` ``m=`` ``o=`` ``u=`` の全てに利用可能である。
:numref:`data_csv_io` は、 :numref:`csv_table` をリストで入力したものを
CSVとして ``dat.csv`` に出力し(最初の ``mread`` メソッド)、
それを再度入力データとして読み込み、``dat2.csv`` に出力する(2番目の ``mread`` メソッド)例である。

  .. code-block:: python
    :caption: CSVファイルの入出力例
    :name: data_csv_io

    >>> import nysol.mcmd as nm
    >>> dat=[
    ["itemID","itemName","class","price"],
    ["0899781","bread","food",128],
    ["8879674","orange juice","drink",98],
    ["3244565","cheese","food",350],
    ["6711298","bowl","tableware",168]
    ]
    >>> nm.mread(i=dat,o="dat.csv").run()
    >>> nm.mread(i="dat.csv",o="dat2.csv").run()

  .. code-block:: sh
    :caption: 出力内容
    :name: data_csv_io_output

    $ cat dat.csv

  .. code-block:: sh
    :caption: :numref:`data_csv_io` の出力内容。 ``dat.csv`` と ``dat2.csv`` の内容は当然同じになる。
    :name: data_csv

    $ cat dat.csv
    itemID,itemName,class,price
    0899781,bread,food,128
    8879674,orange juice,drink,98
    3244565,cheese,food,350
    6711298,bowl,tableware,168
    $ cat dat2.csv
    itemID,itemName,class,price
    0899781,bread,food,128
    8879674,orange juice,drink,98
    3244565,cheese,food,350
    6711298,bowl,tableware,168

CSVの定義
'''''''''''''''''''
CSVは標準化協会や企業主導で作成された標準フォーマットではなく、
それ故にベンダー毎にCSV の扱い方法が異なっているのが現状である。
その中で2005年10月にインターネット標準である |RFC4180| としてCSVフォーマットが 提案されたのは注目すべき動きである。
:numref:`csv_abnf` にRFC4180の中で定義されているCSVの |ABNF| 表現とその意味を示す。

.. |ABNF| raw:: html

  <a href="https://ja.wikipedia.org/wiki/ABNF" target="_blank">ABNF</a>

.. |RFC4180| raw:: html

  <a href="https://www.rfc-editor.org/info/rfc4180" target="_blank">RFC4180</a>

.. list-table:: CSVのABNFによる定義とその意味
  :name: csv_abnf

  * - | **file = [header CRLF] record \*(CRLF record) [CRLF]**
      | ファイル(file)は，ヘッダ(header)と1行以上のレコード(record)から構成される。
      | ヘッダはなくてもよい。ヘッダとレコードの末尾には改行(CRLF)が付く。
      | 最終レコードの改行(CRLF)は任意である。
  * - | **header = name \*(COMMA name)**
      | ヘッダ(header)は1つ以上の名前(name)で構成され，カンマ(COMMA)で区切られる。
  * - | **record = field \*(COMMA field)**
      | レコード(record)は一つ以上の項目(field)で構成されており，
  * - | **name = field**
      | 名前(name)は項目(field)である。
  * - | **field = (escaped / non\-escaped)**
      | 項目(field)はエスケープ(escaped)か，
      | 非エスケープ(non-escaped)のいずれかである。
  * - | **escaped = DQUOTE \*(TEXTDATA / COMMA / CR / LF / 2DQUOTE) DQUOTE**
      | エスケープ(escaped)は，ダブルクォーツで囲まれた0個以上のテキスト文字(TEXTDATA)，
      | カンマ(COMMA)，改行文字(CRもしくはLF)，もしくは2つの連続したダブルクォーツである。
  * - | **non\-escaped = \*TEXTDATA**
      | 非エスケープ(non-escaped)は0個以上のテキスト文字(TEXTDATA)である。
  * - | **COMMA = %x2C**
      | コンマは16進数アスキーコード2Cである。
  * - | **CR = %x0D**
      | キャリッジリターン(CR)は16進数アスキーコード0Dである。
  * - | **DQUOTE = %x22**
      | ダブルクォーツ(DQUOTE)は16進数アスキーコード22である。
  * - | **LF = %x0A**
      | ラインフィード(LF)は16進数アスキーコード0Aである。
  * - | **CRLF = CR LF**
      | 改行ラインフィードはキャリッジリターン+ラインフィードである。
  * - | **TEXTDATA = %x20\-21 / %x23\-2B / %x2D\-7E**
      | テキスト文字(TEXTDATA)は16進数アスキーコードで20〜21，23〜2B，もしくは2D〜7Eである。

mcmdでは上述のCSVの定義に対して以下の制約を追加している。

 * 項目数は全行同じでなければならない。
 * 1行の最大長に制限を設ける(デフォルトでは1MBで、10MBまで拡張可能)
 * 改行はLFのみとする。
 * 最終レコードであっても改行は必須とする。
 * テキスト文字として80〜FFを付け加える(マルチバイト文字を扱うため)。 

利用するCSVファイルが上記の定義を満たしているかどうかを確かめるには
``mchkcsv`` メソッドを用いればよい。

.. _項目名ヘッダー:

項目名ヘッダー
-------------------------
項目名ヘッダーに利用できる文字

項目名ヘッダーの有無
-------------------------


データ変換
----------------
最後に、mcmdの出力データを他のデータ型に変換する方法、及びその逆、
他のデータ型からmcmdの入力データに変換する方法を以下に整理して示しておく。

転置(transpose)
'''''''''''''''''''
mcmdで出力されるリストは、行を要素に出力される。
一方で列全体を一つのリストとして扱いたい場合も多い。
そのような場合は、mcmdから出力されたリストを、以下のような方法に従って変換すれば良い。

  .. code-block:: python
    :caption: リストを転置する方法
    :name: data_transpose

    >>> import numpy as np
    >>> dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

    >>> # numpyを使った方法
    >>> t=np.array(dat).T.tolist()
    >>> print(t)
    [['customer', 'A', 'B', 'B', 'A', 'B'], ['date', '20180101', '20180101', '20180112', '20180105', '20180107'], ['amount', '5200', '800', '3500', '2000', '4000']]
    >>> # 同じことをすれば元に戻る
    >>> tt=np.array(t).T.tolist()
    >>> print(tt)
    [['customer', 'date', 'amount'], ['A', '20180101', '5200'], ['B', '20180101', '800'], ['B', '20180112', '3500'], ['A', '20180105', '2000'], ['B', '20180107', '4000']]


    >>> # mapとzipを使った方法
    >>> t=list(map(list, zip(*dat)))
    >>> print(t)
    [['customer', 'A', 'B', 'B', 'A', 'B'], ['date', '20180101', '20180101', '20180112', '20180105', '20180107'], ['amount', 5200, 800, 3500, 2000, 4000]]
    >>> # 同じことをすれば元に戻る
    >>> tt=list(map(list, zip(*t)))
    >>> print(tt)
    [['customer', 'date', 'amount'], ['A', '20180101', 5200], ['B', '20180101', 800], ['B', '20180112', 3500], ['A', '20180105', 2000], ['B', '20180107', 4000]]

    >>> # ヘッダーを省いて転置する方法
    >>> del dat[0]
    >>> t=list(map(list, zip(*dat)))
    >>> print(t)
    [['A', 'B', 'B', 'A', 'B'], ['20180101', '20180101', '20180112', '20180105', '20180107'], [5200, 800, 3500, 2000, 4000]]

辞書型(Dictionary)
'''''''''''''''''''''''''''''''''''''''
mcmdの出力結果を辞書型に変換する方法、および辞書型のデータをmcmdの入力として用いる時の変換方法は、 :numref:`data_dict` に示される通りである。

  .. code-block:: python
    :caption: 辞書型をヘッダー付きリストに変換する方法
    :name: data_dict

    >>> # 以下のデータをmcmdの出力結果と想定する。
    >>> dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

    >>> # mcmdの出力リストを辞書型に変
    >>> name=dat.pop(0)
    >>> t=list(map(list, zip(*dat))) # 転置は上述の他の方法でもよい
    >>> d=dict(zip(name,t))
    >>> print(d)
    {'customer': ['A', 'B', 'B', 'A', 'B'], 'date': ['20180101', '20180101', '20180112', '20180105', '20180107'], 'amount': [5200, 800, 3500, 2000, 4000]}

    >>> # 辞書型のデータをmcmdの入力リストに変換
    >>> b=list(map(list,zip(*list(a.values()))))
    >>> b.insert(0,list(a.keys()))
    >>> print(b)
    [['customer', 'date', 'amount'], ['A', '20180101', 5200], ['B', '20180101', 800], ['B', '20180112', 3500], ['A', '20180105', 2000], ['B', '20180107', 4000]]


行を辞書型としたリスト
'''''''''''''''''''''''''''''''''''''''
mcmdの出力結果を行を辞書型としたリストに変換する方法、および行を辞書型としたリストのデータをmcmdの入力として用いる時の変換方法は、 :numref:`data_listdict` に示される通りである。

  .. code-block:: python
    :caption: 行ごとに単位に辞書型をヘッダー付きリストに変換する方法
    :name: data_listdict

    >>> # 以下のデータをmcmdの出力結果と想定する。
    >>> dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]
   
    >>> name=dat.pop(0)
    >>> a=list(map(lambda x: dict(zip(name,x)), dat))
    >>> print(a)
    [{'customer': 'A', 'date': '20180101', 'amount': 5200}, {'customer': 'B', 'date': '20180101', 'amount': 800}, {'customer': 'B', 'date': '20180112', 'amount': 3500}, {'customer': 'A', 'date': '20180105', 'amount': 2000}, {'customer': 'B', 'date': '20180107', 'amount': 4000}]

    >>> b=list(map(lambda x: list(x.values()),a))
    >>> b.insert(0,list(a[0].keys()))
    >>> print(b)
    [['customer', 'date', 'amount'], ['A', '20180101', 5200], ['B', '20180101', 800], ['B', '20180112', 3500], ['A', '20180105', 2000], ['B', '20180107', 4000]]

NumPy
'''''''''''''''''''
mcmdの出力結果をNumPyに変換する方法、およびNumPyのデータをmcmdの入力として用いる時の変換方法は、 :numref:`data_numpy` に示される通りである。

  .. code-block:: python
    :caption: NumPyデータの変換
    :name: data_numpy

    >>> import numpy as np
    >>> # 以下のデータをmcmdの出力結果と想定する。
    >>> dat=[
    ["quantity","amount"],
    [5,5200],
    [2,800],
    [1,3500],
    [6,2000],
    [3,4000]
    ]

    >>> # mcmdの出力リストをNumPyに変換
    >>> name=dat.pop(0)
    >>> t=np.array(dat).T
    >>> print(t)
    [[   5    2    1    6    3]
     [5200  800 3500 2000 4000]]

    >>> # NumPyのデータをmcmdの入力リストに変換
    >>> tt=t.T.tolist()
    >>> tt.insert(0,name)
    >>> print(tt)
    [['quantity', 'amount'], [5, 5200], [2, 800], [1, 3500], [6, 2000], [3, 4000]]
 
Pandas DataFrame
''''''''''''''''''''''
mcmdの出力結果をPandas DataFrameに変換する方法、およびPandas DataFrameのデータをmcmdの入力として用いる時の変換方法は、 :numref:`data_pandas` に示される通りである。

  .. code-block:: python
    :caption: Pandas DataFrameデータの変換
    :name: data_pandas

    >>> import pandas as pd
    >>> # 以下のデータをmcmdの出力結果と想定する。
    >>> dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

    >>> # mcmdの出力リストをPandas DataFrameに変換
    >>> name=dat.pop(0)
    >>> df=pd.DataFrame(dat,columns=name)
    >>> print(df)

    >>> # Pandas DataFrameのデータをmcmdの入力リストに変換
    >>> a=df.values.tolist()
    >>> a.insert(0,list(df.columns))
    >>> print(a)


.. [#f1] 実際に変換を行うのは ``i=`` を指定した関数ではなく、 実行時に :doc:`自動追加<autoadd>` される ``readlist`` メソッドである。

