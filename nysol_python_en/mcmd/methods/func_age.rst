age 年令
------------

* 書式1: age(生年月日,date) 
* 書式2: age(生年月日,time) 


日付 :math:`date` (書式1)もしくは時刻 :math:`time` (書式2)における年令を返す。
生年月日は書式1,2によって日付型/時刻型を指定する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,dob
    1,19641010
    2,20000101
    3,
    4,19770812
    ''')


**基本例**

2013年9月1日における年令を求める。

  .. code-block:: python
    :linenos:

    nm.mcal(c='age($d{dob},0d20130901)', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,dob,rsl
    # 1,19641010,48
    # 2,20000101,13
    # 3,,
    # 4,19770812,36


