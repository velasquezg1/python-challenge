import pandas as pd

dat=pd.read_csv('budget_data.csv')
dat=dat.reset_index()
totalmonths=len(dat.index)
x=dat.iloc[:,2]
net=x.sum()
x1=x[0]
x2=0
x3=[]
for i in range(1,totalmonths):
    x2=x[i]-x1
    x1=x[i]
    x3.append(x2)
avg=sum(x3) / float(len(x3))
mini=x3.index(min(x3))+1
maxi=x3.index(max(x3))+1
x4,x5=dat.iloc[maxi,1:]
x6,x7=dat.iloc[mini,1:]    

print('Total Months: ',totalmonths)
print('Total: $',net)
print('Average  Change: $'+str(round(avg,2)))
print('Greatest Increase in Profits: ',x4,'($',x5,')')
print('Greatest Decrease in Profits: ',x6,'($',x7,')')

f = open('PyBank.txt','a')
f.write('Total Months: '+str(totalmonths))
f.write('\nTotal: $'+str(net))
f.write('\nAverage Change: $'+str(round(avg,2)))
f.write('\nGreatest Increase in Profits: '+str(x4)+' ($'+str(x5)+')')
f.write('\nGreatest Decrease in Profits: '+str(x6)+'($'+str(x7)+')')
f.close()