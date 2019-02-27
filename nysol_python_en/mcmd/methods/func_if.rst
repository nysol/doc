if 条件選択
--------------

* 書式1: if(bool,num1,num2) 
* 書式2: if(bool,str1,str2) 
* 書式3: if(bool,date1,date2) 
* 書式4: if(bool,time1,time2) 
* 書式5: if(bool,bool1,bool2) 


第1パラメータの値が真であれば第2パラメータを、偽であれば第3パラメータを返す。
第1パラメータがNULL値であればNULL値を返す。
第2パラメータと第3パラメータは同じ型でなくてはならないことに注意する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,time
    1,101215
    2,210110
    3,
    4,120001
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,val
    1,1
    2,0
    3,
    4,-2
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''id,val
    1,10
    2,0
    3,-5
    4,0
    ''')


**基本例**

time項目が数値として120000以下であれば"AM"、そうでなければ"PM"を出力する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='if(${time}<=120000,"AM","PM")', a='ampm', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,time,ampm
    # 1,101215,AM
    # 2,210110,PM
    # 3,,
    # 4,120001,PM


**真偽値による条件選択**

``$b{項目名}`` によって、データ上の値"1"は真、
"0"は偽、そしてその他の値はNULLとして解釈される。

  .. code-block:: python
    :linenos:

    nm.mcal(c='if($b{val},"true","false")', a='bool', i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,val,bool
    # 1,1,true
    # 2,0,false
    # 3,,
    # 4,-2,


**時刻型として比較**


  .. code-block:: python
    :linenos:

    nm.mcal(c='if($t{time}<=0t120000,"am","pm")', a='ampm', i="dat1.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # id,time,ampm
    # 1,101215,am
    # 2,210110,pm
    # 3,,
    # 4,120001,pm


**if関数のネスト**


  .. code-block:: python
    :linenos:

    nm.mcal(c='if(${val}>0,"plus",if(${val}<0,"minus","zero"))', a='sign', i="dat3.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # id,val,sign
    # 1,10,plus
    # 2,0,zero
    # 3,-5,minus
    # 4,0,zero


