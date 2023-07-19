'''import csv

header=['rno', 'name', 'marks']
rows=[
        ["1","kavya","78"],
        ["2", "Varun", "99"]
     ] 

with open("book.csv", "w", newline='') as f:
        wr=csv.writer(f)
        wr.writerow(header)
        wr.writerows(rows)
        
with open("book.csv", "r") as f:
        rd=csv.reader(f)
        for row in rd:
                print(row)   '''





'''with open("emp.csv", "w", newline='') as f:
      w=csv.writer(f)
      w.writerow(["EMP NO","EMP NAME","EMP SAL","EMP ADDR"])
      n=int(input("Enter Number of Employees:"))
      for i in range(n):
             eno=input("Enter Employee No:")
             ename=input("Enter Employee Name:")
             esal=input("Enter Employee Salary:")
             eaddr=input("Enter Employee Address:")
             w.writerow([eno, ename, esal, eaddr])
print("Total Employees data written to csv file successfully")

with open('emp.csv', 'r') as f:
         csv_reader = csv.reader(f)
         for row in csv_reader:
                 print(row)'''



'''with open("cricket.csv", 'w', newline='') as f:
        w=csv.writer(f)
        w.writerow(['name', 'runs', 'team'])
        n=int(input("Enter the no of players: "))

        for i in range(n):
                name=input("Enter the name: ")
                runs=int(input("Enter the runs: "))
                team=input("Enter the team name: ")
                w.writerow([name,runs,team])


with open("cricket.csv", 'r') as f:
        r=csv.reader(f)
        for row in r:
                print(row)'''
                
                
        






















        
        

