mmvavg 移動平均の算出
------------------------------------------

移動平均(moving average)を算出する。
移動平均としては、単純移動平均($SMA$)、線形荷重移動平均($WMA$)、指数平滑移動平均($EMA$)の３種類の移動平均が計算可能である。
\if0 #no help# following sentences will not apear on the help document. \fi
ある時$t$における値を$x_t$で表したとき、$m$期の各種移動平均は式(\ref{eq:sma},\ref{eq:wma},\ref{eq:ema})で定義される。
\begin{eqnarray}
SMA_t=\frac{1}{m} \sum_{i=0}^{m-1} x_{t-i}
\label{eq:sma}
\end{eqnarray}
\begin{eqnarray}
WMA_t=\sum_{i=0}^{m-1} \frac{m-i}{S} x_{t-i},\ \ S=\sum_{i=1}^m i
\label{eq:wma}
\end{eqnarray}
\begin{eqnarray}
EMA_t=\alpha x_t + (1-\alpha)EMA_{t-1}
\label{eq:ema}
\end{eqnarray}

パラメータ
''''''''''''''''''''''

  .. list-table::
    :header-rows: 1

    * - キーワード
      - 内容

    * - | **i=**
        |   任意
        |   デフォルト:標準入力
      - |   入力データを指定する。
    * - | **o=**
        |   任意
        |   デフォルト:標準出力
      - |   出力データを指定する。
    * - | **s=**
        |   任意
        |   デフォルト:
      - |   ここで指定した項目(複数項目指定可)で並べ替えられた後、移動平均が計算される。
        |   ``q=True`` オプションを指定しないとき、 ``s=`` パラメータは必須。
    * - | **k=**
        |   任意
        |   デフォルト:
      - |   ここで指定された項目(複数項目指定可)を単位として集計する。
    * - | **f=**
        |   必須
      - |   移動平均を求める項目名リスト(複数項目指定可)を指定する。
    * - | **t=**
        |   任意
        |   デフォルト:
      - |   期間数を1以上の整数で指定する。
        |   ``exp=True`` 指定時に ``alpha=`` を指定すれば ``t=`` は指定できない。
    * - | **w=True|False**
        |   任意
        |   デフォルト:False
      - |   線形加重移動平均を求める。
    * - | **exp=True|False**
        |   任意
        |   デフォルト:False
      - |   指数平滑移動平均を求める。
    * - | **alpha=**
        |   任意
        |   デフォルト:
      - |   ``exp=True`` が指定された時の平滑化係数を実数値で与える。
        |   省略時は ``alpha=2/(t=の値+1)`` 。
    * - | **skip=**
        |   任意
        |   デフォルト:
      - |   出力を抑制する最初の行数。
        |   デフォルト値:  ``skip=(t=の値-1)`` ,  ``exp=True`` が指定された場合は ``skip=0``
    * - | **n=True|False**
        |   任意
        |   デフォルト:False
      - |   期間内にNULL値が1つでも含まれていると結果もNULL値とする。

共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
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
    '''id,value
    1,5
    2,1
    3,3
    4,4
    5,4
    6,6
    7,1
    8,4
    9,7
    ''')
            
    with open('dat2.csv','w') as f:
      f.write(
    '''id,key,value
    1,a,5
    2,a,1
    3,a,3
    4,a,4
    5,a,4
    6,b,6
    7,b,1
    8,b,4
    9,b,7
    ''')
            
    with open('dat3.csv','w') as f:
      f.write(
    '''key,value
    a,1
    a,2
    a,3
    a,4
    a,5
    b,6
    b,1
    b,4
    b,7
    ''')
    
**基本例**

最初の行は期数に満たないため出力されない。


  .. code-block:: python
    :linenos:

    >>> nm.mmvavg(s="id", f="value", t="2", i="dat1.csv", o="rsl1.csv").run()
    # ## rsl1.csv の内容
    # id%0,value
    # 2,3
    # 3,2
    # 4,3.5
    # 5,4
    # 6,5
    # 7,3.5
    # 8,2.5
    # 9,5.5

**基本例2**

最初の行は期数に満たないため出力されない。


  .. code-block:: python
    :linenos:

    >>> nm.mmvavg(s="id", f="value", t="2", w=True, i="dat1.csv", o="rsl2.csv").run()
    # ## rsl2.csv の内容
    # id%0,value
    # 2,2.333333333
    # 3,2.333333333
    # 4,3.666666667
    # 5,4
    # 6,5.333333333
    # 7,2.666666667
    # 8,3
    # 9,6

**基本例3**

指数平滑移動平均( ``exp=True`` )の場合は最初の行から出力される。


  .. code-block:: python
    :linenos:

    >>> nm.mmvavg(s="id", f="value", t="2", exp=True, i="dat1.csv", o="rsl3.csv").run()
    # ## rsl3.csv の内容
    # id%0,value
    # 1,5
    # 2,2.333333333
    # 3,2.777777778
    # 4,3.592592593
    # 5,3.864197531
    # 6,5.288065844
    # 7,2.429355281
    # 8,3.47645176
    # 9,5.82548392

**キーを指定する例**



  .. code-block:: python
    :linenos:

    >>> nm.mmvavg(s="key,id", k="key", f="value", t="2", i="dat2.csv", o="rsl4.csv").run()
    # ## rsl4.csv の内容
    # id,key,value
    # 2,a,3
    # 3,a,2
    # 4,a,3.5
    # 5,a,4
    # 7,b,3.5
    # 8,b,2.5
    # 9,b,5.5

**指定した期に満たなくても出力する例**



  .. code-block:: python
    :linenos:

    >>> nm.mmvavg(q=True, k="key", f="value", t="2", skip="0", i="dat3.csv", o="rsl5.csv").run()
    # ## rsl5.csv の内容
    # key,value
    # a,1
    # a,1.5
    # a,2.5
    # a,3.5
    # a,4.5
    # b,6
    # b,3.5
    # b,2.5
    # b,5.5



関連メソッド
''''''''''''

- :doc:`mmvstats` 
- :doc:`mmvsim` 
- :doc:`mwindow` 
