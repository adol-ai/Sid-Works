
def findWaitingTime(processes,n,bt,wt,quantum):
    rem_bt=[0]*n

    for i in range(n):
        rem_bt[i]=bt[i]
    t=0
    while True:
        done=True
        for j in range(n):
            if rem_bt[j]>0:
                done=False

                if rem_bt[j]>quantum:
                    t+=quantum
                    rem_bt[j]-=quantum
                else:
                    t+=rem_bt[j]
                    wt[j]=t-rem_bt[j]
                    rem_bt[j]=0
        if done==True:
            break
        
def findTurnAroundTime(processes,n,bt,wt,tat):
    for i in range(n):
        tat[i]=bt[i]+wt[i]

def findAvgTime(processes,n,bt,quantum):
    wt=[0]*n
    tat=[0]*n
    
    findWaitingTime(processes,n,bt,wt,quantum)

    findTurnAroundTime(processes,n,bt,wt,tat)

    print("Processes \t Burst Time \t Waiting Time \t Turn-Around Time")
    total_bt=0
    total_wt=0
    for i in range(n):
        total_bt+=bt[i]
        total_wt+=wt[i]
        print("  ",i+1,"\t\t", bt[i],"\t\t",wt[i],"\t\t",tat[i])

    print("Avg Waiting Time: ",total_wt/n)
    print("Avg Burst Time: ",total_bt/n)


#main
process=[1,2,3,4]
n=4
bt=[5,7,8,6]
quantum=3

findAvgTime(process,n,bt,quantum)
