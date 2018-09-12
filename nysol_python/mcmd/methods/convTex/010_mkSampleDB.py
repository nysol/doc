#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import sys
import re
import json
from datetime import datetime

fldMap={}
fldMap["数量累計"]=("num","qttAccum")
fldMap["金額累計"]=("num","amtAccum")
fldMap["数量合計"]=("num","qttTotal")
fldMap["金額合計"]=("num","amtTotal")
fldMap["数量平均"]=("num","qttTotal")
fldMap["金額平均"]=("num","amtTotal")
fldMap["金額基準値"]=("num","amtNorm")
fldMap["数量基準値"]=("num","qttNorm")
fldMap["性別"]=("str","gender")
fldMap["女性"]=("str","female")
fldMap["男性"]=("str","male")
fldMap["日付"]=("str","date")
fldMap["顧客"]=("str","customer")
fldMap["数量"]=("num","quantity")
fldMap["金額"]=("num","amount")
fldMap["売上"]=("num","sales")
fldMap["商品"]=("str","item")
# fldMapのkeyを文字数降順に並mtべ替える。
# 置換処理の時に、長い順に処理しないとおかしなことになるから。
fldMapKey=list(fldMap)
fldMapKey.sort(key=len)
fldMapKey.reverse()

argv=sys.argv
if len(argv)!=2:
	print("rubyで書かれたsampleスクリプトをpythonスクリプトに変換")
	print("%s mcut"%argv[0])
	exit()

sys.stderr.write("START: "+" ".join(argv)+" "+str(datetime.now())+"\n")

cmdName=argv[1]
iFile="./samples/ruby/%s.rb"%cmdName
oPath="./db_auto/smp"
os.system("mkdir -p %s"%oPath)
oFile="%s/%s.py"%(oPath,cmdName)

# 項目名を英語に変換
def toEng(txt,ref=False):
	if ref:
		for key in fldMapKey:
			nkey="``"+key+"``"
			rep=" ``"+fldMap[key][1]+"`` "
			txt=re.sub(nkey,rep,txt)

			nkey="「"+key+"」"
			rep=" ``"+fldMap[key][1]+"`` "
			txt=re.sub(nkey,rep,txt)
	else:
		for key in fldMapKey:
			rep=fldMap[key][1]
			txt=re.sub(key,rep,txt)
	return txt

# texの文章をrstに変換
# 1) \verb|xx| => ``xx``
# 2) \verb|-xx| => ``xx=True``
def convText(txt):
	txt1=re.sub("\\\\verb\|(.*?)\|"," ``\\1`` ",txt.strip()).strip()
	txt2=re.sub("``-(.*?)``", "``\\1=True``",txt1)
	#print("txt2",txt2)
	txt3=toEng(txt2,True)
	#print("txt3",txt3)
	return txt3.strip()

# \verb|xx| => xx
def rmVerb(txt):
	convText=re.sub("\\\\verb\|(.*?)\|"," \\1 ",txt.strip()).strip()
	return convText

# ダブルクォーツとシングルクォーツを考慮したsplit
def split2(txt,sep):
	inDBL=False
	inSGL=False
	s=""
	sp=[]
	for i in range(len(txt)):
		if inSGL:
			if txt[i]=="'":
				inSGL=False
				continue
		elif inDBL:
			if txt[i]=='"':
				inDBL=False
				continue
		elif txt[i]=="'":
			inSGL= True
			continue
		elif txt[i]=='"':
			inDBL= True
			continue
		elif txt[i]==sep:
			sp.append(s)
			s=""
			continue

		s+=txt[i]
		if i==len(txt)-1:
			sp.append(s)
	return sp


# コマンドをnmメソッドに変換
# mcut f=顧客,金額 -r i=dat1.csv o=rsl1.csv
# =>
# nm.mcut(f="顧客,金額:売上", r=True, i="dat1.csv", o="rsl1.csv")
def convMethod(txt):
	# 不規則なエラー対応のためのブロック
	if re.search("mbest", txt):
		txt=re.sub('from=',"fr=",txt)
	elif re.search("mcat", txt) and re.search("<", txt):
		txt=""
	elif re.search("mnrjoin", txt) or re.search("mrjoin", txt) or re.search("mnrcommon", txt):
		txt=re.sub('r=',"rf=",txt)
	print("convMethod:",txt)

	#token=txt.split(" ")
	txt=re.sub(" +"," ",txt)
	token=split2(txt," ")
	print(token)
	params=[]
	outputs=[]
	method=""
	for i in range(1,len(token)):
		#print(i,token[i])
		if token[i][0]=="-":
			params.append(token[i][1:]+"=True")
		else:
			pp=token[i].split("=")
			if pp[0]=="i" or pp[0]=="m" or pp[0]=="o" or pp[0]=="u":
				params.append(pp[0]+'="'+pp[1]+'"')
				if pp[0]=="o" or pp[0]=="u":
					outputs.append(pp[1])
			else:
				params.append(pp[0]+'="'+toEng(pp[1])+'"')
	if len(token)!=0:
		method="nm.%s(%s).run()"%(token[0],", ".join(params))
	return method,outputs

