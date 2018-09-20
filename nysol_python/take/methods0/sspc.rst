sspc 類似アイテムペア列挙
------------------------------

実装の詳細は |sspcorg| を参照されたい。

  .. |sspcorg| raw:: html

		<a href="http://research.nii.ac.jp/~uno/code/sspc.html" target="_blank">sspcのオリジナル解説ページ</a>


パラメータ
''''''''''''''''''''''

**type=** : 型=str , 必須

  | * _:no message
  | * +:write solutions in append mode
  | * #:count the number of similar records for each record
  | * i(inclusion): find pairs [ratio] of items (weighted sum) of one is included in the other (1st is included in 2nd)
  | * I(both-inclusion): find pairs s.t. the size (weight sum) of intersection is [ratio] of both
  | * S:set similarity measure to :math:`|A\cap B| / max{|A|,|B|}`
  | * s:set similarity measure to :math:`|A\cap B| / min{|A|,|B|}`
  | * T(intersection): find pairs having common [threshld] items
  | * R(resemblance): find pairs s.t. :math:`|A\cap B|/|A\cup B| >= [threshld]`
  | * P(PMI): set similarity measure to :math:`log(|A\cap B|*|all| / (|A|*|B|))` where :math:`|all|` is the number of all items
  | * C(cosign distance): find pairs s.t. inner product of their normalized vectors >= [threshld]
  | * f,Q:output ratio/size of pairs following/preceding to the pairs
  | * D:the first entry is ID, and unify the records with the same ID
  | * N:normalize the ID of latter sets, in -c mode
  | * n:do not consider a and b in the set when comparing a and b
  | * Y(y):output elements of each set that contribute to no similarity (y:fast with much memory use)
  | * 1:remove duplicated items in each transaction
  | * t:transpose the database so that i-th transaction will be item i
  | * E:input column-row representation
  | * w:load weight of each item in each row (with E command)

**i=** : 型=str , 必須

  | トランザクションファイル名を指定する。

**o=** : 型=str , 必須

  | 出力ファイル名を指定する。

**th=** : 型=float , 必須

  | ``type=`` で指定した類似度の閾値を指定する。

**K=** : 型=int , 任意(default=制限なし)

  | output [num] pairs of most large similarities

**k=** : 型=int , 任意(default=制限なし)

  | output [num] elements of most large similarities, for each element

**l=** : 型=int , 任意(default=制限なし)

  | ignore transactions with size (weight sum) less than [num]

**u=** : 型=int , 任意(default=制限なし)

  | ignore transactions with size (weight sum) more than [num]

**L=** : 型=int , 任意(default=制限なし)

  | ignore items appearing less than [num]

**U=** : 型=int , 任意(default=制限なし)

  | ignore items appearing more than [num]

**w=** : 型=str , 任意(default=全トランザクションの重みは等しいものとする)

  | トランザクションの重みファイル名を指定する。

**W=** : 型=str , 任意(default=重みを使わない)

  | read item weights in each row from [filename]

**c=** : 型=int , 任意(default=制限なし)

  | compare transactions of IDs less than num and the others 
  | (if 0 is given, automatically set to the boundary of the 1st and 2nd file)
  | ignore items appearing more than [num]

**b=** : 型=int , 任意(default=制限なし)

  | ignore pairs having no common item of at least [num]th frequency

**B=** : 型=int , 任意(default=制限なし)

  | ignore pairs having no common item of frequency at most [num]

**T=** : 型=int , 任意(default=制限なし)

  | ignore pairs whose intersection size is less than [num]

**TT=** : 型=int , 任意(default=制限なし)

  | ``T=`` with outputting intersection size to the 1st column of each line

**stop=** : 型=int , 任意(default=制限なし)

  | ここで指定した数のパターンを出力したら停止する。

**separator=** : 型=str , 任意(default=スペース)

  | 出力時のアイテムの区切り文字を指定する。

**Q=** : 型=str , 任意(default=replaceしない)

  | replace the output numbers according to the permutation table given by [filename]



利用例
''''''''''''

関連メソッド
''''''''''''''''''''



