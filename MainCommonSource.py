import os
import findSourceNode
from collections import Counter

topic = []
with open("nodes.csv", "r") as f:
    for line in f:
        temp1 = line.split(",")
        if (len(temp1) > 2):
            topic.append(temp1[2])
topicSet = set(topic)
topicSet = list(topicSet)


sUsers = []
for i in range(len(topicSet)):
    '''temp = "findSourceNode.py " + topicSet[i]'''
    '''m = os.system(temp)'''
    temp = topicSet[i]
    m = findSourceNode.main(temp)
    sUsers.append(m)

count = Counter(sUsers)
xi = count.most_common()
for i in xi:
    print i