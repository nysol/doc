lcmseq 系列パターン列挙
------------------------------

実装の詳細は |lcmseqorg| を参照されたい。

  .. |lcmseqorg| raw:: html

		<a href="http://research.nii.ac.jp/~uno/code/lcm_seq.html" target="_blank">lcmseqのオリジナル解説ページ</a>


パラメータ
''''''''''''''''''''''

**type=** : 型=str , 必須

  | * %:show progress
  | * _:no message
  | * +:write solutions in append mode
  | * F:position occurrence
  | * C:document occurrence
  | * m:output extension maximal patterns only
  | * c:output extension closed patterns only
  | * f,Q:output frequency following/preceding to each output sequence
  | * A:output coverages for positive/negative transactions
  | * I(J):output ID's of transactions including each pattern, 
  | * if J is given, an occurrence is written in a complete stype; transaction ID, starting position and ending position
  | * i:do not output itemset to the output file (only rules)
  | * s:output confidence and item frequency by absolute values
  | * t:transpose the input database (item i will be i-th transaction, and i-th transaction will be item i)

**i=** : 型=str , 必須

  | トランザクションファイル名を指定する。

**o=** : 型=str , 必須

  | 出力ファイル名を指定する。

**sup=** : 型=int , 必須

  | 最小サポートを指定する。

**U=** : 型=int , 任意(default=上限なし)

  | 最大サポートを指定する。

**K=** : 型=int , 任意(default=制限なし)

  | 頻出な上位のアイテム集合のみ出力する

**l=** : 型=int , 任意(default=制限なし)

  | アイム集合のサイズの下限値を指定する。

**u=** : 型=int , 任意(default=制限なし)

  | アイム集合のサイズの上限値を指定する。

**g=** : 型=int , 任意(default=制限なし)

  | ギャップ長の上限を与える。

**G=** : 型=int , 任意(default=制限なし)

  | パターンを含む窓幅の上限を与える。

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

**f=** : 型=float(0以上1以下) , 任意(default=制限なし)

  | output sequences with frequency no less than [ratio] times 
  | the frequency given by the product of appearance probability of each item

**F=** : 型=float(0以上1以下) , 任意(default=制限なし)

  | output sequences with frequency no greater than [ratio] times 
  | the frequency given by the product of appearance probability of each item

**p=** : 型=float(0以上1以下) , 任意(default=制限なし)

  | output sequence only if (frequency)/(abusolute frequency) is no less than [num]

**P=** : 型=float(0以上1以下) , 任意(default=制限なし)

  | output sequence only if (frequency)/(abusolute frequency) is no greater than [num]

**n=** : 型=int , 任意(default=制限なし)

  | output sequence only if its negative frequency is no less than [num] 
  | (negative frequency is the sum of weights of transactions having negative weights)

**n=** : 型=int , 任意(default=制限なし)

  | output sequence only if its negative frequency is no greater than [num] 
  | (negative frequency is the sum of weights of transactions having negative weights)

**opos=** : 型=int , 任意(default=制限なし)

  | output sequence only if its positive frequency is no less than [num] 
  | (positive frequency is the sum of weights of transactions having positive weights)

**Opos=** : 型=int , 任意(default=制限なし)

  | output sequence only if its positive frequency is no greater than [num] 
  | (positive frequency is the sum of weights of transactions having positive weights)

**s=** : 型=float , 任意(default=制限なし)

  | output itemset rule (of the form (a,b,c) => (d,e)) with confidence at least [num] 
  | (only those whose frequency of the result is no less than the support)

**stop=** : 型=int , 任意(default=制限なし)

  | ここで指定した数のパターンを出力したら停止する。

**q=** : 型=str , 任意(default=出力なし)

  | replace the output numbers according to the permutation table given by [filename]

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



