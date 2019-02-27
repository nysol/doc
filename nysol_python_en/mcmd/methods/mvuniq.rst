mvuniq ベクトル要素の単一化
----------------------------------

ベクトル型の項目の要素を単一化する。
内部的にはtree構造を利用して単一化をしているので、
出力される要素の順序は文字列昇順に並び変わる。
一方で、 ``n`` オプションを指定すると、
ベクトルを系列として考え、
要素を先頭から順番に走査し、互いに隣接した要素のみを単一化し出力する。

パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**vf=** : 型=str , 必須

  | 単一化する対象項目名を指定する。複数項目指定可能。
  | 結果の項目名を変更したいときは、:(コロン)に続けて新項目名を指定する。

**A=** : 型=bool , 任意(default=False)

  | ``vf=`` で:(コロン)に続けて指定した項目名で、新たな項目が追加される。
  | なお ``A`` オプションを指定した場合、 ``vf=`` パラメータで指定するすべての
  | 項目に新項目名を指定しなければならない。

**n=** : 型=bool , 任意(default=False)

  | ベクトルを系列と考え隣接する同一要素のみ単一化する

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
    b a c,1 1
    c c,2 2 3
    e a a,3 1
    ''')


**複数項目を単一化する例**


  .. code-block:: python
    :linenos:

    nm.mvuniq(vf="items1,items2", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # items1,items2
    # a b c,1
    # c,2 3
    # a e,1 3


関連メソッド
''''''''''''''''''''



