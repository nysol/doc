
import nysol.mcmd as nm
dat=[
["customer","date","amount"],
["A","20180101",5200],
["B","20180101",800],
["B","20180112",3500],
["A","20180105",2000],
["B","20180107",4000]
]


f1=None
f1 <<= nm.mcut(f="customer,amount",i=dat)
custA  = nm.mselstr(f="customer",v="A",i=f1)
custB  = custA.redirect("u")
custB <<= nm.mselnum(f="amount",c="[1000,]")
f2=None
f2 <<= nm.msum(k="customer", f="amount", i=[custA,custB])
f2.drawModelD3("flow_redirect.html")
print(f2.run())

