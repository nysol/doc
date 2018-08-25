
import nysol.mcmd as nm
dat=[
["customer","date","amount"],
["A","20180101",5200],
["B","20180101",800],
["B","20180112",3500],
["A","20180105",2000],
["B","20180107",4000]
]


f=None
f <<= nm.mcut(f="customer,amount",i=dat)                                                                                             
total=nm.msum(f="amount:totalAmount",i=f)
f <<= nm.msum(k="customer", f="amount")
f <<= nm.mproduct(m=total, f="totalAmount")
f <<= nm.mcal(c='${amount}/${totalAmount}', a="share")
f.drawModelD3("flow_share.html")
print(f.run())

