
mcmdモジュール
------------------
MCMD [#f1]_ とは、大規模な表構造データを高速に処理する目的で開発されたメソッド群である。
MCMDは、単一の機能(例えば、並べ替えや表の結合など)に特化したメソッドを80種類以上提供している。
全てのメソッドは共通して、CSV(カンマ区切りデータ)ファイルもしくはPythonのリストを読み込み、
結果をCSVとして標準出力に書き出すだけの非常にシンプルな処理方式に従っている。
個々のメソッドはスレッド単位で実行され、データはスレッド間パイプを構成することで組み合わせて処理され、
sh等のOSのシェルを用いることなくPython内で完結したプログラミングを可能としている。
MCMDは、特に知識発見プロセス [#f2]_ における **前処理** で威力を発揮するが、その他のプロセスにおいても利用可能である。

.. toctree::
   :maxdepth: 2
   :numbered: 2
   :caption: Contents:

   mcmd/hello
   mcmd/data
   mcmd/field
   mcmd/flow
   mcmd/methods/index
   mcmd/common_param
   mcmd/calsel
   mcmd/methods/func_index
   mcmd/autoadd
   mcmd/special
   mcmd/run
   mcmd/iterator

..
   mcmd/workfile
   mcmd/jupyter


パラメータ

.. rubric:: Footnotes

.. [#f1] これまでの慣習に従って「Mコマンド」と呼ぶが、もはやコマンドではない。MCMDのMは、発案者である松田康之氏のイニシャルに拠っている。
.. [#f2] データ獲得，選択，前処理，変換，知識発見アルゴリズムの適用，解釈，評価といった 一連のサイクルを指す(引用: OR辞典 [#f3]_ )。
.. [#f3] http://www.orsj.or.jp/~wiki/wiki/index.php/%E3%83%87%E3%83%BC%E3%82%BF%E3%83%9E%E3%82%A4%E3%83%8B%E3%83%B3%E3%82%B0
