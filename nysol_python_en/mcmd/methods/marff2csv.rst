marff2csv arff形式からcsv形式への変換
------------------------------------------------------

arff形式(WEKA用のデータフォーマット: http://weka.wikispaces.com/ARFF )のデータからcsv形式のデータへ変換する。
:numref:`marff2csv.py_exp` にarff形式データのフォーマットを記載する。

.. code-block:: bash
  :linenos:
  :caption: arff形式の例
  :name: marff2csv.py_exp

	@RELATION       タイトル
	@ATTRIBUTE      項目名    string(文字列)
	@ATTRIBUTE      項目名    date(日時 フォーマット:フォーマットは省略可能。省略した場合は、"yyyy-MM-dd'T'HH:mm:ss"）
	@ATTRIBUTE      数量    numeric(数字)
	@ATTRIBUTE      商品    {A,B}(カテゴリ型項目)
	@DATA(実データ)
	No.1,20081201,1,10,A
	No.2,20081202,2,20,A
	No.3,20081203,3,30,A
	No.4,20081201,4,40,B
	No.5,20081203,5,50,B


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_nullout=<common_param_assert_nullout>`
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

    with open('dat1.arff','w') as f:
      f.write(
    '''@RELATION       customerPurchaseData
    @ATTRIBUTE      customer    string
    @ATTRIBUTE      date    date yyyyMMdd
    @ATTRIBUTE      quantity    numeric
    @ATTRIBUTE      amount    numeric
    @ATTRIBUTE      item    {A,B}
    @DATA
    No.1,20081201,1,10,A
    No.2,20081202,2,20,A
    No.3,20081203,3,30,A
    No.4,20081201,4,40,B
    No.5,20081203,5,50,B
    ''')


**基本例**

arff形式の顧客購買データをcsv形式のデータへ変換する。

  .. code-block:: python
    :linenos:

    nm.marff2csv(i="dat1.arff", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer,date,quantity,amount,item
    # No.1,20081201,1,10,A
    # No.2,20081202,2,20,A
    # No.3,20081203,3,30,A
    # No.4,20081201,4,40,B
    # No.5,20081203,5,50,B


関連メソッド
''''''''''''''''''''



