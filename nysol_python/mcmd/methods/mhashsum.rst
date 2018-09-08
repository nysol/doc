mhashsum ハッシュ法による項目値の合計
---------------------------------------------------------------------

hash法を使って ``k=`` パラメータで指定した項目を単位にして、 ``f=`` パラメータで指定した項目値を合計する。
\hyperref[sect:msum]{msum}との違いは、キー項目の並べ替えが必要ないため、その分処理速度が速い。
ただし、キーのサイズ(キー項目のとる値の種類数)が多い場合は処理速度が遅くなる。
msumとmhashsumのどちらを利用するかはデータの内容からユーザーが判断する(後半に示す「ベンチマーク」参照)。

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
    * - | **f=**
        |   必須
      - |   ここで指定された項目(複数項目指定可)が合計される。
        |   :(コロン）で新項目名を指定可能。例）f=数量:数量合計
    * - | **k=**
        |   任意
        |   デフォルト:
      - |   ここで指定された項目(複数項目指定可)をキーとして集計する。
    * - | **hs=**
        |   任意
        |   デフォルト:
      - |   ハッシュサイズ
        |   処理対象データのキーサイズから，ユーザが消費メモリ量と速度を判断して指定する。指定する値としては素数がよい。
        |   キーサイズが大きいデータに対してハッシュサイズが十分な大きさでなければ処理速度が遅くなる。
        |   ハッシュサイズが十分に大きいと処理速度は速いが、
        |   その分多くのメモリが必要になる(後半に示す「ベンチマーク」参照)。
        |   必要なメモリ量の目安: K*(24+F*16) byte, K:キーのサイズ, F:f=で指定した項目数
    * - | **n=True|False**
        |   任意
        |   デフォルト:False
      - |   NULL値が1つでも含まれていると結果もNULL値とする。

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
    '''customer,quantity,amount
    A,1,
    B,,15
    A,2,20
    B,3,10
    B,1,20
    ''')
    
**基本例**

``customer`` 項目を単位にして、 ``quantity`` と ``amount`` 項目の合計を計算する。


  .. code-block:: python
    :linenos:

    >>> nm.mhashsum(k="customer", f="quantity,amount", i="dat1.csv", o="rsl1.csv").run()
    # ## rsl1.csv の内容
    # customer,quantity,amount
    # A,3,20
    # B,4,45

**NULL値出力**

``n=True`` オプションを指定することで、NULL値が含まれている場合は、結果もNULL値として出力する。


  .. code-block:: python
    :linenos:

    >>> nm.mhashsum(k="customer", f="quantity,amount", n=True, i="dat1.csv", o="rsl2.csv").run()
    # ## rsl2.csv の内容
    # customer,quantity,amount
    # A,3,
    # B,,45



関連メソッド
''''''''''''

- :doc:`msum` 
- :doc:`mhashavg` 
