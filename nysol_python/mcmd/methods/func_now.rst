now 現在時刻
----------------

* 書式1: now() 
* 書式2: unow() 


now関数は時刻型で現在時刻を返す(秒単位)。
unow関数はマイクロ秒単位で現在時刻を返す。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id
    1
    2
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='now()', a='rsl', i="dat1.csv", o="rsl1-1.csv").run()
    nm.mcal(c='unow()', a='rsl', i="dat1.csv", o="rsl1-2.csv").run()
    ### rsl1-1.csv の内容
    # id,rsl
    # 1,20180920010817
    # 2,20180920010817


**時刻のみ切り出し**


  .. code-block:: python
    :linenos:

    nm.mcal(c='time(now())', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl1-2.csv の内容


**日付のみ切り出し**


  .. code-block:: python
    :linenos:

    nm.mcal(c='date(now())', a='rsl', i="dat1.csv", o="rsl3.csv").run()
    ### rsl2.csv の内容


