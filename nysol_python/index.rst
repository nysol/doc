.. nysol_python documentation master file, created by
   sphinx-quickstart on Sun May 27 10:48:44 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NYSOL
========================================

NYSOLとはビッグデータからの知識発見を効率的かつ効果的に支援するために開発されたソフトウェアライブラリである [#f0]_ 。
これまでに、シェルから利用できるコマンド群として提供してきたが [#f1]_ 
それらをPython上で利用できるように改良したものが **nysol_python** ライブラリである。
現在のところ、nysol_pythonには、
データの前処理に威力を発揮するmcmdモジュールと
アイテム集合マイニングに関する多様なツールを提供するTakeモジュールが含まれている。

.. toctree::
   :maxdepth: 1
   :caption: 目次:

   インストール<install>
   mcmdモジュール<mcmd>
   takeモジュール<take>
   dataset/index
   bench/index
   glossary


* :ref:`genindex`

.. * :ref:`modindex`
.. * :ref:`search`

.. [#f0] 本ソフトウェアの開発には、JST CREST(グラント番号: JPMJCR1401)の研究助成を受けている。
.. [#f1] http://www.nysol.jp/

