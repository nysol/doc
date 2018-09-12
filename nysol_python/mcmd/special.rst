
特殊な処理メソッド
=======================

mcmdのメソッドが行っていることは、バイトストリームとして受け取ったデータに対して
何らかの「処理」を行い、その結果をバイトストリームとして出力しているだけである。
とると、その「処理」をPythonの関数やOSのコマンドで実現できてもおかしくない。
これらの機能を担うのが以下で説明する、 ``runfunc`` と ``cmd`` メソッドである。

runfunc: 関数の実行
-----------------------
``runfunc`` メソッドは、
Pythonの関数をあたかもmcmdのメソッドのように動作させるためのメソッドである。
基本的な利用方法を :numref:`special_runfunc1` に示している。
``bigAmount`` 関数の中で使われている、 ``mstdin`` と ``mstdout`` メソッドがポイントで、
それぞれ、標準入力を読み込む、そして標準出力に書き出す機能を持っている。
このように、関数が、標準入力を入力データとして読み込み、標準出力を出力データとして書き出す機能さえ持っていれば、
``runfunc`` 関数によって、mcmdの処理メソッドのように扱えるようになるのである。
:numref:`special_runfunc1` では、 ``mcut`` の出力が、
``runfunc`` により、 ``bigAmount`` 関数の標準入力に接続されており、
またbigAmount関数の標準出力が、 ``msum`` へと接続されている。

  .. code-block:: python
    :linenos:
    :caption: runfuncメソッドの基本的な利用方法
    :name: special_runfunc1

    import nysol.mcmd as nm
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]   

    def bigAmount(lowerBound):
      f = None
      f <<= nm.mstdin()
      f <<= nm.mselnum(f="amount",c="[lowerBound,]")
      f <<= nm.mstdout()
      f.run()

    sel=None
    sel <<= nm.mcut(f="customer,amount",i=dat)
    sel <<= nm.runfunc(bigAmount,lowerBound=4000)
    sel <<= nm.msum(k="customer",f="amount")
    print(sel.run())
    # [['A', '7200'], ['B', '8300']]

mcmdを用いずに関数を実装する
''''''''''''''''''''''''''''''

:numref:`special_runfunc1` では、mcmdの処理メソッド ``mstdin`` ``mstdout`` をつかって実装したが、
Pythonで利用可能な一般的な標準入出力のライブラリを用いても全く問題ない。
:numref:`special_runfunc2` は :numref:`special_runfunc1` の ``bigAmount`` 関数のみを書き換えたものである。
中では、sysライブラリの ``stdin`` を標準入力として用い、print で標準出力に書き出している。
全てPythonのネイティブコードのため自由度は非常に高くなる。
ただし、この場合、CSVデータのparsingロジックを自分で書く必要があることに注意する。
単純なCSVであれば問題ないが、ダブルクオーテーションやカンマの入った文字列を扱うのは結構面倒である。

  .. code-block:: python
    :linenos:
    :caption: mcmdを利用しない実装
    :name: special_runfunc2

    import sys
    def bigAmount2(lowerBound):
      header = True
      for line in sys.stdin:
        if header:
          print(line.strip())
          header = False
        else:
          tokens = line.strip().split(",")
          if int(tokens[1])>=lowerBound:
            print(",".join(tokens))

mcmdのイテレータを用いた実装
''''''''''''''''''''''''''''''

最後に、:numref:`special_runfunc1` と :numref:`special_runfunc2` の中間的な書き方として、
:numref:`special_runfunc3` に示すように、CSVのparsingはmcmdの ``mstdin`` にまかせて、
その後にmcmdのイテレーションを用いてPythonロジックを書く方法を紹介しておこう。
ポイントは、mcmdのイテレータは項目名ヘッダーを無視するため、 ``for`` 文の中でヘッダー行を意識しなくてもよい一方で、
次のメソッドへの出力には項目名ヘッダーを出力しなければならないという点である。
以下のコードでは、最初に項目名ヘッダーを出力している。

  .. code-block:: python
    :linenos:
    :caption: mstdinとイテレーションを組み合わせた例
    :name: special_runfunc3

    def bigAmount(lowerBound):
      print("customer,amount")
      for line in nm.mstdin():
        if int(line[1])>=lowerBound:
          print(",".join(line))

もしデータから項目名を取得したければ、 ``mstdin`` に続けて、 ``getline`` イテレータに接続し、
そこで項目名行を出力するオプション ``header=True`` を指定すれば良い。
項目名行の扱いは、 :numref:`special_runfunc2` と同様である。

  .. code-block:: python
    :linenos:
    :caption: イテレーションの中で項目名をデータから取得する方法
    :name: special_runfunc4

    def bigAmount(lowerBound):
      header = True   
      for line in nm.mstdin().getline(header=True):
        if header:      
          print(",".join(line))
          header = False  
        else:
          if int(line[1])>=lowerBound:
            print(",".join(line))

