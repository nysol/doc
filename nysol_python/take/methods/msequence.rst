msequence 多頻度系列パターンの列挙
--------------------------------------------

多頻度系列パターンを列挙する。
内部的には、 :doc:`Takeのコアメソッドlcmseq <../methods0/lcmseq>` を用いている。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 必須

  | 系列データファイル名を指定する。

**O=** : 型=str , 任意(default=./take_現在日付時刻)

  | 出力ディレクトリ名を指定する。

**x=** : 型=str , 任意(default=階層分類を使わない)

  | taxonomyファイル名を指定する。
  | ``item`` 項目の値を対応するtaxonomyに変換して実行する。例えば、アイテムa,bのtaxonomyをX、c,dのtaxonomyをYとすると、
  | シーケンス aeadd は XeXYY に変換される。

**tid=** : 型=str , 任意(default=tid)

  | トランザクションID項目名(i=上の項目名)

**time=** : 型=str , 任意(default=time)

  | 系列の順序関係を表す時間項目名を指定する。

**item=** : 型=str , 任意(default=item)

  | アイテム項目名(i=,t=上の項目名)

**cls=** : 型=str , 任意(default=class)

  | クラス項目名(c=上の項目名)

**taxo=** : 型=str , 条件付き必須(x=指定時)

  | 

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

  | パターンサイズの下限(1以上20以下の整数)

**u=** : 型=int , 任意(default=制限なし)

  | パターンサイズの上限(1以上20以下の整数)

**p=** : 型=float , 任意(default=0.5)

  | 最小事後確率

**g=** : 型=float , 任意(default=制限なし)

  | 最小増加率
  | p=,g=共に指定しなければ、p=0.5が指定されたことになる。
  | 両方指定されれば、g=が優先される。

**gap=** : 型=int , 任意(default=0)

  | パターンのギャップ長の上限(0以上の整数)を指定する。
  | 0を指定すれば制限なしとなる。

**win=** : 型=int , 任意(default=0)

  | パターンのウィンドウサイズの上限(0以上の整数)を指定する。
  | 0を指定すれば制限なしとなる。

**padding=** : 型=bool , 任意(default=False)

  | 時刻を整数とみなし、連続でない時刻に特殊なアイテムがあることを想定する。
  | ``gap=`` や ``win=`` の指定に影響する。
  | パターンのウィンドウサイズの上限(0以上の整数)を指定する。

**top=** : 型=int , 任意(default=制限なし)

  | 列挙するパターン数の上限を指定する。
  | 例えばtop=10と指定すると、支持度が10番目高いパターンの支持度を最小支持度として頻出パターンを列挙する。
  | よって、同じ支持度のパターンが複数個ある場合は10個以上のパターンが列挙されるかもしれない。

**T=** : 型=str , 任意(default=/tmp)

  | ワークディレクトリを指定する。



利用例
''''''''''''

**入力データの準備**

  .. code-block:: python
    :linenos:

    with open('dat1.csv','w') as f:
      f.write(
    '''tid,time,item
    T1,0,C
    T1,2,B
    T1,3,A
    T1,7,C
    T2,2,D
    T2,3,A
    T2,5,B
    T2,6,C
    T3,1,C
    T3,2,B
    T3,4,D
    T3,8,E
    T4,2,A
    T4,5,C
    T4,6,B
    T5,0,B
    T5,1,A
    T5,2,D
    T5,3,D
    T5,7,C
    T5,9,C
    T6,0,A
    T6,5,B
    T6,6,D
    T6,8,B
    T6,9,C
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''tid,time,item,class
    T1,0,C,cls1
    T1,2,B,cls1
    T1,3,A,cls1
    T1,7,C,cls1
    T2,2,D,cls1
    T2,3,A,cls1
    T2,5,B,cls1
    T2,6,C,cls1
    T3,1,C,cls1
    T3,2,B,cls1
    T3,4,D,cls1
    T3,8,E,cls1
    T4,2,A,cls1
    T4,5,C,cls1
    T4,6,B,cls1
    T5,0,B,cls2
    T5,1,A,cls2
    T5,2,D,cls2
    T5,3,D,cls2
    T5,7,C,cls2
    T5,9,C,cls2
    T6,0,A,cls2
    T6,5,B,cls2
    T6,6,D,cls2
    T6,8,B,cls2
    T6,9,C,cls2
    ''')


