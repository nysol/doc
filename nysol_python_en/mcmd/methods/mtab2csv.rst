mtab2csv TSVからCSVデータへの変換
------------------------------------------------

タブ区切りデータをCSVデータへ変換する。
``d=`` で区切り文字を指定することで、タブ以外の区切り文字のテキストデータも
変換することが可能である。
変換後の項目数に違いある場合には、その直前行まで出力され、
その後エラー終了する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**d=** : 型=str , 任意(default=)

  | 区切り文字の指定(１バイト文字のみ指定可)。

**r=** : 型=bool , 任意(default=False)

  | 改行コード(CR:  ``\r``  )を取り除く。
  | MCMDが扱うCSVは改行コードがLF(  ``\n``  )固定であるため、
  | Windowsのテキスト改行CR+LF(  ``\r\n``  )やMacのテキスト改行CR(  ``\r``  )があれば、
  | 単なる文字列として扱ってしまい、変換後に不具合が生じる。
  | この問題を回避するためのオプションである。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`tmppath=<common_param_tmppath>`
, :ref:`precision=<common_param_precision>`


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.tab','w') as f:
      f.write(
    '''id	data	data2
    A	1102	a
    A	2203	aaa
    B	1155	bbbb
    B	3104	c
    B	1206	de
    ''')

    with open('dat2.bar','w') as f:
      f.write(
    '''id-data-data2
    A-1102-a
    A-2203-aaa
    B-1155-bbbb
    B-3104-c
    B-1206-de
    ''')


**基本例**

タブ区切りデータをcsvへ変換

  .. code-block:: python
    :linenos:

    nm.mtab2csv(i="dat1.tab", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,data,data2
    # A,1102,a
    # A,2203,aaa
    # B,1155,bbbb
    # B,3104,c
    # B,1206,de


**d=指定**

``d=`` を使用してtab以外の区切り文字を使う

  .. code-block:: python
    :linenos:

    nm.mtab2csv(d="-", i="dat2.bar", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,data,data2
    # A,1102,a
    # A,2203,aaa
    # B,1155,bbbb
    # B,3104,c
    # B,1206,de


関連メソッド
''''''''''''''''''''

* :doc:`mxml2csv` : 
* :doc:`msplit` : 

