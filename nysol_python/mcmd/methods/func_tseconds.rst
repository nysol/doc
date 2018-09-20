tseconds 経過秒数
--------------------------

* 書式1: tseconds(time) 
* 書式2: tuseconds(time) 


00:00:00から時刻 :math:`time` までの経過秒数を計算する。
tsecondsでは秒単位で、tusecondsではマイクロ秒単位で値を返す。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,time
    1,000103
    2,235959
    3,235959.123
    4,000000
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,time
    1,20130901000103
    2,20130902000103
    3,20130902000103.123
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='tseconds($t{time})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,time,rsl
    # 1,000103,63
    # 2,235959,86399
    # 3,235959.123,86399
    # 4,000000,0


**日付が異なっても結果は同じ**


  .. code-block:: python
    :linenos:

    nm.mcal(c='tseconds($t{time})', a='rsl', i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,time,rsl
    # 1,20130901000103,63
    # 2,20130902000103,63
    # 3,20130902000103.123,63


**マイクロ秒**


  .. code-block:: python
    :linenos:

    nm.mcal(c='tuseconds($t{time})', a='rsl', i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,time,rsl
    # 1,000103,63
    # 2,235959,86399
    # 3,235959.123,86399.123
    # 4,000000,0


