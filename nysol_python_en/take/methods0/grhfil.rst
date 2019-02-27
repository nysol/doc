grhfil グラフフィルタ
----------------------------

グラフの加工を行う。


パラメータ
''''''''''''''''''''''

**type=** : 型=str , 必須

  | 以下に示すパラメータを組み合わせて文字列として指定する(ex. "UeEs")。
  | 
  | 	1) グラフタイプ【必須】
  | 	グラフの種類を以下の5つから一つ選んで指定する。
  | 
  | 	* B:二部グラフ
  | 	* d:有向グラフ(入力隣接行列を変更しない)
  | 	* D:逆向きの有向グラフ(隣接行列の下三角行列と上三角行列を入れ替える)
  | 	* U:片方向無向グラフ(隣接行列の下三角行列を削除し、重複したエッジを削除する)
  | 	* u:双方向無向グラフ(入力隣接行列の下三角行列と上三角行列を対称にする)
  | 
  | 	2) グラフの書式【オプション】
  | 	入出力ファイルのグラフの書式は、隣接行列形式がデフォルトであるが、
  | 	それをノードペアのエッジ形式に変更することができる。
  | 
  | 	* e: 入力ファイルをエッジ形式とする。
  | 	* E: 出力ファイルをエッジ形式とする。
  | 
  | 	3) その他の指定
  | 
  | 	* s: 出力のグラフの隣接ノードを昇順に並べる。
  | 	* S: 出力のグラフの隣接ノードを降順に並べる。
  | 	* n: 入力データの一行目を"ノード数 エッジ数"とする。
  | 	* N: 出力データの一行目に"ノード数 エッジ数"を出力する。
  | 	* v: 入力データのノード番号は1から始まるものとする。
  | 	* V: 出力データのノード番号は1からはじまるものとして出力する。
  | 	* 0: 一列目にノード番号を出力する(出力が隣接行列形式の場合のみ)。
  | 	* w: 入力ファイルの隣接ノードの次の数字を重みとする。
  | 	* W: 出力ファイルの隣接ノードの次に重みを出力する。
  | 	* %:show progress
  | 	* _:no message
  | 	* +:write solutions in append mode
  | 
  | 	* v,V:node ID in read/write file starts from 1,
  | 	* q:non-transform mode (valid with -P option)
  | 	* 9:give weight 1 to each vertex ID (with 0)
  | 	* 1:unify consecutive two same numbers into one

**i=** : 型=str , 必須

  | トランザクションファイル名を指定する。

**o=** : 型=str , 必須

  | 出力ファイル名を指定する。

**t=** : 型=int , 任意(default=制約なし)

  | 次数が指定した値より小さいノードは出力しない【デフォルト=制約なし】

**T=** : 型=int , 任意(default=制約なし)

  | 次数が指定した値より大きいノードは出力しない【デフォルト=制約なし】

**ideg=** : 型=int , 任意(default=制約なし)

  | 有向グラフにおいて入次数が指定した値より小さいノードは出力しない

**Ideg=** : 型=int , 任意(default=制約なし)

  | 有向グラフにおいて入次数が指定した値より大きいノードは出力しない

**odeg=** : 型=int , 任意(default=制約なし)

  | 有向グラフにおいて出次数が指定した値より小さいノードは出力しない

**Odeg=** : 型=int , 任意(default=制約なし)

  | 有向グラフにおいて出次数が指定した値より大きいノードは出力しない

**r=** : 型=float , 任意(default=制約なし)

  | 重みが指定した値より小さいエッジは出力しない

**R=** : 型=float , 任意(default=制約なし)

  | 重みが指定した値より大きいエッジは出力しない

**n=** : 型=int , 任意(default=データ上の最大番号+1)

  | ノードの個数を与える

**w=** : 型=bool , 任意(default=均等な重みを使う)

  | 入力ファイルの3項目目を重みとして読み込む(3項目目がなければ0がセットされる)

**W=** : 型=bool , 任意(default=ファイル出力しない)

  | 出力ファイルの3項目目に重みを出力する

**d=** : 型=bool , 任意(default=ファイル出力しない)

  | 指定したグラフとの差異を出力する(gTypeとgFormatは同じでなければならない)

**dth=** : 型=float , 任意(default=)

  | specify the threshold value (d=が必要)

**m=** : 型=str , 任意(default=)

  | 指定したグラフとのintersectionを出力する(gTypeとgFormatは同じでなければならない)

**M=** : 型=str , 任意(default=)

  | 指定したグラフとのunionを出力する(gTypeとgFormatは同じでなければならない)

**P=** : 型=str , 任意(default=)

  | permute the vertex ID to coutinuous numbering and output the permutation table to the file

**Q=** : 型=str , 任意(default=)

  | permute the numbers in the file according to the table



利用例
''''''''''''

**入力データの準備**

  .. code-block:: python
    :linenos:

    with open('dat1.graph','w') as f:
      f.write(
    '''0 1
    0 2
    0 4
    1 2
    1 4
    1 6
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    from nysol.take.extcore import grhfil
    grhfil(type="ueE_",i="dat1.graph",o="result.graph")
    ### result.txt の内容
    # 3 (1) (3,2,0.6)
    # 4 3 (1) (2,1,0.6666)


関連メソッド
''''''''''''''''''''