runfuncのデバッグ
''''''''''''''''''
``runfunc()`` メソッドは指定された関数をPythonにまかせて実行するだけなので、
もし関数の中でエラーが生じても、エラーが生じたことは分かっても、その詳細については感知していない。
例えば、 :numref:`special_debug1` は、上述の :numref:`special_runfunc3` に文法エラーを加えたコードで、
これを実行した時のエラーメッセージは :numref:`special_debug2` に示すとおりである。
このように、runfuncでエラーが起こっていることは分かってもそれ以上の詳細はわからない。

  .. code-block:: python
    :linenos:
    :caption: 関数内にエラーを入れた例(debug1.py)
    :name: special_debug1

    import sys
    import nysol.mcmd as nm

    def bigAmount(lowerBound):
      print("customer,amount")
      for line in nm.mstdin():
        if int(line)>=lowerBound: # lineの要素を指定していないエラー
          print(",".join(line))

    sel=None
    sel <<= nm.mcut(f="customer,amount",i=dat)
    sel <<= nm.runfunc(bigAmount,lowerBound=4000)
    sel <<= nm.msum(k="customer",f="amount")
    print(f.run(msg="on"))

  .. code-block:: bash
    :linenos:
    :caption: :numref:`special_debug1` の実行結果。
    :name: special_debug2

    $ python debug1.py
    #END# kgload; IN=0 OUT=5; 2018/09/05 10:18:51; 2018/09/05 10:18:51
    #END# kgcut f=customer,amount; IN=5 OUT=5; 2018/09/05 10:18:51; 2018/09/05 10:18:51
    #ERROR# error occured in the function, check the detail error message using try-exception in the function. (kgpyfunc); kgpyfunc; ; 2018/09/05 10:18:51; 2018/09/05 10:18:51
    #ERROR# ; kgshell (script RUN KGERROR runmain on kgshell); 2018/09/05 10:18:51
    RuntimeError: runmain on kgshell
    []

関数の中でのエラーの詳細を追跡するには、 ``try`` 〜 ``exception`` を入れることで解決できる。
そのコードを :numref:`special_debug3` に示す。
``exception`` の中で、トレースバック関数を呼び出しているが、出力先を標準エラー出力にするのがポイントである。
標準入出力は、 ``runfunc`` メソッドによってデータとし扱われてしまうからである。
また、デバッグ目的で変数の内容を表示させるときも、標準出力ではなくエラー出力に出さなければならない。
以下のコードでは、 ``sys.stderr`` のメソッドを使って引数 ``lowerBound`` を標準エラー出力に出力している。

実行時のメッセージは :numref:`special_debug4` に示す通りで、
7行目の ``int(line)`` に問題があることが示され、また最初に ``lowerBound`` の内容も表示されている。

  .. code-block:: python
    :linenos:
    :caption: エラーの追跡を可能とする関数の実装例(debug2.py)
    :name: special_debug3

    def bigAmount(lowerBound):
      try:
        sys.stderr.write(str(lowerBound)+"\n")
        print("customer,amount")
        for line in nm.mstdin():
          if int(line)>=lowerBound:
            print(",".join(line))
      except Exception as e:
        with open('/dev/stderr', 'w') as fpe:
          traceback.print_exc(file=fpe)

  .. code-block:: bash
    :linenos:
    :caption: :numref:`special_debug3` の実行結果。
    :name: special_debug4

    $ python debug2.py
    4000
    #END# kgcut f=customer,amount; IN=5 OUT=5; 2018/09/05 10:32:47; 2018/09/05 10:32:47
    #END# kgload; IN=0 OUT=5; 2018/09/05 10:32:47; 2018/09/05 10:32:47
    Traceback (most recent call last):
    File "special_runfunc.py", line 7, in bigAmountBug
    if int(line)>=lowerBound:
    TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
    #END# kgpyfunc; ; 2018/09/05 10:32:47; 2018/09/05 10:32:47
    #END# kgsum f=amount k=customer; IN=0 OUT=0; 2018/09/05 10:32:47; 2018/09/05 10:32:47
    #END# kgload; IN=0 OUT=0; 2018/09/05 10:32:47; 2018/09/05 10:32:47

runfuncは試験運用
''''''''''''''''''
runfuncメソッドは非常に強力で、個人や企業がよく利用する処理機能をメソッド化することが可能となり、
プログラムのモジュール化を促進できる。
しかしながら、一方でrunfuncからrunfuncを実行することも可能で、このようなネストが深くなった時にも
内部的にはどうにか頑張って処理しようとするが、まだ十分な運用と検証ができていない。
現在のところ、このメソッドは試験運用と考えてもらいたい。

