mnullto NULL値の置換
--------------------------------

``f=`` パラメータで指定した項目について
NULL値を ``v=`` パラメータで指定した文字列に置換する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 必須

  | ここで指定した項目(複数項目指定可)のNULL値が置換される。

**v=** : 型=str , 任意(default=)

  | ここで指定した文字列にNULL値を置換する。

**p=** : 型=bool , 任意(default=False)

  | 前の行の値で置換する。
  | ``v=`` パラメータと同時に指定できない。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | ``p`` オプションを指定した時にのみ意味があり、ここで指定した項目値の単位で置換処理を行なう。

**s=** : 型=str , 任意(default=)

  | ``p`` オプションを指定した時にのみ意味があり、 ``k=`` 項目内での並び順を指定する。

**O=** : 型=str , 任意(default=)

  | NULL値以外を置換したい場合は、ここで値を指定する。

**A=** : 型=bool , 任意(default=False)

  | このオプションにより、指定した項目を置き換えるのではなく、
  | ``A`` オプションを指定した場合は必ず、
  | :(コロン）で新項目名を指定する必要がある。例）f=数量:置換後の項目名



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`q=<common_param_q>`
, :ref:`tmppath=<common_param_tmppath>`
, :ref:`precision=<common_param_precision>`


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''customer,birthday
    A,19690103
    B,
    C,19500501
    D,
    E,
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,date
    A,19690103
    B,
    C,19500501
    D,
    E,
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''id,seq,val
    A,1,1
    A,3,2
    A,2,
    B,2,3
    B,1,
    ''')


**基本例**

``birthday`` 項目がNULL値の場合は ``"no value"`` に置換する。

  .. code-block:: python
    :linenos:

    nm.mnullto(f="birthday", v="no value", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer,birthday
    # A,19690103
    # B,no value
    # C,19500501
    # D,no value
    # E,no value


**NULL値以外の置換**

``birthday`` 項目がNULL値の場合は、 ``"no value"``
値がある場合は ``"value"`` 置換し ``entry`` という項目名に変更して出力する。

  .. code-block:: python
    :linenos:

    nm.mnullto(f="birthday:entry", v="no value", O="value", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer,entry
    # A,value
    # B,no value
    # C,value
    # D,no value
    # E,no value


**新しい項目を出力**

``birthday`` 項目がNULL値の場合は ``"no value"`` 、値がある場合は ``"value"`` に置換し ``entry`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mnullto(f="birthday:entry", v="no value", O="value", A=True, i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer,birthday,entry
    # A,19690103,value
    # B,,no value
    # C,19500501,value
    # D,,no value
    # E,,no value


**前行の値に置換**


  .. code-block:: python
    :linenos:

    nm.mnullto(f="val", p=True, i="dat3.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # id,seq,val
    # A,1,1
    # A,3,2
    # A,2,2
    # B,2,3
    # B,1,3


**キー項目を指定した場合の例**


  .. code-block:: python
    :linenos:

    nm.mnullto(k="id", s="seq", f="val", p=True, i="dat3.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # id%0,seq%1,val
    # A,1,1
    # A,2,1
    # A,3,2
    # B,1,
    # B,2,3


関連メソッド
''''''''''''''''''''

* :doc:`mdelnull` : 置換ではなく、行を削除したい場合はこちら。
* :doc:`mchgstr` : NULL値でなく文字列を置換したい場合に使用する。

