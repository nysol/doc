mcal \section{日付型と時刻型について\label{sect:datetime}}
----------------------------------------------------------------------------------------------

``c=`` パラメータで指定した計算式で計算をおこない、 ``a=`` パラメータで指定した項目名に出力する。
``mcal`` が出力する項目は、プログラムの単純化のため、例外なく1つに限定している。
計算式の詳細は後述の「式の構成要素」を参照のこと。
``mcal`` で記述する式を構成する要素は、定数、項目値、演算子、関数の4つに大きく分類できる。
そして、それぞれの要素において、ユーザはデータ型を意識して利用する必要がある。
mcalが扱うデータはCSVテキストなので、値は全て文字列として与えらており、
それら文字列を ``mcal`` でどのようなデータ型として扱うかはユーザに委ねられているからである。
mcalが規定するデータ型は文字列型( :math:`str` ),数値型( :math:`num` )、日付型( :math:`date` )、時刻型( :math:`time` )、論理型( :math:`bool` )の5つである。
以下では、式を構成するそれぞれの要素で、5つのデータ型をどのように扱うかを示す。


.. csv-table:: \caption{定数の書式一覧}
  :header-rows: 1
  :name: None

  データ型,書式,内容,例
  数値( :math:`num` )   , 整数、実数の文字列表記, 内部的には全て倍精度実数を利用           ,  ``20, 0.55, 1.5*e10``
  文字列( :math:`str` ) , "文字列"         , ダブルクオーテーションで括った文字列          ,  ``"abc" "日本語"``
  日付( :math:`date` )  , 0dyyyymmdd       , 先頭に"0d"を付けた年月日固定長                ,  ``0d20080923``
  時刻( :math:`time` )  , 0tyyyymmddHHMMSS , 先頭に"0t"を付けた年月日時分秒固定長          ,  ``0t20080923121115``
  , 0tHHMMSS         , 先頭に"0t"を付けた時分秒固定長                ,  ``0t121115``
  ,                  , (内部的に本日の日付が補完される)              ,
  論理( :math:`bool` )  , 0b1, 0b0         , 先頭に"0b"を付けた"1"(true)もしくは"0"(false) ,  ``0b1, 0b0``


CSVデータ上の項目名を指定するには :numref:`mcal_fld` に示される通り、
CSVデータをどのデータ型として扱うかによって異なってくる。
CSVデータは全て文字列データであるために、それらをどのような型のデータとして扱うかはユーザの判断に任されている。


.. csv-table:: 項目値の書式一覧
  :header-rows: 1
  :name: mcal_fld

  データ型,書式,CSVデータ内容,例
  数値( :math:`num` )   , \ :math:`\{項目名\}  , 整数、実数(指数表現含む) の文字列表記            ,  ``` {amount}, ${株価}``
  文字列( :math:`str` ) , \ :math:`s\{項目名\} , 文字列                                           ,  ``` s{gender}, $s{性別}``
  日付( :math:`date` )  , \ :math:`d\{項目名\} , 年月日固定長(yyyymmdd)                           ,  ``` d{date}, $d{発注日}``
  時刻( :math:`time` )  , \ :math:`t\{項目名\} , 年月日時分秒の固定長(yyyymmddHHMMSS)             ,  ``` d{time}, $d{出発時刻}``
  ,               , 時分秒(HHMMSS)の固定長                           ,
  ,               , (内部的に本日の日付が補完される)                 ,
  論理( :math:`bool` )  , \ :math:`b\{項目名\} , 項目値の一文字目が"1"の時にtrue、"0"の時にfalse、,  ``` b{condition}, $b{条件}``
  ,               , その他の場合にはNULLと解釈される。               ,


