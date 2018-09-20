medset アイテム集合の共通集合
------------------------------------

アイテム集合の共通集合を列挙する。


パラメータ
''''''''''''''''''''''

**ci=** : 型=str , 必須

  | cluster-filename

**si=** : 型=str , 必須

  | set-filename

**th=** : 型=int , 必須

  | threshold

**o=** : 型=str , 必須

  | 出力ファイル名を指定する。

**H=** : 型=bool , 任意(default=False)

  | do not use histgram, just output the items

**R=** : 型=bool , 任意(default=False)

  | do not output singleton clusters

**V=** : 型=bool , 任意(default=False)

  | output ratio of appearances of all items

**T=** : 型=bool , 任意(default=False)

  | clustering by connected component (read edge type file)

**I=** : 型=bool , 任意(default=False)

  | find an independent set, and clustering by using the vertices in it as seeds 
  | (read edge type files)

**i=** : 型=bool , 任意(default=False)

  | output for each item, ratio of records including the item

**t=** : 型=bool , 任意(default=False)

  | transpose the input database, (transaction will be item, and vice varsa)

**l=** : 型=int , 任意(default=制限なし)

  | output clusters of size at least [num]

**progress=** : 型=bool , 任意(default=False)

  | show progress

**nomsg=** : 型=bool , 任意(default=False)

  | no message

**U=** : 型=int , 任意(default=上限なし)

  | 最大サポートを指定する。

**K=** : 型=int , 任意(default=制限なし)

  | 頻出な上位のアイテム集合のみ出力する

**l=** : 型=int , 任意(default=制限なし)

  | アイム集合のサイズの下限値を指定する。

**u=** : 型=int , 任意(default=制限なし)

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

関連メソッド
''''''''''''''''''''



