
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
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
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

    * - メソッド名: 内容
      - パラメータ
    * - `__iter__: 行イテレータ`_
      - なし
    * - `getline: 出力形式指定行イテレータ`_
      - * ``dtype`` ={項目名:str|int|float|bool,...}
        * ``otype`` ="list" | "dict"
        * ``skeys`` =項目名リスト,
        * ``keys`` =項目名リスト
    * - keyblock: キー単位のイテレータ
      - * ``dtype`` ={項目名:str|int|float|bool,...}
        * ``otype`` ="list" | "dict"
        * ``skeys`` =項目名リスト,
        * ``keys`` =項目名リスト
    * - redirect(dir): 出力の切り替え
      - dir="u"
    * - run: 登録されたメソッドの実行
      - msg="off"|"one",runlimit=同時実行数(default:300)
    * - __ilshift__: <<=演算子
      - 左辺:処理フローオブジェクト,右辺:処理フローメソッド
    * - __rlshift__: <<=演算子
      - 処理フローオブジェクトの生成,左項None用 左辺:None,右辺:処理フローメソッド


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
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]
    for line in nm.mcut(f="customer,date,amount",i=dat):
      print(line)

  .. code-block:: sh
    :caption: :numref:`flow_iter` の実行結果
    :name: flow_iter_result

    ['A', '20180101', '5200']
    ['B', '20180101', '800']
    ['B', '20180112', '3500']
    ['A', '20180105', '2000']
    ['B', '20180107', '4000']

getline: 出力形式指定行イテレータ
.................................
``getline`` メソッドは、出力形式を制御できるイテレータである。
``dtype`` パラメータによって出力項目の型を指定し、``otype`` によってコンテナ型としてリストもしくは辞書を指定できる。
``dtype`` を指定しなければ、全ての項目は文字列として出力され、``otype`` を指定しなければリストで出力される。
また ``skeys`` で項目名を指定すると、事前に指定した項目でソーティングできる。
さらに ``keys`` の指定によりキーブレイク情報も出力可能となる。

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
  skeys=項目名リスト: 事前にソーティングを行う。そのソーティングキーを指定する。
      例) skeys="amount%nr,customer" # ``amount`` 項目数値逆順+ ``customer`` 項目昇順
  keys=項目名リスト: 指定された項目名リストに従ったキーブレイク情報も出力する。
    データは([データ],top,bottom)
      例) keys="customer,date"
=================================================================================================

:numref:`flow_getline` は、:numref:`flow_iter` と同様のデータについて、``amount`` のみを整数(``int`` )で出力し、
コンテナとして辞書型(``dict`` ) を指定している。

  .. code-block:: python
    :linenos:
    :caption: データ型を指定してのイテレータの利用スクリプト
    :name: flow_getline

    dtype = {'customer':'str', 'date':'str', 'amount':'int'}
    f=nm.mcut(f="customer,date,amount",i=dat).getline(dtype=dtype,otype="dict"):
    for line in f:
      print(line)

  .. code-block:: sh
    :caption: :numref:`flow_getline` の実行結果
    :name: flow_getline_result

    {'customer': 'A', 'date': '20180101', 'amount': 5200}
    {'customer': 'B', 'date': '20180101', 'amount': 800}
    {'customer': 'B', 'date': '20180112', 'amount': 3500}
    {'customer': 'A', 'date': '20180105', 'amount': 2000}
    {'customer': 'B', 'date': '20180107', 'amount': 4000}

:numref:`flow_getline_skeys` は、:numref:`flow_getline` に加えて、``amount`` で数値降順に並べ替えた後に繰り返し処理を行っている。
数値降順にするためには、項目名の後ろに ``%nr`` を付ける必要があるが、これはmcmdのソーティングに関する一般的規則[参照]に従っている。
なお、``dtype`` での型指定と ``skeys`` で指定するソーティングの型指定は、内部的には全く独立に動作する。
例えば、 ``skeys="amount%nr",dtype={"amount":"str"}`` としていても、並び順は数値降順( ``%nr`` )であり、
出力される ``amount`` 項目は文字列( ``"str"`` )となる。

  .. code-block:: python
    :linenos:
    :caption: ``amount`` で数値降順ソーティングしてから繰り返し処理
    :name: flow_getline_skeys

    f=nm.mcut(f="customer,date,amount",i=dat).getline(dtype=dtype,otype="dict",skeys="amount%nr"):
    for line in f:
      print(line)

  .. code-block:: sh
    :caption: :numref:`flow_getline_skeys` の実行結果
    :name: flow_getline_result

    {'customer': 'A', 'date': '20180101', 'amount': 5200}
    {'customer': 'B', 'date': '20180107', 'amount': 4000}
    {'customer': 'B', 'date': '20180112', 'amount': 3500}
    {'customer': 'A', 'date': '20180105', 'amount': 2000}
    {'customer': 'B', 'date': '20180101', 'amount': 800}

