#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import sys
import re
import glob
from datetime import datetime

argv=sys.argv
if len(argv)!=2:
	print("010スクリプトで生成されたpythonスクリプトを一括して実行する")
	print("%s run"%argv[0])
	exit()

iPath="samples/python"
oPath="../rst"

for scp in glob.glob("%s/*.py"%iPath):
	name=os.path.basename(scp)
	oFile="%s/%s"%(oPath,re.sub("\.py",".rst",name))
	print("cd %s ; python %s >%s"%(iPath,name,oFile))
	os.system("cd %s ; python %s >%s"%(iPath,name,oFile))

