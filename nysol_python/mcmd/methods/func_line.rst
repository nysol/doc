line 行番号
----------------

* 書式1: line() 


mcalコマンドが処理中の行番号を返す。
mcmdでは行番号は全て0から始まるように統一されており、
line関数においても、データの先頭行の行番号は0であることに注意する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id
    1
    2
    3
    4
    ''')


**基本例**

0から始まる番号が出力される。

  .. code-block:: python
    :linenos:

    nm.mcal(c='line()', a='no', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,no
    # 1,0
    # 2,1
    # 3,2
    # 4,3


**1から始める**

1から始まる番号を出力する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='line()+1', a='no', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,no
    # 1,1
    # 2,2
    # 3,3
    # 4,4


