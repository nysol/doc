mvdelim ベクトル要素の区切り文字変更
--------------------------------------------

ベクトル型の要素を区切る文字列を変更する。
ただし、区切り文字に空文字を指定すれば区切り文字を削除することになる。
典型的な例を :numref:`mvdelim_input` 〜 :numref:`mvdelim_out4` に示す。
カンマも指定することはできるが、
ダブルクォーテーションで括られ 一つの項目となる ( :numref:`mvdelim_out2` )。
``v=`` のように値を指定しなければ空文字と見なされ、
結果として区切り文字が消去される( :numref:`mvdelim_out3` )。
文字列や漢字も指定することは可能であるが( :numref:`mvdelim_out4` )、
ベクトルを扱うコマンド(mvsortなど)で指定できる区切り文字
( ``delim=`` によって指定)はアルファベット１文字であるため、
もはやベクトルとして利用することはできなくなることに注意する。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mvdelim_input

  no,items
  1,b a a
  2,a a b b
  3,a b b a
  4,a b c




.. csv-table:: 基本例:区切りをマイナス記号に置換
  :header-rows: 1
  :name: mvdelim_out1

  no,items
  1,b-a-a
  2,a-a-b-b
  3,a-b-b-a
  4,a-b-c




.. csv-table:: 区切り文字にカンマを指定すると。。
  :header-rows: 1
  :name: mvdelim_out2

  no,items
  1,"b a a"
  2,"a a b b"
  3,"a b b a"
  4,"a b c"




.. csv-table:: 空文字を指定すると区切りが消える
  :header-rows: 1
  :name: mvdelim_out3

  no,items
  1,baa
  2,aabb
  3,abba
  4,abc




.. csv-table:: 複数文字も指定できるが。。
  :header-rows: 1
  :name: mvdelim_out4

  no,items
  1,bxxaxxa
  2,axxaxxbxxb
  3,axxbxxbxxa
  4,axxbxxc




パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**vf=** : 型=str , 必須

  | 区切り文字を変更するベクトル項目名を指定する。複数項目指定可能。
  | 結果の項目名を変更したいときは、:(コロン)に続けて新項目名を指定する。

**v=** : 型=str , 必須

  | 新しい区切り文字を指定する。何も指定しなければ空文字として扱われる。

**A=** : 型=bool , 任意(default=False)

  | ``vf=`` で:(コロン)に続けて指定した項目名で、新たな項目が追加される。
  | なお ``A`` オプションを指定した場合、 ``vf=`` パラメータで指定するすべての
  | 項目に新項目名を指定しなければならない。

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
    '''item1
    b a c
    c c
    e a a
    ''')


**基本例**

ベクトル型要素のデフォルトの区切り文字である半角スペースを ``_`` (アンダーバー)に置換する。

  .. code-block:: python
    :linenos:

    nm.mvdelim(vf="item1", v="_", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # item1
    # b_a_c
    # c_c
    # e_a_a


**カンマ**

CSVの区切り文字であるカンマに置換すると、CSVの区切り文字との区別を付けるために、
ベクトル全体がダブルクオーツで囲われる。

  .. code-block:: python
    :linenos:

    nm.mvdelim(vf="item1", v=",", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # item1
    # "b,a,c"
    # "c,c"
    # "e,a,a"


関連メソッド
''''''''''''''''''''



