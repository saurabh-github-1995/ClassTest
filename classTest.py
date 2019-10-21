#initializing empty student list
studentsList=[]

#function for sorting student list using bubble sort and recursion
def sortList():
    length=len(studentsList)
    for i in range(length-1):
        if(studentsList[i+1]["number"]<studentsList[i]["number"]):
           studentsList[i]["number"],studentsList[i+1]["number"]=studentsList[i+1]["number"],studentsList[i]["number"]
           sortList()

            #function for mregisterenig stuent
def registerStudenrs(student):
    
    studentsList.append(student)
    sortList()

    #function for student with lowest number
def retrive():
    return studentsList[0]


    
