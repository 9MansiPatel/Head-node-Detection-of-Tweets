def MakeNetwork():
    records=[]
    with open("testtt.csv","r") as f:
     for line in f:
        records.append(line)

    Nodes=[]
    EdgeValue=[]
    Edge=[]
    date = []
    for index in range(len(records)-1):
        temporary = records[index+1].split(",")
        Nodes.append(temporary[0])
        xi = CleanString(temporary[1])
        EdgeValue.append(xi)
        date.append(temporary[2])


    No=open("nodes.csv","w")
    No.write("Id,Label,Tweetword,Date\n")
    Eo=open("edges.csv","w")
    Eo.write("Source,Target,Type,Id,tweetword,Date\n")

    for i in range(len(Nodes)):
        No.write(str(i+1) + "," + Nodes[i] + "," + EdgeValue[i] + "," + date[i])
    edgecount=0
    for i in range(len(EdgeValue)):
        for j in range(len(EdgeValue)):
            if(i!=j):
                if(EdgeValue[i]==EdgeValue[j]):
                    Eo.write(str(i+1) + "," + str(j+1) + "," + "Undirected" + "," + str(edgecount) + "," + EdgeValue[i]+ "," + date[i])
                    edgecount=edgecount+1
    return

def CleanString(incomingString):
    newstring = incomingString
    newstring = newstring.replace("!", "")
    newstring = newstring.replace("@", "")
    newstring = newstring.replace("#", "")
    newstring = newstring.replace("$", "")
    newstring = newstring.replace("%", "")
    newstring = newstring.replace("^", "")
    newstring = newstring.replace("&", "and")
    newstring = newstring.replace("*", "")
    newstring = newstring.replace("(", "")
    newstring = newstring.replace(")", "")
    newstring = newstring.replace("+", "")
    newstring = newstring.replace("=", "")
    newstring = newstring.replace("?", "")
    newstring = newstring.replace("\'", "")
    newstring = newstring.replace("\"", "")
    newstring = newstring.replace("{", "")
    newstring = newstring.replace("}", "")
    newstring = newstring.replace("[", "")
    newstring = newstring.replace("]", "")
    newstring = newstring.replace("<", "")
    newstring = newstring.replace(">", "")
    newstring = newstring.replace("~", "")
    newstring = newstring.replace("`", "")
    newstring = newstring.replace(":", "")
    newstring = newstring.replace(";", "")
    newstring = newstring.replace("|", "")
    newstring = newstring.replace("\\", "")
    newstring = newstring.replace("/", "")
    return newstring


if __name__ == '__main__':
    MakeNetwork()