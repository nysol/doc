mslide 行ずらし
----------------------

指定した項目の値を指定した行数ずらして出力する。
例えば、日別の株価データにおいて収益率(当日の株価/前日の株価)を計算するなど
レコード間の演算を行いたい場合に利用する。
典型的な例を :numref:`mslide_input` 〜 :numref:`mslide_out3` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mslide_input

  date,val
  4/6,1
  4/7,2
  4/8,3
  4/9,4




.. csv-table:: f=val:nextVal
  :header-rows: 1
  :name: mslide_out1

  date,val,nextVal
  4/6,1,2
  4/7,2,3
  4/8,3,4




.. csv-table:: f=val:nextVal -r
  :header-rows: 1
  :name: mslide_out2

  date,val,nextVal
  4/7,2,1
  4/8,3,2
  4/9,4,3




.. csv-table:: f=val t=2
  :header-rows: 1
  :name: mslide_out3

  date,val,val1,val2
  4/6,1,2,3
  4/7,2,3,4


:numref:`mslide_input` に示される入力データは日別の集計値が4日分示されており、
スーパーの売上推移や株価推移と考えればよい。
この入力データについて、
日々の増加率(ここでは簡単のために「増加率=翌日の値/当日の値」とする)
を計算することを考える。
入力データに示される日付4/6〜4/9について、
それぞれの日の値(val)を１行上にずらし、
新しい項目(newVal)として出力した結果が :numref:`mslide_out1` に示されている。
この出力結果に対してmcalコマンドでnextVal/valを計算すれば増加率が求められる。
ちなみに、4/9の行が消えているのは、4/9の行の次の行が存在しないからである。
存在しない時も-nオプションを指定することでNULL値を出力することができる。
:numref:`mslide_out1` は、下の行の値を上にずらしたが、-rオプションを指定することで、
逆に(上の行の値を下に)ずらすことも可能である( :numref:`mslide_out2` )。
さらに、t=を指定することで、スライドの回数を指定することもできる。
t=2で実行した結果を :numref:`mslide_out3` に示している。
これは " ``mslide f=val:val1 | mslide f=val1:val2`` "のように、
mslideを複数回実行するのと同じ効果がある。
なお、 ``t=`` を指定した場合、新たに出力される項目名は、
``f=`` で指定した項目名に、1から始まる連番が付与されたものとなる。
また ``t=`` と ``l`` オプションを併用することで、最後にずらした結果のみを出力することも可能である。
mslideの機能はmwindowによく似ている。
mslideはレコード間の演算を項目演算として実現し、
一方で、mwindowはレコード間演算を行集計として実現している。
よって、mslideした後の演算はmcalやmselが主役となり、
一方でmwindowしたのちはmsumやmavgなどのデータ集約のコマンドが主役となる。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 必須

  | ずらす対象となる項目名を指定する。複数項目指定可能。
  | ``t=`` を指定しないときは、コロンに続いて窓キーの項目名を指定しなければならない。

**s=** : 型=str , 任意(default=)

  | ここで指定した項目(複数項目指定可)で並べ替えられた後、行をずらす。
  | ``q`` オプションを指定しないとき、 ``s=`` パラメータは必須。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | ここで指定された項目の値を単位に処理する。

**t=** : 型=str , 任意(default=)

  | ずらす回数を指定する。省略すれば ``t=1`` が設定される。

**r=** : 型=bool , 任意(default=False)

  | 逆方向に(上の値を下に)ずらす。

**n=** : 型=bool , 任意(default=False)

  | 次(前)の行がなくてもNULL値を出力する。

**l=** : 型=bool , 任意(default=False)

  | 最後にずらした結果のみを出力する。



共通パラメータ
''''''''''''''''''''

:ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullkey=<common_param_assert_nullkey>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
, :ref:`assert_nullout=<common_param_assert_nullout>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`q=<common_param_q>`
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
    '''date,val
    20130406,1
    20130407,2
    20130408,3
    20130409,4
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mslide(s="date", f="val:newVal", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # date%0,val,newVal
    # 20130406,1,2
    # 20130407,2,3
    # 20130408,3,4


**逆にずらした例**


  .. code-block:: python
    :linenos:

    nm.mslide(s="date", f="val:newVal", r=True, i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # date%0,val,newVal
    # 20130407,2,1
    # 20130408,3,2
    # 20130409,4,3


**複数回指定した場合**


  .. code-block:: python
    :linenos:

    nm.mslide(s="date", f="val", t="2", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # date%0,val,val1,val2
    # 20130406,1,2,3
    # 20130407,2,3,4


**最後にずらした項目だけを出力する例**


  .. code-block:: python
    :linenos:

    nm.mslide(s="date", f="val", t="2", l=True, i="dat1.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # date%0,val,val2
    # 20130406,1,3
    # 20130407,2,4


**複数項目名を変更して出力する例**


  .. code-block:: python
    :linenos:

    nm.mslide(s="date", f="date:d_,val:v_", t="2", i="dat1.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # date%0,val,d_1,d_2,v_1,v_2
    # 20130406,1,20130407,20130408,2,3
    # 20130407,2,20130408,20130409,3,4


関連メソッド
''''''''''''''''''''



