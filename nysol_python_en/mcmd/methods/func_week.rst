week 週
------------

* 書式1: week(date) 
* 書式2: week(time) 
* 書式3: week111(date) 
* 書式4: week111(time) 


日付 :math:`date` もしくは時刻 :math:`time` のISO8601で規定された週番号を返す。
ISO8601で規定された週番号とは、年の最初の木曜日を含む週をその年の第1週と規定している。
一方でweek111を利用すると、曜日に関係なく1/1を第1週の第1日目と考えて週番号を返す。


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
    1,20000102
    1,20000103
    1,20000104
    1,20000105
    1,20000106
    1,20000107
    1,20000108
    1,20000109
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

    nm.mcal(c='week($d{date})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,date,rsl
    # 1,20000101,52
    # 1,20000102,52
    # 1,20000103,1
    # 1,20000104,1
    # 1,20000105,1
    # 1,20000106,1
    # 1,20000107,1
    # 1,20000108,1
    # 1,20000109,1
    # 2,20121021,42
    # 3,,
    # 4,19770812,32


**時刻型でも可能**


  .. code-block:: python
    :linenos:

    nm.mcal(c='week($t{time})', a='rsl', i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,time,rsl
    # 1,20000101000000,52
    # 2,20121021111213,42
    # 3,,
    # 4,19770812122212,32


