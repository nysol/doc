#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
import os

# 010_sampleR2P.pyにて以下のrun,run_dataを呼び出すpythonコードがメソッドごとに出力される(ex. samples/python/mcut.py)
# 020_sampleRUN.pyにて、生成されたpythonスクリプトが一括して実行され、それぞれのスクリプトから以下のrun,run_dataがコールされる。

##########################################################################
# タイトル、コメント、スクリプトとその実行結果をrstフォーマットで出力する
###############
# 以下、実行例
###############
# 基本例
# :::::::::
# 
# 「顧客」と「金額」項目を選択する。ただし、「金額」項目は「売上」と名前を変更して出力している。
# 
# 
#   .. code-block:: python
#     :linenos:
# 
#     >>> nm.mcut(f="顧客,金額:売上", i=dat1).run()
#     [['A', '10'], ['A', '20'], ['B', '15'], ['B', '10'], ['B', '20']]
#
def run(scp,title,comment,dat_str,outputs):
	# 結果を得るために例題のスクリプトを実行できる形で生成する
	# import文の追加+データ定義
	with open("xxscp","w") as fpw:
		fpw.write("import nysol.mcmd as nm")
		for dat in dat_str:
			fpw.write(dat)
		fpw.write("print("+scp+")")
	os.system("python xxscp >/dev/null") #実行

	# 実行結果がoutputsのファイル名に入る
	result=[]
	for fname in outputs.split(","):
		with open(fname,"r") as fpr:
			dat="## %s の内容\n"%(fname) + fpr.read()
			dat=dat[:-1] # 最後に変な文字が入っているので削除
			#dat=dat[:-1]+"\n" # 最後に変な文字が入っているので削除
			result.append(re.sub("^","    # ",dat,flags=(re.MULTILINE)))

	# 出力
	print("**"+title.strip()+"**")
	#print(":"*len(title)*3)
	print(comment)
	print("")
	print("  .. code-block:: python")
	print("    :linenos:")
	print("")
	print("    >>> "+scp.strip())
	print("\n".join(result))
	print("")

##########################################################################
# 例題で共通して利用されるデータを「入力データ」sectionとして出力する。
###############
# 以下、実行例
###############
# 入力データ
# :::::::::::::::
#   .. code-block:: python
#     :linenos:
# 
#     >>> dat1=[
#     ["顧客","数量","金額"],
#     ["A",1,10],
#     ["A",2,20],
#     ["B",1,15],
#     ["B",3,10],
#     ["B",1,20]
#     ]
def run_data(dat_str):
	txt=""

	txt+="**importと入力データ(CSV)の準備**\n"
	txt+="  .. code-block:: python\n"
	txt+="    :linenos:\n"
	txt+="\n"
	txt+="    import nysol.mcmd as nm"
	txt+="    \n"
	for dat in dat_str:
		dat2=re.sub("^","    ",dat,flags=(re.MULTILINE))
		txt+="    %s"%dat2
	print(txt)

