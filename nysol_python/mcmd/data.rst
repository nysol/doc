
データ
-----------------------

mcmdで扱える入力データは、CSVデータファイルとPythonリストである。

リスト
'''''''''''''''''''''''

リストによる指定方法を例をあげて書く。
Noneがnullであることも書く
辞書の場合、リストに変換する方法を示しておく。

mcmdの多くのメソッドでは入出力データとしてPythonのリストとしてデータを指定することができる。
しかし一方で、mcmd内部ではデータは全てテキストのバイトストリームとして扱われるため、
入出力にリストを指定した場合、データ型の変換が生じる。

細かな変換はreadlist,writelistを使う

入力の変換
:::::::::::

mcmdで入力データとして扱い可能なPythonのデータ型は、文字列、数値(int,float,bool)であり、
特殊な値としてNone,nan,infも扱うことができる。
いずれもmcmd内部では文字列に変換されるが、その変換規則は表 :numref:`list:inTypeConv` に示す通りで、
実際のPythonコードとその実行結果を :numref:`list_convTypeCode` に示す。

  .. csv-table:: Pythonのデータ型のmcmdデータへの変換規則と変換例
    :name: list_inTypeConv

    Pythonデータ型/値,変換後文字列,変換前例,変換後例
    string,そのまま          ,\'abc\'       ,\'abc\'
    int   ,文字列としての整数,12            ,\'12\'
    float ,文字列としての実数,0.123         ,\'0.123\'
    nan   ,null値            ,float(\'nan\'),\'\'
    inf   ,null値            ,float(\'inf\'),\'\'
    -inf  ,null値            ,float(\'inf\'),\'\'
    True  ,\'1\'             ,True          ,\'1\'
    False ,\'0\'             ,False         ,\'0\'
    None  ,null値            ,None          ,\'\'

  .. code-block:: python
    :linenos:
    :caption: Pythonデータ型の変換例
    :name: list_convTypeCode

    >>> import nysol.mcmd as nm
    >>> dat=[
    ["str","int","float","nan","inf","-inf","True","False","None"],
    ["A",10,0.123,float("nan"),float("inf"),float("-inf"),True,False,None]
    ]
    >>> nm.mread(i=dat).run()
    ['A', '10', '0.123', '', '', '', '1', '0', '']


出力の変換
:::::::::::
mcmdの内部では全てのデータはテキストのバイトストリームとして扱われるため、
何の指定もなくPythonデータとして出力すれば全て文字列として出力される。
それら文字列を他のデータ型に変換したければ、``writelist`` メソッドを用いればよい。
このメソッドは、項目単位で出力するデータ型を指定できる。
変換可能なデータ型は、str,int,float,boolであり、いずれの型においてもnull値は ``None`` に変換される。

  .. code-block:: python
    :linenos:
    :caption: Pythonデータ型の変換例
    :name: list_convTypeCode

    >>> import nysol.mcmd as nm
    >>> dat=[
    ["str","int","float","zero","nonzero","null"],
    ["A",10,0.123,0,1,""]
    ]
    >>> nm.mread(i=dat).run() # writelistを用いなければ、全ての項目は文字列として出力される
    ['A', '10', '0.12', '0', '1', '']
    >>> nm.mread(i=dat).writelist(dtype="str:str,int:int,float:float,zero:bool,nonzero:bool,null:int").run()
    ['A', 10, 0.12, False, True, None]


ヘッダーの有無

CSV
'''''''''''''''''''''''


