#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import sys
import re
import subprocess
from datetime import datetime

argv=sys.argv
if len(argv)!=2:
	print("texのコマンドマニュアルをrst形式に変換")
	print("事前に010,020を動かして例題のrstを生成しなければならない")
	print("%s mcut"%argv[0])
	exit()

sys.stderr.write("START: "+" ".join(argv)+" "+str(datetime.now())+"\n")

# texのpath
iPath=os.path.expanduser("~/nysol/nysolx/doc/mcmd/jp")

oPath="./db/cmd"
os.system("mkdir -p %s"%oPath)
docPath="./db/doc"
os.system("mkdir -p %s"%docPath)

cmdName=argv[1]
iFile="%s/%s.tex"%(iPath,cmdName)
oFile="%s/%s"%(oPath,cmdName)
docFile="%s/%s"%(docPath,cmdName)

def convText(txt):
	txt1=re.sub("\\\\verb\|(.*?)\|"," ``\\1`` ",txt.strip()).strip() # \verb|xx| => ``xx``
	txt2=re.sub("``-(.*?)``", "``\\1=True``",txt1) # -q => q=True
	txt3=re.sub("ファイル名", "データ",txt2) # ファイル名 => データ
	txt4=re.sub("ファイル", "データ",txt3) # ファイル => データ
	txt5=re.sub("【デフォルト.*】", "",txt4) # 【デフォルト値:xx】を外す

	txt6=re.sub("\$(.+?)\$"," :math:`\\1` ",txt5)
	return txt6

def rmVerb(txt):
	convText=re.sub("\\\\verb\|(.*?)\|"," \\1 ",txt.strip()).strip()
	return convText

# デフォルト値を返す
def getDefault(name,kwd,txt):
	ret=""
	# 説明にデフォルト値の説明があればそれを使う。
# ex. "乱数の最大値を指定する。【デフォルト値:INT_MAX】"
	if re.search("【デフォルト値:",txt):
		ret=re.sub("^.*【デフォルト値:","",txt)
		ret=re.sub("】.*$","",ret)
	else:
		if kwd=="i=" or kwd=="m=":
			ret="標準入力"
		elif kwd=="o=":
			ret="標準出力"
		elif kwd=="u=":
			ret="出力しない"
		elif kwd=="K=":
			ret="k=と同一項目名"
		elif name=="mchgnum" and kwd=="O=":
			ret="null値"
		elif name=="mchgstr" and kwd=="O=":
			ret="null値"
		elif (name=="mnjoin" or name=="mjoin" or name=="mnrjoin" or name=="mproduct") and kwd=="f=":
			ret="全項目"
		elif name=="mnullto" and (kwd=="k=" or kwd=="s="):
			ret=None
	return ""

# 必須パラメータかどうかの判断
def isMand(name,kwdm,mandParams):
	ret=False
	# マニュアルの書式が間違っている場合は、例外判定させる
	if name=="mnewstr" and kwd=="v=":
		ret=True
	#elif name=="mnullto" and (kwd=="v=" or kwd=="="):
	#	ret="必須(p=Falseの時)"
	# マニュアルの初期があっている場合は、それで判断させる 
	else:
		if kwd in mandParams:
			ret=True
	return ret

##\section{mcut 項目の選択\label{sect:mcut}}
# mcut: 項目の選択
# .................................

##指定した項目を選択する。
##\verb|-r|オプションを付けると、指定した項目を削除する。
#指定した項目を選択する。
#``-r``オプションを付けると、指定した項目を削除する。