項目名にはワイルドカードを指定することができる。
例えばsum関数は複数の数値項目の合計を計算する関数であるが、
ワイルドカードを指定することで、多数の項目を一つのワイルドカードで指定することも可能となる。
例えば、入力データとして ``A1,A2,A3`` の3つの数値項目名があったとすると、
``sum(${A*})`` とすれば、 ``A1,A2,A3`` の合計値を計算してくれる。
もちろん ``sum( :math:`{A*},` {B*})`` のように複数のワイルドカードを指定することも可能である。
項目値の指定に ``$`` の代わりに ``#`` を指定すると、前行の項目値となる。
ただし、先頭行は前行がないのでNULLとなる。
各データ型における指定方法を :numref:`mcal_prev` に示す。


.. csv-table:: 前行の項目値の書式一覧
  :header-rows: 1
  :name: mcal_prev

  データ型,書式,例
  数値( :math:`num` )   , \#\{項目名\}  ,  ``#{amount}, #{株価}``
  文字列( :math:`str` ) , \#s\{項目名\} ,  ``#s{gender}, #s{性別}``
  日付( :math:`date` )  , \#d\{項目名\} ,  ``#d{date}, #d{発注日}``
  時刻( :math:`time` )  , \#t\{項目名\} ,  ``#d{time}, #d{出発時刻}``
  論理( :math:`bool` )  , \#b\{項目名\} ,  ``#b{condition}, #b{条件}``


前行項目の指定において項目名を省略すると前行の計算結果項目の値となる。
各データ型における指定方法を :numref:`mcal_prev_rsl` に示す。
if関数とtop()関数とを組み合わせる事で、累計計算などが可能となる。
以下に、金額項目の累計計算例を示す。
`` :math:` mcal c='if(top(),` {金額},${金額}+#{})' a=累計金額``


.. csv-table:: 前行の結果項目値の書式一覧
  :header-rows: 1
  :name: mcal_prev_rsl

  データ型,書式,例
  数値( :math:`num` )   , \#\{\}  ,  ``#{}``
  文字列( :math:`str` ) , \#s\{\} ,  ``#s{}``
  日付( :math:`date` )  , \#d\{\} ,  ``#d{}``
  時刻( :math:`time` )  , \#t\{\} ,  ``#d{}``
  論理( :math:`bool` )  , \#b\{\} ,  ``#b{}``


``+`` や ``=True`` などの算術演算子は数値型だけでなく、文字列型や日付型のデータに対しても定義されている。
それらの一覧を :numref:`mcal_ope` に示す。


.. csv-table:: 算術演算子一覧
  :header-rows: 1
  :name: mcal_ope

  演算子,書式,内容,例
  加算(+) ,  :math:`num_1+num_2`  , 数値の足し算    ,  ``1.5+2.3 (3.8)``
  ,  :math:`str_1+str_2`  , 文字列の結合    ,  ``"150"+"円" ("150円")``
  ,  :math:`date+num`     ,  :math:`num` 日後の日付 ,  ``0d20121130+2 (0d20121202)``
  ,  :math:`time+num`     ,  :math:`num` 秒後の時刻 ,  ``0t095959+2 (0t100001)``
  減算(-) ,  :math:`num_1-num_2`    , 数値の引き算       ,  ``1.5-2.3 (-1.8)``
  ,  :math:`str_1-str_2`    , 部分文字列の削除   ,  ``"aababa"-"a"``  ( ``"bb"`` )
  ,                 , (貪欲マッチによる) ,  ``"aababa"-"aba"``  ( ``"aba"`` )
  ,  :math:`date-num`       ,  :math:`num` 日前の日付    ,  ``0d20121202-2 (0d20121130)``
  ,  :math:`time-num`       ,  :math:`num` 秒前の時刻    ,  ``0t100001-2 (0t095959)``
  ,  :math:`date_1-date_2`  , 日付差             ,  ``0d20121202-0d20121130 (2)``
  ,  :math:`time_1-time_2`  , 時刻差             ,  ``0t095959-0t100001 (-2)``
  乗算(*) ,  :math:`num_1*num_2`  , 掛け算 ,  ``10*2 (20)``
  除算(/) ,  :math:`num_1/num_2`  , 割り算 ,  ``10/2 (5)``
  剰余(\%) ,  :math:`num_1\%num_2`  , 剰余 ,  ``10%3 (1)``
  累乗(\^{}) ,  :math:`num_1` \^{} :math:`num_2`  , 累乗 ,  ``10^3 (1000)``


