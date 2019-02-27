
Data
=========================

The data that MCMD can handle is data in a structured data table with a header of column names such as shown by :numref:`data_table`.
Many processing methods MCMD provides specify input data with  ``i=``, and output data with  ``o=``.
The structured data table that can be specified by those parameters are, as of today, either a CSV data file or a Python List.
As for input, you can specify processing flow object as well, however that is for data flow connections, details are available in  :doc:`Processing flow<flow>`.


  .. csv-table:: Input data example: Structured data table that MCMD can handle
    :name: data_table

    customer,date,amount
    A,20180101,5200
    B,20180101,800
    B,20180112,3500
    A,20180105,2000
    B,20180107,4000

 
List (Python Lists)
---------------------
:numref:`data_list` is the Python code which described  :numref:`data_table` as a list.
It is a two-dimensional list which contains a header of column names as a first element and data in which every one-dimensional list is one element.
All rows have to contain the same number of columns.
Also, the header of column names has special rules, which are explained in " :doc:`field name<field>` ".


  .. code-block:: python
    :linenos:
    :caption: Structured data table described by a list
    :name: data_list

    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

Conversion of input data
'''''''''''''''''''''''''''''''

As all the data is processed as bite stream of text within MCMD,
the operation to convert input data needs to be added when a Python list is specified as input data [#f1]_ .
Data types MCMD can handle as input data are strings, numbers (int, float, bool),
and None, nan, inf as special values.
Each value is converted into a string within MCMD according to the conversion rules described in  :numref:`data_inTypeConv`,
actual python code and its result are shown in  :numref:`data_inTypeConvCode`.
By the way, ``mread``  in the code is a method to output the content specified by ``i=`` as it is.

  .. csv-table:: Conversion rules and examples of Python data types into MCMD data
    :name: data_inTypeConv

    Python data type/value,before conversion,after conversion
    string,\'abc\'       ,\'abc\'
    int   ,12            ,\'12\'
    float ,0.123         ,\'0.123\'
    nan   ,float(\'nan\'),\'\' (null)
    inf   ,float(\'inf\'),\'\' (null)
    -inf  ,float(\'inf\'),\'\' (null)
    True  ,True          ,\'1\'
    False ,False         ,\'0\'
    None  ,None          ,\'\' (null)

  .. code-block:: python
    :linenos:
    :caption: Examples of conversion of Python data types
    :name: data_inTypeConvCode

    import nysol.mcmd as nm
    dat=[
    ["str","int","float","nan","inf","-inf","True","False","None"],
    ["A",10,0.123,float("nan"),float("inf"),float("-inf"),True,False,None]
    ]
    nm.mread(i=dat).run()
    #[['A', '10', '0.123', '', '', '', '1', '0', '']]

Conversion of outout
''''''''''''''''''''''''

You will need to convert text stream data processed within MCMD into Python data types for output, as well as input. 
When nothing is specified, all data will be output as strings.
If you want to convert those into other data types, you can use the method ``writelist``.
This method can specify data types to be output by column.
Data types which data can be converted into are, str, int, float, bool, and empty strings are converted into the null character for str, and ``None`` for other data types.
Conversion rules for output are as shown in  :numref:`data_outTypeConv` .
Actual Python code and its result of execution are shown in  :numref:`data_outTypeConvCode` .


  .. csv-table:: Conversion rules of MCMD output data into Python data type
    :name: data_outTypeConv

    Python data type,before conversion,after conversion
    string,\'abc\'       ,\'abc\'
    int   ,\'12\'        ,12
    float ,\'0.123\'     ,0.123
    bool  ,\'1\'         ,True
    bool  ,\'0\'         ,False
    string,\'\' (null) ,""
    int   ,\'\' (null) ,None
    float ,\'\' (null) ,None
    bool  ,\'\' (null) ,None

  .. code-block:: python
    :linenos:
    :caption: Example of conversion of MCMD output data into Python data types
    :name: data_outTypeConvCode

    import nysol.mcmd as nm
    dat=[
    ["str","int","float","zero","nonzero","null"],
    ["A",10,0.123,0,1,""]
    ]
    nm.mread(i=dat).run() # All data will be output as string if writelist is not used 
    #[['A', '10', '0.123', '0', '1', '']]

    # Specify each item's data type by dtype
    nm.mread(i=dat).writelist(dtype="str:str,int:int,float:float,zero:bool,nonzero:bool,null:int").run()
    #[['A', 10, 0.123, False, True, None]]

    # If you specify header=True, the header of column names will be also output.
    nm.mread(i=dat).writelist(dtype="str:str,int:int,float:float,zero:bool,nonzero:bool,null:int",header=True).run()
    #[['str', 'int', 'float', 'zero', 'nonzero', 'null'], ['A', 10, 0.123, False, True, None]]
    
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
:numref:`data_csv_io` は、 入力したデータを
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
0行目と1行目の ``f1`` 項目はダブルクォーツを含んでおり、オリジナルのデータはそれぞれ ``abc"def`` 、 ``"`` である。

  .. code-block:: bash
    :linenos:
    :caption: ダブルクオーツを値に含むCSV
    :name: data_csv_exp2

    f1,f2
    "abc""def",2
    """",2

改行を含むデータ
:::::::::::::::::::::::::::::
改行を含むデータもダブルクオーツで囲うことで処理可能となる。
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

.. _data_dataType:

mcmd内部でのデータ型
-----------------------
MCMDで扱うデータはプレーンテキストであり、全てのデータは文字列で表されている。
よって、その文字列をどのようなデータ型として扱うかはメソッドによって決まる。
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
      - * mcalのnow関数
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
入力行数，出力行数は共に0件である。

マルチバイト文字
---------------------------
mcmdが扱う漢字等のマルチバイト文字は基本的にはUTF-8を前提としている。
SHIFT JIS 等、異なるエンコーディングによるマルチバイト文字でも運用は可能であるが、
一部の機能は正しく動作しないであろう。
以下ではマルチバイト文字の扱いについてのMCMDでの処理方式について説明する。
MCMD では処理速度を重視する観点から、漢字コードはマルチバイト文字のまま扱っているために、
エンコーディングによっては、文字列検索や置換の処理で思わぬ結果がもたらされることがある。
例えば、SHIFT JIS で「陰」は 0x8941 であるが、
これは2バイトめがシングルバイト文字の「A」にあたる。
そのため「陰」に対して「A」を「B」に置換する処理を付すと「隠」(0x8942) に変換されてしまう。
UTF-8 ではこのような問題が起こらないようなコード体系を採用している。
さらにマルチバイト文字とASCII 文字が混在した文字列において文字数をカウントすることは、
たとえ UTF-8 であろうと非常に困難である。
このような問題を避ける最良の方法は、ASCII コードも含めて全ての文字を固定長に変換してしまうことである。
これがワイド文字と呼ばれるものである (mcmdでは 32bit 固定長を採用している)。
ワイド文字への変換には、マルチバイト文字のエンコーディング方式が分かっている必要がある。
変換プログラムは、環境変数 LANG に設定された値によって、
その方式を識別している。
環境変数は以下のように確認すればよいであろう。

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

Conversion of input / output data of MCMD 
---------------------------------------------
Lastly, the method of converting MCMD output data into other data types, and the reverse case,
converting other data types into MCMD input data are sorted out as follows.


Transpose
'''''''''''''''''''''''''''''''''
Lists MCMD outputs have rows as elements. 
On the contrary, there are many cases you want to process columns as lists .
In those cases, you can convert output lists by MCMD according to the procedure below.


  .. code-block:: python
    :caption: The method to transpose a list
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

    # A method using numpy
    t=np.array(dat).T.tolist()
    print(t)
    #[['customer', 'A', 'B', 'B', 'A', 'B'], ['date', '20180101', '20180101', '20180112', '20180105', '20180107'], ['amount', '5200', '800', '3500', '2000', '4000']]
    # List can be reversed back by doing the same 
    tt=np.array(t).T.tolist()
    print(tt)
    #[['customer', 'date', 'amount'], ['A', '20180101', '5200'], ['B', '20180101', '800'], ['B', '20180112', '3500'], ['A', '20180105', '2000'], ['B', '20180107', '4000']]

    # A method using map and zip
    t=list(map(list, zip(*dat)))
    print(t)
    #[['customer', 'A', 'B', 'B', 'A', 'B'], ['date', '20180101', '20180101', '20180112', '20180105', '20180107'], ['amount', 5200, 800, 3500, 2000, 4000]]
    # List can be reversed back by doing the same 
    tt=list(map(list, zip(*t)))
    print(tt)
    #[['customer', 'date', 'amount'], ['A', '20180101', 5200], ['B', '20180101', 800], ['B', '20180112', 3500], ['A', '20180105', 2000], ['B', '20180107', 4000]]

    # A method of reversing back by omitting a header
    del dat[0]
    t=list(map(list, zip(*dat)))
    print(t)
    #[['A', 'B', 'B', 'A', 'B'], ['20180101', '20180101', '20180112', '20180105', '20180107'], [5200, 800, 3500, 2000, 4000]]

Dictionary by column
'''''''''''''''''''''''''''''''''''''''
How to convert an output of MCMD into a dictionary, and how to convert a dictionary into an input data list of MCMD are shown in  :numref:`data_dict` 
  .. code-block:: python
    :caption: How to convert a dictionary into a list with header
    :name: data_dict

    # Assume the data below is the output of MCMD
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

    # Convert the output list into a dictionary
    name=dat.pop(0)
    t=list(map(list, zip(*dat))) # You can also transpose with another way described above
    d=dict(zip(name,t))
    print(d)
    #{'customer': ['A', 'B', 'B', 'A', 'B'], 'date': ['20180101', '20180101', '20180112', '20180105', '20180107'], 'amount': [5200, 800, 3500, 2000, 4000]}

    # Convert the dictionary into an input list of MCMD
    b=list(map(list,zip(*list(a.values()))))
    b.insert(0,list(a.keys())
    print(b)
    #[['customer', 'date', 'amount'], ['A', '20180101', 5200], ['B', '20180101', 800], ['B', '20180112', 3500], ['A', '20180105', 2000], ['B', '20180107', 4000]]


Dictionary by row
''''''''''''''''''''''''''''''''''''''''''''''''''''
How to convert output results of MCMD into a list using a dictionary to represent each row, and how to convert a list using a dictionary to represent each row into an input data of MCMD are shown in  :numref:`data_listdict` .

  .. code-block:: python
    :caption: How to convert each row into a dictionary of a list
    :name: data_listdict

    # Assume the data below is the output of MCMD
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
How to convert output results of MCMD into NumPy data, and how to covert NumPy data into an input data of MCMD are shown by  :numref:`data_numpy` 

  .. code-block:: python
    :caption: NumPyデータの変換  Conversion of NumPy data
    :name: data_numpy

    import numpy as np
    # Assume the data below is the output of MCMD
    dat=[
    ["quantity","amount"],
    [5,5200],
    [2,800],
    [1,3500],
    [6,2000],
    [3,4000]
    ]

    # Convert the output of MCMD into NumPy data
    name=dat.pop(0)
    t=np.array(dat).T
    print(t)
    #[[   5    2    1    6    3]
    #[5200  800 3500 2000 4000]]

    # Convert NumPy data into an input list of MCMD
    tt=t.T.tolist()
    tt.insert(0,name)
    print(tt)
    #[['quantity', 'amount'], [5, 5200], [2, 800], [1, 3500], [6, 2000], [3, 4000]]
 
Pandas DataFrame
''''''''''''''''''''''
How to convert output results into Pandas DataFrame, and how to convert Pandas DataFram to an input list of MCMD are shown in  :numref:`data_pandas` .


  .. code-block:: python
    :caption: Conversion of Pandas DataFrame
    :name: data_pandas

    import pandas as pd
    # Assume the data below is the output data of MCMD
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

    # Convert the output of MCMD into Pandas DataFrame
    name=dat.pop(0)
    df=pd.DataFrame(dat,columns=name)
    print(df)

    # Convert Pandas DataFrame into an input list of MCMD
    a=df.values.tolist()
    a.insert(0,list(df.columns))
    print(a)
    #[{'customer': 'A', 'date': '20180101', 'amount': 5200}, {'customer': 'B', 'date': '20180101', 'amount': 800}, {'customer': 'B', 'date': '20180112', 'amount': 3500}, {'customer': 'A', 'date': '20180105', 'amount': 2000}, {'customer': 'B', 'date': '20180107', 'amount': 4000}]


.. [#f1] What actually converts is not the function specified by  ``i=`` , but  ``readlist`` method which is :doc:`automatically added<autoadd>` when executed.
.. [#f2] MCMD counts the first row (the first row of the data excluding the header of column names) as 0th row.

..
  readlist
  writelist
  readcsv
  writecsv
  mstdin
  mstdout
  これら6つの裏ではkgloadが動いている。

