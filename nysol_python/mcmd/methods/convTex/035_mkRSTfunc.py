#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import sys
import re
import subprocess
from datetime import datetime

argv=sys.argv
if len(argv)!=2:
	print("dbのcmd,smpのfunc_*.pyからrst形式の文書を構成する")
	print("%s dow"%argv[0])
	exit()

sys.stderr.write("START: "+" ".join(argv)+" "+str(datetime.now())+"\n")
name=argv[1]

# dbのpath
cmdFile="db.cmd.func_%s"%name
smpFile="db.smp.func_%s"%name
oFile="../func_%s.rst"%name

sys.path.append("./db/cmd")
exec("import %s as cmd"%cmdFile)
sys.path.append("./db/smp")
exec("import %s as smp"%smpFile)

def runpy(idat_code,code):
	os.system("rm -rf xxscp.py")
	with open("xxscp.py","w") as fpw:
		fpw.write("#!/usr/bin/env python\n")
		fpw.write("# -*- coding: utf-8 -*-\n")
		fpw.write(re.sub("^    ","",idat_code,flags=(re.MULTILINE)))
		fpw.write("import nysol.mcmd as nm\n")
		fpw.write(code)
	os.system("python xxscp.py")

def getodata(odata):
	s=""
	if os.path.exists(odata):
		with open(odata,"r") as fpr:
			line=fpr.readline()
			while line:
				s+="    # %s\n"%line.strip()
				line=fpr.readline()
	return s

def writeParams1(fpw):
	fpw.write("  .. list-table::\n")
	fpw.write("   :header-rows: 1\n")
	fpw.write("\n")
	fpw.write("   * - キーワード\n")
	fpw.write("     - 内容\n")

	# param={}
	# param['kwd']='i'
	# param['type']='str'
	# param['mand']=False
	# param['cond']=''
	# param['default']=''
	# param['text']='''
	# 入力データを指定する。
	# '''
	# =>
	#     * - | **i=**
	#         |   任意
	#	        |   デフォルト:標準入力
	#	      - |   入力データを指定する。
	for param in cmd.db["params"]:
		## kwd
		fpw.write("   * - | **%s=** *%s*\n"%(param["kwd"],param["type"]))
		## 必須/任意/条件付き必須
		s="任意"
		if param["mand"]:
			s="必須"
		if param["cond"]!="":
			s="条件付き必須("+param["cond"]+")"
		fpw.write("       | %s\n"%(s))
		## デフォルト
		if param["default"]!="":
			fpw.write("       | %s\n"%(param["default"]))
		## 説明
		txt=param["text"].strip().split("\n")
		para=""
		i=0
		for line in txt:
			if i==0:
				para+="     - | %s\n"%line
			else:
				para+="       | %s\n"%line
			i+=1
		fpw.write(para)
	fpw.write("\n\n")

def writeParams2(fpw):

	# param={}
	# param['kwd']='i'
	# param['type']='str'
	# param['mand']=False
	# param['cond']=''
	# param['default']=''
	# param['text']='''
	# 入力データを指定する。
	# '''
	# =>
	# **i=** *str*
	# 任意(デフォルト:標準入力)
	#	入力データを指定する。
	for param in cmd.db["params"]:
		## kwd
		## 必須/任意/条件付き必須
		if param["mand"]:
			if param["cond"]!="":
				s="条件付き必須("+param["cond"]+")"
			else:
				s="必須"
		else:
			s="任意(default=%s)"%param["default"]
		fpw.write("**%s=** : 型=%s , %s\n\n"%(param["kwd"],param["type"],s))

		## 説明
		txt=param["text"].strip().split("\n")
		for line in txt:
			fpw.write("  | %s\n"%line)
		fpw.write("\n")
	fpw.write("\n\n")