# CSVヘッダを解釈し、項目名を英語に変換
# input(txt): 顧客,数量,金額
# output: "customer","quantity","amount"
def parseHeader(txt):
	flds=[]
	for fld in txt.split(","):
		flds.append(toEng(fld))
	return ",".join(flds)

###################################
# ここからmain

## 以下、変換元rubyスクリプト

# #!/usr/bin/env ruby
# # coding: utf-8
# require "./mkTex.rb"
# 
# File.open("dat1.csv","w"){|fpw| fpw.write(
# 	<<'EOF'
# 	顧客,数量,金額
# 	A,1,10
# 	A,2,20
# 	B,1,15
# 	B,3,10
# 	B,1,20
# 	EOF
# 	)}
# 
# File.open("dat2.csv","w"){|fpw| fpw.write(
# 	<<'EOF'
# 	A,1,10
# 	A,2,20
# 	B,1,15
# 	B,3,10
# 	B,1,20
# 	EOF
# 	)}
# 
# 
# ############## 例1
# title="基本例"
# comment=<<'EOF'
# 「顧客」と「金額」項目を選択する。ただし、「金額」項目は「売上」と名前を変更して出力している。
# EOF
# scp=<<'EOF'
# more dat1.csv
# mcut f=顧客,金額:売上 i=dat1.csv o=rsl1.csv
# more rsl1.csv
# EOF
# run(scp,title,comment)
# 
# ############## 例2
# title="項目削除"
# comment=<<'EOF'
# \verb|-r|を指定することで、項目を削除できる。
# EOF
# scp=<<'EOF'
# mcut f=顧客,金額 -r i=dat1.csv o=rsl2.csv
# more rsl2.csv
# EOF
# run(scp,title,comment)

if not os.path.exists(iFile):
	with open(oFile,"w") as fpw:
		fpw.write("# ================================================\n")
		fpw.write("# コマンドマニュアル自動作成用サンプルコードデータ\n")
		fpw.write("# ================================================\n")
		fpw.write("db={}\n")
		fpw.write("db['name']='%s'\n"%cmdName)
		fpw.write("\n")
	exit()

# scpにpythonスクリプトを文字列として追加していく
scp=""
scp+=("#!/usr/bin/env python\n")
scp+=("# -*- coding: utf-8 -*-\n")
scp+=("import os\n")
scp+=("import sys\n")
scp+=("sys.path.append('../..')\n")
scp+=("import LIBmkrst\n")
scp+=("\n")
scp+=("dat_str=[]\n") # dat_strには

