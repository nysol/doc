mcat 併合
---------------------

``i=`` パラメータで指定した全ファイルのレコードを、指定した順に併合する。
ワイルドカードでファイル名を指定した場合は、ファイル名のアルファベット順に併合される。

パラメータ
''''''''''''''''''''''

  .. list-table::
    :header-rows: 1

    * - キーワード
      - 内容

    * - | **i=**
        |   optional
        |   default:
      - |   入力ファイル名リストを指定する。
        |   複数のファイルをカンマで区切って指定する。ワイルドカードを用いることができる。
    * - | **o=**
        |   optional
        |   default:
      - |   出力ファイル名を指定する。
    * - | **f=**
        |   optional
        |   default:
      - |   併合する項目名を指定する。
        |   指定を省略すれば ``i=`` で指定した1つ目のファイルの項目名が使われる。
    * - | **skip_fnf=True|False**
        |   optional
        |   default:False
      - |   ``i=`` で指定したファイルが存在しなくてもエラー終了しない。
        |   ただし、全ファイルがなければエラーとなる。
    * - | **nostop=True|False**
        |   optional
        |   default:False
      - |   ``nostop=True``  , ``skip=True`` , ``force=True`` は、指定の項目名がなかったときの動作を制御するフラグである。
        |   ``nostop=True`` は、指定の項目名がなければnullを出力する。
        |   ``nfn=True`` が同時に指定された場合，項目数が異なればエラー終了する。
    * - | **skip=True|False**
        |   optional
        |   default:False
      - |   指定の項目名がなければそのファイルは併合しない。
        |   ``nfn=True`` が同時に指定された場合、項目数が異なればそのファイルは併合しない。
    * - | **skip_zero=True|False**
        |   optional
        |   default:False
      - |   -nfnを指定していない場合でも0バイトファイルでエラーにならないようにする。
    * - | **flist=**
        |   optional
        |   default:
      - |   併合するファイルリストをCSVデータとして指定する。flist=fileName:fldNameで指定する。
    * - | **kv=**
        |   optional
        |   default:
      - |   パス名に含めた”key-value”の文字列を抜き出し項目名とその値としてデータに付加する。
    * - | **force=True|False**
        |   optional
        |   default:False
      - |   指定の項目名がなければ，項目番号で強制併合する。
        |   指定の項目番号がなければnullを出力する。
    * - | **stdin=True|False**
        |   optional
        |   default:False
      - |   標準入力も併合する。
    * - | **add_fname=True|False**
        |   optional
        |   default:False
      - |   併合元のファイル名を最終項目として追加する。
        |   標準入力は ``/dev/stdin`` という名称になる。
        |   項目名は ``"fileName"`` 固定なので、入力データに同一の項目名があるとエラーとなる。

共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`add_fname=<common_param_add_fname>`
, :ref:`-stdin=<common_param_-stdin>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`tmppath=<common_param_tmppath>`
, :ref:`precision=<common_param_precision>`

利用例
''''''''''''



関連メソッド
''''''''''''

- :doc:`msep` 
