uxt UNIX時刻変換
------------------------

* 書式1: uxt(date) 
* 書式2: uxt(time) 
* 書式3: uxt2d(num) 
* 書式4: uxt2t(num) 


書式1,2では、日付 :math:`date` もしくは時刻 :math:`time` をUNIX時刻に変換する。
逆に書式3,4では、UNIX時刻を日付型もしくは時刻型に変換する。
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

日付型の ``date`` 項目を ``uxt`` 関数でUNIX時刻に変換し、 ``uxt2d`` 関数でまたもとに戻す。

  .. code-block:: python
    :linenos:

    nm.mcal(c='uxt($d{date})', a='uxt', i="dat1.csv", o="rsl1.csv").run()
    nm.mcal(c='uxt2d(${uxt})', a='date2', i="rsl1.csv", o="rsl2.csv").run()
    ### rsl1.csv の内容
    # id,date,uxt
    # 1,20000101,946684800
    # 2,20121021,1350777600
    # 3,,
    # 4,19700101,0


**時刻型も同様**


  .. code-block:: python
    :linenos:

    nm.mcal(c='uxt($t{time})', a='uxt', i="dat2.csv", o="rsl3.csv").run()
    nm.mcal(c='uxt2t(${uxt})', a='time2', i="rsl3.csv", o="rsl4.csv").run()
    ### rsl2.csv の内容


