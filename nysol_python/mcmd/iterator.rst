
イテレータ
=======================
mcmdでは行単位およびキー単位のイテレータが用意されている。
既存のmcmdメソッドを組み合わせるだけでは困難な処理があった場合に利用でき、
行単位もしくはキーブロック単位で処理するPythonコードを書くことができる。
表 :numref:`iterator_list` にmcmdが提供するイテレータの一覧を示している。

  .. list-table:: 処理フローオブジェクトで利用できるメンバーメソッド一覧
    :header-rows: 1
    :name: iterator_list

    * - メソッド名: 内容
      - パラメータ
    * - `__iter__: 行イテレータ`_
      - なし
    * - `getline: 出力形式指定行イテレータ`_
      - * ``dtype`` ={項目名:str|int|float|bool,...}
        * ``otype`` ="list" | "dict"
        * ``skeys`` =項目名リスト,
        * ``keys`` =項目名リスト
        * ``header`` =True|False
        * ``q`` =True|False
    * - `keyblock: キー単位のイテレータ`_
      - * ``dtype`` ={項目名:str|int|float|bool,...}
        * ``otype`` ="list" | "dict"
        * ``skeys`` =項目名リスト,
        * ``keys`` =項目名リスト
        * ``header`` =True|False
        * ``q`` =True|False


__iter__: 行イテレータ
---------------------------
処理フローオブジェクトにはイテレータメソッド(__iter__)が定義されており、
行単位にリストに出力する繰り返し処理を可能としている。
図 :numref:`flow_iter` は、for-in 文を使って一行づつ出力している例である。
すべての値は文字列として出力されることに注意されたい。
これは、mcmdが内部ではデータをすべてテキストのバイトストリームとして処理しているためである。
項目別に型を指定するのであれば、``getline`` メソッドを使えば良い。
また、先頭の項目名行は出力されないのは仕様であり、これも ``getline`` を使えば出力できる。

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
------------------------------------------
``getline`` メソッドは、出力形式を制御できるイテレータである。
``otype="dict"`` を指定することで、リストではなく項目名をキーとする辞書型で出力することが可能で、
``header=True`` でヘッダー行を出力することが可能となる。
``dtype`` パラメータによって出力項目の型を指定し、``otype`` によってコンテナ型としてリストもしくは辞書を指定できる。
``dtype`` を指定しなければ、全ての項目は文字列として出力され、``otype`` を指定しなければリストで出力される。
また ``skeys`` で項目名を指定すると、事前に指定した項目でソーティングできる。
さらに ``keys`` の指定によりキーブレイク情報も出力可能となる。


.. list-table::
  :header-rows: 1

  * - パラメータ
    - 内容
  * - | **dtype={項目名:型,...}**
      |   optional
      |   default:全項目"str"型
    - | 辞書型データで指定し、キーに項目名、値にデータ型を指定する。
      |   変換可能なデータ型は次の通り。
      |   "str":文字列, "int":整数, "float":実数, "bool":真偽値
      | 例) dtype={"customer":"str","date":"str","amount":"int"}
  * - | **otype=型**
      |   optional
      |   default:"list"
    - | 出力データのコンテナ型を指定する。
      |   "list"(リスト型),"dict"(辞書型)の2つの型を指定できる。
      |   "list"を指定した場合、項目名ヘッダーは出力されない。
      |   "dict"を指定した場合、辞書のキーが項目名で、値がその項目の値となる。
      | 例) otype="dict"
  * - | **skeys=項目名リスト**
      |   optional
      |   default:sortingなし
    - | 事前にソーティングを行う。そのソーティングキーを指定する。
      | 例) skeys="amount%nr,customer" # ``amount`` 項目数値降順+ ``customer`` 項目昇順
  * - | **keys=項目名リスト**
      |   optional
      |   default:キーブレイク情報の出力なし
    - | 指定された項目名リストに従ったキーブレイク情報も出力する。
      |   出力されるデータ形式はタプルで、([行データ],top,bottom)となる。
      | 例) keys="customer,date"
  * - | **header=True|False**
      |   optional
      |   default:False
    - | ヘッダー行も出力する。
  * - | **q=True|False**
      |   optional
      |   default:False
    - | ``k=`` 項目で事前にソートしない。

:numref:`iter_header` は、:numref:`flow_iter` と同様の処理を項目名ヘッダーの出力を加えた処理になっている。

  .. code-block:: python
    :linenos:
    :caption: データ型を指定してのイテレータの利用スクリプト
    :name: iter_header

    f=nm.mcut(f="customer,date,amount",i=dat).getline(header=True)
    for line in f:
      print(line)
    # 以下、出力内容
    # ['customer', 'date', 'amount']
    # ['A', '20180101', '5200']
    # ['B', '20180101', '800']
    # ['B', '20180112', '3500']
    # ['A', '20180105', '2000']
    # ['B', '20180107', '4000']


:numref:`flow_getline` は、 :numref:`flow_iter` と同様のデータについて、``amount`` のみを整数(``int`` )で出力し、
コンテナとして辞書型(``dict`` ) を指定している。

  .. code-block:: python
    :linenos:
    :caption: データ型を指定してのイテレータの利用スクリプト
    :name: flow_getline

    dtype = {'customer':'str', 'date':'str', 'amount':'int'}
    f=nm.mcut(f="customer,date,amount",i=dat).getline(dtype=dtype,otype="dict")
    for line in f:
      print(line)
    # {'customer': 'A', 'date': '20180101', 'amount': 5200}
    # {'customer': 'B', 'date': '20180101', 'amount': 800}
    # {'customer': 'B', 'date': '20180112', 'amount': 3500}
    # {'customer': 'A', 'date': '20180105', 'amount': 2000}
    # {'customer': 'B', 'date': '20180107', 'amount': 4000}

