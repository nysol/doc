
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
f <<= nm.msum(k="customer",f="amount")
print( f.run())

nm.drawModelsD3([f],"cust_amount.html")

for line in nm.mcut(f="customer,date,amount",i=dat):
	print(line)

dtype = {'customer':'str', 'date':'str', 'amount':'int'}
#f=nm.mcut(f="customer,date,amount",i=dat).getline(dtype=dtype,otype="dic")
f=nm.mcut(f="customer,date,amount",i=dat).getline_dict(dtype=dtype)
for line in f:
	print(line)

#f=nm.mcut(f="customer,date,amount",i=dat).getline(skeys="amount%nr")
f=nm.mcut(f="customer,date,amount",i=dat).getline_with_keyflag("customer",skeys="amount%nr")
for line in f:
	print(line)

#f=nm.mcut(f="customer,date,amount",i=dat).getline(keys="customer",skeys="date")
f=nm.mcut(f="customer,date,amount",i=dat).getline_with_keyflag("customer",skeys="date")
for line in f:
	print(line)

print("keyblock")
f=nm.mcut(f="customer,date,amount",i=dat).keyblock(keys="customer",skeys="date",dtype=dtype)
for block in f:
	print(block)

