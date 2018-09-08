mcat 併合
---------------------

``i=`` パラメータで指定した全データのレコードを、指定した順に併合する。
ワイルドカードでデータを指定した場合は、データのアルファベット順に併合される。

パラメータ
''''''''''''''''''''''

  .. list-table::
    :header-rows: 1

    * - キーワード
      - 内容

    * - | **i=**
        |   任意
        |   デフォルト:標準入力
      - |   入力データリストを指定する。
        |   複数のデータをカンマで区切って指定する。ワイルドカードを用いることができる。
    * - | **o=**
        |   任意
        |   デフォルト:標準出力
      - |   出力データを指定する。
    * - | **f=**
        |   任意
        |   デフォルト:
      - |   併合する項目名を指定する。
        |   指定を省略すれば ``i=`` で指定した1つ目のデータの項目名が使われる。
    * - | **skip_fnf=True|False**
        |   任意
        |   デフォルト:False
      - |   ``i=`` で指定したデータが存在しなくてもエラー終了しない。
        |   ただし、全データがなければエラーとなる。
    * - | **nostop=True|False**
        |   任意
        |   デフォルト:False
      - |   ``nostop=True``  , ``skip=True`` , ``force=True`` は、指定の項目名がなかったときの動作を制御するフラグである。
        |   ``nostop=True`` は、指定の項目名がなければnullを出力する。
        |   ``nfn=True`` が同時に指定された場合，項目数が異なればエラー終了する。
    * - | **skip=True|False**
        |   任意
        |   デフォルト:False
      - |   指定の項目名がなければそのデータは併合しない。
        |   ``nfn=True`` が同時に指定された場合、項目数が異なればそのデータは併合しない。
    * - | **skip_zero=True|False**
        |   任意
        |   デフォルト:False
      - |   -nfnを指定していない場合でも0バイトデータでエラーにならないようにする。
    * - | **flist=**
        |   任意
        |   デフォルト:
      - |   併合するデータリストをCSVデータとして指定する。flist=fileName:fldNameで指定する。
    * - | **kv=**
        |   任意
        |   デフォルト:
      - |   パス名に含めた”key-value”の文字列を抜き出し項目名とその値としてデータに付加する。
    * - | **force=True|False**
        |   任意
        |   デフォルト:False
      - |   指定の項目名がなければ，項目番号で強制併合する。
        |   指定の項目番号がなければnullを出力する。
    * - | **stdin=True|False**
        |   任意
        |   デフォルト:False
      - |   標準入力も併合する。
    * - | **add_fname=True|False**
        |   任意
        |   デフォルト:False
      - |   併合元のデータを最終項目として追加する。
        |   標準入力は ``/dev/stdin`` という名称になる。
        |   項目名は ``"fileName"`` 固定なので、入力データに同一の項目名があるとエラーとなる。

共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`add_fname=<common_param_add_fname>`
, :ref:`-stdin=<common_param_-stdin>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`tmppath=<common_param_tmppath>`
, :ref:`precision=<common_param_precision>`

利用例
''''''''''''

**importと入力データ(CSV)の準備**
  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm    
        
    with open('dat1.csv','w') as f:
      f.write(
    '''customer,date,amount
    A,20081201,10
    B,20081002,40
    ''')
            
    with open('dat2.csv','w') as f:
      f.write(
    '''customer,date,amount
    A,20081207,20
    A,20081213,30
    B,20081209,50
    ''')
            
    with open('dat3.csv','w') as f:
      f.write(
    '''customer,date,quantity
    A,20081201,3
    B,20081002,1
    ''')
    
**同一項目名ファイルの併合**



  .. code-block:: python
    :linenos:

    >>> nm.mcat(i="dat1.csv,dat2.csv", o="rsl1.csv").run()
    # ## rsl1.csv の内容
    # customer,date,amount
    # A,20081201,10
    # B,20081002,40
    # A,20081207,20
    # A,20081213,30
    # B,20081209,50

**項目名の異なるファイルの併合**

``i=`` の最初のファイル ``dat1.csv`` の項目「顧客,日付,金額」の3項目を併合する。
しかし、 ``dat3.csv`` には ``amount`` 項目がないので、エラーとなる。
ただし、 ``dat1.csv`` の内容は既に出力されていることに注意する。


  .. code-block:: python
    :linenos:

    >>> nm.mcat(i="dat1.csv,dat3.csv", o="rsl2.csv").run()
    # ## rsl2.csv の内容

**項目名の異なるファイルの併合2**

前例に ``nostop=True`` オプションを付けると、項目が見つからないデータについてはNULL値を出力するようになり、
途中でエラー終了することはなくなる。
その他にも、項目が見つからなかった場合の動作を変更するオプションとして、 ``skip,force`` がある。
詳しくはパラメータの説明を参照されたい。


  .. code-block:: python
    :linenos:

    >>> nm.mcat(nostop=True, i="dat1.csv,dat3.csv", o="rsl3.csv").run()
    # ## rsl3.csv の内容
    # customer,date,amount
    # A,20081201,10
    # B,20081002,40
    # A,20081201,
    # B,20081002,

**項目名を指定して併合**

``f=`` で項目名を指定すると、それら指定した項目のみを併合する。


  .. code-block:: python
    :linenos:

    >>> nm.mcat(f="customer,date", i="dat2.csv,dat3.csv", o="rsl4.csv").run()
    # ## rsl4.csv の内容
    # customer,date
    # A,20081207
    # A,20081213
    # B,20081209
    # A,20081201
    # B,20081002

**標準入力の併合**

``stdin=True`` を指定することで、 ``dat2.csv`` を標準入力から追加する。


  .. code-block:: python
    :linenos:

    >>> 


**ファイル名項目を追加**

``add_fname=True`` を指定すると、元ファイルの名前を ``fileName`` 項目で追加する。
標準入力のファイル名は ``/dev/stdin`` となる。


  .. code-block:: python
    :linenos:

    >>> 


**ワイルドカード指定**

カレントディレクトリに ``dat1.csv,dat2.csv,dat3.csv`` の3つのCSVファイルがあったとして、
それらを全て併合するのにワイルドカード ``dat*.csv`` を指定する。


  .. code-block:: python
    :linenos:

    >>> nm.mcat(force=True, i="dat*.csv", o="rsl7.csv").run()
    # ## rsl7.csv の内容
    # customer,date,amount
    # A,20081201,10
    # B,20081002,40
    # A	1102	a,,
    # A	2203	aaa,,
    # B	1155	bbbb,,
    # B	3104	c,,
    # B	1206	de,,
    # A-1102-a,,
    # A-2203-aaa,,
    # B-1155-bbbb,,
    # B-3104-c,,
    # B-1206-de,,
    # A,20081207,20
    # A,20081213,30
    # B,20081209,50
    # A,20081201,3
    # B,20081002,1
    # A,apple,100
    # A,milk,350
    # B,orange,100
    # B,orange,100
    # B,pineapple,500
    # B,wine,1000
    # C,apple,100
    # C,orange,100
    # D,orange,100

**同一ファイルの複数回併合**

同一ファイルを複数指定することも可能である。


  .. code-block:: python
    :linenos:

    >>> nm.mcat(i="dat1.csv,dat1.csv,dat1.csv", o="rsl8.csv").run()
    # ## rsl8.csv の内容
    # customer,date,amount
    # A,20081201,10
    # B,20081002,40
    # A,20081201,10
    # B,20081002,40
    # A,20081201,10
    # B,20081002,40



関連メソッド
''''''''''''

- :doc:`msep` 
