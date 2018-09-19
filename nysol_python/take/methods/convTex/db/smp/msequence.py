# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mitemset'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
tid,time,item
T1,0,C
T1,2,B
T1,3,A
T1,7,C
T2,2,D
T2,3,A
T2,5,B
T2,6,C
T3,1,C
T3,2,B
T3,4,D
T3,8,E
T4,2,A
T4,5,C
T4,6,B
T5,0,B
T5,1,A
T5,2,D
T5,3,D
T5,7,C
T5,9,C
T6,0,A
T6,5,B
T6,6,D
T6,8,B
T6,9,C
'''
db['idatas'].append(data)


data={}
data['name']='dat2.csv'
data['text']='''
tid,time,item,class
T1,0,C,cls1
T1,2,B,cls1
T1,3,A,cls1
T1,7,C,cls1
T2,2,D,cls1
T2,3,A,cls1
T2,5,B,cls1
T2,6,C,cls1
T3,1,C,cls1
T3,2,B,cls1
T3,4,D,cls1
T3,8,E,cls1
T4,2,A,cls1
T4,5,C,cls1
T4,6,B,cls1
T5,0,B,cls2
T5,1,A,cls2
T5,2,D,cls2
T5,3,D,cls2
T5,7,C,cls2
T5,9,C,cls2
T6,0,A,cls2
T6,5,B,cls2
T6,6,D,cls2
T6,8,B,cls2
T6,9,C,cls2
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
出現頻度が3以上の長さが2の系列パターンのみを列挙する。
'''
script['sh_code']='''
msequence.rb  O=result1 i=dat1.csv S=2
msequence.rb  O=result2 i=dat1.csv S=3 l=2 u=2
'''
script['py_code']='''
import nysol.take as nt
nt.msequence(O="result", i="dat1.csv", S=3, l=2, u=2).run()
'''
script['odatas']='result/patterns.csv,result/tid_pats.csv'
db['scripts'].append(script)

script={}
script['title']='パターン長の制限'
script['comment']='''
2件以上で出現する系列パターン。
入力データの項目名は、全てデフォルトのものと同じなので省略していることに注意する。
'''
script['sh_code']='''
msequence.rb  O=result1 i=dat1.csv S=2
'''
script['py_code']='''
import nysol.take as nt
nt.msequence(O="result", i="dat1.csv", S=2).run()
'''
script['odatas']='result/patterns.csv,result/tid_pats.csv'
db['scripts'].append(script)

script={}
script['title']='gap長とwindowサイズの指定'
script['comment']='''
出現頻度が2以上、長さが2以上の系列パターンのうち、gap長が2、windowサイズが4のパターンを列挙する。
'''
script['sh_code']='''
msequence.rb  O=result3 i=dat1.csv S=2 l=2 gap=2 win=4
'''
script['py_code']='''
import nysol.take as nt
nt.msequence(O="result", i="dat1.csv", S=2, l=2, gap=2, win=4).run()
'''
script['odatas']='result/patterns.csv,result/tid_pats.csv'
db['scripts'].append(script)

script={}
script['title']='paddingにより時間を考慮する'
script['comment']='''
前の例と同じ条件で、 ``padding`` オプションを指定することで、
時間を考慮したgap長とwindowサイズ制約により系列パターンを列挙する。
'''
script['sh_code']='''
msequence.rb  O=result4 i=dat1.csv S=2 l=2 gap=2 win=4 -padding
'''
script['py_code']='''
import nysol.take as nt
nt.msequence(O="result", i="dat1.csv", S=2, l=2, gap=2, win=4, padding=True).run()
'''
script['odatas']='result/patterns.csv,result/tid_pats.csv'
db['scripts'].append(script)

script={}
script['title']='顕在系列パターンの列挙'
script['comment']='''
最初の例と同じ条件で、クラス項目を指定することで顕在パターンを列挙する。
'''
script['sh_code']='''
msequence.rb  O=result5 i=dat2.csv S=2 class=class -padding
'''
script['py_code']='''
import nysol.take as nt
nt.msequence(O="result", i="dat2.csv", S=2, cls="class", padding=True).run()
'''
script['odatas']='result/patterns.csv,result/tid_pats.csv'
db['scripts'].append(script)


