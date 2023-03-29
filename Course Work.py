#part 1-Main Version
count=0
total=120
progress=0
module_trailer=0
Exclude=0
module_retriever=0
marks=[0,20,40,60,80,100,120]
progress_array=[] 
module_trailer_array=[]
module_retriever_array=[]
Exclude_array=[]
file=open("myfile.txt","w")
try:
    Pass=int(input("Please enter your credits at pass: "))
    while Pass not in marks:
        print("Out of range")
        Pass=int(input("Please enter your credits at pass: "))
    defer=int(input("Please enter your credits at defer: "))
    while defer not in marks:
        print("Out of range")
        defer=int(input("Please enter your credits at defer: ")) 
    fail= int(input("Please enter your credits at fail: "))
    while fail not in marks:
        print("Out of range")
        fail= int(input("Please enter your credits at fail: "))
    total=120
    t=(Pass+defer+fail)
    if t!=total:
        print("Total incorret")
    else:
        if Pass==120:
            print("Progress")
            progress=progress+1
            progress_array.append([Pass,defer,fail])
        elif Pass>=100:
            print("progress(module trailer)")
            module_trailer=module_trailer+1
            module_trailer_array.append([Pass,defer,fail])
        elif Pass<=40 and fail>=80:
            print("Exclude")
            Exclude=Exclude+1
            Exclude_array.append([Pass,defer,fail])
        else:
            print("module retriever")
            module_retriever=module_retriever+1
            module_retriever_array.append([Pass,defer,fail])
except ValueError:
    print("integer required")
print(" ")
new=input('''Would you like to enter another set of data?
Enter "y" for yes or "q" to quit and view results: ''')
new_set=new.lower()
while new=="y":
    print(" ")
    count=count+1
    try:
        Pass=int(input("Please enter your credits at pass: "))
        while Pass not in marks:
            print("Out of range")
            Pass=int(input("Please enter your credits at pass: "))
        defer=int(input("Please enter your credits at defer: "))
        while defer not in marks:
            print("Out of range")
            defer=int(input("Please enter your credits at defer: ")) 
        fail= int(input("Please enter your credits at fail: "))
        while fail not in marks:
            print("Out of range")
            fail= int(input("Please enter your credits at fail: "))
        total=120
        t=(Pass+defer+fail)
        if t!=total:
            print("Total incorret")
            print(" ")
        else:
            if Pass==120:
                print("Progress")
                progress=progress+1
                progress_array.append([Pass,defer,fail]) 
            elif Pass>=100:
                print("progress(module trailer)")
                module_trailer=module_trailer+1
                module_trailer_array.append([Pass,defer,fail]) 
            elif Pass<=40 and fail>=80:
                print("Exclude")
                Exclude=Exclude+1
                Exclude_array.append([Pass,defer,fail]) 
            else:
                print("module retriever")
                module_retriever=module_retriever+1
                module_retriever_array.append([Pass,defer,fail])
    except ValueError:
         print("integer required")
         print("  ")
    new=input('''Would you like to enter another set of data?
Enter "y" for yes or "q" to quit and view results: ''')
    new_set=new.lower()    
if new=="q":                                             
    print('''------------------------------------------
Horizontal Histrogram''')
print("progress        :",progress,"*"*progress)
print("module trailer  :",module_trailer,"*"*module_trailer)
print("Exclude         :",Exclude,"*"*Exclude)
print("module retriever:",module_retriever,"*"*module_retriever)
total_all=(progress+module_trailer+module_retriever+Exclude)
print(" ")
print(total_all,"outcomes in total")
print('''--------------------------------------------
                                                          ''')
#Part 2- Vertical Histrogram
print("progress    module trailer       Exclude        module retriever")
while True:
    if progress>0:
        print(f'{"*":>2}\n',end=" ") 
        progress=progress-1
    else:
        print(f'{" ":>2}\n',end=" ")
    if module_trailer>0:
        print(f'{"*":>18}\n',end=" ")
        module_trailer=module_trailer-1
    else:
        print(f'{" ":>18}\n',end=" ") 
    if Exclude>0:
        print(f'{"*":>35}\n',end=" ")
        Exclude=Exclude-1
    else:
        print(f'{" ":>35}\n',end=" ") 
    if module_retriever>0:
        print(f'{"*":>50}\n',end=" ")
        module_retriever=module_retriever-1
    else:
        print(f'{" ":>50}\n',end=" ")
    if(progress or module_trailer or Exclude or module_retriever)==0:
        break
# Part 3-List/Tuple/Directory and Part 4-Test File
for i in progress_array:
    print("progress:",i)
    content="progress:"+str(i)+"\n"
    file.write(content) 
for i in module_trailer_array:
    print("module trailer:",i)
    content="module trailer:"+str(i)+"\n"
    file.write(content)
for i in Exclude_array:
    print("Exclude:",i)
    content="Exclude:"+str(i)+"\n"
    file.write(content)           
for i in module_retriever_array:
    print("module retriever:",i)
    content="module retriever:"+str(i)+"\n"
    file.write(content)
file.close()
