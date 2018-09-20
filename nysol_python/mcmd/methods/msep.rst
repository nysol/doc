msep レコードの分割
------------------------

``d=`` パラメータで指定したデータのデータに各レコードを出力する。
指定するデータに項目名を埋め込むことができるので、結果としてレコード分割することになる。
埋め込むデータは ``${項目名}`` によって指定する。
例えば、 ``d=./out/${date}.csv`` と指定すれば、カレントディレクトリの下の ``out`` ディレクトリの下に、
``date`` 項目の値別にデータが作成されることになる。
内部的には、埋め込んだ項目の値をキーとして認識し、並べ替えが行われた後レコードが分割される。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**d=** : 型=str , 必須

  | 異なるデータデータに分割する項目名を指定する。
  | ここで指定した文字列をデータとして各レコードが追記されていく。
  | 項目名は ``${項目名}`` によって埋め込む。

**f=** : 型=str , 任意(default=)

  | 出力する項目名を指定する。

**p=** : 型=bool , 任意(default=False)

  | ``d=``  パラメータで指定したディレクトリ名が存在しなければ作成する。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`q=<common_param_q>`
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
    '''item,date,quantity,price
    A,20081201,1,10
    B,20081201,4,40
    A,20081202,2,20
    A,20081203,3,30
    B,20081203,5,50
    ''')


**基本例**

``dat`` という名前のディレクトリを作成し、
そのディレクトリに日付項目値 ``date`` ごとに異なるファイルに出力する。

  .. code-block:: python
    :linenos:

    nm.msep(d="./dat/${date}.csv", p=True, i="dat1.csv").run()
    ###  の内容


関連メソッド
''''''''''''''''''''

* :doc:`msep2` : ``msep`` と同じような機能だが、データは連番で出力し、キー項目との対応表を別途データに出力する。
* :doc:`mcat` : ``msep`` で分割したデータをこのコマンドで併合すると元に戻る。

