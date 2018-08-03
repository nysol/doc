
処理フロー
-----------------------

mcmdでは、単一機能に特化した80以上のメソッドを自由に組み合わせることで、
データ処理の複雑なフローを構築することができ、それらは並列で処理される。
このようなフロー全体のことを **データ処理フロー** もしくは単に **処理フロー** と呼ぶ。
そして処理フローを扱うオブジェクトを **データ処理フローオブジェクト**  もしくは単に **処理フローオブジェクト** と呼ぶ。
以下では、単純な例から始め、mcmdがデータ処理フローをどのように扱うかについて説明する。

基本例
'''''''''''''''
単純なデータ処理フローから始めよう。
図 :numref:`flow_base` は、「 :doc:`はじめよう<hello>` 」節の :numref:`hello_ope` に示したフローである。
2重リストに格納された3項目5行のデータを入力データとして、
``mcut`` メソッドにより、 ``customer`` と ``amount`` 項目のみを切り出し、
``amount`` 項目を合計するというものである。

  .. code-block:: python
    :linenos:
    :caption: 処理フローの基本例
    :name: flow_base

    >>> import nysol.mcmd as nm
    >>> dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",4000],
    ["B","20180101",3500],
    ["A","20180101",2000],
    ["B","20180101",800]
    ]
    >>> f=None
    >>> f <<= nm.mcut(f="customer,amount",i=dat)
    >>> f <<= nm.msum(k="customer",f="amount")
    >>> f.run()
    [['A', '7200'], ['B', '8300']]

``<<=`` 演算子により、左辺の処理フローオブジェクトに右辺のメソッドが追加登録される。
左辺が ``None`` の場合は、新規に処理フローオブジェクトが生成され、メソッドが登録される。
登録順は重要で、明示的な接続関係(後述)を設定しなければ、前のメソッドの出力データが次のメソッドの入力データとして接続される。
:numref:`flow_base` では、``mcut`` の出力が ``msum`` の入力として接続される。

また、``drawModelD3`` メソッドを利用すれば処理フロー全体を視覚化することができる( :numref:`flow_drawModel` )。
結果は :numref:`flow_drawModelPNG` に示されるように、メソッドの接続関係を有向グラフで描画される。
円のノードでメソッドを、四角のノードでデータを表しており、メソッド名が薄字のものは、mcmdが実行時に裏で追加した処理を示している。

  .. code-block:: python
    :linenos:
    :caption: 処理フローの視覚化
    :name: flow_drawModel

    nm.drawModelsD3(f,"cust_amount.html") 

  .. figure:: flowChart.png
    :scale: 40%
    :align: center
    :name: flow_drawModelPNG
    :target: ../_static/cust_amount.html
    :alt: Alternate Text (キャプションじゃないよ)

    視覚化された処理フロー


処理フローオプジェクト
''''''''''''''''''''''''

処理フローオプジェクトには、[参照]に示された80以上のデータ処理メソッドが定義されており、
それらのメソッドをcallすると、その内容が処理フローオブジェクトに追加登録される。
処理フローオブジェクトには、データ処理メソッド以外にも、以下に示すメンバーメソッドとクラスメソッドが定義されている。

メンバーメソッド
::::::::::::::::::::
  .. list-table:: 処理フローオブジェクトで利用できるメンバーメソッド一覧
    :header-rows: 1
    :name: flow_mmethod

    * - メソッド名
      - 内容
      - パラメータ
    * - getline
      - 型指定付き行イテレータ
      - dtype={項目名:str|int|float|bool,...},otype="list" | "dict"
    * - __iter__
      - 行イテレータ
      - なし
    * - keyblock
      - キーブロックイテレータ
      - keys,skeys=None,dtype=None,otype="list"
    * - redirect(dir)
      - 出力の切り替え
      - dir="u"
    * - run
      - 登録されたメソッドの実行
      - msg="off"|"one",runlimit=同時実行数(default:300)
    * - __ilshift__ 
      - <<=演算子
      - 左辺:処理フローオブジェクト,右辺:処理フローメソッド
    * - __rlshift__
      - <<=演算子(処理フローオブジェクトの生成,左項None用)
      - 左辺:None,右辺:処理フローメソッド


__iter__: 行イテレータ
..........................
処理フローオブジェクトにはイテレータメソッド(__iter__)が定義されており、
行単位にリストに出力する繰り返し処理を可能としている。
図:numref:`flow_iter` は、for in 文を使って一行づつ出力している例である。
すべての値は文字列として出力されることに注意されたい。
これは、mcmdが内部ではデータをすべてテキストのバイトストリームとして処理しているためである。
項目別に型を指定するのであれば、``getline`` メソッドを使えば良い。
また、先頭の項目名行は出力されないのは仕様である。
項目名でデータを扱いたければ、これも``getline`` メソッドを使えば辞書型として出力される。

  .. code-block:: python
    :linenos:
    :caption: イテレータの利用スクリプト
    :name: flow_iter

    import nysol.mcmd as nm
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",4000],
    ["B","20180101",3500],
    ["A","20180101",2000],
    ["B","20180101",800]
    ]
    for line in nm.mcut(f="customer,date,amount",i=dat):
      print(line)

  .. code-block:: sh
    :caption: :numref:`flow_iter` の実行結果
    :name: flow_iter_result

    ['A', '20180101', '5200']
    ['B', '20180101', '4000']
    ['B', '20180101', '3500']
    ['A', '20180101', '2000']
    ['B', '20180101', '800']

getline: 型指定付き行イテレータ
.................................
``getline`` メソッドは、出力形式を制御できるイテレータである。
``dtype`` パラメータによって出力項目の型を指定し、``otype`` によってコンテナ型としてリストもしくは辞書を指定できる。
``dtype`` を指定しなければ、全ての項目は文字列として出力され、``otype`` を指定しなければリストで出力される。


=================================================================================================

**パラメータ**
  dtype={項目名:型,...}: 出力値の型を指定する
    辞書型データで指定し、キーに項目名、値にデータ型を指定する。変換可能なデータ型は次の通り。
    "str":文字列, "int":整数, "float":実数, "bool":真偽値
      例) dtype={"customer":"str","date":"str","amount":"int"}
  otype=型: 出力データのコンテナ型を指定する
    "list"(リスト型),"dict"(辞書型)の2つの型を指定できる。
    "list"を指定した場合、項目名ヘッダーは出力されない。
    "dict"を指定した場合、辞書のキーが項目名で、値がその項目の値となる。
      例) otype="dict"
=================================================================================================

:numref:`flow_getline` は、:numref:`flow_iter` と同様のデータについて、``amount`` のみを整数(``int`` )で出力し、
コンテナとして辞書型(``dict`` ) を指定している。

  .. code-block:: python
    :linenos:
    :caption: データ型を指定してのイテレータの利用スクリプト
    :name: flow_getline

    dtype = {'customer':'str', 'date':'str', 'amount':'int'}
    f=nm.mcut(f="customer,date,amount",i=dat).getline(dtype=dtype,otype="dic"):
    for line in f:
      print(line)

  .. code-block:: sh
    :caption: :numref:`flow_getline` の実行結果
    :name: flow_getline_result

    {'customer': 'A', 'date': '20180101', 'amount': 5200}
    {'customer': 'B', 'date': '20180101', 'amount': 4000}
    {'customer': 'B', 'date': '20180101', 'amount': 3500}
    {'customer': 'A', 'date': '20180101', 'amount': 2000}
    {'customer': 'B', 'date': '20180101', 'amount': 800}

クラスメソッド
::::::::::::::::::::

  .. csv-table:: 処理フローオブジェクトにで利用できるクラスメソッド一覧
    :delim: |
    :header-rows: 1
    :name: flow_mmethod

    メソッド名|内容
    runs(obj)|リストobjに登録された処理フローオブジェクトをすべて実行する
    modelInfos|登録されたmcmdメソッドの情報を出力する
    drawModels|登録されたmcmdメソッドの情報を出力する
    drawModelsSVG|登録されたmcmdメソッドの情報をSVG(html)で出力する


