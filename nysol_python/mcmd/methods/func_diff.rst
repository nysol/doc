diff 期間
--------------

* 書式1: diffyear(date_1,date_2) 
* 書式2: diffyear(time_1,time_2) 
* 書式3: diffmonth(date_1,date_2) 
* 書式4: diffmonth(time_1,time_2) 
* 書式5: diffday(date_1,date_2) 
* 書式6: diffday(time_1,time_2) 
* 書式7: diffhour(time_1,time_2) 
* 書式8: diffminute(time_1,time_2) 
* 書式9: diffsecond(time_1,time_2) 
* 書式10: diffusecond(time_1,time_2) 


二つの引数が日付型の場合、 :math:`date_1` と :math:`date_2` の差( :math:`date_1-date_2` )を計算し、
その年数(difyear)、月数(diffmonth)、日数(diffday)で計算する。
二つの引数が時刻型の場合、 :math:`time_1` と :math:`time_2` の差( :math:`time_1-time_2` )を計算し、
その年数(difyear)、月数(diffmonth)、日数(diffday)、
時間数(diffhour)、分数(diffminute)、秒数(diffsecond)、マイクロ秒数(diffusecond)で計算する。
端数は切り捨てられる。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,date
    1,19641010
    2,20000101
    3,20130831
    4,20130901
    5,20130902
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,time
    1,20120101000000
    2,20120101011112
    3,
    4,20111231235000
    5,20111231235000.123456
    ''')


**月単位での期間**

``date`` 項目から2013年9月1日までの経過期間を日数で計算する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='diffday(0d20130901,$d{date})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,date,rsl
    # 1,19641010,17858
    # 2,20000101,4992
    # 3,20130831,1
    # 4,20130901,0
    # 5,20130902,-1


**分単位での期間**

``time`` 項目から2012年1月1日 00時00分00秒までの経過期間を分単位で計算する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='diffmonth(0t20120101000000,$t{time})', a='rsl', i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,time,rsl
    # 1,20120101000000,0
    # 2,20120101011112,-1
    # 3,,
    # 4,20111231235000,0
    # 5,20111231235000.123456,0


**マイクロ秒単位での期間**

``time`` 項目から2012年1月1日 00時00分00秒までの経過期間を秒単位およびマイクロ秒単位で計算する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='diffsecond(0t20120101000000,$t{time})', a='rsl', i="dat2.csv", o="rsl3.csv").run()
    nm.mcal(c='diffusecond(0t20120101000000,$t{time})', a='rsl', i="dat2.csv", o="rsl4.csv").run()
    ### rsl3.csv の内容
    # id,time,rsl
    # 1,20120101000000,0
    # 2,20120101011112,-4272
    # 3,,
    # 4,20111231235000,600
    # 5,20111231235000.123456,599


