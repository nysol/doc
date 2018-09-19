# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mxml2csv'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.xml'
data['text']='''
<a att="aa">
<b att="bb1">
<c p="pp1" q="qq1"/>
<d>text1</d>
</b>
<b att="bb2">
<c q="qq2"></c>
<d>text2</d>
</b>
<b>
<c p="pp3"/>
<d>text3</d>
</b>
</a>
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
概要にて解説した例。
/a/bをキー要素として、5つのCSV項目を出力する。
'''
script['sh_code']='''
mxml2csv k=/a/b f=@att:b_att,c@p:c_p,c@p%f:c_p_f,d:d,/a:a i=dat1.xml  o=rsl1.csv
'''
script['py_code']='''
nm.mxml2csv(k="/a/b", f="@att:b_att,c@p:c_p,c@p%f:c_p_f,d:d,/a:a", i="dat1.xml", o="rsl1.csv").run()
'''
script['odatas']='rsl1.csv'
db['scripts'].append(script)

script={}
script['title']='絶対パス'
script['comment']='''
基本例と同じ要素を絶対パスで指定する例。
/a/bをキー要素として、5つのCSV項目を出力する。
'''
script['sh_code']='''
mxml2csv k=/a/b f=/a/b@att:b_att,/a/b/c@p:c_p,/a/b/c@p%f:c_p_f,/a/b/d:d,/a:a i=dat1.xml  o=rsl2.csv
'''
script['py_code']='''
nm.mxml2csv(k="/a/b", f="/a/b@att:b_att,/a/b/c@p:c_p,/a/b/c@p%f:c_p_f,/a/b/d:d,/a:a", i="dat1.xml", o="rsl2.csv").run()
'''
script['odatas']='rsl2.csv'
db['scripts'].append(script)

script={}
script['title']='キー要素の変更'
script['comment']='''
絶対パスの例でキー要素をaに変更した例。
aの終了タグは一つしかないので、一行だけ出力されている。
f=で指定した/a/b@attは、2回出現しているが、最後に出現した値が出力されている。
'''
script['sh_code']='''
mxml2csv k=/a f=/a/b@att:b_att,/a/b/c@p:c_p,/a/b/c@p%f:c_p_f,/a/b/d:d,/a:a i=dat1.xml o=rsl3.csv
'''
script['py_code']='''
nm.mxml2csv(k="/a", f="/a/b@att:b_att,/a/b/c@p:c_p,/a/b/c@p%f:c_p_f,/a/b/d:d,/a:a", i="dat1.xml", o="rsl3.csv").run()
'''
script['odatas']='rsl3.csv'
db['scripts'].append(script)