**基本例**

出現頻度が3以上の長さが2の系列パターンのみを列挙する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.msequence(O="result", i="dat1.csv", S=3, l=2, u=2).run()
    ### result/patterns.csv の内容
    # pid,pattern,size,count,total,support%0nr
    # 3,A C,2,5,6,0.8333333333
    # 1,B C,2,4,6,0.6666666667
    # 0,C B,2,3,6,0.5
    # 2,B D,2,3,6,0.5
    # 4,A B,2,3,6,0.5
    #  :
    ### result/tid_pats.csv の内容
    # tid%0,pid%1
    # T1,0
    # T1,1
    # T1,3
    # T2,1
    # T2,3
    #  :


**パターン長の制限**

2件以上で出現する系列パターン。
入力データの項目名は、全てデフォルトのものと同じなので省略していることに注意する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.msequence(O="result", i="dat1.csv", S=2).run()
    ### result/patterns.csv の内容
    # pid,pattern,size,count,total,support%0nr
    # 1,C,1,6,6,1
    # 4,B,1,6,6,1
    # 11,A C,2,5,6,0.8333333333
    # 10,A,1,5,6,0.8333333333
    # 16,D,1,4,6,0.6666666667
    #  :
    ### result/tid_pats.csv の内容
    # tid%0,pid%1
    # T1,0
    # T1,1
    # T1,10
    # T1,11
    # T1,2
    #  :


**gap長とwindowサイズの指定**

出現頻度が2以上、長さが2以上の系列パターンのうち、gap長が2、windowサイズが4のパターンを列挙する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.msequence(O="result", i="dat1.csv", S=2, l=2, gap=2, win=4).run()
    ### result/patterns.csv の内容
    # pid,pattern,size,count,total,support%0nr
    # 0,C B,2,3,6,0.5
    # 2,B C,2,3,6,0.5
    # 3,B D,2,3,6,0.5
    # 4,A C,2,3,6,0.5
    # 5,A B,2,3,6,0.5
    #  :
    ### result/tid_pats.csv の内容
    # tid%0,pid%1
    # T1,0
    # T1,1
    # T1,2
    # T1,4
    # T2,2
    #  :


**paddingにより時間を考慮する**

前の例と同じ条件で、 ``padding`` オプションを指定することで、
時間を考慮したgap長とwindowサイズ制約により系列パターンを列挙する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.msequence(O="result", i="dat1.csv", S=2, l=2, gap=2, win=4, padding=True).run()
    ### result/patterns.csv の内容
    # pid,pattern,size,count,total,support%0nr
    # 0,C B,2,3,6,0.5
    # 3,B D,2,3,6,0.5
    # 1,B A,2,2,6,0.3333333333
    # 2,B C,2,2,6,0.3333333333
    ### result/tid_pats.csv の内容
    # tid%0,pid%1
    # T1,0
    # T1,1
    # T2,2
    # T3,0
    # T3,3
    #  :


**顕在系列パターンの列挙**

最初の例と同じ条件で、クラス項目を指定することで顕在パターンを列挙する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.msequence(O="result", i="dat2.csv", S=2, cls="class", padding=True).run()
    ### result/patterns.csv の内容
    # class%0nr,pid,pattern,size,pos%2nr,neg,posTotal,negTotal,total,support,growthRate,postProb%1nr
    # cls1,1,B C,2,3,0,4,2,6,0.75,inf,1
    # cls2,10,A D,2,2,0,2,4,6,1,inf,1
    # cls2,9,B C D,3,2,0,2,4,6,1,inf,1
    # cls2,11,A C D,3,2,0,2,4,6,1,inf,1
    # cls1,0,C,1,4,2,4,2,6,1,1,0.6666666667
    #  :
    ### result/tid_pats.csv の内容
    # tid%0,class%1,pid%2
    # T1,cls1,0
    # T1,cls1,1
    # T1,cls1,2
    # T1,cls1,3
    # T1,cls1,4
    #  :


関連メソッド
''''''''''''''''''''

* :doc:`mitemset` : アイテム集合列挙ならこちら

