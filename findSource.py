import sys
import dateparser

def openEdges():
    records = []
    with open("edges.csv","r") as f:
        for line in f:
            records.append(line)
    return records

def createCSV(filesource,id,EdgeValue,date):
    filesource = filesource.replace(" ","_")
    filename = filesource + ".csv"
    w = open(filename, "w")
    w.write("Id,Tweet,Date" + "\n")
    for i in range(len(EdgeValue)):
        w.write(id[i] + "," + EdgeValue[i] + "," + date[i])

def searchSource(source):
    eRecords = openEdges()
    id = []
    EdgeValue = []
    date = []
    flag = 0
    for index in range(len(eRecords) - 1):
        temporary = eRecords[index + 1].split(",")
        if(source == temporary[4]):
            flag = 1
            id.append(temporary[0])
            EdgeValue.append(temporary[4])
            date.append(temporary[5])
    if (flag ==1):
        createCSV(source,id,EdgeValue,date)
    else:
        nrecords = []
        with open("nodes.csv", "r") as f:
            for line in f:
                nrecords.append(line)
        for index in range(len(nrecords) - 1):
            temporary1 = nrecords[index + 1].split(",")
            if (source == temporary1[2]):
                flag = 1
                id.append(temporary1[0])
                EdgeValue.append(temporary1[2])
                date.append(temporary1[3])
        createCSV(source,id,EdgeValue,date)



def main(twitter_tag):
    searchSource(twitter_tag)
    return

if __name__ == '__main__':
    main(" ".join(sys.argv[1:]))