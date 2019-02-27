mnewrand 乱数データの新規生成
--------------------------------------

0.0から1.0の範囲の実数乱数を生成する。
``int`` オプションを指定することで、整数乱数を生成することもできる。
乱数の生成にはメルセンヌ・ツイスター法を利用している
(\href{http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html}{原作者のページ}
, \href{http://www.boost.org/doc/libs/1_54_0/doc/html/boost_random.html}{boostライブラリ})。


パラメータ
''''''''''''''''''''''

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**a=** : 型=str , 必須

  | 新規に作成するデータの項目名を指定する。
  | ``nfn`` もしくは ``nfno`` オプション指定時は指定の必要はない。

**max=** : 型=str , 任意(default=INT\_MAX)

  | 乱数の最大値を指定する。
  | このパラメータを指定するときは ``int`` オプションも指定しなければならない。

**min=** : 型=str , 任意(default=0)

  | 乱数の最小値を指定する。
  | このパラメータを指定するときは ``int`` オプションも指定しなければならない。

**S=** : 型=str , 任意(default=現在時刻)

  | 乱数の種を指定する。

**l=** : 型=str , 任意(default=10)

  | 行数
  | 新規作成する乱数データの行数を指定する。

**int=** : 型=bool , 任意(default=False)

  | 整数乱数を生成する



共通パラメータ
''''''''''''''''''''

:ref:`o=<common_param_o>`
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


**基本例**

実数乱数を10行生成する。乱数の種は1に固定しているので、いつ実行しても乱数系列は同じになる。

  .. code-block:: python
    :linenos:

    nm.mnewrand(a="rand", S="1", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # rand
    # 0.4170219984
    # 0.9971848081
    # 0.7203244893
    # 0.9325573612
    # 0.0001143810805
    # 0.1281244478
    # 0.3023325677
    # 0.9990405154
    # 0.1467558926
    # 0.2360889763


**整数乱数**

最小値が0、最大値が1000、乱数の種が1の整数乱数を5行作成する。

  .. code-block:: python
    :linenos:

    nm.mnewrand(a="rand", int=True, max="1000", min="0", l="5", S="1", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # rand
    # 417
    # 998
    # 721
    # 933
    # 0


**ヘッダ行なしで出力**

``nfn=True`` でヘッダーなしのデータが生成される。

  .. code-block:: python
    :linenos:

    nm.mnewrand(nfn=True, l="5", S="1", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # 0.4170219984
    # 0.9971848081
    # 0.7203244893
    # 0.9325573612
    # 0.0001143810805


関連メソッド
''''''''''''''''''''

* :doc:`mnewnumber` : 連番を生成する。
* :doc:`mnewstr` : 固定文字列を生成する。

