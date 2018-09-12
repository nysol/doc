mcat 併合
--------------

``i=`` パラメータで指定した全データのレコードを、指定した順に併合する。
ワイルドカードでデータを指定した場合は、データのアルファベット順に併合される。

パラメータ
''''''''''''''''''''''

  .. list-table::
   :header-rows: 1

   * - キーワード
     - 内容
   * - | **i=str**
       | 任意
     - | 入力データリストを指定する。
       | 複数のデータをカンマで区切って指定する。ワイルドカードを用いることができる。
   * - | **o=str**
       | 任意
     - | 出力データを指定する。
   * - | **f=str**
       | 任意
     - | 併合する項目名を指定する。
       | 指定を省略すれば ``i=`` で指定した1つ目のデータの項目名が使われる。
   * - | **skip_fnf=bool**
       | 任意
     - | ``i=`` で指定したデータが存在しなくてもエラー終了しない。
       | ただし、全データがなければエラーとなる。
   * - | **nostop=bool**
       | 任意
     - | ``nostop=True``  , ``skip=True`` , ``force=True`` は、指定の項目名がなかったときの動作を制御するフラグである。
       | ``nostop=True`` は、指定の項目名がなければnullを出力する。
       | ``nfn=True`` が同時に指定された場合，項目数が異なればエラー終了する。
   * - | **skip=bool**
       | 任意
     - | 指定の項目名がなければそのデータは併合しない。
       | ``nfn=True`` が同時に指定された場合、項目数が異なればそのデータは併合しない。
   * - | **skip_zero=bool**
       | 任意
     - | -nfnを指定していない場合でも0バイトデータでエラーにならないようにする。
   * - | **flist=str**
       | 任意
     - | 併合するデータリストをCSVデータとして指定する。flist=fileName:fldNameで指定する。
   * - | **kv=str**
       | 任意
     - | パス名に含めた”key-value”の文字列を抜き出し項目名とその値としてデータに付加する。
   * - | **force=bool**
       | 任意
     - | 指定の項目名がなければ，項目番号で強制併合する。
       | 指定の項目番号がなければnullを出力する。
   * - | **stdin=bool**
       | 任意
     - | 標準入力も併合する。
   * - | **add_fname=bool**
       | 任意
     - | 併合元のデータを最終項目として追加する。
       | 標準入力は ``/dev/stdin`` という名称になる。
       | 項目名は ``"fileName"`` 固定なので、入力データに同一の項目名があるとエラーとなる。


共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`add_fname=<common_param_add_fname>`
, :ref:`-stdin=<common_param_-stdin>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
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

    with open('dat1.csv','w') as f:
      f.write(
    '''customer,date,amount
    A,20081201,10
    B,20081002,40
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''customer,date,amount
    A,20081207,20
    A,20081213,30
    B,20081209,50
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''customer,date,quantity
    A,20081201,3
    B,20081002,1
    ''')


**同一項目名ファイルの併合**


  .. code-block:: python
    :linenos:

    nm.mcat(i="dat1.csv,dat2.csv", o="rsl1.csv").run()
