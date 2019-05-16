#!/usr/bin/env python

# do stats in teh DL.log fine from fetch

import matplotlib.pyplot as plt

data = open('DL.log','r').readlines()

dates = {}
scripts = {}
users = {}

for i in data:
    (user,date,script) = (i.split()[0],''.join(i.split()[1].split('-')[0:2]),i.split()[3].split('/')[-1])
    try:
        dates[date] +=1
    except:
        dates[date] = 1
    try:
        users[user] +=1
    except:
        users[user] = 1
    try:
        scripts[script] +=1
    except:
        scripts[script] = 1

def makeplot(dict,name):
    dkeys = dict.keys()
    dkeys.sort()
    vals = [dict[x] for x in dkeys]
    x= range(len(vals))
    plt.bar(x,vals,align='center')
    plt.xticks(x,dkeys,rotation='vertical',fontsize =10,horizontalalignment='center')
    plt.ylabel('downloads')
    plt.xlim(-1,len(vals))
    plt.tight_layout()
    plt.savefig('{0}.png'.format(name))
    plt.show()
    plt.close()

makeplot(scripts,'scripts')    
makeplot(dates,'dates')    
makeplot(users,'users')    

    
