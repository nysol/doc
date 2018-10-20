mpal 相互類似関係にあるアイテムペア列挙
--------------------------------------------

トランザクションデータから2アイテム相関ルールを求め、
ランクに基づいた類似関係にある相関ルールを選択する

入力ファイル形式:

* トランザクションIDとアイテムの２項目によるトランザクションデータ。

o=の出力形式:

* 辺ファイル: simType,simPriority,node1,node2,sim,dir,color
* 節点ファイル: node,support,frequency,total


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 必須

  | トランザクションデータファイル名を指定する。

**tid=** : 型=str , 必須

  | トランザクションID項目名を指定する。

**item=** : 型=str , 必須

  | アイテム項目名を指定する。

**ro=** : 型=str , 任意(default=ファイル出力なし)

  | 出力ルールファイル名を指定する。

**eo=** : 型=str , 必須

  | 出力の辺データファイル名を指定する。

**s=** : 型=float , 任意(default=0.05)

  | 最小支持度(全トランザクション数に対する割合による指定)

**S=** : 型=int , 条件付き必須(S= or s=を指定しなければならない)

  | 最小支持度(件数による指定)

**filter=** : 型=str , 任意(default=相関ルール評価指数でのルール選択をしない)

  | 相関ルールの評価指標(省略可,複数指定可)
  | 指定できる類似度は以下の3つ(括弧内は値域)。
  | J: Jaccard(0..1), P:normalized PMI(-1..0..1), C:Confidence(0..1)

**lb=** : 型=float , 任意(default=)

  | filter=で指定した相関ルール評価指標の下限値を指定する。
  | 例1: sim=P lb=0.5 : normalized PMIが0.5以上1以下の相関ルールを列挙する
  | 例2: sim=P,C lb=0.5,0.2 ub=,0.8 : 例1に加えて、confidenceが0.2以上0.8以下の相関ルールを列挙する

**ub=** : 型=float , 任意(default=)

  | filter=で指定した相関ルール評価指標の上限値を指定する。

**sim=** : 型=str , 任意(default=S)

  | 列挙された相関ルールを元にして枝を張る条件となる指標を指定する。
  | 以下に示す4つの相関ルール評価指標が指定できる。
  | S:Support, J: Jaccard, P:normalized PMI, C:Confidence

**rank=** : 型=str , 任意(default=3)

  | 辺を張る条件で、類似枝の上位何個までを選択するかを指定する。

**dir=** : 型=str , 任意(default=)

  | 双方向類似関係(b)のみを出力するか、単方向類似関係(m)のみか、両方とも含める(x)かを指定する。
  | 相関ルールa=>bの類似度をsim(a=>b)としたとき、
  | b:(bi-directional) sim(a=>b)およびsim(b=>a)がrank=で指定した順位内である相関ルールのみ選択される。
  | m:(mono-directional) 片方向の類似度のみが、指定された順位内である相関ルールが選択される。
  | x:(both) bとmの両方共含める。
  | 以上の3つのパラメータは複数指定することが可能(3つまで)。
  |  例1: sim=S dir=b rank=3 :
  |   アイテムaからみてsupport(a=>b)が3位以内で、かつ
  |   アイテムbからみてsupport(b=>a)も3位以内であるような相関ルールを選択する
  |  例2: sim=S,C dir=b,m rank=3,1
  |   例1に加えて、アイテムaから見てconfidenc(a=>b)が3以内、もしくは
  |   アイテムbから見てconfidenc(b=>a)が3以内であれば、そのような相関ルールも選択する

**prune=** : 型=bool , 任意(default=False)

  | sim=等を複数指定した場合、マルチ枝を単一化する。
  | 第1優先順位: 双方向>片方向
  | 第2優先順位: パラメータ位置昇順

**T=** : 型=str , 任意(default=/tmp)

  | ワークディレクトリ名を指定する。



利用例
''''''''''''

**入力データの準備**

  .. code-block:: python
    :linenos:

    with open('tra.csv','w') as f:
      f.write(
    '''id,item
    1,a
    1,b
    2,a
    2,b
    3,a
    3,b
    4,b
    4,c
    5,a
    5,c
    6,a
    6,c
    7,d
    7,e
    8,d
    8,e
    9,d
    9,e
    A,d
    A,c
    B,e
    B,b
    C,e
    C,a
    D,f
    D,c
    E,f
    E,b
    F,f
    F,a
    ''')


**基本例**

最小支持度を1件で指定しているの( ``S=1`` )、全アイテムペアを列挙し、
そこから類似度として支持度( ``sim="S"`` )が相互に1位のアイテムペアのみを選択する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mpal(i="tra.csv", no="node.csv", eo="edge.csv", tid="id", S=1, item="item", sim="S", rank="1", dir="b").run()
    ### node.csv の内容
    # node,support,frequency,total
    # a,0.4666666667,7,15
    # b,0.4,6,15
    # c,0.3333333333,5,15
    # d,0.2666666667,4,15
    # e,0.3333333333,5,15
    #  :
    ### edge.csv の内容
    # simType,simPriority,node1,node2,sim,dir,color
    # support,0,a,b,0.2,W,FF000080
    # support,0,d,e,0.2,W,FF000080


関連メソッド
''''''''''''''''''''

* :doc:`mfriends` : グラフデータから相互類似関係にあるアイテムペア(辺)を求める