:numref:`flow_getline_keys` は、``customer`` 項目で並べ替えた時のキーブレイク情報を出力に付加する。
出力形式は、コンテナはタップルで、([行データリスト],先頭行フラグ,最終行フラグ)である。
先頭行フラグは、同じキー値の先頭行を読み込んでいるときのみ ``True`` となるBool値である。
最終行フラグは、同様に同じキー値の最終行を読み込んでいるときのみ ``False`` となるBool値である。
なお、同じキー内での並び順は、``skeys`` パラメータを用いれば良い。
:numref:`flow_getline_keys` では、 ``skeys="amount%nr"`` と指定しており、
結果として、``customer`` 昇順+ ``amount`` 数値降順で出力される。

  .. code-block:: python
    :linenos:
    :caption: ``customer`` でキーブレイク情報を付加
    :name: flow_getline_keys

    f=nm.mcut(f="customer,date,amount",i=dat).getline(keys="customer",skeys="amount%nr"):
    for line in f:
      print(line)

  .. code-block:: sh
    :caption: :numref:`flow_getline_keys` の実行結果。例えば、最初の行は、キー項目値 ``A``  の先頭行であるためタップル二番目の要素が ``True`` になっており、最終行はキー項目 ``B`` の最終行なのでタップル三番目の要素が ``True`` となっている。
    :name: flow_getline_result

    (['A', '20180101', '5200'], True, False)
    (['A', '20180105', '2000'], False, True)
    (['B', '20180101', '800'], True, False)
    (['B', '20180107', '4000'], False, False)
    (['B', '20180112', '3500'], False, True)

keyblock: キー単位のイテレータ
.................................
``getline`` メソッドが行単位で繰り返し処理をする一方で、``keyblock`` メソッドでは、キーブロック(キー項目の値が同じ行)を単位として繰り返し処理を行う。
よって、データは2重リストもしくは辞書inリストの形式で得られることになる。
指定可能なパラメータは ``getline`` メソッドと同様であるが、``keys`` の指定は必須である。

+-----------------------------------------------------------------------------------------------+
|**パラメータ**                                                                                 |
|                                                                                               |
|  keys=項目名リスト: キーブロックとなる項目を指定する。                                        |
|    データは([データ],top,bottom)                                                              |
|      例) keys="customer,date"                                                                 |
|  skeys=項目名リスト: キーブロック内でのソーティング項目を指定する。                           |
|      例) skeys="amount%nr,date" # ``amount`` 項目数値逆順+ ``date`` 項目昇順                  |
|  dtype={項目名:型,...}: 出力値の型を指定する                                                  |
|    辞書型データで指定し、キーに項目名、値にデータ型を指定する。変換可能なデータ型は次の通り。 |
|    "str":文字列, "int":整数, "float":実数, "bool":真偽値                                      |
|      例) dtype={"customer":"str","date":"str","amount":"int"}                                 |
|  otype=型: 出力データのコンテナ型を指定する                                                   |
|    "list"(リスト型),"dict"(辞書型)の2つの型を指定できる。                                     |
|    "list"を指定した場合、項目名ヘッダーは出力されない。                                       |
|    "dict"を指定した場合、辞書のキーが項目名で、値がその項目の値となる。                       |
|      例) otype="dict"                                                                         |
+-----------------------------------------------------------------------------------------------+

:numref:`flow_keyblock` は、:numref:`flow_iter` と同様のデータについて、``customer`` をキーブロック項目に指定した例である。
出力結果を見てもわかるように、``customer`` 項目の値ごとに繰り返し処理が行われており、行とブロックの二重リストでデータが得られる。
また、このケースでは ``skeys="date"`` と指定しているので、``customer`` の中では日付順に並んでいる。


  .. code-block:: python
    :linenos:
    :caption: キーブロック単位でのイテレータの利用スクリプト
    :name: flow_keyblock

    dtype = {'customer':'str', 'date':'str', 'amount':'int'}
    f=nm.mcut(f="customer,date,amount",i=dat).keyblock(keys="customer",skeys="date",dtype=dtype):
    for line in f:
      print(line)

  .. code-block:: sh
    :caption: :numref:`flow_keyblock` の実行結果
    :name: flow_keyblock_result

    [['A', '20180101', 5200], ['A', '20180105', 2000]]
    [['B', '20180101', 800], ['B', '20180107', 4000], ['B', '20180112', 3500]]

``dtype`` , ``otype`` の指定方法は``getline`` メソッドと同様である。
:numref:`flow_keyblock_dict` は、:numref:`flow_keyblock` の例を辞書型で出力した例である。

  .. code-block:: python
    :linenos:
    :caption: キーブロック単位でのイテレータで出力を辞書型にした例
    :name: flow_keyblock_dict

    dtype = {'customer':'str', 'date':'str', 'amount':'int'}
    f=nm.mcut(f="customer,date,amount",i=dat).keyblock(keys="customer",skeys="date",dtype=dtype,otype="dict"):
    for line in f:
      print(line)

  .. code-block:: sh
    :caption: :numref:`flow_keyblock_dict` の実行結果
    :name: flow_keyblock_dict_result

    [{'customer': 'A', 'date': '20180101', 'amount': 5200},{'customer': 'A', 'date': '20180105', 'amount': 2000}]
    [{'customer': 'B', 'date': '20180101', 'amount': 800},{'customer': 'B', 'date': '20180107', 'amount': 4000},{'customer': 'B', 'date': '20180112', 'amount': 3500}]

同じキーの行数が膨大なデータに対して ``keyblock`` を利用する場合は注意が必要である。
``keyblock`` メソッドは、メモリが許す限り、ブロック内のデータをpythonのリスト上に展開しようと試みるが、
メモリ制限を超えた場合の動作は不定である。

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
    drawModelsD3|登録されたmcmdメソッドの情報をSVG(html)で出力する


