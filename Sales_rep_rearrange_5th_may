article_qty = {}
st = {}


def process(inp, artcls):
	print inp
	outlet_name=inp[0].split(',')[0]
	items={}
	for ids in artcls:
		items[ids]=0
	for lin in inp:
		if ',33' in lin:
			per_line=lin.split(',')
			items[int(per_line[1])]=int(per_line[3])
			try:
				article_qty[int(per_line[1])]+=int(per_line[3])
			except:
				article_qty[int(per_line[1])]=int(per_line[3])
	write=''
	write+=outlet_name
	for a in artcls:
		write+=','+str(items[a])
	sm=0
	for ids in artcls:
		sm+=items[ids]
	st[outlet_name]=sm
	write+=','+str(sm)+'\n'
	ot=open('out.csv','a')
	print write
	ot.write(write)

file_name=raw_input('Input File name:')
f=file(file_name).read().split('\n')
indx=0
flag=0
was=0
strt_stp=[]
articles=[]
id_to_name={}

for line in f:
	if ',33' in line:
		comma_sep=line.split(',')
		#print comma_sep
		#print comma_sep[1]
		if int(comma_sep[1]) not in articles:
			articles.append(int(comma_sep[1]))
			id_to_name[int(comma_sep[1])]=comma_sep[2].replace('S200921','')
		if comma_sep[0]!='' and flag==0:
			start=indx
			strt_stp.append(start)
			flag=1
		elif comma_sep[0]!='' and flag==1:
			stop=indx
			strt_stp.append(stop)
			flag=0
		else:
			was+=1
		
	indx+=1
strt_stp.append(len(f)-1) 
articles.sort()
init='Outlet name'	
for a in articles:
	init+=','+id_to_name[a]+'('+str(a)+')'
init+=','+'Shop_total'+'\n'
ot=open('out.csv','w')
ot.write(init)
ot.close()
for i in range(1,len(strt_stp)):
	process(f[strt_stp[i-1]:strt_stp[i]],articles)
#print strt_stp
total='Total'
sum=0
for a in articles:
	sum+=article_qty[a]
	total+=','+str(article_qty[a])
print sum
ot=open('out.csv','a')
ot.write(total+','+str(sum))



ot.close()