:numref:`flow_getline_skeys` は、:numref:`flow_getline` に加えて、``amount`` で数値降順に並べ替えた後に繰り返し処理を行っている。
数値降順にするためには、項目名の後ろに ``%nr`` を付ける必要があるが、これはmcmdのソーティングに関する一般的規則[参照]に従っている。
なお、``dtype`` での型指定と ``skeys`` で指定するソーティングの型指定は、内部的には全く独立に動作する。
例えば、 ``skeys="amount%nr",dtype={"amount":"str"}`` としていても、並び順は数値降順( ``%nr`` )であり、
出力される ``amount`` 項目は文字列( ``"str"`` )となる。

  .. code-block:: python
    :linenos:
    :caption: ``amount`` で数値降順ソーティングしてから繰り返し処理
    :name: flow_getline_skeys

    f=nm.mcut(f="customer,date,amount",i=dat).getline(dtype=dtype,otype="dict",skeys="amount%nr")
    for line in f:
      print(line)
    # {'customer': 'A', 'date': '20180101', 'amount': 5200}
    # {'customer': 'B', 'date': '20180107', 'amount': 4000}
    # {'customer': 'B', 'date': '20180112', 'amount': 3500}
    # {'customer': 'A', 'date': '20180105', 'amount': 2000}
    # {'customer': 'B', 'date': '20180101', 'amount': 800}

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

    f=nm.mcut(f="customer,date,amount",i=dat).getline(keys="customer",skeys="amount%nr")
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
------------------------------------------
``getline`` メソッドが行単位で繰り返し処理をする一方で、``keyblock`` メソッドでは、キーブロック(キー項目の値が同じ行)を単位として繰り返し処理を行う。
よって、データは2重リストもしくは辞書inリストの形式で得られることになる。
指定可能なパラメータは ``getline`` メソッドと同様であるが、``keys`` の指定は必須である。


.. list-table::
  :header-rows: 1

  * - パラメータ
    - 内容
  * - | **keys=項目名リスト**
      |   必須
    - | キーブロックとなる項目を指定する。
      |   出力されるデータ形式は二重リスト(もしくはdict要素のリスト)で、
      |   ([[行データ1],[行データ2],...,[行データn])となる(nはブロックに含まれる行数)。
      | 例) keys="customer"
  * - | **skeys=項目名リスト**
      |   optional
      |   default:sortingなし
    - | キーブロック内でのソーティング項目を指定する。
      | 例) skeys="amount%n" # ``amount`` 項目数値昇順
  * - | **dtype={項目名:型,...}**
      |   optional
      |   default:全項目"str"型
    - | 辞書型データで指定し、キーに項目名、値にデータ型を指定する。
      |   変換可能なデータ型は次の通り。
      |   "str":文字列, "int":整数, "float":実数, "bool":真偽値
      | 例) dtype={"customer":"str","date":"str","amount":"int"}
  * - | **otype=型**
      |   optional
      |   default:"list"
    - | 出力データのコンテナ型を指定する。
      |   "list"(リスト型),"dict"(辞書型)の2つの型を指定できる。
      |   "list"を指定した場合、項目名ヘッダーは出力されない。
      |   "dict"を指定した場合、辞書のキーが項目名で、値がその項目の値となる。
      | 例) otype="dict"
  * - | **header=True|False**
      |   optional
      |   default:False
    - | ヘッダー行も出力する。
  * - | **q=True|False**
      |   optional
      |   default:False
    - | ``k=`` 項目で事前にソートしない。

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
    # [['A', '20180101', 5200], ['A', '20180105', 2000]]
    # [['B', '20180101', 800], ['B', '20180107', 4000], ['B', '20180112', 3500]]

``header=True`` を付けた場合は、最初に項目名ヘッダー行がブロックとして二重リストで出力される( :numref:`flow_keyblock_header` )。

  .. code-block:: python
    :linenos:
    :caption: 項目名ヘッダーも出力する例
    :name: flow_keyblock_header

    dtype = {'customer':'str', 'date':'str', 'amount':'int'}
    f=nm.mcut(f="customer,date,amount",i=dat).keyblock(header=True,keys="customer",skeys="date",dtype=dtype):
    for line in f:
      print(line)
    # [['customer', 'date', 'amount']]
    # [['A', '20180101', 5200], ['A', '20180105', 2000]]
    # [['B', '20180101', 800], ['B', '20180107', 4000], ['B', '20180112', 3500]]


``dtype`` , ``otype`` の指定方法は ``getline`` メソッドと同様である。
:numref:`flow_keyblock_dict` は、:numref:`flow_keyblock` の例を辞書型で出力した例である。

  .. code-block:: python
    :linenos:
    :caption: キーブロック単位でのイテレータで出力を辞書型にした例
    :name: flow_keyblock_dict

    dtype = {'customer':'str', 'date':'str', 'amount':'int'}
    f=nm.mcut(f="customer,date,amount",i=dat).keyblock(keys="customer",skeys="date",dtype=dtype,otype="dict"):
    for line in f:
      print(line)
    # [{'customer': 'A', 'date': '20180101', 'amount': 5200},{'customer': 'A', 'date': '20180105', 'amount': 2000}]
    # [{'customer': 'B', 'date': '20180101', 'amount': 800},{'customer': 'B', 'date': '20180107', 'amount': 4000},{'customer': 'B', 'date': '20180112', 'amount': 3500}]

同じキーの行数が膨大なデータに対して ``keyblock`` を利用する場合は注意が必要である。
``keyblock`` メソッドは、メモリが許す限り、ブロック内のデータをpythonのリスト上に展開しようと試みるが、
メモリ制限を超えた場合の動作は不定である。


