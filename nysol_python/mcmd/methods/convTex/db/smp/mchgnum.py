# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mchgnum'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
customer,quantity
A,5
B,10
C,15
D,2
E,50
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``quantity`` 項目の値が最小以上10未満を ``low`` 、
10以上20未満を ``middle`` 、20以上最大未満を ``high`` という文字列に置換する。
'''
script['sh_code']='''
mchgnum f=quantity R=MIN,10,20,MAX v=low,middle,high i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mchgnum(f="quantity", R="MIN,10,20,MAX", v="low,middle,high", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='パラメータ範囲にイコールをつける例'
script['comment']='''
``quantity`` 項目の値が最小より多く10以下を ``low`` 、
10より多く20以下を ``middle`` 、20より多く最大以下を ``high`` という文字列に置換する。
'''
script['sh_code']='''
mchgnum f=quantity R=MIN,10,20,MAX v=low,middle,high -r i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mchgnum(f="quantity", R="MIN,10,20,MAX", v="low,middle,high", r=True, i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='数値範囲リストに合致しない値を置換'
script['comment']='''
``quantity`` 項目の値が10以上20未満を ``low`` 、
20以上30未満を ``middle`` 、30以上最大未満を ``high`` 、
数量が10より小さい値は ``out of range`` という文字列に置換する。
'''
script['sh_code']='''
mchgnum f=quantity R=10,20,30,MAX v=low,middle,high O="out of range" i=dat1.csv o=rsl3.csv
'''
script['py_code']='''
nm.mchgnum(f="quantity", R="10,20,30,MAX", v="low,middle,high", O="out of range", i="dat1.csv", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

script={}
script['title']='新たな項目の追加'
script['comment']='''
``quantity`` 項目の値が最小以上10未満を ``low`` 、
10以上20未満を ``middle`` 、20以上最大未満を ``high`` という文字列に置換し
``evaluate`` という項目名で出力する。
'''
script['sh_code']='''
mchgnum f=quantity:evaluate R=MIN,10,20,MAX v=low,middle,high -A i=dat1.csv o=rsl4.csv
'''
script['py_code']='''
nm.mchgnum(f="quantity:evaluate", R="MIN,10,20,MAX", v="low,middle,high", A=True, i="dat1.csv", o="rsl4.csv").run()
'''
script['odatas']='rsl4.csv'
db['scripts'].append(script)

script={}
script['title']='範囲外を項目の値として出力'
script['comment']='''
``quantity`` 項目の値が10以上20未満を ``low`` 、20以上30未満を ``middle`` 、
30以上最大未満を ``high`` 、数量が10より小さい値は置換しないでそのまま出力する。
'''
script['sh_code']='''
mchgnum f=quantity R=10,20,30,MAX v=low,middle,high -F i=dat1.csv o=rsl5.csv
'''
script['py_code']='''
nm.mchgnum(f="quantity", R="10,20,30,MAX", v="low,middle,high", F=True, i="dat1.csv", o="rsl5.csv").run()
'''
script['odatas']='rsl5.csv'
db['scripts'].append(script)

