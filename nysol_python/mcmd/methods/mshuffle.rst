mshuffle レコード分割
------------------------------

``f=`` で指定した項目のhash値に従って指定した数のデータに入力データを分割する。
分割数(hashサイズ)を :math:`n` とすると、f=で指定した「項目の値」 :math:`v` のhash値は
:math:`n` の剰余( :math:`v` \ mod\  :math:`n` )として計算される。
「項目の値」は、データを文字列として考え、バイト単位の文字コードの合計値として計算される。
``f=`` を指定しなかった場合は、「項目の値」として行番号が用いられる。
そして、各行は、得られたhash値を名前に持ったデータに出力される。
以上の方法により、同じ項目データを持つ行は全て同一のデータに出力されることが保証される。
また、 ``v=`` で重みを指定することで、分割される各データに複数のhash値を割り当てることもできる。
``n=3,v=2,1,3`` と指定すれば、hashサイズを重みの合計 :math:`2+1+3=6` とし、
2つのhash値(0,1)を分割データ0に、1つのhash値(2)を分割データ1に、
そして3つのhash値(3,4,5)を分割データ2に出力する。
重みはhash値の割当数の重みであり、出力行数の重みではないことに注意する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**d=** : 型=str , 必須

  | 出力するデータの接頭辞を指定する
  | ここで指定した値＋連番(hash値)が実際に出力されるデータになる

**f=** : 型=str , 任意(default=)

  | 分割単位となるキーを指定する
  | ここで指定した項目値が等しいものは同じデータに出力される

**n=** : 型=str , 任意(default=)

  | 分割するデータ数を指定する

**v=** : 型=str , 任意(default=)

  | 分割するデータごとにデータ量の重みを指定する



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`tmpPath=<common_param_tmpPath>`
, :ref:`precision=<common_param_precision>`


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''customer,quantity,amount
    A,20,5200
    B,18,4000
    C,15,3500
    D,10,2000
    E,3,800
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''customer,date,amount
    A,20081201,10
    A,20081207,20
    A,20081213,30
    B,20081002,40
    B,20081209,50
    C,20081003,60
    C,20081219,20
    ''')


**基本例**

指定した項目の値(顧客)が同じであれば同一のファイルに出力にされるように2つのファイルに分割する

  .. code-block:: python
    :linenos:

    nm.mshuffle(f="customer", d="./dat/d", n="2", i="dat2.csv").run()
    ###  の内容


**f=を指定しない例**

f=を指定せず2つのファイルに分割する。
行番号のhash値を用いるので、2つのファイルの行数はほぼ等しくなる。

  .. code-block:: python
    :linenos:

    nm.mshuffle(d="./dat/d", n="2", i="dat2.csv").run()
    ###  の内容


**v=,f=の指定**

v=2,1を指定することで、ファイル0(d\_0)には2つのhash値を割り当て、
ファイル1(d\_1)には1つのhash値を割り当てて分割する。

  .. code-block:: python
    :linenos:

    nm.mshuffle(f="customer", d="./dat/d", v="2,1", i="dat2.csv").run()
    ###  の内容


**v=の指定**

例3をf=の指定なしで実行する。
行番号のhash値を用いるので、この場合は出力行数の比と重みの比がほぼ等しくなる。

  .. code-block:: python
    :linenos:

    nm.mshuffle(d="./dat/d", v="2,1", i="dat2.csv").run()
    ###  の内容


関連メソッド
''''''''''''''''''''

* :doc:`msep` : 項目値によるレコードの分割

