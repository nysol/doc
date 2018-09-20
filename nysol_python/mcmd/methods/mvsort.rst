mvsort ベクトル要素のソート
----------------------------------

ベクトル型の項目をソートする。
ベクトル型の項目とは、 :numref:`mvsort_input` のitems項目のように、
スペースで区切られた複数の文字列を値として持つ項目である。
典型的な例を :numref:`mvsort_input` 〜 :numref:`mvsort_out3` に示す。
オプションに何も指定しなければ文字列昇順に並べられ( :numref:`mvsort_out1` )、
項目名の後ろに ``%`` に続けて ``n`` を付けることで数値順に並べられる( :numref:`mvsort_out2` )。
ただし、ベクトルにアルファベットや漢字が含まれる場合の動作は不定である。
また項目名の後ろに ``r`` を指定することで逆順に並べることもできる( :numref:`mvsort_out3` )。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mvsort_input

  no,items
  1,2 1 13
  2,4 5 2 5
  3,112 14
  4,5 31




.. csv-table:: 基本的な利用:ベクトルの要素を文字列昇順に並べる
  :header-rows: 1
  :name: mvsort_out1

  no,items
  1,1 13 2
  2,2 4 5 5
  3,112 14
  4,31 5




.. csv-table:: 数値昇順で並べる
  :header-rows: 1
  :name: mvsort_out2

  no,items
  1,1 2 13
  2,2 4 5 5
  3,14 112
  4,5 31




.. csv-table:: 数値降順として並べる
  :header-rows: 1
  :name: mvsort_out3

  no,items
  1,13 2 1
  2,5 5 4 2
  3,112 14
  4,31 5




パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**vf=** : 型=str , 必須

  | ソーティングするベクトル項目名を指定する。複数項目指定可能。
  | ``%`` に続けて ``n`` を指定すれば数値ソートに、
  | ``%`` に続けて ``r`` を指定すれば逆順ソートに、
  | また、 ``n`` と ``r`` の両方を指定すれば数値逆順ソートとなる。
  | 結果の項目名を変更したいときは、:(コロン)に続けて新項目名を指定する。

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
    '''items1,items2
    b a c,10 2
    c c,2 5 3
    e a a,1
    ''')


**複数項目を並べる例**

``item1`` 項目を文字列降順に並べ、 ``item2`` 項目を数値昇順に並べる。

  .. code-block:: python
    :linenos:

    nm.mvsort(vf="items1%r,items2%n", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # items1,items2
    # c b a,2 10
    # c c,2 3 5
    # e a a,1


関連メソッド
''''''''''''''''''''



