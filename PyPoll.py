import pandas as pd

dat=pd.read_csv('election_data.csv')
dat=dat.reset_index()
totalvotes=len(dat.index)
x=dat.iloc[:,3]
l1=[]
for i in range(0,totalvotes):
    if(x[i] not in l1):
        l1.append(x[i])
l2=[0]*len(l1)
for i in l1:
    for j in x:
        if(i==j):
           l2[l1.index(i)]+=1 
sum1=sum(l2)
l3=[0.0]*len(l2)    
for i in range(0,len(l2)):
    l3[i]=l2[i]/sum1

winner=l1[l2.index(max(l2))]

print('Total Votes: ',totalvotes)
for i in range(0,len(l2)):
    #print(l1[i]+" "+str(l3[i]*100.0)+"% ("+str(l2[i])+")")
    print(f'{l1[i]}  {l3[i]*100.0:.3f}%  {l2[i]}')

print("Winner: ",winner)

f = open('PyPoll.txt','a')

f.write('Total Votes: '+str(totalvotes))
for i in range(0,len(l2)):
    f.write(f'\n{l1[i]}  {l3[i]*100.0:.3f}%  {l2[i]}')
f.write('\nWinner: '+str(winner))
f.close()


