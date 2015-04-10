article_qty={}
st={}
def process(inp,artcls):
	outlet_name=inp[0].split(',')[0]
	items={}
	for ids in artcls:
		items[ids]=0
	for lin in inp:
		if 'S2' in lin:
			per_line=lin.split(',')
			print per_line
			items[per_line[1]]=int(per_line[2])
			try:
				article_qty[per_line[1]]+=int(per_line[2])
			except:
				article_qty[per_line[1]]=int(per_line[2])
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


f=raw_input('File name:')
inp=file(f).read().split('\n')
ArticleName=[]
indx=0
flag=0
strt_stp=[]
was=0
#Isolating article names and collecting start index and stop index for every outlet
for line in inp:
	if 'S2' in line:
		CommaSeparated=line.split(',')
		if CommaSeparated[1] not in ArticleName:
			ArticleName.append(CommaSeparated[1])
		if CommaSeparated[0]!='' and flag==0:
				start=indx
				strt_stp.append(start)
				flag=1
		elif CommaSeparated[0]!='' and flag==1:
			stop=indx
			strt_stp.append(stop)
			flag=0
		else:
			was+=1
		
	indx+=1 

ArticleName.sort()
strt_stp.append(len(inp)-2)

init='Outlet name'	
for a in ArticleName:
	init+=','+a
init+=','+'Shop_total'+'\n'
ot=open('out.csv','w')
ot.write(init)
ot.close()

for i in range(1,len(strt_stp)):
	process(inp[strt_stp[i-1]:strt_stp[i]],ArticleName)
	

total='Total'
sum=0
for a in ArticleName:
	sum+=article_qty[a]
	total+=','+str(article_qty[a])
print sum
ot=open('out.csv','a')
ot.write(total+','+str(sum))
