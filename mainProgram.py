import pandas as pd
data = pd.read_csv('workoutlist3.csv', index_col=0)
import csv
import random
#print(data.head(10))

#new_data = data.loc[data['Body part'] == "CHEST EXERCISES"]
#data = data.reset_index(drop=True, inplace = True)
#new_data.reset_index(drop=True, inplace=True)
#print(new_data)

#new_data = data.loc[data['Body part'] == "CHEST EXERCISES"]
#data.reset_index(drop=True, inplace = True)
#1print(new_data)

#print(data.iloc[0,1])
#global sets
#global reps

workoutList = []
'''new_data = data.loc[data['Body part'] == "BICEP EXERCISES"]
w1 = new_data.iloc[1,0]
w2 = new_data.iloc[1,1]
workoutList.append([w1,w2])
w1 = new_data.iloc[2,0]
w2 = new_data.iloc[2,1]
workoutList.append([w1,w2])
print(workoutList)
'''


def mainmenu():
    while True:
        #print("What would you like to do?\nA. Find certain exercises\nB. Create a random workout\nC. Quit")
        answer = int(input("What would you like to do?\n1. Find certain exercises\n2. Create a workout\n3. Quit\n"))
        #answer = answer.capitalize()
        #print(answer)
        if answer == 1:
            option1()

        elif answer == 2:
            option2()
            
        elif answer == 3:
            print("QUITTING PROGRAM")
            exit()
            
        else:
            print("INVALID OPTION")
            break
