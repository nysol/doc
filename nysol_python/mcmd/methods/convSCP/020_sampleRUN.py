#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import sys
import re
import glob
from datetime import datetime

argv=sys.argv
if len(argv)!=2:
	print("010スクリプトで生成されたpythonスクリプトを実行する")
	print("%s all"%argv[0])
	print("%s mcut"%argv[0])
	exit()

sys.stderr.write("START: "+" ".join(argv)+" "+str(datetime.now())+"\n")

iPath="samples/python"
oPath="../rst"

if argv[1]=="all":
	for scp in glob.glob("%s/*.py"%iPath):
		name=os.path.basename(scp)
		oFile="%s/%s"%(oPath,re.sub("\.py",".rst",name))
		print("cd %s ; python %s >%s"%(iPath,name,oFile))
		os.system("cd %s ; python %s >%s"%(iPath,name,oFile))
else:
	scp="%s/%s.py"%(iPath,argv[1])
	name=os.path.basename(scp)
	oFile="%s/%s"%(oPath,re.sub("\.py",".rst",name))
	print("cd %s ; python %s >%s"%(iPath,name,oFile))
	os.system("cd %s ; python %s >%s"%(iPath,name,oFile))