with open(iFile,"r") as fpr:
	paramBlock=False
	sectBlock=False
	formBlock=False
	relatedBlock=False

	title=None
	doc=""
	params=[]

	comParams=[] # 共通パラメータリスト
	mandParams=[] # 必須パラメータリスト
	for line in fpr:
		line=line.strip()
		#print(line,paramBlock,sectBlock,relatedBlock)
		#print("xxxxxxxxxxxxxx",line)
		if line=="": # 空行飛ばし
			continue
		if line[0]=="%": # コメント飛ばし
			continue

		# sectionの処理
		# \section{mcut 項目の選択\label{sect:mcut}}
		if line.find(r"\section{")!=-1:
			title=re.sub("\\\\section{(.*?)\\\\label.*$","\\1",line.strip())
			sectBlock=True

		elif line==r"\subsection*{書式}":
			#print("xx2")
			sectBlock=False
			formBlock=True

		elif sectBlock:
			#print("xx3")
			if line.find(r"\index{")!=-1:
				continue
			doc+=(convText(line).strip()+"\n") ## 本文

		# 書式の処理
		# \subsection*{書式} 
		# \verb|mcut f= [-r] [-nfni]|
		# \hyperref[sect:option_i]{[i=]}
		# \hyperref[sect:option_o]{[o=]}
		# \hyperref[sect:option_assert_diffSize]{[-assert\_diffSize]}
		# \hyperref[sect:option_assert_nullin]{[-assert\_nullin]}
		# \hyperref[sect:option_nfn]{[-nfn]} 
		# \hyperref[sect:option_nfno]{[-nfno]}  
		# \hyperref[sect:option_x]{[-x]}
		# \hyperref[sect:option_option_tmppath]{[tmpPath=]}
		# \hyperref[sect:option_precision]{[precision=]}
		# \verb|[-params]|
		# \verb|[--help]|
		# \verb|[--helpl]|
		# \verb|[--version]|\\
		elif formBlock and re.search("^\\\\hyperref",line):
			com=re.sub("\\\\hyperref\[sect:(.*?)\].*","\\1",line)
			com=re.sub("option_(.*)","\\1",com)
			com=re.sub("option_(.*)","\\1",com) # tmppathの前に/optionが2つついているため
			comParams.append(":ref:`%s=<common_param_%s>`\n"%(com,com))
		elif formBlock and re.search(cmdName,line): # 必須かどうかの情報を得る
			if re.search("verb\|",line): # verb|xxx|
				form=re.sub("\\\\verb\|","",line)
				form=re.sub("\|","",form)
			elif re.search("verb\/",line): # verb/xxx/
				form=re.sub("\\\\verb\/","",line)
				form=re.sub("\/","",form)
			form=re.sub(cmdName+" ","",form)
			form=re.sub(" +"," ",form)
			#print(form)
			for p in form.strip().split(" "):
				if p[0]!="[":
					mandParams.append(p)

		# パラメータsubsectionの処理
		##############
		# 入力
		# \subsection*{パラメータ}
		# \begin{table}[htbp]
		# %\begin{center}
		# {\small
		# \begin{tabular}{ll}
		# \verb|i=|    & 入力ファイル名を指定する。\\
		# \verb|o=|    & 出力ファイル名を指定する。\\
		# \verb|f=|    & 抜き出す項目名\\
		#              & 項目名をコロンで区切ることで、出力項目名を変更することができる。\\
		#              & ex. \verb|f=a:A,b:B| \\
		# \verb|-r|    & 項目削除スイッチ\\
		#              & \verb|f=|で指定した項目を削除し、それ以外の項目が抜き出される。\\
		# \verb|-nfni| & 入力データの１行目を項目名行とみなさない。よって項目番号で指定しなければならない。\\
		#              & 以下のように、新項目名を組み合わせて指定することで項目名行を追加出力することが可能となる。\\
		#              & 例）f=0:日付,2:店,3:数量 \\
		# \end{tabular}
		# }
		# \end{table}
		##############
		# 出力
		#.. list-table::
		#  :header-rows: 1
		#
		#  * - パラメータ
		#    - 内容
		#  * - | **dtype={項目名:型,...}**
		#      |   optional
		#      |   default:全項目"str"型
		#    - | 辞書型データで指定し、キーに項目名、値にデータ型を指定する。
		#      |   変換可能なデータ型は次の通り。
		#      |   "str":文字列, "int":整数, "float":実数, "bool":真偽値
		#      | 例) dtype={"customer":"str","date":"str","amount":"int"}
		#  * - | **otype=型**
		#      |   optional
		#      |   default:"list"
		#    - | 出力データのコンテナ型を指定する。
		#      |   "list"(リスト型),"dict"(辞書型)の2つの型を指定できる。
		#      |   "list"を指定した場合、項目名ヘッダーは出力されない。
		#      |   "dict"を指定した場合、辞書のキーが項目名で、値がその項目の値となる。
		#      | 例) otype="dict"
		elif line=='\subsection*{パラメータ}':
			#print("xx4")
			paramBlock=True
			formBlock=False

		elif paramBlock and line==r"\end{table}":
			#print("xx6")
			paramBlock=False

		elif paramBlock and line.find("&")==-1: # 表データ行は必ず"&"を含む
			#print("xx5")
			continue

		# (kwd,type,mand ,cond              ,default   ,doc)
		# ("f",str ,True ,None              ,None      ,"xxxx")
		# ("v",str ,True ,"p=Falseの時"     ,None      ,"xxxx")
		# ("v",str ,True ,"-pが指定された時",None      ,"xxxx")
		# ("i",str ,False,None              ,"標準入力","入力データをxxxx")
		# ("q",bool,False,None,             ,False     ,"xxxx")
		# ##PARAM("v",sh,py,rb)
		# ###TYPE("str",sh,py,rb)
		# ###MANDATORY(True,sh,py,rb)
		# ###CONDITION(py)
		# p=Falseの時
		# ###CONDITION_END
		# ###CONDITION(sh)
		# p=-pが指定された時
		# ###CONDITION_END
		# ###DOC(sh,py,rb)
		# xxxxx
		# ###DOC_END
		# ##PARAM_END

		elif paramBlock:
			#print("xx7")
			line=re.sub("\\\\\\\\$","",line)  # 行末の\\を削除
			cols=line.split('&')
			if cols[0]!="":
				params.append({})
				kwd=rmVerb(cols[0])
				if(kwd[0]=="-"):
					params[-1]["kwd"]=kwd[1:]
					params[-1]["type"]="bool"
					params[-1]["mand"]=False
					params[-1]["cond"]=""
					params[-1]["default"]=""
					params[-1]["text"]=(convText(cols[1])+"\n")
				else:
					params[-1]["kwd"]=kwd[:-1]
					params[-1]["type"]="str" # 後で手編集
					params[-1]["mand"]=isMand(cmdName,kwd,mandParams)
					params[-1]["cond"]=""
					params[-1]["default"]=getDefault(cmdName,kwd,cols[1])
					params[-1]["text"]=(convText(cols[1])+"\n")
			else:
				params[-1]["text"]+=(convText(cols[1])+"\n")

		elif line==r"\subsection*{利用例}":
			pass

		#	関連メソッドの処理
		#	\hyperref[sect:mfldname]{mfldname} : 項目名を変更したいだけの場合は\verb|mfldname|を使う。
		elif line==r"\subsection*{関連コマンド}":
			relatedBlock=True

		elif relatedBlock:
			related=re.sub("\\\\hyperref\[sect:(.*?)\].*","\\1",line)
			#print("xx10")
			#print(re.sub("\\\\hyperref\[sect:(.*?)\].*","- :doc:`\\1` ",line))
			#print(re.sub("\\\\hyperref\[sect:(.*?)\].*","- :doc:`mcut` ",line))

