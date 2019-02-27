mvcommon ベクトル要素の参照選択
----------------------------------------

ベクトルから、参照データで指定された要素を選択する。
なお、参照データデータを一旦全てメモリにセットするので、
巨大な参照データを指定した場合はメモリを使い果たす可能性があることに注意する。

パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**vf=** : 型=str , 必須

  | 結合キーとなるアイテム集合の項目名( ``i=`` データ上)を指定する。
  | 複数項目指定可能。アイテムはソーティングされている必要はない。
  | 結果の項目名を変更したいときは、:(コロン)に続けて新項目名を指定する。
  | 例) f=数量:置換後の項目名

**A=** : 型=bool , 任意(default=False)

  | ``vf=`` で:(コロン)に続けて指定した項目名で、新たな項目が追加される。
  | なお ``A`` オプションを指定した場合、 ``vf=`` パラメータで指定するすべての
  | 項目に新項目名を指定しなければならない。

**m=** : 型=str , 任意(default=標準入力)

  | 参照データを指定する。
  | このパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)

**K=** : 型=str , 必須

  | 参照データ( ``m=`` )上の結合キーとなるアイテムの項目名を指定する。

**r=** : 型=bool , 任意(default=False)

  | ``vf=`` と ``K=`` の要素がマッチしない要素を選択する。

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
    '''items1,items2
    b a c,b b
    c c,a d
    e a a,a a
    ''')

    with open('ref1.csv','w') as f:
      f.write(
    '''item
    a
    c
    e
    ''')


**複数項目に対して結合する例**


  .. code-block:: python
    :linenos:

    nm.mvcommon(vf="items1,items2", K="item", m="ref1.csv", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # items1,items2
    # a c,
    # c c,a
    # e a a,a a


**項目名を変更する例**

``item2`` に新項目名 ``new2`` を指定しているので、
項目名が変更され出力される。

  .. code-block:: python
    :linenos:

    nm.mvcommon(vf="items1,items2:new2", K="item", m="ref1.csv", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # items1,new2
    # a c,
    # c c,a
    # e a a,a a


**項目を追加する例**

``item1`` に新項目名 ``new1`` を、
``item2`` に新項目名 ``new2`` を指定し、
``A=True`` オプションを付けているので
新項目 ``new1`` と ``new2`` が追加され出力される。

  .. code-block:: python
    :linenos:

    nm.mvcommon(vf="items1:new1,items2:new2", A=True, K="item", m="ref1.csv", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # items1,items2,new1,new2
    # b a c,b b,a c,
    # c c,a d,c c,a
    # e a a,a a,e a a,a a


関連メソッド
''''''''''''''''''''

* :doc:`mvjoin` : 選択でなくベクトル要素を結合する。

