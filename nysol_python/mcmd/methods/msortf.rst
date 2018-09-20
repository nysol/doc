msortf レコードの並べ換え
--------------------------------

``f=`` パラメータで指定した項目を基準にして、レコードを並べ換える。\
ソーティングアルゴリズムはquick sortを利用しており、
安定ソート(キーの値が同じ行については元の順序を保存する)にはならないことに注意する。\
出力CSVの項目名の後ろには、並び順情報として ``%`` で始まる文字列が付加される。
書式は ``%優先順位[並び順]`` で、
詳細は以下、 ``f=`` パラメータを参照のこと。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 必須

  | レコードを並べ換える基準となる項目名リストを指定する。
  | 並び順は、数値/文字列、昇順/降順の組み合せで4通り指定できる。
  | 指定方法は ``%`` に続けて ``n`` と ``r`` を以下の通り組み合わせる。
  | 文字列昇順: ``項目名`` ( ``%`` 指定なし)、文字列逆順: ``f=項目名%r`` 、数値昇順: ``f=項目名%n`` 、数値降順: ``f=項目名%nr`` 。

**noflg=** : 型=bool , 任意(default=False)

  | 出力CSVのヘッダーにソーティングの印( ``%0,%0n`` など)を付けない。

**pways=** : 型=str , 任意(default=)

  | 同時併合データ数([2-100]:デフォルト32)【任意】
  | 分割ソートされた複数のデータを同時に何個併合するかを指定する。

**blocks=** : 型=str , 任意(default=)

  | バッファブロック数([1-1000]:デフォルト10)【任意】
  | メモリ内でソートする際のメモリサイズ上限をブロックサイズで指定する。
  | 1ブロックは入力バッファサイズ×4で、デフォルトは4MB。

**maxlines=** : 型=str , 任意(default=)

  | メモリソートレコード件数上限([100-1000万]:デフォルト50万)【任意】
  | メモリ内でソートする際の件数の上限を指定する。
  | データの一行あたりの平均サイズに応じて、

**threadCnt=** : 型=str , 任意(default=)

  | メモリ内でソートを実行するthread数 ([1-50]:デフォルト8)【任意】
  | 分割ソートする際に、マルチスレッドの機能を用いて同時にソートする数を指定する。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
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
    '''item,date,quantity,price
    B,20081201,4,40
    A,20081201,10,200
    A,20081201,10,100
    B,20081203,5,50
    B,20081201,2,500
    A,20081201,3,300
    ''')


**基本例**

``item、date`` 順に並べ替える。

  .. code-block:: python
    :linenos:

    nm.msortf(f="item,date", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # item%0,date%1,quantity,price
    # A,20081201,10,200
    # A,20081201,10,100
    # A,20081201,3,300
    # B,20081201,4,40
    # B,20081201,2,500
    # B,20081203,5,50


**数量(quantity)降順，金額(price)昇順に並べ替える例**


  .. code-block:: python
    :linenos:

    nm.msortf(f="quantity%nr,price%n", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # item,date,quantity%0nr,price%1n
    # A,20081201,10,100
    # A,20081201,10,200
    # B,20081203,5,50
    # B,20081201,4,40
    # A,20081201,3,300
    # B,20081201,2,500


関連メソッド
''''''''''''''''''''



