import nysol.mcmd as nm
dat=[
["customer","date","amount"],
["A","20180101",5200],
["B","20180101",800],
["B","20180112",3500],
["A","20180105",2000],
["B","20180107",4000]
]

f1 = nm.mcut(f="customer,amount", i=dat)
total=nm.msum(f="amount:totalAmount", i=f1)
f2 = nm.msum(k="customer", f="amount", i=f1)
f3 = nm.mproduct(m=total, f="totalAmount", i=f2)
f4 = nm.mcal(c='${amount}/${totalAmount}', a="share", i=f3)
print(f4.run())

