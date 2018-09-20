null NULL値
--------------------

* 書式1: nulln() 
* 書式2: nulls() 
* 書式3: nulld() 
* 書式4: nullt() 
* 書式5: nullb() 


型に応じたNULL値を返す。
if関数と組み合わせてNULL値を出力したい時に使うことができる。


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
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,val
    1,a
    2,
    3,b
    ''')


**基本例**

rslという項目の全行にNULL値を出力する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='nulls()', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,rsl
    # 1,
    # 2,
    # 3,


**if文の中での利用**

if文の第二パラメータで数値を指定しているので、それに合わせてnulln()関数を用いる。

  .. code-block:: python
    :linenos:

    nm.mcal(c='if(${id}==1,1,nulln())', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,rsl
    # 1,1
    # 2,
    # 3,


**isnullと同等の指定**


  .. code-block:: python
    :linenos:

    nm.mcal(c='if(${val}==nulln(),"null","notNull")', a='rsl', i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,val,rsl
    # 1,a,
    # 2,,
    # 3,b,


