mdformat 日付時刻抽出
------------------------------

他のシステムからエクスポートしたCSVデータでは、
日付時刻項目にスラッシュ記号やコロン記号が入っていることが多く、
また月日や時が1桁で格納されている場合もある
(例: ``2014/7/18 1:57`` )。
このような項目をそのままMCMDで扱おうとすると、
日付計算や並べ替え、範囲検索がうまくいかない。
``mdformat`` コマンドを使うことで、
``f=`` パラメータで指定した項目から、
``c=`` パラメータで指定したフォーマットに従って
年月日・時分秒を抽出し、MCMDで扱うことが可能な
:doc:`日付型や時刻型`
に変換することができる。

パラメータ
''''''''''''''''''''''

  .. list-table::
   :header-rows: 1

   * - キーワード
     - 内容
   * - | **i=str**
       | 任意
     - | 入力データを指定する。
   * - | **o=str**
       | 任意
     - | 出力データを指定する。
   * - | **f=str**
       | 必須
     - | 抽出対象となる項目名リスト(複数項目指定可)を指定する。
   * - | **c=str**
       | 必須
     - | 文字列のフォーマットを指定する。フォーマットの変換指定文字参照
   * - | **A=bool**
       | 任意
     - | このオプションにより、指定した項目を置き換えるのではなく、新たに項目が追加される。


共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
, :ref:`assert_nullout=<common_param_assert_nullout>`
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
    '''fld
    date:20120304 time:121212
    date:20101204 time:011309.1234
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''fld,fld2
    2010/11/20,2010/11/21
    2010/1/1,2010/1/2
    2011/01/01,2010/01/02
    2010/1/01,2010/1/02
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''fld
    2010 11 20 12:34:56
    2011 01 01 23:34:56
    2010  1 01 123455
    ''')


**基本例**

``fld`` 項目から日付・時刻を抽出し変換する。
``fld`` 項目には「date:年月日 time:時分秒.マイクロ秒」の形式で日付・時刻が格納されているので、
``c=`` パラメータには「 ``date:%Y%m%d time:%H%M%s`` 」と指定している。

  .. code-block:: python
    :linenos:

    nm.mdformat(f="fld", c="date:%Y%m%d time:%H%M%s", i="dat1.csv", o="rsl1.csv").run()