cmd: コマンドの実行
-----------------------
``runfunc`` が処理をPythonの関数で実現していた一方で、 ``cmd`` メソッドは、OSのコマンドによって実現するものである。
UNIX系OSの多くは標準入力からデータを受け取り、コマンド内部で一定の処理を付し、標準出力に結果を書き込む。
基本的な利用方法を :numref:`special_cmd1` に示している。
ここでは、 ``customer`` と ``amount`` 項目を選択したのち、 ``tr`` コマンドに接続している(あまり意味のある例ではない)。
``tr`` コマンドは 入力のバイトストリームに対して1文字単位の置換を実行する。
以下の例では 文字 ``A`` を ``C`` に置換している。
結果として、顧客 ``A`` が ``C`` に置き換わった集計結果が計算されている。
ただし、``cmd`` メソッドには、項目名もデータ本体も区別することはなく、
さらにはカンマ区切りの項目も区別なくデータストリームとして流されるだけであることに注意する。
例えば、以下の例では、もし項目名に ``A`` が含まれていれば、それも ``C`` に変換されてしまい、意図した動きにはならない。
項目名ヘッダーの問題だけであれば、 :numref:`special_cmd2` に示されるように、直前のメソッド ``mcut`` で項目名ヘッダーを抑制し( ``nfno=True`` )
そして、コマンド実行後に ``mcut`` メソッドにより項目名ヘッダー行を追加してやれば良い。

  .. code-block:: python
    :linenos:
    :caption: mcmdのインポートと入力データの設定
    :name: special_cmd1

    import nysol.mcmd as nm
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

    f=None
    f <<= nm.mcut(f="customer,amount",i=dat)
    f <<= nm.cmd("tr 'A' 'C'")
    f <<= nm.msum(k="customer",f="amount")
    print(f.run())
    # [['B', '8300'], ['C', '7200']]


  .. code-block:: python
    :linenos:
    :caption: 項目名ヘッダーをスキップする例
    :name: special_cmd2

    f=None
    f <<= nm.mcut(f="customer,amount",nfno=True,i=dat)
    f <<= nm.cmd("tr 'A' 'C'")
    f <<= nm.mcut(f="0:customer,1:amount",nfni=True)
    f <<= nm.msum(k="customer",f="amount")
    print(f.run(msg="on"))
    # [['B', '8300'], ['C', '7200']]


ファイル一覧の取得
''''''''''''''''''''''

UNIX系OSには多くの便利なコマンドが多く存在する。
例えば、 表構造データを柔軟に扱うawk、パターンマッチで行を選択するgrep、
正規表現による文字列置換のsedなどである。
UNIX系のコマンドの扱いに慣れた人にとっては、cmdメソッドを利用することで、
これらのコマンドをmcmdメソッドと連携して利用することができるようになる。
以下に、 ``ls`` ``tail`` ``sed`` の3つのコマンドを用いて、ファイルリストの一覧を処理するプログラムをに紹介しておく。
:numref:`special_ls` はそのコードである。
``ls -l`` でパーミッションやサイズ、ファイル名といった情報が標準出力に出力される。
最初の行にファイル数の情報が出力されるので ``tail`` コマンドでその行をスキップしている(2行目から読み込む)。
そして、 ``ls`` の出力の区切り文字である複数のスペース文字を ``sed`` コマンドによりカンマに変換している。
あとは、 ``mcut`` メソッドで項目名ヘッダーを付けてファイル一覧の出来上がりである。

  .. code-block:: python
    :linenos:
    :caption: lsコマンドを使ってファイル一覧を取得する例
    :name: special_ls

    f=None
    f <<= nm.cmd("ls -l")
    f <<= nm.cmd("tail +2")
    f <<= nm.cmd("sed 's/  */,/g'")
    f <<= nm.mcut(nfni=True,f="0:permission,1:link,2:user,3:group,4:volume,5:month,6:day,7:time,8:filename")
    print(f.run())
    # [['-rw-r--r--', '1', 'foo', 'staff', '4997', '8', '3', '16:44', 'dat.csv'], ['-rw-r--r--', '1', 'foo', 'staff', '104', '9', '6', '10:56', 'dat2.csv'], ...]


マルチバイト文字の変換
''''''''''''''''''''''

最後に、データクリーニングでよく利用されるマルチバイトコードの変換コマンドである |nkf| の利用例を
:numref:`special_nkf` に示しておく。
ただし、これは動作させるためのコーディング例であるため、データ ``dat.csv`` にはマルチバイト文字は含まれていないが、
このファイルがShift_jisコードであることを想定している。
また、OSコマンドとして |nkf| をインストールしておく必要がある。

  .. code-block:: python
    :linenos:
    :caption: nkfによるShift_jisコードをutf-8コードに変換する例
    :name: special_nkf

    >>> import nysol.mcmd as nm
    >>> with open('dat.csv','w') as f:
    >>>   f.write(
    '''customer,quantity,amount
    A,20180101,5200
    B,20180101,800
    B,20180112,3500
    A,20180105,2000
    B,20180107,4000
    ''')

    >>> f=None
    >>> f <<= nm.cmd("iconv -f Shift_JIS -t UTF-8 dat.csv")
    >>> f <<= nm.mcut(f="customer,amount")
    >>> f <<= nm.msum(k="customer",f="amount")
    >>> print(f.run())
    [['A', '7200'], ['B', '8300']]

  .. |nkf| raw:: html

    <a href="https://en.wikipedia.org/wiki/Network_Kanji_Filter" target="_blank">nkf</a>

