month 月
--------------

* 書式1: month(date) 数値型月番号
* 書式2: month(time) 数値型月番号
* 書式3: months(date) 文字列型2桁固定長月番号
* 書式4: months(time) 文字列型2桁固定長月番号
* 書式5: monthe(date) 英語表記
* 書式6: monthe(time) 英語表記
* 書式7: monthes(date) 英語短縮表記
* 書式8: monthes(time) 英語短縮表記


日付 :math:`date` もしくは時刻 :math:`time` から月を返す。
月の表記によって書式1〜8を使い分ける。


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

    nm.mcal(c='month($d{date})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,date,rsl
    # 1,20000101,1
    # 2,20121021,10
    # 3,,
    # 4,19770812,8


**固定長文字列として**


  .. code-block:: python
    :linenos:

    nm.mcal(c='months($d{date})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,date,rsl
    # 1,20000101,01
    # 2,20121021,10
    # 3,,
    # 4,19770812,08


**英語表記**


  .. code-block:: python
    :linenos:

    nm.mcal(c='monthe($d{date})', a='rsl', i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,date,rsl
    # 1,20000101,January
    # 2,20121021,October
    # 3,,
    # 4,19770812,August


**英語短縮表記**


  .. code-block:: python
    :linenos:

    nm.mcal(c='monthes($d{date})', a='rsl', i="dat1.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # id,date,rsl
    # 1,20000101,Jan
    # 2,20121021,Oct
    # 3,,
    # 4,19770812,Aug


**時刻型でも可能**


  .. code-block:: python
    :linenos:

    nm.mcal(c='month($t{time})', a='rsl', i="dat2.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # id,time,rsl
    # 1,20000101000000,1
    # 2,20121021111213,10
    # 3,,
    # 4,19770812122212,8


