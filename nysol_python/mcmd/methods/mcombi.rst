mcombi 組合せ計算
------------------------

``f=`` パラメータで指定した項目について、
``n=`` パラメータで指定した数の組み合せを求め、
``a=`` パラメータで指定した項目名で出力する。
``p=True`` を指定することで順列として出力することも可能である。

パラメータ
''''''''''''''''''''''

  .. list-table::
   :header-rows: 1

   * - キーワード
     - 内容
   * - | **i=str**
       | 任意
     - | 入力データを指定する。
   * - | **o=str**
       | 任意
     - | 出力データを指定する。
   * - | **a=str**
       | 必須
     - | 新たに追加される項目の名前を指定する。
   * - | **f=str**
       | 必須
     - | 組合せを求める項目名リスト（複数項目指定可）を指定する。
       | ここで指定した項目の値の全組合せを出力する。
   * - | **n=str**
       | 必須
     - | 組合せの数を指定する。
       | 組み合わせ数を大きくすると、出力レコードが爆発的に大きくなることに注意する。
   * - | **s=str**
       | 任意
     - | ここで指定した項目(複数項目指定可)で並べ替えられた後、 ``f=`` で指定した項目の組み合わせを求める。
   * - | **k=str**
       | 任意
     - | キー項目名リスト(複数項目指定可)
       | 組合せを求める単位となる項目名リスト。
   * - | **p=bool**
       | 任意
     - | 組合せでなく順列を求める。
   * - | **dup=bool**
       | 任意
     - | 同一の値の組み合せも出力する


共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
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
    '''customer,item
    A,a1
    A,a2
    A,a3
    B,a4
    B,a5
    ''')


**基本例**

``customer`` 項目を単位に、 ``item`` 項目の2アイテムの組み合わせを求め、
``item1,item2`` という項目名で出力する。
``k=,f=`` で指定していない項目(ここでは ``item`` 項目)は、キーの最終行の値が出力される。

  .. code-block:: python
    :linenos:

    nm.mcombi(k="customer", f="item", n="2", a="item1,item2", i="dat1.csv", o="rsl1.csv").run()
