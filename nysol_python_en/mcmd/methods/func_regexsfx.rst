regexsfx マッチ文字列のサフィックス
--------------------------------------------

* 書式1: regexsfx(str,正規表現) 
* 書式2: regexsfxw(str,正規表現) 


指定した正規表現が最長マッチする文字列 :math:`str` の部分文字列のサフィックス
(部分文字列より末尾側の文字列)を返す。
同じ文字列及び正規表現によってregexpfx関数,regexstr関数,regexsfx関数の3関数を実行した場合、
それぞれで得られた文字列をその順番に結合すると元の文字列が再現できる関係にある。
:math:`str` もしくは正規表現にマルチバイト文字を含み、
Shift\_JISなど文字の出現順によっては意に沿わない検索結果となる場合はregexsfxw関数を使うこと。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,str
    1,xcbbbayy
    2,xxcbaay
    3,
    4,bacabbca
    ''')


**基本例**

正規表現 ``c.*a`` に最も長くマッチする部分文字列のサフィックスを得る。
例えば ``id=4`` では、$str$項目の ``cabbca`` にマッチしており、そのサフィックス
すなわちnull文字を返している。
``regexstr,regexpfx`` と同じ入力データを使っているので、比較すると分かりやすい。

  .. code-block:: python
    :linenos:

    nm.mcal(c='regexsfx($s{str},"c.*a")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,xcbbbayy,yy
    # 2,xxcbaay,y
    # 3,,
    # 4,bacabbca,


