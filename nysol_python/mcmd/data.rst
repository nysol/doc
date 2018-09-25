
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
また、項目名ヘッダーには特殊な規則があり 詳しくは、別節「 :doc:`項目名ヘッダー<field>` 」で解説している。

  .. code-block:: python
    :linenos:
    :caption: リストによる表構造データの表現
    :name: data_list

    dat=[
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
いずれもmcmd内部では文字列に変換されるが、その変換規則は :numref:`data_inTypeConv` に示す通りで、
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

    import nysol.mcmd as nm
    dat=[
    ["str","int","float","nan","inf","-inf","True","False","None"],
    ["A",10,0.123,float("nan"),float("inf"),float("-inf"),True,False,None]
    ]
    nm.mread(i=dat).run()
    #[['A', '10', '0.123', '', '', '', '1', '0', '']]

出力の変換
'''''''''''''''
出力も入力と同様に、mcmdの内部で処理されるテキストのバイトストリームデータを
Pythonの各種型に変換する必要が出てくる。
特に何も指定しなければ、全て文字列として出力される。
それら文字列を他のデータ型に変換したければ、``writelist`` メソッドを用いればよい。
このメソッドは、項目単位で出力するデータ型を指定できる。
変換可能なデータ型は、str,int,float,boolであり、strは 空文字に、その他の型は ``None`` に変換される。
出力時の変換規則は :numref:`data_outTypeConv` に示す通りで、
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

    import nysol.mcmd as nm
    dat=[
    ["str","int","float","zero","nonzero","null"],
    ["A",10,0.123,0,1,""]
    ]
    nm.mread(i=dat).run() # writelistを用いなければ、全ての項目は文字列として出力される
    #[['A', '10', '0.123', '0', '1', '']]
    nm.mread(i=dat).writelist(dtype="str:str,int:int,float:float,zero:bool,nonzero:bool,null:int").run()
    #[['A', 10, 0.123, False, True, None]]

CSV
-------------------
CSV(Comma Separated Values)フォーマットとは、 :numref:`data_csv` に例示されるような値をカンマで区切った表構造データである。
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
:numref:`data_csv_io` は、 :numref:`data_list` をリストで入力したものを
CSVとして ``dat.csv`` に出力し(最初の ``mread`` メソッド)、
それを再度入力データとして読み込み、``dat2.csv`` に出力する(2番目の ``mread`` メソッド)例である。

  .. code-block:: python
    :caption: CSVファイルの入出力例
    :name: data_csv_io

    import nysol.mcmd as nm
    dat=[
    ["itemID","itemName","class","price"],
    ["0899781","bread","food",128],
    ["8879674","orange juice","drink",98],
    ["3244565","cheese","food",350],
    ["6711298","bowl","tableware",168]
    ]
    nm.mread(i=dat,o="dat.csv").run()
    #'dat.csv'
    nm.mread(i="dat.csv",o="dat2.csv").run()
    #'dat2.csv'

  .. code-block:: sh
    :caption: :numref:`data_csv_io` の出力内容。 ``dat.csv`` と ``dat2.csv`` の内容は当然同じになる。
    :name: data_csv_io_output

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

特殊文字を含むCSVの例
''''''''''''''''''''''
以下に CSV データで注意すべき点について、例を交えながら説明する。

カンマを含むデータ
:::::::::::::::::::
カンマを含むデータはダブルクォーツで囲われる。
:numref:`data_csv_exp1` は、``f1,f2`` の 2 項目から構成される CSV ファイルで、
0行目 [#f2]_ の ``f1`` 項目はカンマを含んでいるのでダブルクォーツで囲われている。

  .. code-block:: bash
    :linenos:
    :caption: カンマを値に含むCSV
    :name: data_csv_exp1

    f1,f2
    "abc,def",2
    xyz,2

ダブルクォーツを含むデータ
:::::::::::::::::::::::::::::::::::::::::::
ダブルクォーツを含むデータはダブルクォーツで囲われ，
かつ連続するダブルクォーツとして表現される。
:numref:`data_csv_exp2` は、 ``f1,f2`` の 2 項目から構成される CSV ファイルで、
0行目と1行目の ``f1`` 項目はダブルクォーツを含んでおり、オリジ ナルのデータはそれぞれ ``abc"def`` 、 ``"`` である。

  .. code-block:: bash
    :linenos:
    :caption: ダブルクオーツを値に含むCSV
    :name: data_csv_exp2

    f1,f2
    "abc""def",2
    """",2

改行を含むデータ
:::::::::::::::::::::::::::::
改行を含むデータもダブルクオーツで囲うことで処理可能である。
:numref:`data_csv_exp3` の 0行目の ``f1`` 項目は、 ``abc`` の後に改行 が含まれているが、ダブルクオーツで囲われているため、
行末ではなくデータの一部として識別される。

  .. code-block:: bash
    :linenos:
    :caption: 改行を値に含むCSV
    :name: data_csv_exp3

    f1,f2
    "abc
    def",1

必要のないダブルクオーツ
::::::::::::::::::::::::::::::::::::::::
:numref:`data_csv_exp4` のようにダブルクオーツで囲う必要のないデータに対して
ダブルクオーツを用いていた場合、メソッドの出力時には外される。

  .. code-block:: bash
    :linenos:
    :caption: 不要なダブルクオーツは外される
    :name: data_csv_exp4

    import nysol.mcmd as nm
    with open('dat.csv','w') as f:
    f.write(
    '''f1,f2
    "abc",efg
    "","efg"
    ''')

    print(nm.mcut(f="f1,f2",i="dat.csv").run())    
    # [['f1', 'f2'], ['"abc"', 'efg'], ['abc', '"efg"']]
    print(nm.mcut(f="f1,f2",i="dat.csv").run())
    # [['abc', 'efg'], ['', 'efg']]

mcmd内部でのデータ型
-----------------------
MCMDで扱うデータはプレーンテキストであり、全てのデータは文字列で表されている。
よってその文字列をどのようなデータ型として扱うかはメソッドによって決まる。
例えば、 ``msum`` の ``f=`` で指定した項目データは、
メソッド内部で文字列から数値へと変換される。
MCMDで扱うことのできる型は、:numref:`data_type` に示される通り、
数値型、文字列型、日付型、時刻型、論理型、ベクトル型の6つである。
また、 :numref:`data_typecmd` に各データ型として扱う代表的なコマンドを示しておく。

  .. list-table:: mcmdが扱う6つのデータ型
    :header-rows: 1
    :name: data_type

    * - データ型
      - テキスト例
      - 変換内容
    * - 数値型
      - "10", "2.5", "1.5E+10"
      - 倍精度実数に変換した値
    * - 文字列型
      - "abc", "あいう"
      - 変換なし
    * - 日付型
      - "20130920"
      - 8 桁固定長をグレゴリオ暦のオブジェクトに変換
    * - 時刻型
      - "20180906150620", "150620"
      - 6桁もしくは14桁固定長をグレゴリオ暦+POSIX 時刻のオブジェクトに変換
    * - 論理型
      - "1", "0"
      - 1を真、0を偽の bool 値に変換する
    * - ベクトル型
      - "a c b", "1 5 11"
      - スペースで区切られた文字列を、上記のいずれかのデータ型に変換したもの

  .. list-table:: 各データ型を扱う代表的なメソッド
    :header-rows: 1
    :name: data_typecmd

    * - データ型
      - テキスト例
      - 変換内容
    * - 数値型
      - * msum
        * msim
      - * 数値項目の合計計算
        * 2つの項目の類似度計算
    * - 文字列型
      - * mjoin
        * mcombi
      - * 参照ファイルの結合
        * 組合せの列挙
    * - 日付型
      - * mcalのage関数
        * mcalのleapyear関数
      - * 年令計算
        * うるう年の判定
    * - 時刻型
      - * mcalのnowe関数
        * mcalのdiffminute関数
      - * 現在時刻の出力
        * 分単位での時刻差の計算
    * - 論理型
      - * mcalのand関数
        * mcalのif関数
      - * 論理積の計算
        * 条件に寄る値の設定
    * - ベクトル型
      - * mvsort
        * mvuniq
      - * ベクトル要素の並べ替え
        * ベクトル要素の単一化

データ本体がない場合の動作
---------------------------
データ本体 (項目名行を除いたデータ) がないデータに対する動作は、
項目名ヘッダー付きのデータが入力の場合は、
処理内容に応じた項目名のみが出力され、正常に終了する。
一方で、項目名ヘッダーなしのデータが入力の場合、
データ本体がないということは空リストもしくは0バイトファイルということになり、
出力結果も0バイトファイルとなる。
入力行数，出力行数は共に0件である。

マルチバイト文字
---------------------------
mcmdが扱う漢字等のマルチバイト文字は基本的にはUTF-8を前提としている。
SHIFT JIS 等、異なるエンコーディングによるマルチバイト文字でも運用は可能であるが、
一部の機能は正しく動作しないであろう。
以下ではマルチバイト文字の扱いについてのMCMDでの処理方式について説明する。
MCMD では処理速度を重視する観点から、漢字コードはマルチバイト文字のまま扱っているために、
エンコーディングによっては、文字列検索や置換の処理で思わぬ結果がもたらされることがある。
例えば、SHIFT JIS で「陰」は 0x8941 であるが、
これは2バイト目がシングルバイト文字の「A」にあたる。
そのため「陰」に対して「A」を「B」に置換する処理を付すと「隠」(0x8942) に変換されてしまう。
UTF-8 ではこのような問題が起こらないようなコード体系を採用している。
さらにマルチバイト文字とASCII 文字が混在した文字列において文字数をカウントすることは、
たとえ UTF-8 であろうと非常に困難である。
このような問題を避ける最良の方法は、ASCII コードも含めて全ての文字を固定長に変換してしまうことである。
これがワイド文字と呼ばれるものである (mcmdでは 32bit 固定長を採用)。
ワイド文字への変換には、マルチバイト文字のエンコーディング方式が分かっている必要がある。
変換プログラムは、環境変数 LANG に設定された値によって、
その方式を識別している。
環境変数は以下のように確認すればよい。

  .. code-block:: bash
    :linenos:
    :caption: LANG環境変数の確認
    :name: data_lang

    $ echo $LANG
    ja_JP.UTF-8

mcmdの中の一部のメソッドは、データ処理に先立ち、
入力データを全てワイド文字に変換してから処理するオプション( ``W=True`` )が提供されている。
対応しているコマンド一覧を :numref:`data_wide` に示す。
これらのメソッドは検索もしくは置換の機能を有するものであり、エンコーディングが UTF-8 であれば利用する必要はない。 

  .. list-table:: ワイド文字変換の機能をもつメソッド一覧
    :header-rows: 1
    :name: data_wide

    * - メソッド名
      - 機能
      - 説明
    * - mchgstr
      - 置換
      - ``W=True`` を指定することで ``f=`` で指定した項目データは内部でワイド文字に変換される。
    * - mselstr
      - 検索
      - 部分文字列マッチング ( ``sub=True`` ) を行う場合、``W=True`` を指定することで ``f=`` で指定した項目データは内部でワイド文字に変換される。

    * - msed
      - 置換
      - ``W=True`` を指定することで ``f=`` で指定した項目データは内部でワイド文字に変換される。
    * - mtonull
      - 検索
      - 部分文字列マッチング ( ``sub=True`` ) を行う場合、``W=True`` を指定することで ``f=`` で指定した項目データは内部でワイド文字に変換される。

mcmdの入出力データの変換
--------------------------
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

    import numpy as np
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

    # numpyを使った方法
    t=np.array(dat).T.tolist()
    print(t)
    #[['customer', 'A', 'B', 'B', 'A', 'B'], ['date', '20180101', '20180101', '20180112', '20180105', '20180107'], ['amount', '5200', '800', '3500', '2000', '4000']]
    # 同じことをすれば元に戻る
    tt=np.array(t).T.tolist()
    print(tt)
    #[['customer', 'date', 'amount'], ['A', '20180101', '5200'], ['B', '20180101', '800'], ['B', '20180112', '3500'], ['A', '20180105', '2000'], ['B', '20180107', '4000']]

    # mapとzipを使った方法
    t=list(map(list, zip(*dat)))
    print(t)
    #[['customer', 'A', 'B', 'B', 'A', 'B'], ['date', '20180101', '20180101', '20180112', '20180105', '20180107'], ['amount', 5200, 800, 3500, 2000, 4000]]
    # 同じことをすれば元に戻る
    tt=list(map(list, zip(*t)))
    print(tt)
    #[['customer', 'date', 'amount'], ['A', '20180101', 5200], ['B', '20180101', 800], ['B', '20180112', 3500], ['A', '20180105', 2000], ['B', '20180107', 4000]]

    # ヘッダーを省いて転置する方法
    del dat[0]
    t=list(map(list, zip(*dat)))
    print(t)
    #[['A', 'B', 'B', 'A', 'B'], ['20180101', '20180101', '20180112', '20180105', '20180107'], [5200, 800, 3500, 2000, 4000]]

辞書型(Dictionary)
'''''''''''''''''''''''''''''''''''''''
mcmdの出力結果を辞書型に変換する方法、および辞書型のデータをmcmdの入力として用いる時の変換方法は、 :numref:`data_dict` に示される通りである。

  .. code-block:: python
    :caption: 辞書型をヘッダー付きリストに変換する方法
    :name: data_dict

    # 以下のデータをmcmdの出力結果と想定する。
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

    # mcmdの出力リストを辞書型に変
    name=dat.pop(0)
    t=list(map(list, zip(*dat))) # 転置は上述の他の方法でもよい
    d=dict(zip(name,t))
    print(d)
    #{'customer': ['A', 'B', 'B', 'A', 'B'], 'date': ['20180101', '20180101', '20180112', '20180105', '20180107'], 'amount': [5200, 800, 3500, 2000, 4000]}

    # 辞書型のデータをmcmdの入力リストに変換
    b=list(map(list,zip(*list(a.values()))))
    b.insert(0,list(a.keys())
    print(b)
    #[['customer', 'date', 'amount'], ['A', '20180101', 5200], ['B', '20180101', 800], ['B', '20180112', 3500], ['A', '20180105', 2000], ['B', '20180107', 4000]]


行を辞書型としたリスト
'''''''''''''''''''''''''''''''''''''''
mcmdの出力結果を行を辞書型としたリストに変換する方法、および行を辞書型としたリストのデータをmcmdの入力として用いる時の変換方法は、 :numref:`data_listdict` に示される通りである。

  .. code-block:: python
    :caption: 行ごとに単位に辞書型をヘッダー付きリストに変換する方法
    :name: data_listdict

    # 以下のデータをmcmdの出力結果と想定する。
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]
   
    name=dat.pop(0)
    a=list(map(lambda x: dict(zip(name,x)), dat))
    print(a)
    #[{'customer': 'A', 'date': '20180101', 'amount': 5200}, {'customer': 'B', 'date': '20180101', 'amount': 800}, {'customer': 'B', 'date': '20180112', 'amount': 3500}, {'customer': 'A', 'date': '20180105', 'amount': 2000}, {'customer': 'B', 'date': '20180107', 'amount': 4000}]

    b=list(map(lambda x: list(x.values()),a))
    b.insert(0,list(a[0].keys()))
    print(b)
    #[['customer', 'date', 'amount'], ['A', '20180101', 5200], ['B', '20180101', 800], ['B', '20180112', 3500], ['A', '20180105', 2000], ['B', '20180107', 4000]]

NumPy
'''''''''''''''''''
mcmdの出力結果をNumPyに変換する方法、およびNumPyのデータをmcmdの入力として用いる時の変換方法は、 :numref:`data_numpy` に示される通りである。

  .. code-block:: python
    :caption: NumPyデータの変換
    :name: data_numpy

    import numpy as np
    # 以下のデータをmcmdの出力結果と想定する。
    dat=[
    ["quantity","amount"],
    [5,5200],
    [2,800],
    [1,3500],
    [6,2000],
    [3,4000]
    ]

    # mcmdの出力リストをNumPyに変換
    name=dat.pop(0)
    t=np.array(dat).T
    print(t)
    #[[   5    2    1    6    3]
    #[5200  800 3500 2000 4000]]

    # NumPyのデータをmcmdの入力リストに変換
    tt=t.T.tolist()
    tt.insert(0,name)
    print(tt)
    #[['quantity', 'amount'], [5, 5200], [2, 800], [1, 3500], [6, 2000], [3, 4000]]
 
Pandas DataFrame
''''''''''''''''''''''
mcmdの出力結果をPandas DataFrameに変換する方法、およびPandas DataFrameのデータをmcmdの入力として用いる時の変換方法は、 :numref:`data_pandas` に示される通りである。

  .. code-block:: python
    :caption: Pandas DataFrameデータの変換
    :name: data_pandas

    import pandas as pd
    # 以下のデータをmcmdの出力結果と想定する。
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

    # mcmdの出力リストをPandas DataFrameに変換
    name=dat.pop(0)
    df=pd.DataFrame(dat,columns=name)
    print(df)

    # Pandas DataFrameのデータをmcmdの入力リストに変換
    a=df.values.tolist()
    a.insert(0,list(df.columns))
    print(a)
    #[{'customer': 'A', 'date': '20180101', 'amount': 5200}, {'customer': 'B', 'date': '20180101', 'amount': 800}, {'customer': 'B', 'date': '20180112', 'amount': 3500}, {'customer': 'A', 'date': '20180105', 'amount': 2000}, {'customer': 'B', 'date': '20180107', 'amount': 4000}]

.. [#f1] 実際に変換を行うのは ``i=`` を指定した関数ではなく、 実行時に :doc:`自動追加<autoadd>` される ``readlist`` メソッドである。
.. [#f2] mcmdでは統一的に先頭行 (項目名行を除いた最初の行) を 0 行目と呼称する。

readlist
writelist
readcsv
writecsv
mstdin
mstdout
これら6つの裏ではkgloadが動いている。