比較演算は同一のデータ型の値同士でのみ適用可能である。
全てのデータ型に共通した書式であり、以下では数値型についてのみ(例では文字型につても) :numref:`mcal_ope_comp` に示す。
文字型、日付型、時刻型においても同様に利用できる。


.. csv-table:: 比較演算子一覧
  :header-rows: 1
  :name: mcal_ope_comp

  比較内容,書式,例
  等しい     ,  :math:`num_1==num_2`  ,  ``1.5==1.5(0b1), "abc"=="abcd" (0b0)``
  等しくない ,  :math:`num_1!=num_2`  ,  ``1.5!=1.5(0b0), "abc"=="abcd" (0b1)``
  より大きい ,  :math:`num_1>num_2`   ,  ``10>5(0b1), "abc">"abcd" (0b0)``
  より小さい ,  :math:`num_1<num_2`   ,  ``10<5(0b0), "abc"<"abcd" (0b1)``
  以上       ,  :math:`num_1>=num_2`  ,  ``10>=10(0b1), "a">"" (0b1) ``
  以下       ,  :math:`num_1<=num_2`  ,  ``8<=9(0b1), "a"<="a" (0b1)``


3つの論理演算子(論理積、論理和、排他的論理和)が利用でき、それぞれの書式を :numref:`mcal_bool` に示す。
また、それぞれの演算における真偽(1:真,0:偽)の組み合せとその結果を :numref:`mcal_and` , :numref:`mcal_or` , :numref:`mcal_xor` に示す。


.. csv-table:: 論理演算子一覧
  :header-rows: 1
  :name: mcal_bool

  内容,書式,例
  論理積       ,  :math:`bool_1 \,\, bool_2`  ,  ``"abc"=="abc" ,, "xyz"=="abc" (0b0)``
  論理和       ,  :math:`bool_1 ||   bool_2`  , erb/"abc"=="abc" || "xyz"=="abc" (0b1)/
  排他的論理和 ,  :math:`bool_1`  \^{}\^{}  :math:`bool_2`  ,  ``"abc"=="abc" ^^ "xyz"=="abc" (0b1)``




.. csv-table:: 論理積
  :header-rows: 1
  :name: mcal_and

   :math:`bool_1`  ,  :math:`bool_2`  , 結果
  1  , 1  , 1
  1  , 0  , 0
  0  , 1  , 0
  0  , 0  , 0
  null , 1  , null
  null , 0  , 0
  null , null , null




.. csv-table:: 論理和
  :header-rows: 1
  :name: mcal_or

   :math:`bool_1`  ,  :math:`bool_2`  , 結果
  1  , 1  , 1
  1  , 0  , 1
  0  , 1  , 1
  0  , 0  , 0
  null , 1  , 1
  null , 0  , null
  null , null , null




.. csv-table:: 排他的論理和
  :header-rows: 1
  :name: mcal_xor

   :math:`bool_1`  ,  :math:`bool_2`  , 結果
  1  , 1  , 0
  1  , 0  , 1
  0  , 1  , 1
  0  , 0  , 0
  null , 1  , null
  null , 0  , null
  null , null , null


演算子(後述)の優先順位は :numref:`mcal_pri_ope` に示すとおりである。
同一の演算子間の優先順位は出現順序による。
優先順位を変更するときは括弧を利用すれば良い。


.. csv-table:: 演算子の優先順位
  :header-rows: 1
  :name: mcal_pri_ope

  優先順位,演算子
  1 ,  ``*,/,%,^``
  2 ,  ``+,-``
  3 ,  ``>,<,>=,<=``
  4 ,  ``== ,!=``
  5 ,  ``,,``
  6 , erb/||,^^/


