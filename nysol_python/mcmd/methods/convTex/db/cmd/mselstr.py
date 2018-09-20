# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mselstr'
db['title']='文字列による行選択'
db['related']=[
  ["msel","より複雑な条件で行選択を行う。"],
  ["mcommon","選択対象となる文字列の数が多いときは、参照データを用意することで ``mcommon`` コマンドが使える。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` で指定した項目の値が、 ``v=`` で指定した文字列に一致すれば、その行を選択する。
典型例を :numref:`mselstr_input` 〜 :numref:`mselstr_out2` に示す。
:numref:`mselstr_out1` では ``key`` に関係なく ``val`` が ``"y"`` である行を選択する。
:numref:`mselstr_out2` では、 ``val`` が ``"x"`` の行を含んでいる同一キーの行全て、
すなわち ``key`` 項目が ``"a"`` である行全てを選択する。
すなわち ``key`` 項目が ``"b"`` の行はいずれも ``"x"`` を含んでいないので選択されない。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mselstr_input

  key,val
  a,x
  a,y
  b,y
  b,z




.. csv-table:: f=val v=y
  :header-rows: 1
  :name: mselstr_out1

  key,val
  a,y
  b,y




.. csv-table:: k=key f=val v=x
  :header-rows: 1
  :name: mselstr_out2

  key,val
  a,x
  a,y


また、以下に示すように多様な選択条件を指定することも可能である。
このコマンドで指定できない複雑な条件(例えば正規表現など)を設定するのであれば
:doc:`msel` コマンドを利用すればよい。

 *   ``v=`` に複数の文字列を指定すれば、いずれかの文字列にマッチすれば選択される。
 *   ``f=`` に複数項目を指定すれば、いずれかの項目の値がマッチすれば選択される。
 *  複数項目のマッチ条件をAND条件とすることも可能( ``F`` オプション)。
 *  完全一致だけでなく、先頭一致、末尾一致、部分一致の指定も可能( ``head`` , ``tail`` ``sub`` オプション)。
 *   ``k=`` を指定することでキー単位で選択することが可能。
 *  キー単位選択の場合、複数レコードのAND条件を指定可能( ``R`` オプション)。

いま同じキーのデータとして２項目２行からなるデータ( :numref:`mselstr_input2` )に対して、
``mselstr k=key f=fld1,fld2 v=s1,s2``
を実行した場合、
オプション ``R`` , ``F`` の指定の有無によるマッチ条件を :numref:`mselstr_cond` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mselstr_input2

  :math:` ``key`` ` , :math:` ``fld1`` ` , :math:` ``fld2`` `
  k, :math:`v_{a1}` , :math:`v_{a2}`
  k, :math:`v_{b1}` , :math:`v_{b2}`




.. csv-table::  :numref:`mselstr_input2` で示されるデータに、mselstr k=key f=fld1,fld2 v=v1,v2を実行した時の、-R,-Fオプションの指定の有無によるマッチ条件の違い。条件にマッチすれば全行(２行)出力され、アンマッチなら１行も出力されない。
  :header-rows: 1
  :name: mselstr_cond

  ``F`` オプション, ``R`` オプション,マッチ条件
  ,,(( :math:`v_{a1}`   ``==``  s1 or  :math:`v_{a1}`   ``==``  s2)  or ( :math:`v_{a2}`   ``==``  s1 or  :math:`v_{a2}`   ``==``  s2)) or (( :math:`v_{b1}`   ``==``  s1 or  :math:`v_{b1}`   ``==``  s2)  or ( :math:`v_{b2}`   ``==``  s1 or  :math:`v_{b2}`   ``==``  s2))
  -F,,(( :math:`v_{a1}`   ``==``  s1 or  :math:`v_{a1}`   ``==``  s2)  and ( :math:`v_{a2}`   ``==``  s1 or  :math:`v_{a2}`   ``==``  s2)) or (( :math:`v_{b1}`   ``==``  s1 or  :math:`v_{b1}`   ``==``  s2)  and ( :math:`v_{b2}`   ``==``  s1 or  :math:`v_{b2}`   ``==``  s2))
  ,-R,(( :math:`v_{a1}`   ``==``  s1 or  :math:`v_{a1}`   ``==``  s2)  or ( :math:`v_{a2}`   ``==``  s1 or  :math:`v_{a2}`   ``==``  s2)) and (( :math:`v_{b1}`   ``==``  s1 or  :math:`v_{b1}`   ``==``  s2)  or ( :math:`v_{b2}`   ``==``  s1 or  :math:`v_{b2}`   ``==``  s2))
  -F,-R,(( :math:`v_{a1}`   ``==``  s1 or  :math:`v_{a1}`   ``==``  s2)  and ( :math:`v_{a2}`   ``==``  s1 or  :math:`v_{a2}`   ``==``  s2)) and (( :math:`v_{b1}`   ``==``  s1 or  :math:`v_{b1}`   ``==``  s2)  and ( :math:`v_{b2}`   ``==``  s1 or  :math:`v_{b2}`   ``==``  s2))



'''

############################### PARAMETERS
db['params']=[]

param={}
param['kwd']='i'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='標準入力'
param['text']='''
入力データを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
検索対象となる項目名リスト(複数項目指定可)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='v'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
``f=`` パラメータで指定した項目の値が、ここで指定した文字列リスト(複数項目指定可)の1つにマッチすれば選択される。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
選択する単位となるキー項目(複数項目指定可)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='o'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='標準出力'
param['text']='''
指定の条件に一致する行を出力するデータを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='出力しない'
param['text']='''
指定の条件に一致しない行を出力するデータを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='F'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``f=``  パラメータで複数項目を指定した場合、その全ての値がマッチする行を撰択する。
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
条件反転
選択ではなく削除する。
'''
db['params'].append(param)

param={}
param['kwd']='R'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``k=``  パラメータを指定した場合、その全ての行がマッチすれば行を撰択する。
'''
db['params'].append(param)

param={}
param['kwd']='sub'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
検索を完全一致ではなく部分文字列マッチで比較する。
すなわち、 ``f=`` パラメータで指定した項目の値に、
``v=`` パラメータで指定の文字列が部分文字列として含まれていればその行を撰択する。
'''
db['params'].append(param)

param={}
param['kwd']='head'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
先頭文字列マッチオプション
'''
db['params'].append(param)

param={}
param['kwd']='tail'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
末尾文字列マッチオプション
'''
db['params'].append(param)

param={}
param['kwd']='W'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``sub`` , ``head`` , ``tail`` オプションが指定されているときにワイド文字として部分文字列マッチをおこなう。
'''
db['params'].append(param)

param={}
param['kwd']='bufcount'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
バッファのサイズ数を指定する。
'''
db['params'].append(param)

db['comParams']='i,o,bufcount,assert_diffSize,assert_nullkey,assert_nullin,nfn,nfno,x,q,tmppath,precision'