def option1():
    while True:
            #print("Which body part exercises are you looking for?\nCHEST\nSHOULDER\nBICEP\nTRICEP\nLEGS\nBACK\nGLUTES\nABS\nCALVES\nFOREARM FLEXOR\nFOREARM EXTENSOR\nCARDIO")
            filter = int(input("\nWhich body part exercises are you looking for?\n1.CHEST\n2.SHOULDER\n3.BICEP\n4.TRICEP\n5.LEGS\n6.BACK\n7.GLUTES\n8.ABS\n9.CALVES\n10.FOREARM FLEXOR\n11.FOREARM EXTENSOR\n12.CARDIO\n13.RETURN TO MAIN MENU\n14.QUIT\n"))
                    
                    
            if (filter == 1):
                new_data = data.loc[data['Body part'] == "CHEST EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                print(new_data)
                            
            elif(filter == 2):
                new_data = data.loc[data['Body part'] == "SHOULDER EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                print(new_data)
                    
            elif(filter == 3):
                new_data = data.loc[data['Body part'] == "BICEP EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                print(new_data)
            elif(filter == 4):
                new_data = data.loc[data['Body part'] == "TRICEPS EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                print(new_data)
            elif(filter == 5):
                new_data = data.loc[data['Body part'] == "LEG EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                print(new_data)
            elif(filter == 6):
                new_data = data.loc[data['Body part'] == "BACK EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                print(new_data)
            elif(filter == 7):
                new_data = data.loc[data['Body part'] == "GLUTE EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                print(new_data)
            elif(filter == 8):
                new_data = data.loc[data['Body part'] == "AB EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                print(new_data)
            elif(filter == 9):
                new_data = data.loc[data['Body part'] == "CALVES EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                print(new_data)
            elif(filter == 10):
                new_data = data.loc[data['Body part'] == "FOREARM FLEXORS & GRIP EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                print(new_data)
            elif(filter == 11):
                new_data = data.loc[data['Body part'] == "FOREARM EXTENSOR EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                print(new_data)
            elif(filter == 12):
                new_data = data.loc[data['Body part'] == "CARDIO EXERCISES & EQUIPMENT"]
                new_data.reset_index(drop=True, inplace = True)
                print(new_data)
            elif(filter == 13):
                mainmenu()
            elif(filter == 14):
                print("EXITTING PROGRAM")
                exit()

            else:
                print("INVALID INPUT")
                continue

def option2():
    #int(input("What split would you like to hit?\n1.CHEST/BACK\n2.ARMS\n3.LEGS\n4.RETURN TO MAIN MENU\n5.QUIT"))
    while True:
        filter2 = int(input("Create a workout\n1.Custom workout\n2.Split options\n"))
        match filter2:
            case 1:
                global path1
                path1 = 1
                option3()
                #op4?
                
            case 2:
                path1 = 2
                option3()

            case _:
                print("INVALID OPTION")
                continue

        
def option3():
    while True:
        filter3 = int(input("What is your goal?\n1.Stength\n2.Hypertrophy\n3.BACK\n"))
        match filter3:
            case 1:
                global reps
                global sets
                reps =  "1-5"
                sets = "3-4"
                if path1 == 1:
                    option5()
                else:
                    option10()
                
            case 2:
                
                reps =  "8-12"
                sets = "3-4"
                if path1 == 1:
                    option5()
                else:
                    option10()
                
            case 3:
                break

            case _:
                print("INVALID INPUT")
                continue

def option4():
        while True:
            filter4 = int(input(""))

def option5():
    while True:
        filter5 = int(input("What split would you like to hit?\n1.CHEST/BACK\n2.ARMS\n3.LEGS\n4.Others\n5.RETURN TO MAIN MENU\n6.QUIT\n"))
        match filter5:
            case 1:
                option6()

            case 2:
                option7()
            case 3:
                option8()
            case 4:
                option9()
            case 5:
                break
            case 6:
                exit()

def option6():
    while True:
        filter6 = int(input("Which muscle exercise would you like to add?\n1.Chest\n2.Back\n3.Show workout\n4.Back\n"))
        match filter6:
            case 1:
                new_data = data.loc[data['Body part'] == "CHEST EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                num = random.randint(0,(len(new_data)-1))    
                while True:
                    try:
                        w1 = new_data.iloc[num,1]
                        if w1 not in workoutList:
                            workoutList.append(w1)
                            break
                    except:
                        print("Error getting exercise")
                        break

                
            case 2:
                new_data = data.loc[data['Body part'] == "BACK EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                num = random.randint(0,(len(new_data)-1))    
                w1 = new_data.iloc[num,1]
                if w1 not in workoutList:
                    workoutList.append(w1)
            case 3:
                print1()
                
            case 4:
                break
                
                    #print(exercise)
                    #obj1 = enumerate(workoutList)
                    #a = sets + " " list(obj1) + " of " + reps + " reps\n"
                #for i in range(0, (len(workoutList)-1)):
                    #a = sets + " " workoutList[i] + " of " + reps + " reps\n"
                    #print(workoutList[i])


                
                #print(a)
        #ew_data = data['Exercise']
        #for index, row in new_data.iterrows():
        
        #print(new_data.sample())
def option7():
    while True:
        filter6 = int(input("Which muscle exercise would you like to add?\n1.Shoulder\n2.Bicep\n3.Triceps\n4.Forearms\n5.Show workout\n6.Back\n"))
        match filter6:
            case 1:
                new_data = data.loc[data['Body part'] == "SHOULDER EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                num = random.randint(0,(len(new_data)-1))    
                while True:
                    try:
                        w1 = new_data.iloc[num,1]
                        if w1 not in workoutList:
                            workoutList.append(w1)
                            break
                    except:
                        print("Error getting exercise")
                        break
                
            case 2:
                new_data = data.loc[data['Body part'] == "BICEP EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                num = random.randint(0,(len(new_data)-1))    
                w1 = new_data.iloc[num,1]
                if w1 not in workoutList:
                    workoutList.append(w1)
            case 3:
                new_data = data.loc[data['Body part'] == "TRICEPS EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                num = random.randint(0,(len(new_data)-1))    
                w1 = new_data.iloc[num,1]
                if w1 not in workoutList:
                    workoutList.append(w1)

                    #FOREARM FLEXORS & GRIP EXERCISES
            case 4: 
                new_data = data.loc[(data['Body part'] == "FOREARM FLEXORS & GRIP EXERCISES") | (data["Body part"] == "FOREARM EXTENSOR EXERCISES")]
                new_data.reset_index(drop=True, inplace = True)
                num = random.randint(0,(len(new_data)-1))    
                w1 = new_data.iloc[num,1]
                if w1 not in workoutList:
                    workoutList.append(w1)

            case 5:
                print1()
                
            case 6:
                break   

def option8():
    while True:
            
            filter8 = int(input("Which muscle exercise would you like to add?\n1.Quads\n2.Calves\n3.Glutes\n4.Show workout\n5.Back\n"))
            match filter8:
                    case 1:
                        new_data = data.loc[data['Body part'] == "LEG EXERCISES"]
                        new_data.reset_index(drop=True, inplace = True)
                        num = random.randint(0,(len(new_data)-1))
                        w1 = new_data.iloc[num,1]
                        #for workout in workoutList:
                        #    if w1 not in workoutList:
                        #        workoutList.append(w1)   
                        while True:
                            try:
                                w1 = new_data.iloc[num,1]
                                if w1 not in workoutList:
                                    workoutList.append(w1)
                                    break
                            except:
                                print("Error getting exercise")
                                break 
                        '''while True:
                            try:
                                w1 = new_data.iloc[num,1]
                                if w1 not in workoutList:
                                    workoutList.append(w1)
                                    break
                            except:
                                print("Error getting exercise")
                                break'''
                    #case 2:
                    #    new_data = data.loc[data['Body part'] == "CHEST EXERCISES"]
                    #    new_data.reset_index(drop=True, inplace = True)
                    #    num = random.randint(0,(len(new_data)-1))  
                    #    w1 = new_data.iloc[num,1]  
                        
                        
                        '''
                        while True:
                            try:
                                w1 = new_data.iloc[num,1]
                                if w1 not in workoutList:
                                    workoutList.append(w1)
                                    break
                            except:
                                print("Error getting exercise")
                                break'''
                        '''if w1 not in workoutList:
                            workoutList.append(w1)
                            break
                        while w1 in workoutList:
                            num = random.randint(0,(len(new_data)-1))
                            w1 = new_data.iloc[num,1]
                            break'''
                        #not sure what to do here once i get to the last one im stuck in a permanent loop
                        
                            



                    case 2:
                        new_data = data.loc[data['Body part'] == "CALVES EXERCISES"]
                        new_data.reset_index(drop=True, inplace = True)
                        num = random.randint(0,(len(new_data)-1))    
                        while True:
                            try:
                                w1 = new_data.iloc[num,1]
                                if w1 not in workoutList:
                                    workoutList.append(w1)
                                    break
                            except:
                                print("Error getting exercise")
                                break
                    case 3:
                        new_data = data.loc[data['Body part'] == "GLUTE EXERCISES"]
                        new_data.reset_index(drop=True, inplace = True)
                        num = random.randint(0,(len(new_data)-1))    
                        while True:
                            try:
                                w1 = new_data.iloc[num,1]
                                if w1 not in workoutList:
                                    workoutList.append(w1)
                                    break
                            except:
                                print("Error getting exercise")
                                break
                    
                        
                    case 4:
                        print1()

                    case 5:
                        break
                        
def option9():
        while True:
            filter9 = int(input("Which muscle exercise would you like to add?\n1.Abs\n2.Cardio\n3.Show workout\n4.Back\n"))
            match filter9:
                case 1:
                    new_data = data.loc[data['Body part'] == "AB EXERCISES"]
                    new_data.reset_index(drop=True, inplace = True)
                    num = random.randint(0,(len(new_data)-1))
                    w1 = new_data.iloc[num,1]
                    #for workout in workoutList:
                    #    if w1 not in workoutList:
                    #        workoutList.append(w1)
                    while True:
                            try:
                                w1 = new_data.iloc[num,1]
                                if w1 not in workoutList:
                                    workoutList.append(w1)
                                    break
                            except:
                                print("Error getting exercise")
                                break    

                case 2:
                    new_data = data.loc[data['Body part'] == "CARDIO EXERCISES & EQUIPMENT"]
                    new_data.reset_index(drop=True, inplace = True)
                    num = random.randint(0,(len(new_data)-1))
                    w1 = new_data.iloc[num,1]
                    #for workout in workoutList:
                    #    if w1 not in workoutList:
                    #        workoutList.append(w1)
                    while True:
                            try:
                                w1 = new_data.iloc[num,1]
                                if w1 not in workoutList:
                                    workoutList.append(w1)
                                    break
                            except:
                                print("Error getting exercise")
                                break
                case 3:
                    print1()
                    
                case 4:
                    break    

def option10():
    while True:
        filter10 = int(input("What premade split would you like to follow?\n1.Chest/Back\n2.Arms\n3.Legs\n4.Show Exercises\n5.EXIT\n"))
        match filter10:
            case 1:
                option11()
            case 2:
                option12()
                return
            case 3:
                #option13()
                return
            case 4:
                print1()
            case 5:
                break

def option11():
    filter11 = int(input("How many sets of each work out would you like? (Ex. 3 = 3 sets of chest and 3 sets of back)\n"))
    while True:
        for i in range(0,filter11):
                try:
                    new_data = data.loc[data['Body part'] == "CHEST EXERCISES"]
                    new_data.reset_index(drop=True, inplace = True)
                    num = random.randint(0,(len(new_data)-1))
                    w1 = new_data.iloc[num,1]
                    w2 = new_data.iloc[num,0]
                    #w1 = new_data.iloc[num,1]
                    if w1 not in workoutList:
                        workoutList.append([w2,w1])               
                except:
                    print("Error getting exercise")
                    break  
        for i in range(0,filter11):
                try:
                    new_data = data.loc[data['Body part'] == "BACK EXERCISES"]
                    new_data.reset_index(drop=True, inplace = True)
                    num = random.randint(0,(len(new_data)-1))
                    #w1 = new_data.iloc[num,1]
                    #w1 = new_data.iloc[num,1]
                    #if w1 not in workoutList:
                    #    workoutList.append(w1)
                    w1 = new_data.iloc[num,1]
                    w2 = new_data.iloc[num,0]
                    #w1 = new_data.iloc[num,1]
                    if w1 not in workoutList:
                        workoutList.append([w2,w1])
                except:
                    print("Error getting exercise")
                    break
        if(filter11 > 0):
            break
        else:
            option11()
                
    
                
        

        
def option12():
    
    filter12 = int(input("How many sets of each work out would you like? (Arm split is made up of bicep/tricep/forearms/shoulder)\n"))
    while True:
        for i in range(0,filter12):
            try:
                new_data = data.loc[data['Body part'] == "BICEP EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                num = random.randint(0,(len(new_data)-1))
                w1 = new_data.iloc[num,1]
                if w1 not in workoutList:
                    workoutList.append(w1)
                new_data = data.loc[data['Body part'] == "TRICEPS EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                num = random.randint(0,(len(new_data)-1))
                w1 = new_data.iloc[num,1]
                if w1 not in workoutList:
                    workoutList.append(w1)
                new_data = data.loc[data['Body part'] == "SHOULDER EXERCISES"]
                new_data.reset_index(drop=True, inplace = True)
                num = random.randint(0,(len(new_data)-1))
                w1 = new_data.iloc[num,1]
                if w1 not in workoutList:
                    workoutList.append(w1)
                new_data = data.loc[(data['Body part'] == "FOREARM FLEXORS & GRIP EXERCISES") | (data["Body part"] == "FOREARM EXTENSOR EXERCISES")]
                new_data.reset_index(drop=True, inplace = True)
                num = random.randint(0,(len(new_data)-1))    
                w1 = new_data.iloc[num,1]
                if w1 not in workoutList:
                    workoutList.append(w1)
                
            except:
                print("Error getting exercise")
                break
        
    
        option10()

def print1():
    for exercise in workoutList:
            a = exercise[0] + ":" + sets + " " + exercise[1] + " of " + reps + " reps\n"                            
            print(a)

#def append():


                


                        

            
        




mainmenu()