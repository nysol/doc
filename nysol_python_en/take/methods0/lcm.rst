lcm Linear time Closed itemset Miner
------------------------------------------------------------------------

実装の詳細は |lcmorg| を参照されたい。

  .. |lcmorg| raw:: html

		<a href="http://research.nii.ac.jp/~uno/code/lcm.html" target="_blank">lcmのオリジナル解説ページ</a>


パラメータ
''''''''''''''''''''''

**type=** : 型=str , 必須

  | 列挙するアイテム集合のタイプ(F|C|M)、及び出力形式を文字列として指定する。
  | アイテム集合のタイプとして以下の３つから一つを選ぶ。
  | 
  | * F:頻出アイテム集合
  | * C:飽和アイテム集合
  | * M:極大アイテム集合
  | 
  | また出力形式として以下の組み合わせで指定する。
  | 	
  | * f:アイテム集合の後ろに出現件数を出力する。
  | * Q:アイテム集合の前に出現件数を出力する。
  | * I:アイテム集合の次の行に出現集合(出現するトランザクション行番号)を出力する。
  | * t:トランザクションデータベースを転置する(アイテムiはi番目のトランザクションとなり、j番目のトランザクションはアイテムjとなる)。
  | * A:w=でプラスとマイナスのトランザクションの重みを指定した場合、プラス/マイナスそれぞれの件数とその比を出力する。
  | * P:positive-closed itemset mining
  | * R:output redundant items for rule mining (usually, redundant items are removed, to be minimal, in the case of rule mining)
  | * i:do not output itemset to the output file (only rules)
  | * s:output confidence and item frequency by absolute values

**i=** : 型=str , 必須

  | トランザクションファイル名を指定する。

**o=** : 型=str , 必須

  | 出力ファイル名を指定する。

**sup=** : 型=<class 'int'> , 必須

  | 最小サポートを指定する。

**U=** : 型=<class 'int'> , 任意(default=上限なし)

  | 最大サポートを指定する。

**K=** : 型=<class 'int'> , 任意(default=制限なし)

  | 頻出な上位のアイテム集合のみ出力する

**l=** : 型=<class 'int'> , 任意(default=制限なし)

  | アイム集合のサイズの下限値を指定する。

**u=** : 型=<class 'int'> , 任意(default=制限なし)

  | アイム集合のサイズの上限値を指定する。

**w=** : 型=str , 任意(default=全トランザクションの重みは等しいものとする)

  | トランザクションの重みファイル名を指定する。

**a=** : 型=float(0以上1以下) , 任意(default=制限なし)

  | 相関ルールマイニングを実施しconfidenceの下限値を与える。

**A=** : 型=float(0以上1以下) , 任意(default=制限なし)

  | 相関ルールマイニングを実施しconfidenceの上限値を与える。

**r=** : 型=float(0以上1以下) , 任意(default=制限なし)

  | 相関ルールマイニングを実施しrelational confidenceの下限値を与える。

**R=** : 型=float(0以上1以下) , 任意(default=制限なし)

  | 相関ルールマイニングを実施しrelational confidenceの上限値を与える。

**item=** : 型=int , 任意(default=)

  | 指定した番号のアイテムに関する相関ルールを出力する。

**so=** : 型=str , 任意(default=ファイル出力しない)

  | 標準出力の内容を指定のファイルに出力する。

**separator=** : 型=str , 任意(default=スペース)

  | 出力時のアイテムの区切り文字を指定する。



利用例
''''''''''''

**入力データの準備**

  .. code-block:: python
    :linenos:

    with open('dat1.tra','w') as f:
      f.write(
    '''2 4
    3 4 5
    0 1 3 5
    1 3 5
    0 1 3 4
    0 1 3 4 5
    ''')

    with open('weight.txt','w') as f:
      f.write(
    '''-1
    1
    -1
    1
    1
    -1
    ''')


**基本例**

頻出アイテム集合( ``F`` )の列挙。
``type=`` に ``f`` を指定すると出現件数を出力する。
``type=`` に ``_`` を含めることでメッセージを表示しなくなる。
出力結果の各行が頻出アイテム集合を表しており、末尾の括弧内の数字が出現件数を表している。
一行目には空のアイテム集合が出力されている。

  .. code-block:: python
    :linenos:

    from nysol.take.extcore import lcm
    lcm(type="Ff_",sup=3,i="dat1.tra",o="result.txt")
    ### result.txt の内容
    # (6)
    # 3 (5)
    # 1 (4)
    # 1 3 (4)
    # 4 (4)
    # 4 3 (3)
    # 5 (4)
    # 5 3 (4)
    # 5 1 (3)
    # 5 1 3 (3)
    # 0 (3)
    # 0 1 (3)
    # 0 1 3 (3)
    # 0 3 (3)


**飽和集合の列挙**

``type=`` に ``C`` を指定することで、頻出飽和アイテム集合を列挙する。

  .. code-block:: python
    :linenos:

    from nysol.take.extcore import lcm
    lcm(type="Cf_",sup=3,i="dat1.tra",o="result.txt")
    ### result.txt の内容
    # (6)
    # 3 (5)
    # 1 3 (4)
    # 4 (4)
    # 4 3 (3)
    # 5 3 (4)
    # 5 1 3 (3)
    # 0 3 1 (3)


**極大集合の列挙**

``type=`` に ``M`` を指定することで、頻出極大アイテム集合を列挙する。

  .. code-block:: python
    :linenos:

    from nysol.take.extcore import lcm
    lcm(type="Mf_",sup=3,i="dat1.tra",o="result.txt")
    ### result.txt の内容
    # 4 3 (3)
    # 5 1 3 (3)
    # 0 3 1 (3)


**アイテム集合サイズを制限**

``l=3`` でアイテム集合のサイズを3以上に限定する。

  .. code-block:: python
    :linenos:

    from nysol.take.extcore import lcm
    lcm(type="Mf_",sup=3,l=3,i="dat1.tra",o="result.txt")
    ### result.txt の内容
    # 5 1 3 (3)
    # 0 3 1 (3)


**出現集合の出力**

``type=`` に ``I`` を加えることで、アイテム集合の下に出現集合が出力される。
アイテム集合 ``{5,1,3}`` はトランザクションデータ( ``dat1.tra`` )の2,3,5行目に出現している(先頭行は0行目と数える}。

  .. code-block:: python
    :linenos:

    from nysol.take.extcore import lcm
    lcm(type="FfI_",sup=3,l=3,i="dat1.tra",o="result.txt")
    ### result.txt の内容
    # 5 1 3 (3)
    # 2 3 5
    # 0 1 3 (3)
    # 2 4 5


**データベースの転置**

``type=`` に ``t`` を加えることでトランザクションデータベースを転置してから実行する。
トランザクション集合 ``{4,2,5}`` はアイテム ``{0,1,3}`` に出現する(先頭行は0行目と数える}。

  .. code-block:: python
    :linenos:

    from nysol.take.extcore import lcm
    lcm(type="FftI_",sup=3,l=3,i="dat1.tra",o="result.txt")
    ### result.txt の内容
    # 4 2 5 (3)
    # 0 1 3
    # 3 2 5 (3)
    # 1 3 5


**上位k番目の出現件数**

``K=4`` で頻出上位4番目の出現件数を出力する。
「基本例」での結果から、頻出上位4番目のルールは ``1 3 (4)`` であり、その出現件数 ``4`` が出力されている。

  .. code-block:: python
    :linenos:

    from nysol.take.extcore import lcm
    lcm(type="Ff",K=4,sup=1,i="dat1.tra",so="topk.txt")
    ### topk.txt の内容
    # 4


**トランザクション重みの利用**

``w=`` を指定すると、指定されたトランザクションの重みで件数をカウントする。
``type=`` に ``A`` を加えることで、マイナス重みとプラス重みの件数情報が表示される。
アイテム ``3`` は、1,2,3,4,5行目に含まれ、その重み合計は1(=1-1+1+1-1)となる
(プラス重み件数3件、マイナス重み件数2件、プラス率は3/5=0.6)。
同様にアイテム集合{4,3}は1,4,5行目に含まれ、その重み合計は1(=1+1-1)となる
(プラス重み件数2件、マイナス重み件数1件、プラス率は2/3=0.6666)。

  .. code-block:: python
    :linenos:

    from nysol.take.extcore import lcm
    lcm(type="FfA_",sup=1,w="weight.txt",i="dat1.tra",o="result.txt")
    ### result.txt の内容
    # 3 (1) (3,2,0.6)
    # 4 3 (1) (2,1,0.6666)


関連メソッド
''''''''''''''''''''



