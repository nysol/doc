online retailデータセット
==========================
|uci| より配布されている |uci_onlineretail| の利用方法について解説する。
このデータは雑貨を扱う英国のオンラインストアの顧客ID付きPOSデータで、
:numref:`uci_online_fields` に示される8項目から構成される。

.. note::

  Abstract: This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.

  概要: 英国を拠点にしたオンラインストアの2010年1月12日〜2011年9月12日のトランザクションデータである。

  (上記URLより引用)

.. csv-table:: 入力データ例:mcmdが扱う表構造データ
    :name: uci_online_fields
    :header: 項目名,      日本語,    型,    内容

    InvoiceNo   ,請求番号  ,文字列,基本は6桁の整数で、"c"から始まるコードはキャンセルを表す。
    StockCode   ,商品コード,文字列,基本は5桁の整数だが、末尾にアルファベットが付くものもある。
    Description ,商品名    ,文字列,商品の名称(商品コードと1:1に対応していないものもある)
    Quantity    ,数量      ,整数  ,購入数量
    InvoiceDate ,請求日時  ,実数  ,トランザクションが生成された日時
    UnitPrice   ,単価      ,実数  ,一商品あたりの英貨
    CustomerID  ,顧客コード,文字列,5桁の整数で顧客の識別コード
    Country     ,国名      ,文字列,顧客が居住する国


このデータはMicrosoft Excelのデータとして配布されている。
:numref:`uci_online_download` に、ダウンロードの方法を示している。
wgetやcurlコマンドを用いて、コマンドラインからダウンロードするのであれば、 :numref:`uci_online_wget` に従えば良い。

とExcelをCSVに変換する方法を示している。

  .. |uci| raw:: html

    <a href="https://archive.ics.uci.edu/ml/index.php" target="_blank">UCI machine learning repository</a>

  .. |uci_onlineretail| raw:: html

    <a href="https://archive.ics.uci.edu/ml/datasets/online+retail" target="_blank">online retailデータセット</a>

  .. code-block:: python
    :linenos:
    :caption: OnlineRetailのExcelファイルのダウンロード
    :name: uci_online_download

    >>> import urllib.request
    >>> url="https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
    >>> urllib.request.urlretrieve(url,"onlineRetail.xlsx")

  .. code-block:: bash
    :linenos:
    :caption: curlもしくはwgetによるダウンロード
    :name: uci_online_wget

    $ curl https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx >onlineRetail.xlsx
    $ wget -O onlineRetail.xlsx https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx

次に、ExcelファイルをCSVに変換する。変換にはPandasの ``to_csv`` メソッドを用いる。
ExcelデータにはASCIIコード以外に、マルチバイトコード(通貨記号など)も利用されているので、
``to_csv`` に ``encoding='utf-8'`` を指定する。

  .. code-block:: python
    :linenos:
    :caption: Pandasを用いて、ExcelファイルをCSVに変換する
    :name: uci_online_excel2csv

    >>> import pandas as pd
    >>> data = pd.read_excel('onlineRetail.xlsx', 'Online Retail', index_col=None)
    >>> data.to_csv('onlineRetail.csv', encoding='utf-8', index=None)

変換されたCSVは :numref:`uci_online_csv` に示される通り、8項目の54万行ほどのデータである。

  .. code-block:: bash
    :linenos:
    :caption: 変換されたCSVデータの内容
    :name: uci_online_csv

    $ head onlineRetail.csv 
    InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country
    536365,85123A,WHITE HANGING HEART T-LIGHT HOLDER,6,2010-12-01 08:26:00,2.55,17850.0,United Kingdom
    536365,71053,WHITE METAL LANTERN,6,2010-12-01 08:26:00,3.39,17850.0,United Kingdom
    536365,84406B,CREAM CUPID HEARTS COAT HANGER,8,2010-12-01 08:26:00,2.75,17850.0,United Kingdom
    536365,84029G,KNITTED UNION FLAG HOT WATER BOTTLE,6,2010-12-01 08:26:00,3.39,17850.0,United Kingdom
    536365,84029E,RED WOOLLY HOTTIE WHITE HEART.,6,2010-12-01 08:26:00,3.39,17850.0,United Kingdom
    536365,22752,SET 7 BABUSHKA NESTING BOXES,2,2010-12-01 08:26:00,7.65,17850.0,United Kingdom
    536365,21730,GLASS STAR FROSTED T-LIGHT HOLDER,6,2010-12-01 08:26:00,4.25,17850.0,United Kingdom
    536366,22633,HAND WARMER UNION JACK,6,2010-12-01 08:28:00,1.85,17850.0,United Kingdom
    536366,22632,HAND WARMER RED POLKA DOT,6,2010-12-01 08:28:00,1.85,17850.0,United Kingdom

    $ wc onlineRetail.csv 
    541910 3522965 48039726 onlineRetail.csv

このデータには ``InvoiceDate`` という日付時刻項目が含まれている。
mcmdでは、日付はyyyymmddの8桁固定長に、時刻はhhmmssの6桁固定長にしておくと扱いやすい。
その変換を行うスクリプトを :numref:`uci_online_convdate` に示している。
変換後のデータは :numref:`uci_online2_csv`  に示される通りで、 ``InvoiceDate`` 項目から
日付8桁と時刻6桁が切り出され、 それぞれ ``date`` と ``time`` 項目として追加されている。

  .. code-block:: python
    :linenos:
    :caption: 日付時刻項目を固定長に変換する。
    :name: uci_online_convdate

    >>> import nysol.mcmd as nm
    >>> f=None
    >>> f <<= nm.mdformat(f="InvoiceDate", c="%Y-%m-%d %H:%M:%S", i="onlineRetail.csv")
    >>> f <<= nm.mcal(c="left($s{InvoiceDate},8)", a="date")
    >>> f <<= nm.mcal(c="right($s{InvoiceDate},6)", a="time")
    >>> f <<= nm.mcut(f="InvoiceDate", r=True, o="onlineRetail2.csv")
    >>> f.run(msg="on")

  .. code-block:: bash
    :linenos:
    :caption: 日付時刻項目が固定長に変換されたCSVデータ
    :name: uci_online2_csv

    $ head onlineRetail2.csv 
    InvoiceNo,StockCode,Description,Quantity,UnitPrice,CustomerID,Country,date,time
    536365,85123A,WHITE HANGING HEART T-LIGHT HOLDER,6,2.55,17850.0,United Kingdom,20101201,082600
    536365,71053,WHITE METAL LANTERN,6,3.39,17850.0,United Kingdom,20101201,082600
    536365,84406B,CREAM CUPID HEARTS COAT HANGER,8,2.75,17850.0,United Kingdom,20101201,082600
    536365,84029G,KNITTED UNION FLAG HOT WATER BOTTLE,6,3.39,17850.0,United Kingdom,20101201,082600
    536365,84029E,RED WOOLLY HOTTIE WHITE HEART.,6,3.39,17850.0,United Kingdom,20101201,082600
    536365,22752,SET 7 BABUSHKA NESTING BOXES,2,7.65,17850.0,United Kingdom,20101201,082600
    536365,21730,GLASS STAR FROSTED T-LIGHT HOLDER,6,4.25,17850.0,United Kingdom,20101201,082600
    536366,22633,HAND WARMER UNION JACK,6,1.85,17850.0,United Kingdom,20101201,082800
    536366,22632,HAND WARMER RED POLKA DOT,6,1.85,17850.0,United Kingdom,20101201,082800

以上で、online retail データセットをmcmdで利用する準備が整った。
