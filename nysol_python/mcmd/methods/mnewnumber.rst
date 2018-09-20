mnewnumber 連番データの新規生成
------------------------------------------

``S=`` パラメータで指定した開始数値もしくはアルファベットにより、
``I=`` パラメータで指定した間隔で連番もしくはアルファベット連番を新規作成し、 ``a=`` パラメータで指定した項目名で出力する。
アルファベット連番とは、AからZの26文字を用いた26進数のこと(A,B, :math:`\cdots` ,Z,AA,AB, :math:`\cdots` ,AZ,BA,BB, :math:`\cdots` ,ZZ,AAA,AAB, :math:`\cdots` )。


パラメータ
''''''''''''''''''''''

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**a=** : 型=str , 必須

  | 新規に作成する連番行の項目名を指定する。
  | ``nfn`` もしくは ``nfno`` オプション指定時は指定の必要はない。

**I=** : 型=str , 任意(default=1)

  | 連番をふる間隔を指定する。

**S=** : 型=str , 任意(default=1)

  | 開始数値/アルファベット(大文字)
  | 連番の開始数値もしくはアルファベットを指定する。
  | 数値を指定した場合は数値の連番がふられる。
  | アルファベットを指定した場合はアルファベット連番がふられる。(小文字は指定できない)

**l=** : 型=str , 任意(default=10)

  | 作成するデータ行数を指定する。



共通パラメータ
''''''''''''''''''''

:ref:`o=<common_param_o>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`tmppath=<common_param_tmppath>`
, :ref:`precision=<common_param_precision>`


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm


**基本例**

1から始まる間隔が1の連番をふり、 ``No.`` という項目名で新規に5行のデータを作成する。

  .. code-block:: python
    :linenos:

    nm.mnewnumber(a="No.", I="1", S="1", l="5", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # No.
    # 1
    # 2
    # 3
    # 4
    # 5


**開始番号と間隔の変更**

10から始まる間隔が5の連番をふり、 ``No.`` という項目名で新規に5行のデータを作成する。

  .. code-block:: python
    :linenos:

    nm.mnewnumber(a="No.", I="5", S="10", l="5", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # No.
    # 10
    # 15
    # 20
    # 25
    # 30


**アルファベット連番**

Aから始まる間隔が1のアルファベット連番をふり、 ``No.`` という項目名で新規に5行のデータを作成する。

  .. code-block:: python
    :linenos:

    nm.mnewnumber(a="No.", I="1", S="A", l="5", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # No.
    # A
    # B
    # C
    # D
    # E


**ヘッダ行なしで新規作成**

Bから始まる間隔が3のアルファベット連番をふり、ヘッダなしで新規に11行のデータを作成する。

  .. code-block:: python
    :linenos:

    nm.mnewnumber(nfn=True, I="3", l="11", S="B", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # B
    # E
    # H
    # K
    # N
    # Q
    # T
    # W
    # Z
    # AC
    # AF


関連メソッド
''''''''''''''''''''

* :doc:`mnewrand` : 新たに乱数を生成する。
* :doc:`mnewstr` : 固定文字列を生成する。

