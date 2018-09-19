mitemset アイテム集合列挙
----------------------------------

多頻度アイテム集合を列挙する。
列挙のアルゴリズムにはlcmを用いている。
以下のような特徴を持っている。

* 分類階層を扱うことが可能
* 頻出パターン, 飽和頻出パターン, 極大頻出パターンの3種類のパターンを列挙可能
* 分類クラスを指定することで、上記3パターンに関する顕在パターン(emerging patterns)を列挙可能


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 必須

  | アイテム集合データベースファイル名を指定する。

**O=** : 型=str , 任意(default=./take_現在日付時刻)

  | 出力ディレクトリ名を指定する。

**x=** : 型=str , 任意(default=階層分類を使わない)

  | taxonomyファイル名を指定する。
  | x=が指定されたとき、itemに対応するtaxonomyをトランザクションに追加して実行する。
  | 例えば、アイテムa,bのtaxonomyをX、c,dのtaxonomyをYとすると、あるトランザクションabdはabdXYとなる。
  | ただしreplaceTaxoオプションが指定されると、taxonomyは追加ではなく置換して実行する。
  | 前例ではトランザクションabdはXYに置換される。

**tid=** : 型=str , 任意(default=tid)

  | トランザクションID項目名(i=上の項目名)

**item=** : 型=str , 任意(default=item)

  | アイテム項目名(i=,t=上の項目名)

**cls=** : 型=str , 任意(default=class)

  | クラス項目名(i=上の項目名)

**taxo=** : 型=str , 条件付き必須(x=指定時)

  | 

**type=** : 型=str , 任意(default=F)

  | 抽出するパターンの型(F,C,M)を指定する。
  | F:頻出集合, C:飽和集合, M:極大集合

**s=** : 型=float , 任意(default=0.05)

  | 最小支持度(全トランザクション数に対する割合による指定)

**S=** : 型=int , 任意(default=1)

  | 最小支持度(件数による指定)
  | s=,S=共に指定しなければ、s=0.05が指定されたことになる。
  | 両方指定されれば、S=が優先される。

**sx=** : 型=float , 任意(default=1.0)

  | 最大支持度(全トランザクション数に対する割合による指定)

**Sx=** : 型=bool , 任意(default=False)

  | 最大支持度(件数による指定)
  | sx=,Sx=共に指定しなければ、sx=1.0が指定されたことになる。
  | 両方指定されれば、Sx=が優先される。

**l=** : 型=int , 任意(default=制限なし)

  | パターンサイズ(アイテム数)の下限(1以上20以下の整数)

**u=** : 型=int , 任意(default=制限なし)

  | パターンサイズ(アイテム数)の上限(1以上20以下の整数)

**p=** : 型=float , 任意(default=0.5)

  | 最小事後確率

**g=** : 型=float , 任意(default=制限なし)

  | 最小増加率
  | p=,g=共に指定しなければ、p=0.5が指定されたことになる。
  | 両方指定されれば、g=が優先される。

**top=** : 型=int , 任意(default=制限なし)

  | 列挙するパターン数の上限を指定する。
  | 例えばtop=10と指定すると、支持度が10番目高いパターンの支持度を最小支持度として頻出パターンを列挙する。
  | よって、同じ支持度のパターンが複数個ある場合は10個以上のパターンが列挙されるかもしれない。

**replaceTaxo=** : 型=bool , 任意(default=False)

  | taxonomyを置換する。

**T=** : 型=str , 任意(default=/tmp)

  | ワークディレクトリを指定する。



利用例
''''''''''''

**入力データの準備**

  .. code-block:: python
    :linenos:

    with open('dat1.csv','w') as f:
      f.write(
    '''tid,item
    T1,C
    T1,E
    T2,D
    T2,E
    T2,F
    T3,A
    T3,B
    T3,D
    T3,F
    T4,B
    T4,D
    T4,F
    T5,A
    T5,B
    T5,D
    T5,E
    T6,A
    T6,B
    T6,D
    T6,E
    T6,F
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''tid,item,class
    T1,C,cls1
    T1,E,cls1
    T2,D,cls1
    T2,E,cls1
    T2,F,cls1
    T3,A,cls1
    T3,B,cls1
    T3,D,cls1
    T3,F,cls1
    T4,B,cls1
    T4,D,cls1
    T4,F,cls1
    T5,A,cls2
    T5,B,cls2
    T5,D,cls2
    T5,E,cls2
    T6,A,cls2
    T6,B,cls2
    T6,D,cls2
    T6,E,cls2
    T6,F,cls2
    ''')

    with open('taxo.csv','w') as f:
      f.write(
    '''item,taxonomy
    A,X
    B,X
    C,Y
    D,Z
    E,Z
    F,Z
    ''')


