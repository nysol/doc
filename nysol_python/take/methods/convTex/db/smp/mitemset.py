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
tid,item
T1,C
T1,E
T2,D
T2,E
T2,F
T3,A
T3,B
T3,D
T3,F
T4,B
T4,D
T4,F
T5,A
T5,B
T5,D
T5,E
T6,A
T6,B
T6,D
T6,E
T6,F
'''
db['idatas'].append(data)


data={}
data['name']='dat2.csv'
data['text']='''
tid,item,class
T1,C,cls1
T1,E,cls1
T2,D,cls1
T2,E,cls1
T2,F,cls1
T3,A,cls1
T3,B,cls1
T3,D,cls1
T3,F,cls1
T4,B,cls1
T4,D,cls1
T4,F,cls1
T5,A,cls2
T5,B,cls2
T5,D,cls2
T5,E,cls2
T6,A,cls2
T6,B,cls2
T6,D,cls2
T6,E,cls2
T6,F,cls2
'''
db['idatas'].append(data)

data={}
data['name']='taxo.csv'
data['text']='''
item,taxonomy
A,X
B,X
C,Y
D,Z
E,Z
F,Z
'''
db['idatas'].append(data)


############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
3件以上で出現する頻出アイテム集合を列挙する。
'''
script['sh_code']='''
mitemset.rb  S=3 tid=tid item=item i=dat1.csv O=result
'''
script['py_code']='''
import nysol.take as nt
nt.mitemset(S=3,tid="tid",item="item",i="dat1.csv",O="result").run()
'''
script['odatas']='result/patterns.csv,result/tid_pats.csv'
db['scripts'].append(script)

script={}
script['title']='アイテム集合のサイズに制限を加えた例'
script['comment']='''
出現頻度が3以上で、アイテム集合のサイズ3のパターンを列挙する。
'''
script['sh_code']='''
mitemset.rb S=3 l=3 u=3 tid=tid item=item i=dat1.csv O=result
'''
script['py_code']='''
import nysol.take as nt
nt.mitemset(S=3,l=3,u=3,tid="tid",item="item",i="dat1.csv",O="result").run()
'''
script['odatas']='result/patterns.csv'
db['scripts'].append(script)

script={}
script['title']='飽和集合の列挙例'
script['comment']='''
'''
script['sh_code']='''
mitemset.rb S=3 type=C tid=tid item=item i=dat1.csv O=result
'''
script['py_code']='''
import nysol.take as nt
nt.mitemset(S=3,type="C",tid="tid",item="item",i="dat1.csv",O="result").run()
'''
script['odatas']='result/patterns.csv'
db['scripts'].append(script)

script={}
script['title']='極大集合の列挙例'
script['comment']='''
'''
script['sh_code']='''
mitemset.rb S=3 type=M tid=tid item=item i=dat1.csv O=result4
'''
script['py_code']='''
import nysol.take as nt
nt.mitemset(S=3,type="M",tid="tid",item="item",i="dat1.csv",O="result").run()
'''
script['odatas']='result/patterns.csv'
db['scripts'].append(script)

script={}
script['title']='アイテムの階層分類を使った例'
script['comment']='''
'''
script['sh_code']='''
mitemset.rb S=4 tid=tid item=item i=dat1.csv x=taxo.csv taxo=taxonomy O=result
'''
script['py_code']='''
import nysol.take as nt
nt.mitemset(S=4,tid="tid",item="item",i="dat1.csv",x="taxo.csv",taxo="taxonomy",O="result").run()
'''
script['odatas']='result/patterns.csv'
db['scripts'].append(script)

script={}
script['title']='オリジナルアイテムを階層分類で置換する例'
script['comment']='''
'''
script['sh_code']='''
mitemset.rb S=4 tid=tid item=item i=dat1.csv x=taxo.csv taxo=taxonomy -replaceTaxo O=result6
'''
script['py_code']='''
import nysol.take as nt
nt.mitemset(S=4,tid="tid",item="item",i="dat1.csv",x="taxo.csv",taxo="taxonomy",replaceTaxo=True,O="result").run()
'''
script['odatas']='result/patterns.csv'
db['scripts'].append(script)

script={}
script['title']='顕在パターンの列挙例'
script['comment']='''
'''
script['sh_code']='''
mitemset.rb S=2 tid=tid item=item class=class i=dat2.csv p=0.6 O=result7
'''
script['py_code']='''
import nysol.take as nt
nt.mitemset(S=2,tid="tid",item="item",cls="class",i="dat2.csv",p=0.6,O="result").run()
'''
script['odatas']='result/patterns.csv'
db['scripts'].append(script)

