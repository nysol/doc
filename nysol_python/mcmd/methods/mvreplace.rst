mvreplace ベクトル要素の参照置換
------------------------------------------

ベクトル要素をキーにして参照データ上のベクトル型データで置換する。
ベクトル型の項目とは、 :numref:`mvreplace_input` のitems項目のように、
スペースで区切られた複数の文字列を値として持つ項目である。
典型的な例を :numref:`mvreplace_input` 〜 :numref:`mvreplace_out3` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mvreplace_input

  no,items
  1,a b c
  2,a d
  3,b f e f
  4,f c d




.. csv-table:: 参照データ
  :header-rows: 1
  :name: mvreplace_ref

  item,taxo
  a,X
  b,Y
  c,Z
  e,X
  f,Z




.. csv-table:: 基本例
  :header-rows: 1
  :name: mvreplace_out2

  no,items
  1,X Y Z
  2,X d
  3,Y Z X Z
  4,Z Z d




.. csv-table:: アンマッチ要素の指定例
  :header-rows: 1
  :name: mvreplace_out3

  no,items
  1,X Y Z
  2,X *
  3,Y Z X Z
  4,Z Z *


``mvreplace`` コマンドは、参照データデータを一旦全てメモリにセットするので、
巨大な参照データを指定した場合はメモリを使い果たす可能性があることに注意する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**vf=** : 型=str , 必須

  | 結合キーとなるベクトルの項目名( ``i=`` データ上)を指定する。
  | 複数項目指定可能。ベクトル要素はソーティングされている必要はない。
  | 結果の項目名を変更したいときは、:(コロン)に続けて新項目名を指定する。

**A=** : 型=bool , 任意(default=False)

  | ``vf=`` で:(コロン)に続けて指定した項目名で、新たな項目が追加される。
  | なお ``A`` オプションを指定した場合、 ``vf=`` パラメータで指定するすべての
  | 項目に新項目名を指定しなければならない。

**m=** : 型=str , 任意(default=標準入力)

  | 参照データを指定する。

**K=** : 型=str , 必須

  | 参照データ( ``m=`` )上の結合キーとなるベクトル要素の項目名を指定する。
  | 並べ変わっている必要はないが、ベクトル要素は単一化されていなければならない。
  | 単一化されていない時の動作は不定である。

**f=** : 型=str , 必須

  | 結合するベクトル(要素)項目名を指定する。

**n=** : 型=str , 任意(default=)

  | ``vf=`` と ``K=`` のベクトル要素がマッチしなかった場合に結合する文字列を指定する。
  | 省略した場合、対象のベクトル(要素)の結合は行われない。

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
    '''items
    b a c
    c c
    e a a
    ''')

    with open('ref1.csv','w') as f:
      f.write(
    '''item,taxo
    a,X Y
    b,X
    c,Z Z
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''items1,items2
    b a c,b b
    c c,a d
    e a a,a a
    ''')

    with open('ref2.csv','w') as f:
      f.write(
    '''item,taxo
    a,X
    b,X
    c,Y
    d,Y
    ''')


**ベクトルで置換する例**


  .. code-block:: python
    :linenos:

    nm.mvreplace(vf="items", K="item", m="ref1.csv", f="taxo", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # items
    # X X Y Z Z
    # Z Z Z Z
    # e X Y X Y


**複数項目に対して適用する例**


  .. code-block:: python
    :linenos:

    nm.mvreplace(vf="items1,items2", K="item", m="ref2.csv", f="taxo", i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # items1,items2
    # X X Y,X X
    # Y Y,X Y
    # e X X,X X


関連メソッド
''''''''''''''''''''

* :doc:`mvjoin` : 要素の置換ではなく、結合であれば ``mvjoin`` を使う。

