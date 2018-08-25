
import nysol.mcmd as nm
dat=[
["customer","date","amount"],
["A","20180101",5200],
["B","20180101",4000],
["B","20180112",3500],
["A","20180105",2000],
["B","20180107",800]
]

print(nm.mcut(f="customer,amount",i=dat).run())

print(nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount").run())

f=None
f <<= nm.mcut(f="customer,amount",i=dat)
f <<= nm.msum(k="customer",f="amount")
print(f.run())
