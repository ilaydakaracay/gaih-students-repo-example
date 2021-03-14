d = {"Name and Surname":[], "Midterm":[],"Final":[],"Project":[],"Passing grade":[]}
list54 = ""
for i in range(5):
     print("Name and Surname? ")
     name = input()
     d["Name and Surname"].append(name)
     print("Midterm score? ")
     midterm = float(input())
     d["Midterm"].append(midterm)
     print("Final score? ")
     final = float(input())
     d["Final"].append(final)
     print("Project score? ")
     project = float(input())
     d["Project"].append(project)
     finalgrade = (0.3 * midterm) + (0.3 * project) + (0.4 * final)
     d["Passing grade"].append(finalgrade)
for k,v in d.items():
    if (k=="Passing grade"):
        list54 = v
list54.sort()
mylist = list54[::-1]
print(mylist)






