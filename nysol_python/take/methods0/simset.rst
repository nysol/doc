sspc アイテム集合のクラスタリング
--------------------------------------

実装の詳細は |simsetorg| を参照されたい。

  .. |simsetorg| raw:: html

		<a href="http://research.nii.ac.jp/~uno/code/simset.html" target="_blank">simsetのオリジナル解説ページ</a>


パラメータ
''''''''''''''''''''''

**type=** : 型=str , 必須

  | * _:no message
  | * +:write solutions in append mode
  | * =:do not remove temporal files
  | * @:do not execute data polishing, E:read edge list file
  | * i:set similarity measure to the ratio of one is included in the other
  | * I:set similarity measure to the ratio of both are included in the other
  | * S:set similarity measure to :math:`|A\cap B|/max(|A|,|B|)`
  | * s:set similarity measure to :math:`|A\cap B|/min(|A|,|B|)`
  | * C:set similarity measure to the cosign distance, the inner product of the normalized characteristic vectors
  | * T:set similarity measure to the intersection size, i.e., :math:`|A\cap B|`
  | * R:(recemblance) set similarity measure to :math:`|A\cap B|/|A\cup B|`
  | * P(PMI): set similarity measure to :math:`log(|A\cap B|*|all| / (|A|*|B|))` where :math:`|all|` is the number of all items
  | * M:output intersection of each clique, instead of IDs of its members
  | * v (with M): output ratio of records, including each item
  | * m:do not remove edges in the data polishing phase
  | * O:repeatedly similarity clustering until convergence
  | * Y:take intersection of original graph and polished graph, instead of clique mining
  | * 1:do not remove the same items in a record (with -G)
  | * W:load weight of each element
  | * t:transpose the input database, so that each line will be considered as a record

**i=** : 型=str , 必須

  | similarity-graph-filename

**o=** : 型=str , 必須

  | 出力ファイル名を指定する。

**th_s=** : 型=float , 必須

  | similarity-threshold

**th_d=** : 型=int , 必須

  | degree-threshold

**G=** : 型=str , 任意(default=)

  | use [similarity] of [threshold] in the first phase (file is regarded as a transaction database)

**k=** : 型=int , 任意(default=)

  | find only k-best for each record in ``G`` option

**M=** : 型=str , 任意(default=)

  | merge similar cliques of similarity in [num] of recemblance (changes to 'x' by giving '-Mx')

**m=** : 型=str , 任意(default=)

  | take independently cliques from similar cliques of similarity in [num] of recemblance, 
  | and merge the neighbors of each independent clique ('recemblance' changes to 'x' by giving '-Mx')

**v=** : 型=float , 任意(default=)

  | specify majority threshold (default=0.5) 
  | (if negative is given, items of frequency no more than -[num] are output)

**u=** : 型=int , 任意(default=制限なし)

  | ignore vertices of degree more than [num]

**l=** : 型=int , 任意(default=制限なし)

  | ignore vertices of degree less than [num]

**U=** : 型=int , 任意(default=上限なし)

  | ignore transactions of size more than [num] (with -G)

**L=** : 型=int , 任意(default=上限なし)

  | ignore transactions of size less than [num] (with -G)

**I=** : 型=int , 任意(default=上限なし)

  | ignore items of frequency more than [num] (with -G)

**i=** : 型=int , 任意(default=上限なし)

  | ignore items of frequency less than [num] (with -G)

**II=** : 型=float , 任意(default=上限なし)

  | give thresholds by the ratio of #ransactions/#items)

**ii=** : 型=float , 任意(default=上限なし)

  | give thresholds by the ratio of #ransactions/#items)

**t=** : 型=int , 任意(default=上限なし)

  | ignore pairs whose intersection size is less than [num] (T for first phase with -G option, and t for polishing)

**T=** : 型=int , 任意(default=上限なし)

  | ignore pairs whose intersection size is more than [num] (T for first phase with -G option, and t for polishing)

**O=** : 型=int , 任意(default=制限なし)

  | specify the number of repetitions

**9=** : 型=int , 任意(default=制限なし)

  | shrink records of similarity more than [num]

**X=** : 型=float , 任意(default=制限なし)

  | multiply the weight by [num] (and trancate by 1, for C command)

**x=** : 型=float , 任意(default=制限なし)

  | power the weight by [num] (and normalize, for C command)

**y=** : 型=float , 任意(default=制限なし)

  | at last, remove edges with weight less than [num]

**w=** : 型=str , 任意(default=重みは等しいものとする)

  | load weight of elements from the file

**multi=** : 型=int , 任意(default=1)

  | use multicores of [num] (compile by 'make multicore')

**W=** : 型=str , 任意(default=)

  | specify the working directory (folder). 
  | The last letter of the directory has to be '/' ('')

**separator=** : 型=str , 任意(default=スペース)

  | give the separator of the numbers in the output

**Q=** : 型=str , 任意(default=replaceしない)

  | replace the output numbers according to the permutation table given by [filename]

**K=** : 型=int , 任意(default=制限なし)

  | 頻出な上位のアイテム集合のみ出力する

**l=** : 型=int , 任意(default=制限なし)

  | アイム集合のサイズの下限値を指定する。

**u=** : 型=int , 任意(default=制限なし)

  | アイム集合のサイズの上限値を指定する。

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



