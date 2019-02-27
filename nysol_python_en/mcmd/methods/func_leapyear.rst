leapyear 閏年判定
--------------------------

* 書式1: leapyear(date) 
* 書式2: leapyear(time) 


日付 :math:`date` もしくは時刻 :math:`time` が閏年かどうか判定する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,date
    1,20000101
    2,20121021
    3,
    4,19770812
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,time
    1,20000101000000
    2,20121021111213
    3,
    4,19770812122212
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='leapyear($d{date})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,date,rsl
    # 1,20000101,1
    # 2,20121021,1
    # 3,,
    # 4,19770812,0


**時刻型でも判定可能**


  .. code-block:: python
    :linenos:

    nm.mcal(c='leapyear($t{time})', a='rsl', i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,time,rsl
    # 1,20000101000000,1
    # 2,20121021111213,1
    # 3,,
    # 4,19770812122212,0