以下では、数値関連(ef{tbl_mcal_func_num})、三角関数関連( :numref:`mcal_sankaku` )、
文字列関連( :numref:`mcal_char` )、正規表現関連( :numref:`mcal_regex` )、
日付時間関連( :numref:`mcal_date` )、論理関数( :numref:`mcal_logical` )、
行/項目情報関連( :numref:`mcal_line` )、NULL値関連( :numref:`mcal_null` )、
そして型変換関連( :numref:`mcal_cast` )の9つに分けて解説する。


.. csv-table:: 数値関連関数一覧
  :header-rows: 1
  :name: None

  節,関数名,機能,出力型
  合計, :math:`num` 
  平均, :math:`num` 
  平方和, :math:`num` 
  最小値, :math:`num` 
  最大値, :math:`num` 
  積, :math:`num` 
  階乗, :math:`num` 
  最大公約数, :math:`num` 
  最小公倍数, :math:`num` 
  平方根, :math:`num` 
  絶対値, :math:`num` 
  符号, :math:`num` 
  整数部, :math:`num` 
  小数部, :math:`num` 
  四捨五入, :math:`num` 
  切り捨て, :math:`num` 
  切り上げ, :math:`num` 
  累乗, :math:`num` 
  指数関数, :math:`num` 
  対数, :math:`num` 
  自然対数, :math:`num` 
  底が2の対数, :math:`num` 
  常用対数, :math:`num` 
  距離, :math:`num` 
  GPS距離, :math:`num` 
  三角形の面積, :math:`num` 
  一様乱数, :math:`num` 
  整数一様乱数, :math:`num` 
  正規乱数, :math:`num` 
  円周率, :math:`num` 
  ネイピア数, :math:`num` 
  書式付き出力, :math:`str` 




.. csv-table:: 三角関数関連関数一覧
  :header-rows: 1
  :name: mcal_sankaku

  節,関数名,機能,出力範囲
  コサインの逆関数, :math:`0\sim\pi` 
  サインの逆関数, :math:`-\pi\sim\pi` 
  タンジェントの逆関数, :math:`-\pi\sim\pi` 
  座標( :math:`num_1,num_2` )の角度, :math:`-\pi\sim\pi` 
  コサイン, :math:`-1.0\sim 1.0` 
  サイン, :math:`-1.0\sim 1.0` 
  タンジェント, :math:`-\infty\sim\infty` 
  角度, :math:`-\pi\sim\pi` 
  度数を入力したときのラジアンを出力, :math:`-\pi\sim\pi` 
  双曲線余弦, :math:`0\sim\infty` 
  双曲線正弦, :math:`-\infty\sim\infty` 
  双曲線逆正接, :math:`-1.0\sim 1.0` 




.. csv-table:: 文字列関連関数一覧
  :header-rows: 1
  :name: mcal_char

  節,関数名,機能,出力型
  文字列併合, :math:`str` 
  文字列長, :math:`num` 
  固定長変換, :math:`str` 
  末尾切り出し, :math:`str` 
  先頭切り出し, :math:`str` 
  部分文字列切り出し , :math:`str` 
  小文字大文字変更, :math:`str` 
  大文字小文字変更, :math:`str` 
  先頭文字大文字変換, :math:`str` 
  検索, :math:`bool` 
  空白類文字検索, :math:`bool` 




.. csv-table:: 正規表現関連関数一覧
  :header-rows: 1
  :name: mcal_regex

  節,関数名,機能,出力型
  全体マッチ, :math:`bool` 
  マッチ, :math:`bool` 
  マッチ文字列の置換, :math:`str` 
  マッチ文字数, :math:`num` 
  開始位置, :math:`num` 
  マッチ文字列, :math:`str` 
  マッチ文字列のプレフィックス, :math:`str` 
  マッチ文字列のサフィックス, :math:`str` 




