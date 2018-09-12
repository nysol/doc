mfldname 項目名の変更
------------------------------

``f=`` で指定した項目名を変更する。又、 ``n=`` で項目名を新規設定する。

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
   * - | **f=str**
       | 任意
     - | ここで指定された項目名のみを変更する。(現項目名:新項目名)
       | 指定していない項目名は変更せずに元の項目名が出力される。
   * - | **n=str**
       | 任意
     - | ここで指定された項目名が新たに採用される。
       | データ項目数と同じ数の項目名を指定する必要がある。
   * - | **nfni=bool**
       | 任意
     - | 入力データの１行目を項目名行とみなさない。このオプションが指定された場合は ``f=`` は利用できない。


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
    '''customer,itemID,10月
    a,xx,11
    b,yy,122
    c,zz,
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''a,xx,11
    b,yy,122
    c,zz,
    ''')


**基本例**

項目名の ``customer`` を「cust」に、「10月」を「Oct.」に変更する。

  .. code-block:: python
    :linenos:

    nm.mfldname(f="customer:cust,10月:Oct.", i="dat1.csv", o="rsl1.csv").run()
