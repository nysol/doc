match 検索
----------------

* 書式1: match(検索文字列,str_1,str_2,...) 
* 書式2: matcha(検索文字列,str_1,str_2,...) 
* 書式3: matchs(検索文字列,str_1,str_2,...) 
* 書式4: matchas(検索文字列,str_1,str_2,...) 


:math:`str_1,str_2,\cdots` から指定した検索文字列を検索し、
マッチすれば真をマッチしなければ偽を返す。
OR検索かAND検索か、そして完全一致か部分一致かにより、
表ef{tbl:func_match_cond}に示すとおり異なる関数名を指定する。
egin{table}[htbp]
egin{center}
\caption{入力データ\label{tbl:func_match_cond}}
{\small
egin{tabular}{l|ll}
\hline
& OR検索 & AND検索 \
\hline
完全一致 & match  & matcha  \
部分一致 & matchs & matchas \
\hline
\end{tabular}
}
\end{center}
\end{table}
``match`` 関数は、指定した検索文字列が、 :math:`str_1,str_2,\cdots` のいずれかに完全一致すれば真を返す。
``matcha`` 関数は、指定した検索文字列が、 :math:`str_1,str_2,\cdots` の全てに完全一致すれば真を返す。
``matchs`` 関数は、指定した検索文字列が、 :math:`str_1,str_2,\cdots` のいずれかに部分一致すれば真を返す。
``matchas`` 関数は、指定した検索文字列が、 :math:`str_1,str_2,\cdots` の全てに部分一致すれば真を返す。
NULL値を含めたOR/AND論理演算の真偽値表は表ef{tbl:mcal_and}を参照のこと。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,f1,f2,f3
    1,1,1,1
    2,1,0,1
    3,,,
    4,1,,1
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,s1,s2,s3
    1,ab,abx,x
    2,abc,xaby,xxab
    3,,,
    4,#ac,x,x
    ''')


**OR完全一致**

``f1,f2,f3`` 項目のいずれかが ``1`` であれば真を返す。

  .. code-block:: python
    :linenos:

    nm.mcal(c='match("1",$s{f1},$s{f2},$s{f3})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,f1,f2,f3,rsl
    # 1,1,1,1,1
    # 2,1,0,1,1
    # 3,,,,0
    # 4,1,,1,1


**AND完全一致**

``f1,f2,f3`` 項目の全てが文字列 ``"1"`` であれば真を返す。

  .. code-block:: python
    :linenos:

    nm.mcal(c='matcha("1",$s{f1},$s{f2},$s{f3})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,f1,f2,f3,rsl
    # 1,1,1,1,1
    # 2,1,0,1,0
    # 3,,,,0
    # 4,1,,1,0


**OR部分一致**

``s1,s2,s3`` 項目のいずれかが、文字列 ``ab`` を含んでいれば真を返す。

  .. code-block:: python
    :linenos:

    nm.mcal(c='matchs("ab",$s{s1},$s{s2},$s{s3})', a='rsl', i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,s1,s2,s3,rsl
    # 1,ab,abx,x,1
    # 2,abc,xaby,xxab,1
    # 3,,,,0
    # 4,#ac,x,x,0


**AND部分一致**

文字列 ``ab`` が ``s1,s2,s3`` 項目の全てに、文字列 ``ab`` が含まれて入れば真を返す。

  .. code-block:: python
    :linenos:

    nm.mcal(c='matchas("ab",$s{s1},$s{s2},$s{s3})', a='rsl', i="dat2.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # id,s1,s2,s3,rsl
    # 1,ab,abx,x,0
    # 2,abc,xaby,xxab,1
    # 3,,,,0
    # 4,#ac,x,x,0


**NULL値の検索**

``str`` 項目がNULL値であれば真を返す。

  .. code-block:: python
    :linenos:

    nm.mcal(c='match(nulls(),$s{s1},$s{s2},$s{s3})', a='rsl', i="dat2.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # id,s1,s2,s3,rsl
    # 1,ab,abx,x,0
    # 2,abc,xaby,xxab,0
    # 3,,,,1
    # 4,#ac,x,x,0


