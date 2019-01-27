import os,json
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB,BernoulliNB,MultinomialNB
import numpy as np
import time
t1=time.time()
filelist=os.listdir('matches')
trainset=[]
trainlabels=[]
testset=[]
testlabels=[]
count=0
for i in filelist:
    #print count
    data=[]
    with open('matches/'+i,'r') as json_file:
        data=json.load(json_file)
        #Hero_ids start from 1
        #Array indexes start from 0
        #Hero ID = Index+1
    radiant=[0 for i in range(115)]
    dire=[0 for i in range(115)]
    win=-1
    for i in data['players']:
        if i['player_slot'] in [0,1,2,3,4]:
            radiant[i['hero_id']-1]=1
        if i['player_slot'] in [128,129,130,131,132]:
            dire[i['hero_id']-1]=1
    if data['radiant_win']==True:
        win=0
    else:
        win=1
    match=radiant+dire
    trainset.append(match)
    trainlabels.append(win)
    count+=1
    #if count%10==0:
    #    testset.append(match)
    #    testlabels.append(win)
    #    count+=1
    #else:
    #    trainset.append(match)
    #    trainlabels.append(win)
    #    count+=1
t2=time.time()
print "Data Ready",t2-t1
X=np.array(trainset[:-1])
Y=np.array(trainlabels[:-1])
X_test=np.array(testset)
Y_test=np.array(testlabels)
"""
clf = GaussianNB()
clf.fit(X, Y)
result=clf.predict(X_test)
print "Gaussian Accuracy:",accuracy_score(result,Y_test)
 
clf = MultinomialNB()
clf.fit(X, Y)
result=clf.predict(X_test)
print "Multinomial Accuracy:",accuracy_score(result,Y_test)
"""
clf = BernoulliNB()
clf.fit(X, Y)
result=clf.predict(X_test)
print len(X_test)
print len(clf.predict_proba(X_test))
print "Bernoulli Accuracy:",accuracy_score(result,Y_test)
