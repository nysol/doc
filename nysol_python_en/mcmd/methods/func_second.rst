second 秒
----------------

* 書式1: second(time) 数値
* 書式2: seconds(time) 2桁固定長文字列
* 書式3: usecond(time) 数値
* 書式4: useconds(time) 2桁.6桁固定長文字列


時刻 :math:`time` から秒を取り出す。
書式1では数値(整数)として秒を返し、書式2では秒の2桁を固定長文字列とした返す。
書式3は、マイクロ秒で返す。書式4では、秒の2桁固定長、マイクロ秒の小数6桁固定長を文字列として返す。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,time
    1,20000101121103
    2,20121021111209.123
    3,211209
    4,211209.123
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='second($t{time})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,time,rsl
    # 1,20000101121103,3
    # 2,20121021111209.123,9
    # 3,211209,9
    # 4,211209.123,9


**文字列とし出力**


  .. code-block:: python
    :linenos:

    nm.mcal(c='seconds($t{time})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,time,rsl
    # 1,20000101121103,03
    # 2,20121021111209.123,09
    # 3,211209,09
    # 4,211209.123,09


**マイクロ秒を出力**


  .. code-block:: python
    :linenos:

    nm.mcal(c='usecond($t{time})', a='rsl', i="dat1.csv", o="rsl3.csv").run()
    nm.mcal(c='useconds($t{time})', a='rsl', i="dat1.csv", o="rsl4.csv").run()
    ### rsl3.csv の内容
    # id,time,rsl
    # 1,20000101121103,3
    # 2,20121021111209.123,9.123
    # 3,211209,9
    # 4,211209.123,9.123


