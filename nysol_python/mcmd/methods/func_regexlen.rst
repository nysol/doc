regexlen マッチ文字数
------------------------------

* 書式1: regexlen(str,正規表現) 
* 書式2: regexlenw(str,正規表現) 


指定した正規表現が最長マッチする文字列 :math:`str` の部分文字列の長さを返す。
マッチしなければ0を返す。すなわち0文字にマッチしたと解釈する。
:math:`str` もしくは正規表現にマルチバイト文字を含む場合はregexlenw関数を使うこと。


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

    with open('dat2.csv','w') as f:
      f.write(
    '''id,str
    1,漢漢あbbbいyy
    2,漢あbいいy
    3,
    4,bあいあbbいあ
    ''')


**基本例**

正規表現 ``c.*a`` に最も長くマッチする部分文字列の長さを得る。
マッチした部分文字列については ``regexstr`` と同じ入力データを使っているので、比較すると分かりやすい。

  .. code-block:: python
    :linenos:

    nm.mcal(c='regexlen($s{str},"c.*a")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,xcbbbayy,5
    # 2,xxcbaay,4
    # 3,,0
    # 4,bacabbca,6


**マルチバイト文字**

正規表現 ``"あ.*い"`` に最も長くマッチする部分文字列の長さを得る。
ただし、以下ではマルチバイト文字対応でないregexlen関数を使っているので、
文字数ではなくバイト数を返している。

  .. code-block:: python
    :linenos:

    nm.mcal(c='regexlen($s{str},"あ.*い")', a='rsl', i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,str,rsl
    # 1,漢漢あbbbいyy,9
    # 2,漢あbいいy,10
    # 3,,0
    # 4,bあいあbbいあ,14


**マルチバイト文字2**

正規表現 ``"あ.*い"`` に最も長くマッチする部分文字列の長さを得る。
regexlenw関数を使うと、正しくマルチバイト文字を扱ってくれる。

  .. code-block:: python
    :linenos:

    nm.mcal(c='regexlenw($s{str},"あ.*い")', a='rsl', i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,str,rsl
    # 1,漢漢あbbbいyy,5
    # 2,漢あbいいy,4
    # 3,,0
    # 4,bあいあbbいあ,6


