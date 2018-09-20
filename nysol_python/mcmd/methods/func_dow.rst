dow 曜日
------------

* 書式1: dow(date) 曜日番号(1〜7)
* 書式2: dow(time) 曜日番号(1〜7)
* 書式3: dowj(date) 日本語曜日
* 書式4: dowj(time) 日本語曜日
* 書式5: dowe(date) 英語曜日
* 書式6: dowe(time) 英語曜日
* 書式7: dowes(date) 英語短縮曜日
* 書式8: dowes(time) 英語短縮曜日


日付 :math:`date` もしくは時刻 :math:`time` から曜日を返す。
曜日の表記によって書式1〜8を使い分ける。
曜日番号は、ISO8601の規定に従い、1が月曜日で7が日曜日に対応する。


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

    nm.mcal(c='dow($d{date})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,date,rsl
    # 1,20000101,6
    # 2,20121021,7
    # 3,,
    # 4,19770812,5


**日本語表記**


  .. code-block:: python
    :linenos:

    nm.mcal(c='dowj($d{date})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,date,rsl
    # 1,20000101,土
    # 2,20121021,日
    # 3,,
    # 4,19770812,金


**英語表記**


  .. code-block:: python
    :linenos:

    nm.mcal(c='dowe($d{date})', a='rsl', i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,date,rsl
    # 1,20000101,Saturday
    # 2,20121021,Sunday
    # 3,,
    # 4,19770812,Friday


**英語短縮表記**


  .. code-block:: python
    :linenos:

    nm.mcal(c='dowes($d{date})', a='rsl', i="dat1.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # id,date,rsl
    # 1,20000101,Sat
    # 2,20121021,Sun
    # 3,,
    # 4,19770812,Fri


**時刻型でも可能**


  .. code-block:: python
    :linenos:

    nm.mcal(c='dow($t{time})', a='rsl', i="dat2.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # id,time,rsl
    # 1,20000101000000,6
    # 2,20121021111213,7
    # 3,,
    # 4,19770812122212,5