.. csv-table:: 日付時間関連関数一覧
  :header-rows: 1
  :name: mcal_date

  節,関数名,機能,出力型
  本日の日付, :math:`date` 
  現在時刻, :math:`time` 
  経過秒数, :math:`num` 
  閏年判定, :math:`bool` 
  西暦年, :math:`num` 
  月, :math:`num` 
  日, :math:`num` 
  週番号, :math:`num` 
  曜日, :math:`num` 
  時分秒, :math:`str` 
  年月日, :math:`str` 
  時, :math:`num` 
  分, :math:`num` 
  秒, :math:`num` 
  年令, :math:`num` 
  期間, :math:`num` 
  UNIX時変換, :math:`num` (UNIX時刻)
  ユリウス通日変換, :math:`num` (ユリウス通日)




.. csv-table:: 論理関連関数一覧
  :header-rows: 1
  :name: mcal_logical

  節,関数名,機能,出力型
  ef{sect:and}, and( :math:`bool_1,bool_2,\cdots)` , 論理積 , :math:`bool` 
  ef{sect:or}, or( :math:`bool_1,bool_2,\cdots)`   , 論理和 , :math:`bool` 
  ef{sect:not}, not( :math:`bool)`                 , 否定   , :math:`bool` 
  ef{sect:if}, if( :math:`bool,num_1,num_2` )      ,条件選択,  :math:`num` 
  ef{sect:if}, if( :math:`bool,str_1,str_2` )      ,        ,  :math:`str` 
  ef{sect:if}, if( :math:`bool,date_1,date_2)`     ,        ,  :math:`date` 
  ef{sect:if}, if( :math:`bool,time_1,time_2)`     ,        ,  :math:`time` 




.. csv-table:: 行/項目情報関連関数一覧
  :header-rows: 1
  :name: mcal_line

  節,関数名,機能,出力型
  ef{sect:line}   , line()   ,現在処理中の行番号を返す, :math:`num` 
  ef{sect:top}    , top()    ,先頭行, :math:`bool` 
  ef{sect:bottom} , bottom() ,終端行, :math:`bool` 
  ef{sect:fldsize}, fldsize(),項目数, :math:`num` 
  ef{sect:argsize}, argsize( :math:`str_1,str_2,\cdots` ),引数の数, :math:`num` 




.. csv-table:: NULL値関連関数一覧
  :header-rows: 1
  :name: mcal_null

  節,関数名,機能,出力型
  ef{sect:null}, nulln(),NULL値,  :math:`num` 
  ef{sect:null}, nulls(),      ,  :math:`str` 
  ef{sect:null}, nulld(),      ,  :math:`date` 
  ef{sect:null}, nullt(),      ,  :math:`time` 
  ef{sect:null}, nullb(),      ,  :math:`bool` 
  ef{sect:isnull}, isnull( :math:`num` ),NULL値判定,  :math:`bool` 
  ef{sect:isnull}, isnull( :math:`str` ),          ,  :math:`bool` 
  ef{sect:isnull}, isnull( :math:`date` ),         ,  :math:`bool` 
  ef{sect:isnull}, isnull( :math:`time` ),         ,  :math:`bool` 
  ef{sect:isnull}, isnull( :math:`bool` ),         ,  :math:`bool` 
  ef{sect:countnull}, countnull( :math:`num_1,num_2,\cdots` ), NULL値の数 ,  :math:`num` 
  ef{sect:countnull}, countnull( :math:`str_1,str_2,\cdots` ), ,  :math:`num` 
  ef{sect:countnull}, countnull( :math:`date_1,date_2,\cdots` ), ,  :math:`num` 
  ef{sect:countnull}, countnull( :math:`time_1,time_2,\cdots` ), ,  :math:`num` 
  ef{sect:countnull}, countnull( :math:`bool_1,bool_2,\cdots` ), ,  :math:`num` 




.. csv-table:: 型変換関連関数一覧
  :header-rows: 1
  :name: mcal_cast

  ef{sect:cast} ,  :math:`num`        ,  :math:`str`        ,  :math:`date`      ,  :math:`time`      ,  :math:`bool` 
   :math:`num`   ,             , n2s( :math:`num` )  ,            ,            , n2b( :math:`num` )
   :math:`str`   , s2n( :math:`str` )  ,             , s2d( :math:`str` ) , s2t( :math:`str` ) , s2b( :math:`str` )
   :math:`date`  ,             , d2s( :math:`date` ) ,            , d2t( :math:`date` ),
   :math:`time`  ,             , t2s( :math:`time` ) , t2d( :math:`time` ),            ,
   :math:`bool`  , b2n( :math:`bool` ) , b2s( :math:`bool` ) ,            ,            ,


mcalでは日付時刻について2つの型を用意している。
一つは日付型で他方は時刻型である。
時刻型は時刻だけでなく日付とセットで表現する。
内部的にはグレゴリオ暦に基づいたboost C++ライブラリのdate\_timeライブラリを利用しており、
日付型にはboost::gregorian::dateクラスを、
時刻型にはboost::posix\_time::ptimeクラスを使っている。
詳細は\href{http://www.boost.org/}{boost.org}のドキュメントを参照されたい。
dateクラスは32ビット整数で管理されており、1400年1月1日から9999年12月31日の範囲をサポートしている。
日付の演算は全てグレゴリオ暦に基づいたものとなっている。
不正な日付(例えば、2013/2/29や1399/12/31)が与えられたときはNULL値が出力される。
一方でptimeクラスは、64ビットで管理されており、ミリ秒まで扱える時刻システムであるが、
mcalコマンドにおいてはミリ秒を扱うインターフェースは備えていない。
またptimeクラスはdateクラスも内部で参照しており、日付をまたいだ時間計算を可能としている。
不正な時刻(例えば、18:62:11)が与えられたときはNULL値が出力される。
MCMDはCSVテキストを扱うので、日付/時刻は、データ上は文字列で表現される必要がある。
それらの文字列を日付型および時刻型に内部で変換して各種演算を行い、最終結果を再度文字列に戻して出力している。
文字列のフォーマットは、日付型は8桁固定長文字列(例えば、"20130911")、
時刻型は14桁固定長文字列(例えば、"20130911110528")、もしくは6桁固定長文字列(例えば、"110528")を標準としている。
日付型と時刻型と各種関数の関係を図ef{fig:mcal_datetime}に示す。
egin{figure}[hbt]
egin{center}
\includegraphics[scale=.50]{figure/datetime/datetime.eps}
\caption{2013年9月6日10時43分27秒を例に、date型とtime型と各種関数の関係を図示している。
実線で囲われたボックスは実データを表し、アンダーラインを付したものは関数等を表している。\label{fig:mcal_datetime}}
\end{center}
\end{figure}
またユーザは日付/時刻として固定長文字列を標準とせずに、
ユリウス通日(紀元前4713年1月1日正午からの日数)やUNIX時刻(1970年1月1日00時00分00秒(GMT)からの
経過秒数)などの整数を標準の日時の表記として利用してもよいであろう。
ユリウス通日やUNIX時刻と、日付型/時刻型との変換関数も備えており、十分に運用可能である。
ただし、mcalが提供する日付/時刻関数を使う限りにおいては、内部的にはグレゴリオ暦によって管理されており、
その範囲は、1400年1月1日から9999年12月31日に限定されることに注意する。
またUNIX時刻は32ビット整数で管理されているため、2038年1月19日3時14分7秒を超えると正しく計算できないことに注意する。
ただユリウス通日やUNIX時刻を利用する欠点は、その数字を見ただけでは実際にいつの日付時刻なのか理解出来ない点にあろう。

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
   * - | **a=str**
       | 必須
     - | 新たに計算結果の出力として追加される項目の名前を指定する。
   * - | **c=str**
       | 必須
     - | 用意された関数を組み合わせて計算する式を指定する。


共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullout=<common_param_assert_nullout>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`tmppath=<common_param_tmppath>`
, :ref:`precision=<common_param_precision>`


利用例
''''''''''''

