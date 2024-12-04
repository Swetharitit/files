marks=[11,12,45,5,6,3,2,1]
for x in range(len (marks)):
    print(marks[x],x)
    


marks=[11,12,45,5,6,3,2,1]
for x in range(len (marks)):
    for y in range(len(marks)):
        print(marks[x],marks[y])




marks=[11,12,45,5,6,3,2,1]
for x in range(len(marks)):
    for y in range(len(marks)):
        if marks[x]<marks[y]:
            marks[x],marks[y]=marks[y],marks[x]
        else:
            marks[y],marks[x]=marks[y],marks[x]
#ascending order
print(marks)




marks=[11,12,45,5,6,3,2,1]
for x in range(len(marks)):
    for y in range(len(marks)):
        if marks[x]<marks[y]:
            marks[x],marks[y]=marks[y],marks[x]
        else:
            marks[y],marks[x]=marks[y],marks[x]
#ascending order
print(marks[0]+marks[-1])



marks=[11,12,45,5,6,3,2,1]
for x in range(len(marks)):
    for y in range(len(marks)):
        if marks[x]<marks[y]:
            marks[x],marks[y]=marks[y],marks[x]
        else:
            marks[y],marks[x]=marks[y],marks[x]
print(marks,(len(marks)/2))



marks=[11,12,45,5,6,3,2,1]
for x in range(len(marks)):
    for y in range(len(marks)):
        if marks[x]<marks[y]:
            marks[x],marks[y]=marks[y],marks[x]
        else:
            marks[y],marks[x]=marks[y],marks[x]
print(marks[len(marks)//2])


