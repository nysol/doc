
'''
import urllib.request
url="https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
urllib.request.urlretrieve(url,"onlineRetail.xlsx")
'''

import pandas as pd
dtype={
	"InvoiceNo":"object",
	"StockCode":"object",
	"Description":"object",
	"Quantity":"int",
	"InvoiceDate":"object",
	"UnitPrice":"float",
	"CustomerID":"object",
	"Country":"object"
}
data = pd.read_excel('onlineRetail.xlsx', 'Online Retail', index_col=None,dtype=dtype)
data.to_csv('onlineRetail.csv', encoding='utf-8', index=None)
exit


import nysol.mcmd as nm
f=None
f <<= nm.mdformat(f="InvoiceDate", c="%Y-%m-%d %H:%M:%S", i="onlineRetail.csv")
f <<= nm.mcal(c="left($s{InvoiceDate},8)", a="date")
f <<= nm.mcal(c="right($s{InvoiceDate},6)", a="time")
f <<= nm.mcut(f="InvoiceDate", r=True, o="onlineRetail2.csv")
f.run(msg="on")


