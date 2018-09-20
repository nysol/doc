mvcat ベクトルの併合
--------------------------

複数のベクトルを併合して新しいベクトルを生成する。
典型的な例を :numref:`mvcat_input` 〜 :numref:`mvcat_out2` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mvcat_input

  no,items1 items2
  1,a c b
  2,a d a e
  3,b f
  4,e e




.. csv-table:: 基本例
  :header-rows: 1
  :name: mvcat_out1

  no,catItems
  1,a c b
  2,a d a e
  3,b f
  4,e e




.. csv-table:: 併合前のベクトルを残す例
  :header-rows: 1
  :name: mvcat_out2

  no,items1 items2 new
  1,a c b a c b
  2,a d a e a d a e
  3,b f  b f
  4,e e e e




パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**vf=** : 型=str , 必須

  | 併合する複数のベクトル項目名( ``i=`` データ上)を指定する。
  | 項目名にワイルドカードを使うことができる。

**a=** : 型=str , 必須

  | 併合後の項目名を指定する。

**A=** : 型=bool , 任意(default=False)

  | 新しい項目として追加する。このオプションを指定しなければ、併合元の項目( ``vf=`` )は削除される。

**delim=** : 型=str , 任意(default=)

  | ベクトル型データの区切り文字を指定する。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`delim=<common_param_delim>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
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
    '''items1,items2,items3,items4
    b a c,b,x,y
    c c,,x,y
    e a a,a a a,x,y
    ''')


**ワイルドカードを利用した例**


  .. code-block:: python
    :linenos:

    nm.mvcat(vf="items*", a="items", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # items
    # b a c b x y
    # c c x y
    # e a a a a a x y


関連メソッド
''''''''''''''''''''



