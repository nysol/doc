
メソッドの自動追加
-----------------------

いくつかのmcmdメソッドを登録し、``run`` メソッドで実行する前に、
自動的にmcmdメソッドが追加されることがある。
以下では、その条件と内容について説明する。

キーブレイク処理に伴うmsortの追加
'''''''''''''''''''''''''''''''''''
キーブレイク処理(キー項目単位の処理)を利用しているメソッドの前にmsortメソッドが自動追加される。
各メソッドのマニュアルには、msortメソッドが自動追加されるかどうかが明記されている。
キー単位のイテレータ ``keyblock`` や ``k=`` を指定した ``getline`` メソッドも対象となる。
msortメソッドの自動追加を抑制したい場合は ``q=True`` を指定すればよい。
:numref:`autoadd_sort` に ``msum`` メソッドを使った例を示している。
``q=True`` を指定すると、入力データの順序でキーブレイク処理が行われていることがわかる。
なお、msortの自動追加機能は各メソッドに組み込まれた機能であるため、
``drawModelsDS`` 等で内容を表示させても出力されず、
また実行時にメッセージを表示させてもmsortのENDメセージは表示されない。

  .. code-block:: python
    :linenos:
    :caption: 自動sortありとなしの例
    :name: autoadd_sort

    >>> import nysol.mcmd as nm
    >>> dat=[
    ["customer","amount"],
    ["A",5200],
    ["B",800],
    ["B",3500],
    ["A",2000],
    ["B",4000]
    ]
    >>> f1=nm.msum(k="customer",f="amount",i=dat)
    >>> f1.run()
    [['A', '7200'], ['B', '8300']]
    >>> f2=nm.msum(k="customer",f="amount",i=dat,q=True)
    >>> f2.run()
    [['A', '5200'], ['B', '4300'], ['A', '2000'], ['B', '4000']]

入出力によるデータ変換
'''''''''''''''''''''''''''''''''''''''''''''
多くのmcmdメソッドでは、``i=`` にリストを指定すると、そのリストデータを入力データとして読み込んでくれる。
一方で、mcmdメソッドは内部では全てのデータをテキストのバイトストリームとして扱っている。
そのため、リストをバイトストリームに変換する必要がある。
入力時にリストをバイトストリームに変換するメソッドが ``readlist`` で、
出力時にバイトストリームをリストに変換するメソッドが ``writecsv`` である。
そこで、``i=`` にリストを指定した場合は ``readlist`` が追加され、
また出力先が明示的/暗黙的に指定されていなければ ``writelist`` が自動追加される。

  .. code-block:: python
    :linenos:
    :caption: readlistとwritelistの自動追加の例
    :name: autoadd_list

    >>> import nysol.mcmd as nm
    >>> dat=[
    ["customer","amount"],
    ["A",5200],
    ["B",800],
    ["B",3500],
    ["A",2000],
    ["B",4000]
    ]
    >>> nm.msum(k="customer",f="amount",i=dat).drawModelD3("autoadd_list.html")

  .. figure:: autoadd_list.png
    :scale: 40%
    :align: center
    :name: autoadd_list.png
    :target: ../_static/autoadd_list.html

    readlistとwritelistが自動追加された処理フロー

同様にCSVファイルをバイトストリームに変換するメソッドとして、 ``readcsv`` と ``writecsv`` がある。
ただし、mcmdメソッドでは、``i=`` ``o=`` にファイル名を指定する一般的な使い方であれば、メソッド内部でこの変換が行われるため、
``readcsv`` や ``writecsv`` が自動追加されることはない。
``writecsv`` が自動追加される典型例は、フローの途中で ``o=ファイル名`` を指定することである。
:numref:`autoadd_csv` にその例を示している。
これは2つの ``mcut`` をつなげただけの意味のない単純なフローである。
最初の ``mcut`` でその途中経過をCSVファイル ``tmp.csv`` に出力しており、
``m2tee`` の追加でストリームを2分岐させ(後述)、``mfifo`` でバッファリングをかませた上で(後述)、
一方を ``writecsv`` に他方を ``mcut`` に接続している。

  .. code-block:: python
    :linenos:
    :caption: writecsvの自動追加の例
    :name: autoadd_csv

    >>> nm.mcut(f="customer,amount",i=dat,o="tmp.csv").mcut(f="customer").drawModelD3("autoadd_csv.html")

  .. figure:: autoadd_csv.png
    :scale: 40%
    :align: center
    :name: autoadd_csv.png
    :target: ../_static/autoadd_csv.html

    writecsvが自動追加された処理フロー

処理フローの併合によるm2catの追加
'''''''''''''''''''''''''''''''''''''''''''''
2つの処理フローの出力データを併合(行方向にまとめる)したい場合、
mcmdメソッドで ``i=[obj1,obj2,...``　のように ``i=`` に複数の処理フローオブジェクトをリストで与えることによって実現できる。
その時、これら複数のフローから出力されるデータを併合するメソッドとして ``m2cat`` が自動挿入される。
:numref:`autoadd_m2cat` には、1つの``mcut`` から構成される2つの処理フローオブジェクト ``f1`` と ``f2`` を
``msum`` メソッドの入力として指定している。
この場合、``msum`` の前に ``m2cat`` が挿入される。

  .. code-block:: python
    :linenos:
    :caption: m2catの自動追加の例
    :name: autoadd_m2cat

    >>> f1=nm.mcut(f="customer,amount",i=dat)
    >>> f2=nm.mcut(f="customer,amount",i=dat)
    >>> f3=nm.msum(k="customer",f="amount",i=[f1,f2])
    >>> f3.drawModel("autoadd_m2cat.html")
    >>> f3.run()
    [['A', '14400'], ['B', '16600']]

  .. figure:: autoadd_m2cat.png
    :scale: 40%
    :align: center
    :name: autoadd_m2cat.png
    :target: ../_static/autoadd_m2cat.html

    m2catが自動追加された処理フロー

フロー分岐によるmtee,mfifoの追加
'''''''''''''''''''''''''''''''''''''''''''''
``m2cat`` の自動追加とは逆に、ある1つのフローの出力が複数のフローの入力として接続される場合、
``mtee`` が自動追加される。


自動追加される処理。sort,fifo,writelist,readlistなど。

x i=,m=で複数指定したらm2catを追加(core.py 578)。

x o=が途中に指定されていればwritecsvが追加される(600)。

一つのオブジェクトが複数の入力になるばあい(518) teeが追加
f1=nm.mcut
nm.msum(i=f1
nm.msum(i=f1

fifoの追加条件:2つに分かれる場合(
1.o=,u=両方追加されたばあい
2.teeが追加された時

f1=mselstr()
f2=f1.redirect(u=)
mcat i=[f1,f2]

f1=mcut
total=msum(i=f1)
f1<<=mjoin(m=total)

NYSOL_MOD_DSP_TYPE=1
でrunするとオブジェクトを実行して結果を出力(上と下だけ)

sorting
::::::::::::

fifo
::::::::::::

readlist
::::::::::::

writelist
::::::::::::



