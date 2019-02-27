minute 分
----------------

* 書式1: minute(time) 数値
* 書式2: minutes(time) 2桁固定長文字列


時刻 :math:`time` から分を取り出す。
返す型によって、書式1,2を使い分ければよい。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
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

    nm.mcal(c='minute($t{time})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,time,rsl
    # 1,20000101000000,0
    # 2,20121021111213,12
    # 3,,
    # 4,19770812122212,22


**文字列とし出力**


  .. code-block:: python
    :linenos:

    nm.mcal(c='minutes($t{time})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,time,rsl
    # 1,20000101000000,00
    # 2,20121021111213,12
    # 3,,
    # 4,19770812122212,22


