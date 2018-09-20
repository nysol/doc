dist 距離
--------------

* 書式1: dist(タイプ,num_1,num_2,...,n_k,num_{k+1},num_{k+2},...,num_{2k}) 


２つのk次元ベクトル( :math:`num_1,num_2,\cdots,n_k),(num_{k+1},num_{k+2},\cdots,num_{2k}` )の距離を計算する。
距離としては以下のものが利用できる。
詳細な定義はmsimを参照のこと。
egin{itemize}
\item  ``euclid`` : ユークリッド距離
\item  ``cityblock`` : 都市ブロック距離
\item  ``hamming`` : ハミング距離
\end{itemize}
ハミング距離については、値は文字型として指定しなければならない(以下の例を参考のこと)。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,x1,y1,x2,y2
    1,0,0,1,1
    2,0,1,2,0
    3,,,,
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,x1,y1,x2,y2
    1,a,b,a,c
    2,0,1,0,1
    3,,,,
    ''')


**ユークリッド距離**


  .. code-block:: python
    :linenos:

    nm.mcal(c='dist("euclid",${x1},${y1},${x2},${y2})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,x1,y1,x2,y2,rsl
    # 1,0,0,1,1,1.414213562
    # 2,0,1,2,0,2.236067977
    # 3,,,,,


**都市ブロック距離**


  .. code-block:: python
    :linenos:

    nm.mcal(c='dist("cityblock",${x1},${y1},${x2},${y2})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,x1,y1,x2,y2,rsl
    # 1,0,0,1,1,2
    # 2,0,1,2,0,3
    # 3,,,,,


**ハミング距離**

ハミング距離の計算では、値を文字列として指定していることに注意する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='dist("hamming",$s{x1},$s{y1},$s{x2},$s{y2})', a='rsl', i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,x1,y1,x2,y2,rsl
    # 1,a,b,a,c,1
    # 2,0,1,0,1,2
    # 3,,,,,


