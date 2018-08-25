インストール
==================

事前にインストールが必要なソフトウェア
----------------------------------------

pipインストール
-------------------------------------
他のパッケージ同様、pipを利用してインストールできる。
PyPiにおけるnysolのページは  |pypi_nysol| を参照されたい。

  .. code-block:: bash
    :linenos:
    :caption: nysolのインストール
    :name: install_pip

    $ pip install nysol


  .. |pypi_nysol| raw:: html

    <a href="https://test.pypi.org/project/nysol" target="_blank">https://test.pypi.org/project/nysol</a>

オフラインインストール
-------------------------------------
ネット環境がない環境では、あらかじめgitHubよりソース一式をダウンロードしておき、以下の手順でインストールを行う。

  .. code-block:: bash
    :linenos:
    :caption: nysolのダウンロードとオフラインインストール
    :name: custAmount

    # 以下、オンライン環境でソース一式をgitHubよりダウンロード(clone)しておく。
    $ git clone https://github.com/nysol/nysol_python.git
    # nysol_pythonディレクトリをオフライン環境に移し、以下でインストールする。
    $ cd nysol_python
    $ pip install .

