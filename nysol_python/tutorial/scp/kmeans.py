#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import nysol.mcmd as nm
import pyper

base=None
base <<= nm.mcut(f="CustomerID,StockCode,date",i="onlineRetail2.csv")
base <<= nm.mdelnull(f="*")
base <<= nm.muniq(k="CustomerID,StockCode,date")
base <<= nm.mcut(f="date",r=True)
base <<= nm.mcount(k="CustomerID,StockCode",a="freq")

freq=None
freq <<= nm.msum(k="StockCode", f="freq", i=base)
freq <<= nm.mselnum(f="freq",c="[1000,]")

matrix=None
matrix <<= nm.mcommon(k="StockCode",m=freq,i=base)
matrix <<= nm.m2cross(k="CustomerID", s="StockCode", f="freq")
matrix <<= nm.mnullto(f="*", v=0, o="custVectors.csv")
matrix.run(msg="on")
matrix.drawModelD3("kmeans.html")

r = pyper.R()
r("d=read.csv('custVectors.csv')")
r("rownames(d)=d[,1]")
r("d=d[,-1]")
r("m=kmeans(d,10)")
r("md=as.data.frame(m$cluster)")
r("write.table(md,file='r_cluster.csv',col.names=FALSE,sep=',')")
m = r.get("m")
print(m)
print(m["cluster"])
centers = r.get("m$centers")
print(centers)
sizes = r.get("m$size")
print(sizes)

f=None
f <<= nm.mcut(nfni=True,f="0:CustomerID,1:cluster",i="r_cluster.csv",o="cust_cluster.csv")
f.run(msg="on")
f.run()
