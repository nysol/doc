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
# sampleのpath
sPath="./samples/rst"

name=argv[1]
iFile="%s/%s.tex"%(iPath,name)
sFile="%s/%s.rst"%(sPath,name) # サンプルrst

def convText(txt):
	txt1=re.sub("\\\\verb\|(.*?)\|"," ``\\1`` ",txt.strip()).strip() # \verb|xx| => ``xx``
	txt2=re.sub("``-(.*?)``", "``\\1=True``",txt1) # -q => q=True
	txt3=re.sub("ファイル名", "データ",txt2) # ファイル名 => データ
	txt4=re.sub("ファイル", "データ",txt3) # ファイル => データ
	return txt4

def rmVerb(txt):
	convText=re.sub("\\\\verb\|(.*?)\|"," \\1 ",txt.strip()).strip()
	return convText

# -r => r=
def opt2par(txt):
	return txt[1:]+"="

def getSample(sFile):
	doc=None
	with open(sFile,"r") as fpr:
		doc=fpr.read()
	return doc

# デフォルト値を返す
def getDefault(name,kwd):
	ret=""
	if kwd=="i=" or kwd=="m=":
		ret="標準入力"
	elif kwd=="o=" or kwd=="u=":
		ret="標準出力"
	elif name=="mchgnum" and kwd=="O=":
		ret="null値"
	elif name=="mchgstr" and kwd=="O=":
		ret="null値"
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
			#print("xx1")
			title=re.sub("\\\\section{(.*?)\\\\label.*$","\\1",line.strip())
			print(title)
			print("-"*len(title)*3)
			print("")
			sectBlock=True

		elif line==r"\subsection*{書式}":
			#print("xx2")
			sectBlock=False
			formBlock=True
			print("")

		elif sectBlock:
			#print("xx3")
			if line.find(r"\index{")!=-1:
				continue
			print(convText(line).strip())

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
		elif formBlock and re.search(name,line): # 必須かどうかの情報を得る
			if re.search("verb\|",line): # verb|xxx|
				form=re.sub("\\\\verb\|","",line)
				form=re.sub("\|","",form)
			elif re.search("verb\/",line): # verb/xxx/
				form=re.sub("\\\\verb\/","",line)
				form=re.sub("\/","",form)
			form=re.sub(name+" ","",form)
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
			print("パラメータ")
			print("''''''''''''''''''''''")
			print("")
			print("  .. list-table::")
			print("    :header-rows: 1")
			print("")
			print("    * - キーワード")
			print("      - 内容")
			print("")

		elif paramBlock and line==r"\end{table}":
			#print("xx6")
			print("")
			print("共通パラメータ")
			print("''''''''''''''''''''")
			print("")
			print(", ".join(comParams))
			paramBlock=False

		elif paramBlock and line.find("&")==-1: # 表データ行は必ず"&"を含む
			#print("xx5")
			continue

		elif paramBlock:
			#print("xx7")
			line=re.sub("\\\\\\\\$","",line)
			cols=line.split('&')
			if cols[0]!="":
				kwd=rmVerb(cols[0])
				if(kwd[0]=="-"):
					print("    * - | **%sTrue|False**"%(opt2par(kwd)))
					print("        |   任意")
					print("        |   デフォルト:False")
					print("      - |   %s"%(convText(cols[1])))
				else:
					print("    * - | **%s**"%(kwd))
					if kwd in mandParams:
						print("        |   必須")
					else:
						print("        |   任意")
						default=getDefault(name,kwd)
						print("        |   デフォルト:%s"%(default))
					print("      - |   %s"%(convText(cols[1])))
			else:
				print("        |   %s"%(convText(cols[1])))

		elif line==r"\subsection*{利用例}":
			#print("xx8")
			print("利用例")
			print("''''''''''''")
			print("")
			print(getSample(sFile))
			print("")

		#	関連メソッドの処理
		#	\hyperref[sect:mfldname]{mfldname} : 項目名を変更したいだけの場合は\verb|mfldname|を使う。
		elif line==r"\subsection*{関連コマンド}":
			#print("xx9")
			print("関連メソッド")
			print("''''''''''''")
			print("")
			relatedBlock=True

		elif relatedBlock:
			#print("xx10")
			print(re.sub("\\\\hyperref\[sect:(.*?)\].*","- :doc:`\\1` ",line))
			#print(re.sub("\\\\hyperref\[sect:(.*?)\].*","- :doc:`mcut` ",line))

