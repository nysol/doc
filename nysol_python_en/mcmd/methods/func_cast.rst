cast 型変換
----------------

* 書式1: s2n(str) 
* 書式2: n2s(num) 
* 書式3: n2b(num) 
* 書式4: s2n(str) 
* 書式5: s2d(str) 
* 書式6: s2t(str) 
* 書式7: s2b(str) 
* 書式8: d2s(date) 
* 書式9: d2t(date) 
* 書式10: t2s(time) 
* 書式11: t2d(time) 
* 書式12: b2n(bool) 
* 書式13: b2s(bool) 


型変換を行う関数群。
mcalでは型の自動変換は行わないため、必要なときはユーザが明示的に型変換を指定しなければならない。
n2b(s2b)関数は、1("1")を真に0("0")を偽に、それ以外をNULL値に変換する。
b2n(b2s)関数は、真は1("1")に偽は0("0")に変換する。
d2t関数は、日付型を時刻型に変換するが、そのとき時刻として12:00:00を自動的に補完する。
d2s関数は、8文字固定長文字列("yyyymmdd")に変換し、t2s関数は14文字固定長文字列("yyyymmddHHMMSS")に変換する。
日付/時刻についての詳細は「ef{sect:datetime}日付型と時刻型」を参照のこと。


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
    3
    4
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,v1,v2,v3
    1,10,5,7
    2,5,12,11
    3,3,6,2
    4,14,16,11
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''id,val
    1,10
    2,0
    3,-5
    4,0
    ''')


**乱数の固定長化**

1から9999の整数乱数を発生させ、4桁固定長で出力する。
fixlen関数は整数型のデータ(ここではrandiの結果)には対応していないので、
n2s関数で文字列型に変換する必要がある。

  .. code-block:: python
    :linenos:

    nm.mcal(c='fixlen(n2s(randi(1,9999,11)),4,"R","0")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,rsl
    # 1,1803
    # 2,0684
    # 3,0195
    # 4,6647


**真偽パターン**

項目v1,v2,v3が10異常かどうかを判定し、01のパターンを出力する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='cat("",b2s(${v1}>=10),b2s(${v2}>=10),b2s(${v3}>=10))', a='rsl', i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,v1,v2,v3,rsl
    # 1,10,5,7,100
    # 2,5,12,11,011
    # 3,3,6,2,000
    # 4,14,16,11,111


