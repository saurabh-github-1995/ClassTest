studentsList=[]

def sortList():
    length=len(studentsList)
    for i in range(length-1):
        if(studentsList[i+1]["number"]<studentsList[i]["number"]):
           studentsList[i]["number"],studentsList[i+1]["number"]=studentsList[i+1]["number"],studentsList[i]["number"]
           sortList()

def registerStudenrs(student):
    
    studentsList.append(student)
    sortList()

def retrive():
    return studentsList[0]

    
