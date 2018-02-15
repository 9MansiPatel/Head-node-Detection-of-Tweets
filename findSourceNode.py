import sys
import os
import dateparser

def findNode(file1):
    file = file1.replace(" ","_")
    filename = file + ".csv"
    stamp = []
    with open(filename) as f:
        for line in f:
            stamp.append(line)
    d_id = []
    d_date = []
    for index in range(len(stamp) - 1):
        temp = stamp[index + 1].split(",")
        d_id.append(temp[0])
        d_date.append(dateparser.parse(temp[2]))
    if(d_date):
        source_date = min(d_date)
    else:
        return "Empty"
    sourceNode_index = d_date.index(source_date)
    flag = 1
    with open("nodes.csv", "r") as f:
        for line in f:
            temp1 = line.split(",")
            if(temp1[2] == file1 and dateparser.parse(temp1[3]) == source_date):
                headNodeUser = temp1[1]
                flag = 0
                headNodeId = temp[0]
                break;
    if(flag == 0):
        return headNodeUser
    else:
        return "Nothing"


def main(s):
    twitter_tag = s
    value = "findSource.py " + twitter_tag
    os.system(value)
    x = findNode(twitter_tag)
    return x

if __name__ == '__main__':
    x = main(" ".join(sys.argv[1:]))