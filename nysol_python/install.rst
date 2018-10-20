インストール
==================

対応OS
-----------------
nysolは、Linux, MacOSX, Bash on Ubuntu on Windowsといった、
代表的なOSでの動作確認はとれている。
その他にも、UNIX系のOSであれば利用できるであろう。
以下に動作が確認できているOSおよびそのバージョン一覧を示す。

* MacOS 10.9.5(Marverics)以上
* CentOS 7.3 1611
* Ubuntu 16.04 LTS
* Bash on Ubuntu on Windows(Windows 10)

Pythonのバージョン
-----------------------
Pythonのバージョンは、3.6.5での動作確認は取れている。
2.xは未対応である。

必要なライブラリ
-----------------------
Nysolのインストールには、以下のソフトウェアが必要となる。

* c++コンパイラ
* |boost|
* |lib2xml|

.. |boost| raw:: html

  <a href="http://www.boost.org/" target="_blank">boost C++ library</a>

.. |lib2xml| raw:: html

  <a href="http://xmlsoft.org/" target="_blank">lib2xml library</a>

pipインストール
-------------------------------------
他の多くのPythonのパッケージ同様、pipを利用してインストールできる。
PyPiにおけるnysolのページは  |pypi_nysol| を参照されたい。

  .. code-block:: bash
    :linenos:
    :caption: MAC OSでのインストール
    :name: install_pip_mac

    $ brew install boost
    $ pip install nysol

  .. code-block:: bash
    :linenos:
    :caption: CentOSでのインストール
    :name: install_pip_centos

    $ sudo yum install boost-devel
    $ sudo yum install libxml2-devel
    $ pip install nysol

  .. code-block:: bash
    :linenos:
    :caption: Ubuntu,Bash on Windowsでのインストール
    :name: install_pip_bow

    $ sudo apt-get install libboost-all-dev
    $ sudo apt-get install libxml2-dev
    $ pip install nysol
    # 共有ライブラリのパス設定
    # 起動時に毎回設定するのであれば.bash_profileに記載しておく(ログインし直すまでは反映されない)。
    $ export LD_LIBRARY_PATH=/usr/local/lib

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

インストール完了の確認
-------------------------------------
インストールが完了すれば、Pythonを起動し、Nysolモジュールをimportしてみよう。
エラーメッセージが表示されなければインストール完了である。
mcmdモジュールの「 :doc:`mcmd/hello` 」節の例題を実行してみよう！

  .. code-block:: bash
    :linenos:
    :caption: モジュールのimport
    :name: install_import

    $ python
    Python 3.6.5 (default, Apr  4 2018, 11:29:29) 
    [GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import nysol.mcmd as nm # mcmdモジュールのimport
    >>> import nysol.take as tk # takeモジュールのimport

