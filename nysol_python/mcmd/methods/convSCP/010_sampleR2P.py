#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import sys
import re
from datetime import datetime

fldMap={}
fldMap["数量累計"]=("num","qttAccum")
fldMap["金額累計"]=("num","amtAccum")
fldMap["数量合計"]=("num","qttTotal")
fldMap["金額合計"]=("num","amtTotal")
fldMap["数量平均"]=("num","qttTotal")
fldMap["金額平均"]=("num","amtTotal")
fldMap["性別"]=("str","gender")
fldMap["女性"]=("str","female")
fldMap["男性"]=("str","male")
fldMap["日付"]=("str","date")
fldMap["顧客"]=("str","customer")
fldMap["数量"]=("num","quantity")
fldMap["金額"]=("num","amount")
fldMap["売上"]=("num","sales")
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

iFile="./samples/ruby/%s.rb"%argv[1]
oFile="./samples/python/%s.py"%argv[1]

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
	#if re.search("mchgnum", txt):
	#	txt=re.sub('"out of range"',"outOfRange",txt)
	#elif re.search("mchgstr", txt):
	#	txt=re.sub('"out of range"',"outOfRange",txt)
	#	txt=re.sub('"item info"',"itemInfo",txt)
	print("convMethod:",txt)

	#token=txt.split(" ")
	token=split2(txt," ")
	print(token)
	params=[]
	outputs=[]
	for i in range(1,len(token)):
		print(i,token[i])
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
	headerBlock=False
	commentBlock=False
	scpBlock=False
	scpFirstTime=True
	outputs=None

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
			dat=""
			datName=re.sub("File\.open\(\"(.*)\.csv.*$","\\1",line).strip()
			dat+="with open('%s.csv','w') as f:\n"%datName
			dat+="  f.write(\n"
			dat+=("'''")
			lines=[]
			fileBlock=True

		elif fileBlock and line==r"EOF":
			dat+=("''')\n")
			scp+=dat
			scp+='dat_str.append("""\n'
			scp+=dat
			scp+='""")'
			fileBlock=False
			continue

		elif fileBlock and line=="<<'EOF'":
			headerBlock=True
			continue
		elif fileBlock:
			if headerBlock: # ヘッダー行
				header=parseHeader(line)
				dat+=(header+"\n")
				headerBlock=False
			else: # 値の行
				dat+=(toEng(line)+"\n")

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
			if scpFirstTime: #scpに入る直前で「利用データ」セクションの出力関数(run_data)を入れる
				scp+=("LIBmkrst.run_data(dat_str)\n")
				scpFirstTime=False

			scp+=(line+"\n")

		# comment
		elif re.search("comment=",line):
			scp+=(re.sub(r"<<'EOF'",'"""'+"\n",line))
			commentBlock=True
		elif commentBlock and line=="EOF":
			scp+=('"""'+"\n")
			commentBlock=False
		elif commentBlock:
			scp+=(convText(line)+"\n")

		# scp
		elif re.search("scp=",line):
			scp+=(re.sub(r"<<'EOF'",'"""'+"\n",line))
			scpBlock=True
		elif scpBlock and line=="EOF":
			scp+=('"""'+"\n")
			scpBlock=False
		elif scpBlock and re.search("more ",line):
			continue
		elif scpBlock:
			methods,outputs=convMethod(line)
			scp+=(methods+"\n")

		# run
		elif re.search(r"^run\(",line):
			#scp+=("LIBmkrst."+re.sub(r"comment","comment,dat_str",line)+"\n")
			scp+=("LIBmkrst.run(scp,title,comment,dat_str,'%s')"%(','.join(outputs)))

# 出力
with open(oFile,"w") as fpw:
#with open("xxscp.py","w") as fpw:
	fpw.write(scp)