**基本例**

3件以上で出現する頻出アイテム集合を列挙する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mitemset(S=3,tid="tid",item="item",i="dat1.csv",O="result").run()
    ### result/patterns.csv の内容
    # pid,size,count,total,support%0nr,lift,pattern
    # 1,1,5,6,0.8333333333,1,D
    # 7,2,4,6,0.6666666667,1.2,D F
    # 6,1,4,6,0.6666666667,1,F
    # 4,1,4,6,0.6666666667,1,E
    # 2,1,4,6,0.6666666667,1,B
    #  :
    ### result/tid_pats.csv の内容
    # tid,pid
    # T1,4
    # T2,1
    # T2,4
    # T2,7
    # T2,6
    #  :


**アイテム集合のサイズに制限を加えた例**

出現頻度が3以上で、アイテム集合のサイズ3のパターンを列挙する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mitemset(S=3,l=3,u=3,tid="tid",item="item",i="dat1.csv",O="result").run()
    ### result/patterns.csv の内容
    # pid,size,count,total,support%0nr,lift,pattern
    # 0,3,3,6,0.5,1.35,B D F
    # 1,3,3,6,0.5,1.8,A B D


**飽和集合の列挙例**


  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mitemset(S=3,type="C",tid="tid",item="item",i="dat1.csv",O="result").run()
    ### result/patterns.csv の内容
    # pid,size,count,total,support%0nr,lift,pattern
    # 1,1,5,6,0.8333333333,1,D
    # 2,2,4,6,0.6666666667,1.2,B D
    # 3,1,4,6,0.6666666667,1,E
    # 5,2,4,6,0.6666666667,1.2,D F
    # 4,2,3,6,0.5,0.9,D E
    #  :


**極大集合の列挙例**


  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mitemset(S=3,type="M",tid="tid",item="item",i="dat1.csv",O="result").run()
    ### result/patterns.csv の内容
    # pid,size,count,total,support%0nr,lift,pattern
    # 0,2,3,6,0.5,0.9,D E
    # 1,3,3,6,0.5,1.35,B D F
    # 2,3,3,6,0.5,1.8,A B D


**アイテムの階層分類を使った例**


  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mitemset(S=4,tid="tid",item="item",i="dat1.csv",x="taxo.csv",taxo="taxonomy",O="result").run()
    ### result/patterns.csv の内容
    # pid,size,count,total,support%0nr,lift,pattern
    # 1,1,6,6,1,1,Z
    # 2,1,5,6,0.8333333333,1,D
    # 19,2,4,6,0.6666666667,1.2,D X
    # 13,2,4,6,0.6666666667,1,B Z
    # 14,1,4,6,0.6666666667,1,X
    #  :


**オリジナルアイテムを階層分類で置換する例**


  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mitemset(S=4,tid="tid",item="item",i="dat1.csv",x="taxo.csv",taxo="taxonomy",replaceTaxo=True,O="result").run()
    ### result/patterns.csv の内容
    # pid,size,count,total,support%0nr,lift,pattern
    # 1,1,6,6,1,1,Z
    # 2,1,4,6,0.6666666667,1,X
    # 3,2,4,6,0.6666666667,1,X Z


**顕在パターンの列挙例**


  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mitemset(S=2,tid="tid",item="item",cls="class",i="dat2.csv",p=0.6,O="result").run()
    ### result/patterns.csv の内容
    # class%0nr,pid,pattern,size,pos%2nr,neg,posTotal,negTotal,total,support,growthRate,postProb%1nr
    # cls2,18,B D E,3,2,0,2,4,6,1,inf,1
    # cls2,14,B E,2,2,0,2,4,6,1,inf,1
    # cls2,13,A E,2,2,0,2,4,6,1,inf,1
    # cls2,17,A D E,3,2,0,2,4,6,1,inf,1
    # cls2,15,A B E,3,2,0,2,4,6,1,inf,1
    #  :


関連メソッド
''''''''''''''''''''

* :doc:`msequence` : 系列列挙ならこちら

