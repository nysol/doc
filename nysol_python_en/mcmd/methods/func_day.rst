day 日
----------

* 書式1: day(date) 
* 書式2: day(time) 
* 書式3: days(date) 
* 書式4: days(time) 


日付 :math:`date` もしくは時刻 :math:`time` から日を取り出す。
書式1,2では数値として、書式3,4では2桁固定長文字列として返す。


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

    nm.mcal(c='day($d{date})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,date,rsl
    # 1,20000101,1
    # 2,20121021,21
    # 3,,
    # 4,19770812,12


**時刻型でも可能**


  .. code-block:: python
    :linenos:

    nm.mcal(c='day($t{time})', a='rsl', i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,time,rsl
    # 1,20000101000000,1
    # 2,20121021111213,21
    # 3,,
    # 4,19770812122212,12


