その他
==============================

バージョン番号について
----------------------------

逆引き
----------------------------

ソーティングキーの指定方法

sortingなどの自動追加の仕組みをどこかに入れる

結果全体を2重リストに出力、writelist(dtype=), writedictみたいなのはない。
=> 項目別の配列にするpythonの方法も書いておく。できれば転置して出力。

項目名の指定方法:文字列でもリストでもOK

tag="xxx"を付けるとメッセージに表示される。
msgレベルについて各


メソッド
----------------------------

処理フローオプジェクトには、[参照]に示された80以上のデータ処理メソッドが定義されており、
それらのメソッドをcallすると、その内容が処理フローオブジェクトに追加登録される。
処理フローオブジェクトには、データ処理メソッド以外にも、以下に示すメンバーメソッドとクラスメソッドが定義されている。

メンバーメソッド
'''''''''''''''''''
  .. list-table:: 処理フローオブジェクトで利用できるメンバーメソッド一覧
    :header-rows: 1
    :name: flow_mmethod

    * - メソッド名: 内容
      - パラメータ
    * - redirect(dir): 出力の切り替え
      - dir="u"
    * - run: 登録されたメソッドの実行
      - msg="off"|"one",runlimit=同時実行数(default:300)
    * - __ilshift__: <<=演算子
      - 左辺:処理フローオブジェクト,右辺:処理フローメソッド
    * - __rlshift__: <<=演算子
      - 処理フローオブジェクトの生成,左項None用 左辺:None,右辺:処理フローメソッド


クラスメソッド
'''''''''''''''''''''''''

  .. csv-table:: 処理フローオブジェクトにで利用できるクラスメソッド一覧
    :delim: |
    :header-rows: 1
    :name: flow_mmethod

    メソッド名|内容
    runs(obj)|リストobjに登録された処理フローオブジェクトをすべて実行する
    modelInfos|登録されたmcmdメソッドの情報を出力する
    drawModels|登録されたmcmdメソッドの情報を出力する
    drawModelsD3|登録されたmcmdメソッドの情報をSVG(html)で出力する

上限128
RUN_LIMIT=で上限は突破できる。 => 自己責任

実際の同時実行の計算は
メモリから計算している。
実メモリを取得して、47で割っている。
kgcsvのバッファサイズ47M