# 出力
#with open(oFile,"w") as fpw:
with open(oFile,"w") as fpw:
	fpw.write("#COM ===================================================================================\n")
	fpw.write("#COM コマンドリファレンス自動作成用データ(#COMから始まる行はコメント行,空行は無視される)\n")
	fpw.write("#COM ===================================================================================\n")
	fpw.write("#CMD(%s,sh,py,rb)\n"%cmdName)
	fpw.write("\n")

	fpw.write("##TITLE(sh,py,rb)\n")
	fpw.write(title+"\n")
	fpw.write("##TITLE_END\n")
	fpw.write("\n")

	for i in range(len(params)):
		fpw.write("#PARAM(%s,sh,py,rb)\n"%params[i]["kwd"])
		fpw.write("##TYPE(%s,sh,py,rb)\n"%params[i]["type"])
		fpw.write("##MAND(%s,sh,py,rb)\n"%params[i]["mand"])
		fpw.write("##COND(sh,py,rb)\n")
		fpw.write(params[i]["cond"])
		fpw.write("##COND_END\n")
		fpw.write("##DEFAULT(sh,py,rb)\n")
		fpw.write(params[i]["default"])
		fpw.write("##DEFAULT_END\n")
		fpw.write("##TEXT(sh,py,rb)\n")
		fpw.write(params[i]["text"])
		fpw.write("##TEXT_END\n")
		fpw.write("\n")

	fpw.write("##RELATED(sh,py,rb)\n")
	fpw.write(related)
	fpw.write("##RELATED_END\n")

with open(docFile,"w") as fpw:
	fpw.write("#COM ===================================================================================\n")
	fpw.write("#COM コマンドリファレンス自動作成用データ(#COMから始まる行はコメント行,空行は無視される)\n")
	fpw.write("#COM ===================================================================================\n")
	fpw.write("#CMD(%s,sh,py,rb)\n"%cmdName)
	fpw.write("\n")
	fpw.write("#DOC(sh,py,rb)\n")
	fpw.write(doc)
	fpw.write("#DOC_END\n")

