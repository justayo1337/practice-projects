def arithmetic_arranger(problems,*args):
    Lproblems=len(problems)
    if args[0]==True:
        changedList=[]
        for i in problems:
            a=i.split()
            changedList.append(a)
            #arranged_problems=0
        currentPosition=0
        while currentPosition!=3:
            value=""
            spacingMain="     "
            
            for i in range(Lproblems):
                variableSpacing=" "
                if currentPosition==1:
                    if abs(len(changedList[i][0])-len(changedList[i][2]))==0:
                        variableSpacing*=6
                    elif (len(changedList[i][0])-len(changedList[i][2]))==1:
                        variableSpacing=spacingMain+"  "
                    elif (len(changedList[i][0])-len(changedList[i][2]))==2:
                        variableSpacing=spacingMain+"   "
                    elif (len(changedList[i][0])-len(changedList[i][2]))==3:
                        variableSpacing=spacingMain+"    "
                    elif (len(changedList[i][0])-len(changedList[i][2]))==-1:
                        variableSpacing*=3
                    elif (len(changedList[i][0])-len(changedList[i][2]))==-2:
                        variableSpacing*=4
                    elif (len(changedList[i][0])-len(changedList[i][2]))==-3:
                        variableSpacing*=5
                    if i>0:
                            value+=spacingMain+ changedList[i][currentPosition] +variableSpacing+ changedList[i][currentPosition+1]
                    else:
                        value+=changedList[i][currentPosition] + spacingMain + changedList[i][currentPosition+1]
                    
                elif currentPosition==0:
                    value+="     "+changedList[i][currentPosition]+variableSpacing
            currentPosition+=1
            print(value)
    
        print(changedList)
    
    



arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)