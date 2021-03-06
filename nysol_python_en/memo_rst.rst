
執筆要領
====================

.. todolist::

節の記号
--------------
一つのドキュメントの中での節を表す記号のレベルは以下のとおりとする。

1) ``=======``
2) ``-------``
3) ``'''''''``
4) ``:::::::``

.. _節の参照:

節の参照
--------------
節の前には節タイトルと同じラベルを作成し、そのラベルを ``:ref:`` ロールで参照する。
ラベルはタイトルと空行で区切らなければならない。
ラベルがユニークにならなければ、上位の節タイトルを含めるなど工夫する。
「 :ref:`節の参照` 」もしくは「 :ref:`ここ<節の参照>` 」のように参照する。

ドキュメントの参照
----------------------
ファイル単位のドキュメントの参照は ``:doc:`` ロールで参照する。
例えば、「はじめに」のドキュメントファイル名は hello.rst なので、
「 :doc:`mcmd/hello` 」の節を参照、のように指定する。

自由な参照
---------------------

.. _anywhere_reference:
を置いた場所にリンクするには

:ref:`どこでもリンク<anywhere_reference>` のように用いる。

外部リンク
---------------------
外部リンクは別窓で開くようにする。
yahooの検索は |yahoo| で！

  .. |yahoo| raw:: html

    <a href="https://www.yahoo.com/" target="_blank">ヤフー</a>

用語集
------------------
用語集はglossary.rstにまとめる。
用語の参照は、 :term:`キーブレイク処理` のようにする。

コマンド名
--------------
リストの入出力 :command:`rm` は削除コマンド

略語
--------------
CSVの入出力は :abbr:`LIFO (last-in, first-out)` を通じて行われる

表
--------------
.. csv-table:: 入力データ例:mcmdが扱う表構造データ
  :name: hello_intable
  :header: customer,date,amount

  A,20180101,5200
  B,20180101,4000

.. list-table:: mcmdが扱う6つのデータ型
  :header-rows: 1
  :name: data_type

  * - データ型
    - テキスト例
    - 変換内容
  * - 数値型
    - "10", "2.5", "1.5E+10"
    - | 倍精度実数に変換した値
      | 行マタギ
  * - 文字列型
    - "abc", "あいう"
    - 変換なし

+------+----------------+------+-------------------------+
|      |                |      | data size               |
+------+----------------+関数名+-------+--------+--------+
| task | program        |      | small |   mid  |  large |
+======+================+======+=======+========+========+
|      | pandas         | pd1  | 0.130 |   1.28 |  29.18 |
|      +----------------+------+-------+--------+--------+
| avg  | mcmd           | nm1  | 0.036 |   0.33 |  _7.39 |
|      +----------------+------+-------+--------+--------+
|      | mcmd+multi     | nm1a |       |        |  _5.38 |
+------+----------------+------+-------+--------+--------+
|      | pandas         | pd2  | 16.91 |  19.22 |  74.88 |
|      +----------------+------+-------+--------+--------+
| win  | mcmd           | nm2  | 0.27  |   2.54 |  63.94 |
|      +----------------+------+-------+--------+--------+
|      | mcmd+file      | nm2a | 0.19  |   1.63 |  41.87 |
+------+----------------+------+-------+--------+--------+
|      | pandas         | pd3  | 18.72 | 174.54 |        |
|      +----------------+------+-------+--------+--------+
| for  | pandas(values) | pd3a | 0.35  |   3.10 |  73.42 |
|      +----------------+------+-------+--------+--------+
|      | mcmd           | nm3  | 0.27  |   2.73 |  60.43 |
+------+----------------+------+-------+--------+--------+

footnote
--------------
脚注を書きたい場所で [#name]_ というマークアップを書く。
脚注の本体をドキュメントの下の方の “脚注” のためのrubric見出しの中に書く。

MCMD [#f1]_ とは、・・・

.. rubric:: Footnotes

.. [#f1] これまでの慣習に従って「Mコマンド」と呼ぶが、・・・

