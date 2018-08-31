marff2csv arff形式からcsv形式への変換
---------------------------------------------------------------------------------

arff形式(WEKA用のデータフォーマット)のデータからcsv形式のデータへ変換する。
\subsubsection*{arff形式データ}
以下arff形式データのフォーマットを記載する。
\begin{Verbatim}[baselinestretch=0.7,frame=single,fontsize=\small]
@RELATION       タイトル
@ATTRIBUTE      項目名    string(文字列)
@ATTRIBUTE      項目名    date(日時 フォーマット:フォーマットは省略可能。
省略した場合は、"yyyy-MM-dd'T'HH:mm:ss"）
@ATTRIBUTE      数量    numeric(数字)
@ATTRIBUTE      商品    {A,B}(カテゴリ型項目)
@DATA(実データ)
No.1,20081201,1,10,A
No.2,20081202,2,20,A
No.3,20081203,3,30,A
No.4,20081201,4,40,B
No.5,20081203,5,50,B
\end{Verbatim}

パラメータ
''''''''''''''''''''''

  .. list-table::
    :header-rows: 1

    * - キーワード
      - 内容

    * - | **i=**
        |   optional
        |   default:
      - |   入力ファイル名を指定する。
    * - | **o=**
        |   optional
        |   default:
      - |   出力ファイル名を指定する。

共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_nullout=<common_param_assert_nullout>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`q=<common_param_q>`
, :ref:`tmppath=<common_param_tmppath>`
, :ref:`precision=<common_param_precision>`

利用例
''''''''''''



関連メソッド
''''''''''''

- :doc:`mcsv2arff` 
\subsection*{参考資料}
\href{http://weka.wikispaces.com/ARFF}{http://weka.wikispaces.com/ARFF}
