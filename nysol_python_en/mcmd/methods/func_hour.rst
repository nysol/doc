hour 時
------------

* 書式1: hour(time) 数値
* 書式2: hours(time) 2桁固定長文字列


時刻 :math:`time` から時刻を取り出す。
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

    nm.mcal(c='hour($t{time})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,time,rsl
    # 1,20000101000000,0
    # 2,20121021111213,11
    # 3,,
    # 4,19770812122212,12


**文字列とし出力**


  .. code-block:: python
    :linenos:

    nm.mcal(c='hours($t{time})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,time,rsl
    # 1,20000101000000,00
    # 2,20121021111213,11
    # 3,,
    # 4,19770812122212,12


