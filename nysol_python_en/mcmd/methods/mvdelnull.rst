mvdelnull ベクトルのNULL要素の削除
------------------------------------------------

ベクトル要素でNULLの要素を全て削除する。
ベクトル要素がNULLであれば、要素の区切り文字が連続する。
以下に示したベクトルは全てNULLを含む。
ただし、わかりやすさのためにベクトルの末尾に  ``\n``  を記している。
上から順番に、3番目、1番目、4番目の要素がNULLである。

.. code-block:: bash
  :linenos:

  ab c\n
   ab\n
  abc \n



パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**vf=** : 型=str , 必須

  | NULL要素を削除する対象となる項目名( ``i=`` データ上)を指定する。
  | 複数項目指定可能。
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
    '''items
    b a  c
    c c
    e a   b
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''items
    b.a..c
    .c.c
    e.a...b.
    ''')


**nullを削除する基本例**


  .. code-block:: python
    :linenos:

    nm.mvdelnull(vf="items", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # items
    # b a c
    # c c
    # e a b


**分かりやすく区切り文字を.(ドット)にした例**


  .. code-block:: python
    :linenos:

    nm.mvdelnull(vf="items", delim=".", i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # items
    # b.a.c
    # c.c
    # e.a.b


**項目名を変更して出力**


  .. code-block:: python
    :linenos:

    nm.mvdelnull(vf="items:new", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # new
    # b a c
    # c c
    # e a b


**-Aを指定することで追加項目として出力**


  .. code-block:: python
    :linenos:

    nm.mvdelnull(vf="items:new", A=True, i="dat1.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # items,new
    # b a  c,b a c
    # c c,c c
    # e a   b,e a b


関連メソッド
''''''''''''''''''''

* :doc:`mvnullto` : NULL要素を任意の値に置換する。

