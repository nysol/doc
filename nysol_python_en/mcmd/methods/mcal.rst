mcal 項目間演算
--------------------

``c=`` パラメータで指定した計算式で計算をおこない、 ``a=`` パラメータで指定した項目名に出力する。
``mcal`` が出力する項目は、プログラムの単純化のため、例外なく1つに限定している。
計算式の詳細はの「 :doc:`../calsel` 」の節を参照のこと。

**エラーメッセージについて**

``#ERROR# unknown function or operator``

このエラーメッセージが出るということは、関数もしくは演算子の指定に誤りがある。
例えば、以下のような文字列の結合関数catについてのエラーメッセージについて考える。

  .. code-block:: python
    :linenos:
    :caption: cat関数のエラー
    :name: mcal_error

		nm.mcal(c='cat("-",1,2)').run()
		#ERROR# : unknown function or operator: cat_SNN(cat_SN) (kgcal)
 
「cat_SNN」のアンダーバーの前のcatは関数名を示し、その後のSNNは引数の型を示している。
Sは文字列型、Nは数字型、Dは日付型、Tは時刻型、Bは真偽型である。
3つの引数を指定しているので3文字(SNN)となっている。
すなわち、このエラーメッセージは「引数としてSNNをとるcatという関数」
は登録されていないということを意味する。
ここで、エラーメッセージの括弧の中は2文字(SN)となっているが、
それは2番目以降のパラメータが可変個指定可能であるため、
それらの代表として１つだけ表記しているためである。

以下のように2,3番目の引数を文字列型にすればよい。

  .. code-block:: python
    :linenos:
    :caption: cat関数のエラー
    :name: mcal_error2

		nm.mcal(c='cat("-","1","2")').run()

パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**a=** : 型=str , 必須

  | 新たに計算結果の出力として追加される項目の名前を指定する。

**c=** : 型=str , 必須

  | 用意された関数を組み合わせて計算する式を指定する。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullout=<common_param_assert_nullout>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`tmppath=<common_param_tmppath>`
, :ref:`precision=<common_param_precision>`


利用例
''''''''''''

関連メソッド
''''''''''''''''''''

* :doc:`msel` : 演算の結果を用いて行選択するのであればこちらを使う。