with open(iFile,"r") as fpr:
	fileBlock=False
	dataBlock=False
	headerBlock=False
	commentBlock=False
	scpBlock=False
	scpFirstTime=True
	outputs=None

	dataDocs=[]
	idatDocs=[]
	odatDocs=[]
	titleDocs=[]
	commentDocs=[]
	shDocs=[]
	pyDocs=[]

	for line in fpr:
		#print(line,fileBlock,headerBlock,commentBlock)
		line=line.strip()
		if line.find("/usr/bin/env")!=-1:
			continue
		elif line.find("coding: utf-8")!=-1:
			continue

		elif line=="":
			scp+=("\n")

		elif line[0]=="#":
			scp+=(line+"\n")

		#######################################################################################
		# dataの処理:以下のように、ファイル名を変数名にCSVをリストとして代入するコードと
		# その代入式を文字列としてdat_str変数に入れるコードを生成している。
		# dat_strは、rstを出力する際に、「利用データ」sectionに出力するコード用に作成している。
		#=======
		# 変換元
		#=======
		# File.open("dat1.csv","w"){|fpw| fpw.write(
		# <<'EOF'
		# 顧客,数量,金額
		# A,1,10
		# A,2,20
		# B,1,15
		# B,3,10
		# B,1,20
		# EOF
		# )}

		#=======
		# 変換後
		#=======
		# with open("xxham", mode='w') as f:
		#	  f.write(
		#	'''顧客,数量,金額
		# A,1,10
		# A,2,20
		# B,1,15
		# B,3,10
		# B,1,20
		#	''')
		elif line.find(r"fpw.write(")!=-1:
			idatDocs.append(re.sub("File\.open\(\"(.*?\..*?)\".*$","\\1",line).strip())
			fileBlock=True
		elif fileBlock and line.find(r"<<'EOF'")!=-1:
			dataBlock=True
			dataDocs.append("")
		elif fileBlock and line.find(r"EOF")!=-1:
			dataBlock=False
		elif dataBlock:
			dataDocs[-1]+=(toEng(line)+"\n")

		#######################################################################################
		# スクリプトの処理
		#=======
		# 変換元
		#=======
		# title="基本例"
		# comment=<<'EOF'
		# 「顧客」と「金額」項目を選択する。ただし、「金額」項目は「売上」と名前を変更して出力している。
		# EOF
		# scp=<<'EOF'
		# more dat1.csv
		# mcut f=顧客,金額:売上 i=dat1.csv o=rsl1.csv
		# more rsl1.csv
		# EOF
		# run(scp,title,comment)
		#=======
		# 変換後
		#=======
		# title="基本例"
		# comment="""
		# 「顧客」と「金額」項目を選択する。ただし、「金額」項目は「売上」と名前を変更して出力している。
		# """
		# scp="""
		# nm.mcut(f="顧客,金額:売上", i=dat1, o="rsl1.csv").run()
		# """
		# LIBmkrst.run(scp,title,comment,dat_str)

		# title
		elif re.search("title=",line):
			fileBlock=False
			title=re.sub("title=\"(.*)\"","\\1",line)
			titleDocs.append(title)

		# comment
		elif re.search("comment=",line):
			commentBlock=True
			commentDocs.append("")
		elif commentBlock and line=="EOF":
			commentBlock=False
		elif commentBlock:
			commentDocs[-1]+=(convText(line)+"\n")

		# scp
		elif re.search("scp=",line):
			shDocs.append([])
			pyDocs.append([])
			scpBlock=True
		elif scpBlock and line=="EOF":
			scpBlock=False
		elif scpBlock and (re.search("more ",line) or re.search("ls ",line)):
			continue
		elif scpBlock:
			#print("line",line)
			methods,outputs=convMethod(line)
			shDocs[-1].append(line)
			pyDocs[-1].append(methods)
			odatDocs.append(outputs)

		# run
		#elif re.search(r"^run\(",line):
		#	#scp+=("LIBmkrst."+re.sub(r"comment","comment,dat_str",line)+"\n")
		#	scp+=("LIBmkrst.run(scp,title,comment,dat_str,'%s')"%(','.join(outputs)))

# 出力
with open(oFile,"w") as fpw:
#with open("xxscp.txt","w") as fpw:
	fpw.write("# ================================================\n")
	fpw.write("# コマンドマニュアル自動作成用サンプルコードデータ\n")
	fpw.write("# ================================================\n")
	fpw.write("db={}\n")
	fpw.write("db['name']='%s'\n"%cmdName)
	fpw.write("\n")

	fpw.write("############################### IDATA\n")
	fpw.write("db['idatas']=[]\n\n")
	for i in range(len(idatDocs)):
		fpw.write("data={}\n")
		fpw.write("data['name']='%s'\n"%idatDocs[i])
		fpw.write("data['text']='''\n%s'''\n"%dataDocs[i])
		fpw.write("db['idatas'].append(data)\n")
		fpw.write("\n")

	fpw.write("############################### SCRIPTS\n")
	fpw.write("db['scripts']=[]\n\n")
	for i in range(len(titleDocs)):
		fpw.write("script={}\n")
		fpw.write("script['title']='%s'\n"%titleDocs[i])
		fpw.write("script['comment']='''\n%s'''\n"%commentDocs[i])
		fpw.write("script['sh_code']='''\n")
		for j in range(len(shDocs[i])):
			fpw.write(shDocs[i][j]+"\n")
		fpw.write("'''\n")
		fpw.write("script['py_code']='''\n")
		for j in range(len(shDocs[i])):
			fpw.write(pyDocs[i][j]+"\n")
		fpw.write("'''\n")

		fpw.write("script['odatas']='%s'\n"%(",".join(odatDocs[i])))
		fpw.write("db['scripts'].append(script)\n")
		fpw.write("\n")

