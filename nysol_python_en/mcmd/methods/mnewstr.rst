mnewstr 固定文字列データの新規生成
------------------------------------------

``v=`` パラメータで指定した文字列データを新規作成し、 ``a=`` パラメータで指定した項目名で出力する。
一度に複数の項目を生成することも可能。


パラメータ
''''''''''''''''''''''

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**a=** : 型=str , 必須

  | 新規に作成するデータの項目名を指定する。
  | 複数の項目を生成する場合は、項目名をカンマで区切る。
  | ``nfn`` もしくは ``nfno`` オプション指定時は指定の必要はない。

**v=** : 型=str , 必須

  | 新しく作成する文字列を指定する。
  | 複数の項目を生成する場合は、値をカンマで区切る。 ``a=`` で指定した個数と同数でなければならない。

**l=** : 型=str , 任意(default=10)

  | 新規作成する乱数データの行数を指定する。



共通パラメータ
''''''''''''''''''''

:ref:`o=<common_param_o>`
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


**基本例**

``custNo`` と ``A0001`` という文字列データを5行作成し、 ``attribute,code`` という名前の項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mnewstr(a="attribute,code", v="custNo,A0001", l="5", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # attribute,code
    # custNo,A0001
    # custNo,A0001
    # custNo,A0001
    # custNo,A0001
    # custNo,A0001


関連メソッド
''''''''''''''''''''

* :doc:`mnewnumber` : 連番を生成する。
* :doc:`mnewrand` : 乱数を生成する。

