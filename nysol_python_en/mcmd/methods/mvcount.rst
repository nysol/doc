mvcount ベクトルサイズの計算
------------------------------------

ベクトルのサイズ(ベクトルの要素数)を計算する。

パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**vf=** : 型=str , 必須

  | 要素数をカウントするベクトルの項目名( ``i=`` データ上)を指定する。
  | 結果項目を ``:`` に続けて複数項目指定可能。
  | 複数項目指定可能。

**delim=** : 型=str , 任意(default=)

  | ベクトル型データの区切り文字を指定する。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`delim=<common_param_delim>`
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
    '''items1,items2
    b a c,b
    c c,
    e a a,a a a
    ''')


**複数項目に対して適用する例**


  .. code-block:: python
    :linenos:

    nm.mvcount(vf="items1:size1,items2:size2", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # items1,items2,size1,size2
    # b a c,b,3,1
    # c c,,2,0
    # e a a,a a a,3,3


関連メソッド
''''''''''''''''''''



