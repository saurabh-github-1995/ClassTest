#initializing empty student list which will containe number of dictionaries of student data
studentsList=[]

#function for sorting student list using bubble sort and recursion
def sortList():
    length=len(studentsList)
    for i in range(length-1):
        if(studentsList[i+1]["number"]<studentsList[i]["number"]):
           studentsList[i]["number"],studentsList[i+1]["number"]=studentsList[i+1]["number"],studentsList[i]["number"]
           sortList()

#function for mregisterenig stuentd one at a time
def registerStudenrs(student):
    
    studentsList.append(student)
    sortList()

#function for student with lowest number
def retrive():
    return studentsList[0]

#Second Logic for sorting
def sortList2(student):
    if(student["number"]>studentsList[-1]["number"]):
        studentsList.append(student)
    else:
        for i in range(len(studentsList)-1):
            if(student["number"]<studentsList[i]["number"]):
                studentsList.insert(i,student)
    
