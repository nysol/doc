# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mkeybreak'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.csv'
data['text']='''
id,k1,k2,val
1,A,a,1
2,A,b,2
3,A,b,3
4,B,a,4
5,B,a,5
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
``k1`` 項目で並べ替えた後、 ``k1`` キー項目の先頭( ``top`` 項目)と終端( ``bottom`` 項目)に印( ``1`` )をつける。
'''
script['sh_code']='''
mkeybreak k=k1 i=dat1.csv o=rsl1.csv
'''
script['py_code']='''
nm.mkeybreak(k="k1", i="dat1.csv", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='2項目キー'
script['comment']='''
``k1`` ・ ``k2`` 項目で並べ替えた後、 ``k1`` キー項目の先頭( ``top`` 項目)と終端( ``bottom`` 項目)に印( ``1`` )をつける。
'''
script['sh_code']='''
mkeybreak s=k1,k2 k=k1 i=dat1.csv o=rsl2.csv
'''
script['py_code']='''
nm.mkeybreak(s="k1,k2", k="k1", i="dat1.csv", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

