julian ユリウス暦変換
----------------------------

* 書式1: julian(date) 
* 書式2: julian(time) 
* 書式3: julian2d(num) 
* 書式4: julian2t(num) 


書式1,2では、日付 :math:`date` もしくは時刻 :math:`time` をユリウス通日に変換する。
逆に書式3,4では、ユリウス通日を日付型もしくは時刻型に変換する。
ここで、日付型が与えられたときは、その日の最初の時刻である ``00:00:00`` として計算される。


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
    4,19700101
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,time
    1,20000101000000
    2,20121021111213
    3,
    4,19700101000100
    ''')


**基本例**

日付型の ``date`` 項目を ``julian`` 関数でユリウス通日に変換し、 ``julian2d`` 関数でまたもとに戻す。

  .. code-block:: python
    :linenos:

    nm.mcal(c='julian($d{date})', a='julian', i="dat1.csv", o="rsl1.csv").run()
    nm.mcal(c='julian2d(${julian})', a='date2', i="rsl1.csv", o="rsl2.csv").run()
    ### rsl1.csv の内容
    # id,date,julian
    # 1,20000101,2451545
    # 2,20121021,2456222
    # 3,,
    # 4,19700101,2440588


**時刻型も同様**


  .. code-block:: python
    :linenos:

    nm.mcal(c='julian($t{time})', a='julian', i="dat2.csv", o="rsl3.csv").run()
    nm.mcal(c='julian2t(${julian})', a='time2', i="rsl3.csv", o="rsl4.csv").run()
    ### rsl2.csv の内容


