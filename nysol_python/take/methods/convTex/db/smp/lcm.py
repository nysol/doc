# ================================================
# コマンドマニュアル自動作成用サンプルコードデータ
# ================================================
db={}
db['name']='mitemset'

############################### IDATA
db['idatas']=[]

data={}
data['name']='dat1.tra'
data['text']='''
2 4
3 4 5
0 1 3 5
1 3 5
0 1 3 4
0 1 3 4 5
'''
db['idatas'].append(data)

data={}
data['name']='weight.txt'
data['text']='''
-1
1
-1
1
1
-1
'''
db['idatas'].append(data)

############################### SCRIPTS
db['scripts']=[]

script={}
script['title']='基本例'
script['comment']='''
頻出アイテム集合( ``F`` )の列挙。
``type=`` に ``f`` を指定すると出現件数を出力する。
``type=`` に ``_`` を含めることでメッセージを表示しなくなる。
出力結果の各行が頻出アイテム集合を表しており、末尾の括弧内の数字が出現件数を表している。
一行目には空のアイテム集合が出力されている。
'''
script['sh_code']='''
'''
script['py_code']='''
from nysol.take.extcore import lcm
lcm(type="Ff_",sup=3,i="dat1.tra",o="result.txt")
'''
script['odatas']='result.txt:0'
db['scripts'].append(script)

script={}
script['title']='飽和集合の列挙'
script['comment']='''
``type=`` に ``C`` を指定することで、頻出飽和アイテム集合を列挙する。
'''
script['sh_code']='''
'''
script['py_code']='''
from nysol.take.extcore import lcm
lcm(type="Cf_",sup=3,i="dat1.tra",o="result.txt")
'''
script['odatas']='result.txt:0'
db['scripts'].append(script)

script={}
script['title']='極大集合の列挙'
script['comment']='''
``type=`` に ``M`` を指定することで、頻出極大アイテム集合を列挙する。
'''
script['sh_code']='''
'''
script['py_code']='''
from nysol.take.extcore import lcm
lcm(type="Mf_",sup=3,i="dat1.tra",o="result.txt")
'''
script['odatas']='result.txt:0'
db['scripts'].append(script)

script={}
script['title']='アイテム集合サイズを制限'
script['comment']='''
``l=3`` でアイテム集合のサイズを3以上に限定する。
'''
script['sh_code']='''
'''
script['py_code']='''
from nysol.take.extcore import lcm
lcm(type="Mf_",sup=3,l=3,i="dat1.tra",o="result.txt")
'''
script['odatas']='result.txt:0'
db['scripts'].append(script)

script={}
script['title']='出現集合の出力'
script['comment']='''
``type=`` に ``I`` を加えることで、アイテム集合の下に出現集合が出力される。
アイテム集合 ``{5,1,3}`` はトランザクションデータ( ``dat1.tra`` )の2,3,5行目に出現している(先頭行は0行目と数える}。
'''
script['sh_code']='''
'''
script['py_code']='''
from nysol.take.extcore import lcm
lcm(type="FfI_",sup=3,l=3,i="dat1.tra",o="result.txt")
'''
script['odatas']='result.txt:0'
db['scripts'].append(script)

script={}
script['title']='データベースの転置'
script['comment']='''
``type=`` に ``t`` を加えることでトランザクションデータベースを転置してから実行する。
トランザクション集合 ``{4,2,5}`` はアイテム ``{0,1,3}`` に出現する(先頭行は0行目と数える}。
'''
script['sh_code']='''
'''
script['py_code']='''
from nysol.take.extcore import lcm
lcm(type="FftI_",sup=3,l=3,i="dat1.tra",o="result.txt")
'''
script['odatas']='result.txt:0'
db['scripts'].append(script)

script={}
script['title']='上位k番目の出現件数'
script['comment']='''
``K=4`` で頻出上位4番目の出現件数を出力する。
「基本例」での結果から、頻出上位4番目のルールは ``1 3 (4)`` であり、その出現件数 ``4`` が出力されている。
'''
script['sh_code']='''
'''
script['py_code']='''
from nysol.take.extcore import lcm
lcm(type="Ff",K=4,sup=1,i="dat1.tra",so="topk.txt")
'''
script['odatas']='topk.txt'
db['scripts'].append(script)

script={}
script['title']='トランザクション重みの利用'
script['comment']='''
``w=`` を指定すると、指定されたトランザクションの重みで件数をカウントする。
``type=`` に ``A`` を加えることで、マイナス重みとプラス重みの件数情報が表示される。
アイテム ``3`` は、1,2,3,4,5行目に含まれ、その重み合計は1(=1-1+1+1-1)となる
(プラス重み件数3件、マイナス重み件数2件、プラス率は3/5=0.6)。
同様にアイテム集合{4,3}は1,4,5行目に含まれ、その重み合計は1(=1+1-1)となる
(プラス重み件数2件、マイナス重み件数1件、プラス率は2/3=0.6666)。
'''
script['sh_code']='''
'''
script['py_code']='''
from nysol.take.extcore import lcm
lcm(type="FfA_",sup=1,w="weight.txt",i="dat1.tra",o="result.txt")
'''
script['odatas']='result.txt:0'
db['scripts'].append(script)


