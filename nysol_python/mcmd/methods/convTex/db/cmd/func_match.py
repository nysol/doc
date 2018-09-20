# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='match'
db['title']='検索'
db['forms']=[
  ["match","検索文字列,str_1,str_2,...","m,m,m,r",""],
  ["matcha","検索文字列,str_1,str_2,...","m,m,m,r",""],
  ["matchs","検索文字列,str_1,str_2,...","m,m,m,r",""],
  ["matchas","検索文字列,str_1,str_2,...","m,m,m,r",""]
]
############################### DOCUMENT
db['doc']='''
:math:`str_1,str_2,\cdots` から指定した検索文字列を検索し、
マッチすれば真をマッチしなければ偽を返す。
OR検索かAND検索か、そして完全一致か部分一致かにより、
表\ref{tbl:func_match_cond}に示すとおり異なる関数名を指定する。
\begin{table}[htbp]
\begin{center}
\caption{入力データ\label{tbl:func_match_cond}}
{\small
\begin{tabular}{l|ll}
\hline
& OR検索 & AND検索 \\
\hline
完全一致 & match  & matcha  \\
部分一致 & matchs & matchas \\
\hline
\end{tabular}
}
\end{center}
\end{table}
``match`` 関数は、指定した検索文字列が、 :math:`str_1,str_2,\cdots` のいずれかに完全一致すれば真を返す。
``matcha`` 関数は、指定した検索文字列が、 :math:`str_1,str_2,\cdots` の全てに完全一致すれば真を返す。
``matchs`` 関数は、指定した検索文字列が、 :math:`str_1,str_2,\cdots` のいずれかに部分一致すれば真を返す。
``matchas`` 関数は、指定した検索文字列が、 :math:`str_1,str_2,\cdots` の全てに部分一致すれば真を返す。
NULL値を含めたOR/AND論理演算の真偽値表は表\ref{tbl:mcal_and}を参照のこと。
'''

