# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mselnum'
db['title']='数値範囲による行選択'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
``f=`` で指定した項目の値が、
``c=`` で指定した数値範囲にマッチする行を選択する。
以下に示すように多様な選択条件を指定することが可能である。
このコマンドで指定できないより複雑な条件(文字列マッチとの組み合せなど)
を設定するのであれば :doc:`msel` コマンドを利用すればよい。
OR条件、AND条件およびキー指定についての詳細は ``mselstr`` コマンドを参照されたい。

 *  開区間、閉区間、半開区間、無限区間の制定が可能である。
 *   ``c=`` に複数の範囲を指定すれば、いずれかの範囲にマッチすれば選択される(OR条件)。
 *   ``f`` =に複数項目を指定すれば、いずれかの項目の値がマッチすれば選択される(OR条件)。
 *   ``f=`` のOR条件をAND条件に変更することも可能( ``F`` オプション)。
 *   ``k=`` を指定することでキー単位で選択することが可能。
 *  キー単位選択の場合、複数レコードのAND条件を指定可能( ``R`` オプション)。

典型的な例を :numref:`mselnum_input` 〜 :numref:`mselnum_out3` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mselnum_input

  key,val
  a,1
  a,-3
  b,3
  b,6




.. csv-table:: val項目が1以上3以下の行を選択
  :header-rows: 1
  :name: mselnum_out1

  key,val
  a,1
  b,3




.. csv-table:: val項目が1以上3未満の行を選択
  :header-rows: 1
  :name: mselnum_out2

  key,val
  a,1




.. csv-table:: 5以上の行を選択
  :header-rows: 1
  :name: mselnum_out3

  key,val
  b,6




.. csv-table:: 1以下もしくは5以上の行を選択
  :header-rows: 1
  :name: mselnum_out4

  key,val
  a,1
  a,-3
  b,6



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
param['kwd']='c'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
``f=`` パラメータで指定した項目の値が、ここで指定した文字列リスト(複数範囲指定可)の1つにマッチすれば選択される。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
撰択する単位となるキー項目(複数項目指定可)を指定する。
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
``f=`` パラメータで複数項目を指定した場合、その全ての値がマッチする行を撰択する。
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
``k=`` パラメータを指定した場合、その全ての行がマッチすれば行を撰択する。
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
