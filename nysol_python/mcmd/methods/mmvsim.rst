mmvsim 移動窓の類似度計算
------------------------------------------------

移動窓を設定し、各種類似度(2変量の統計量)を計算する。
\hyperref[sect:msim]{msim}コマンドの移動窓バージョンとして考えればよい。
``msim`` との違いは、指定できる類似度は一つだけで、また類似度計算の対象項目は2つのみである。

パラメータ
''''''''''''''''''''''

  .. list-table::
    :header-rows: 1

    * - キーワード
      - 内容

    * - | **i=**
        |   任意
        |   デフォルト:標準入力
      - |   入力データを指定する。
    * - | **o=**
        |   任意
        |   デフォルト:標準出力
      - |   出力データを指定する。
    * - | **s=**
        |   任意
        |   デフォルト:
      - |   ここで指定した項目(複数項目指定可)で並べ替えられた後、各種類似度が計算される。
        |   ``q=True`` オプションを指定しないとき、 ``s=`` パラメータは必須。
    * - | **k=**
        |   任意
        |   デフォルト:
      - |   ここで指定された項目(複数項目指定可)を単位として集計する。
    * - | **f=**
        |   必須
      - |   集計項目名リスト(複数項目指定可)を指定する。
    * - | **t=**
        |   任意
        |   デフォルト:
      - |   期間数を1以上の整数で指定する。
    * - | **c=**
        |   必須
      - |   類似度(以下のリストから一つだけ)指定する。
        |   \verb/covar|ucovar|pearson|spearman|kendall|euclid|/
        |   \verb/cosine|cityblock|hamming|chi|phi|jaccard|support|lift/
        |   詳細な定義は\hyperref[sect:msim]{msim}コマンドを参照のこと。
    * - | **skip=**
        |   任意
        |   デフォルト:\verb|skip=(t=の値-1)|
      - |   出力を抑制する最初の行数を指定する。
    * - | **a=**
        |   必須
      - |   計算結果の出力として追加される項目の名前を指定する。
    * - | **n=True|False**
        |   任意
        |   デフォルト:False
      - |   期間内にNULL値が1つでも含まれていると結果もNULL値とする。

共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullkey=<common_param_assert_nullkey>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
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
        
    with open('dat1.csv','w') as f:
      f.write(
    '''t,x,y
    1,14,0.17
    2,11,0.2
    3,32,0.15
    4,13,0.33
    5,8,0.1
    6,19,0.56
    ''')
    
**基本例**

``x、y`` 項目についてのピアソンの積率相関係数を3期を窓として計算する。


  .. code-block:: python
    :linenos:

    >>> nm.mmvsim(s="t", t="3", c="pearson", f="x,y", a="sim", i="dat1.csv", o="rsl1.csv").run()
    # ## rsl1.csv の内容
    # t%0,x,y,sim
    # 3,32,0.15,-0.8746392857
    # 4,13,0.33,-0.6515529194
    # 5,8,0.1,-0.1164257338
    # 6,19,0.56,0.9986254289



関連メソッド
''''''''''''

- :doc:`msim` 
- :doc:`mwindow` 
- :doc:`mmvavg` 
