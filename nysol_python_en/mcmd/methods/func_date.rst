date 年月日
----------------

* 書式1: date(time) 


時刻 :math:`time` から年月日を8桁固定長文字列として取り出す。


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

    nm.mcal(c='date($t{time})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,time,rsl
    # 1,20000101000000,20000101
    # 2,20121021111213,20121021
    # 3,,
    # 4,19770812122212,19770812