with open(oFile,"w") as fpw:
	title="%s %s"%(cmd.db["name"],cmd.db["title"])
	fpw.write(title+"\n")
	fpw.write("-"*2*len(title)+"\n\n")

	# 書式
	#   ["dow","date","m","曜日番号(1〜7)"],
	i=1
	for form in cmd.db["forms"]:
		name=form[0]
		params=form[1].split(",")
		mands =form[2].split(",")
		paraStr=[]
		for j in range(len(params)):
			if mands[j]=="o":
				paraStr.append("[%s]"%params[j])
			else:
				paraStr.append("%s"%params[j])
		comment=form[3]
		s="* 書式%d: %s(%s) %s"%(i,name,",".join(paraStr),comment)
		i+=1
		fpw.write(s+"\n")
	fpw.write("\n")

	# 解説
	fpw.write(cmd.db["doc"]+"\n\n")

	# data={}
	# data['name']='dat1.csv'
	# data['text']='''
	# item,amount
	# apple,100
	# milk,350
	# orange,100
	# pineapplejuice,500
	# wine,1000
	# '''
	# ===========>>>>>>>>
	# 利用例
	# ''''''''''''
	# 
	# **importと入力データ(CSV)の準備**
	#   .. code-block:: python
	#     :linenos:
	# 
	#     import nysol.mcmd as nm    
	#         
	#     with open('dat1.csv','w') as f:
	#       f.write(
	#     '''customer,quantity
	#     A,5
	#     B,10
	#     C,15
	#     D,2
	#     E,50
	#     ''')

	fpw.write("利用例\n")
	fpw.write("''''''''''''\n\n")

	if "idatas" in smp.db:
		fpw.write("**importと入力データ(CSV)の準備**\n\n")
		fpw.write("  .. code-block:: python\n")
		fpw.write("    :linenos:\n")
		fpw.write("\n")
		idat_code=""
		idat_code+="    import nysol.mcmd as nm\n\n"
		for data in smp.db["idatas"]:
			s=""
			i=0
			for line in data['text'][1:].strip().split("\n"): # 1:は最初に\nが入っているのを無視するため
				if i==0:
					s+=(line+"\n")
				else:
					s+=("    "+line+"\n")
				i+=1
			idat_code+="    with open('%s','w') as f:\n"%data["name"]
			idat_code+="      f.write(\n"
			idat_code+="    '''%s    ''')\n\n"%s
		fpw.write(idat_code)
		fpw.write("\n")

	# script={}
	# script['title']='基本例'
	# script['comment']='''
	# ``item`` 項目の値が ``apple、orange`` に完全一致する行を選択し、
	# ``rsl1.csv`` に出力する。
	# ``u=oth1.csv`` を指定すれば、それ以外の行は ``oth1.csv`` に出力する。
	# ``pineapplejuice`` は完全一致ではないので、 ``oth1.csv`` に出力される。
	# '''
	# script['sh_code']='''
	# mselstr f=商品 v=apple,orange u=oth1.csv i=dat1.csv o=rsl1.csv
	# '''
	# script['py_code']='''
	# nm.mselstr(f="item", v="apple,orange", u="oth1.csv", i="dat1.csv", o="rsl1.csv").run()
	# '''
	# script['odatas']='oth1.csv,rsl1.csv'
	# ===========>>>>>>>>
	# **基本例**
	# 
	# ``quantity`` 項目の値が最小以上10未満を ``low`` 、
	# 10以上20未満を ``middle`` 、20以上最大未満を ``high`` という文字列に置換する。
	# 
	# 
	#   .. code-block:: python
	#     :linenos:
	# 
	#     nm.mchgnum(f="quantity", R="MIN,10,20,MAX", v="low,middle,high", i="dat1.csv", o="rsl1.csv").run()
	#     # ## rsl1.csv の内容
	#     # customer,quantity
	#     # A,low
	#     # B,middle
	#     # C,middle
	#     # D,low
	#     # E,high
	#print("scp",smp.db["scripts"])
	if "scripts" in smp.db:
		for scp in smp.db["scripts"]:
			fpw.write("**%s**\n\n"%scp["title"])
			fpw.write(scp["comment"][1:]+"\n")
			fpw.write("  .. code-block:: python\n")
			fpw.write("    :linenos:\n\n")
			s=""
			# pythonコードの出力
			for line in scp["py_code"][1:].strip().split("\n"):
				fpw.write("    %s\n"%line)
			# サンプルスクリプトの実行(実行前にofileを消しておく)
			for odata in scp["odatas"].split(","):
				os.system("rm -f %s"%odata)
			runpy(idat_code,scp["py_code"])
			# 結果ファイルの表示
			for odata in scp["odatas"].split(","):
				dat=getodata(odata)
				fpw.write("    ### %s の内容\n"%odata)
				fpw.write(dat)
			fpw.write("\n\n")

