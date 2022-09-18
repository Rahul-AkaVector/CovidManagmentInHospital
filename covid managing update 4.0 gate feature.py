def trials():
    print("Admin:program")
    print("Gate:records")

from datetime import datetime
def dateandtime():
    now=datetime.now()
    return now

import random
import string
def randomid():
    return ''.join(random.choice(string.digits) for _ in range(10))

#Covid 19 Management in a hospital
from datetime import date
print("**************************************************************************************************************")
print("**                                                                                                                                                               **")
print("**               C    O    V    I    D                1    9                   M    A    N    G    E    M     E    N    T                   ")
print("**                                                                                                                                                               **")
print("**************************************************************************************************************")

#temperory
print("==============================================================================================")
print("to check the passwords select an option 4 and then type ' trials() ' and rerun the program ")
#remove upper two lines 
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="0000")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists covid19_management ")
mycursor.execute("use covid19_management ")
mycursor.execute("create table if not exists staff(staffid varchar(25) not null ,sno varchar(25) not null ,age varchar (25) not null, gender char (1) not null , post varchar (25) not null, specialist varchar(25) not null , dob date not null , adhar_no varchar(15) not null ,address varchar(100) not null , phone varchar(10) , salary varchar (25) not null)")
mycursor.execute("create table if not exists patients(patientid varchar(25) not null ,sno varchar(25) not null ,age varchar (25) not null, gender char (1) not null , weight varchar(6) not null ,height varchar(6) not null ,address varchar(100) not null ,phone varchar(10) not null , c19_conf_date date not null)")
mycursor.execute("create table if not exists login(admin varchar (25) not null, password varchar(25) not null)")
mycursor.execute("create table if not exists login1(admin varchar (25) not null, password varchar(25) not null)")
mycursor.execute("create table if not exists sno(patients varchar (25) not null, staff varchar(25) not null)")
mycursor.execute("create table if not exists Watchman_records(Entry_token varchar(10), Entry_mode varchar(25) not null , vehical_no varchar(12) , name varchar(25) not null,Entry_date_and_time datetime not null, exit_date_and_time datetime)")
mycursor.execute("select * from sno")
z=0
for i in mycursor:
    z=1
if z==0:
    mycursor.execute("insert into sno values('0','0')")
mydb.commit()
#===========================================================
j=0
mycursor.execute("select * from login")

for i in mycursor:
    j=1
if (j==0):
    mycursor .execute("insert into login values('Admin','program')")
    mydb.commit()
#==========================================================
j=0
mycursor.execute("select * from login1")
for i in mycursor:
    j=1
if (j==0):
    mycursor .execute("insert into login1 values('watchman','records')")
    mydb.commit()
#=======================================================
loop1='y'
while (loop1=='y' or loop1=='Y'):
    print("==============================================================")
    print("1.Admin")
    print("2.Patient")
    print("3.Gate")
    print("4.Exit")
    print("==============================================================")
    ch1=input("enter your choice:")
    if ch1.isdigit() and len(ch1)==1:
        if (ch1=='1'):
            pas=input("enter your password:  ")
            mycursor.execute("select * from login")
            for i in mycursor :
                username,password=i
            if (pas==password):
                loop2='n'
                while (loop2=='n' or loop2=='N'):
                    print("======================================================")
                    print("1.Add patients")
                    print("2.Add staff")
                    print("3.Display patients Record")
                    print("4.Display staff record")
                    print("5.Change password")
                    print("6.Rempove patients ")
                    print("7.Remove Staff")
                    print("8.Logout")
                    print("======================================================")
                    ch2=input("Enter your choice :")
                    if (ch2=='1'):
                        loop3='y'
                        while (loop3=='y' or loop3=='Y'):
                            patientid=randomid()
                            name=input("Enter patients name :")
                            age=input("Enter Patients Age ")
                            gender=input("Enter patients gender:")
                            weight=input("Enter weight in kgs : ")
                            height=input("Enter height in cms : ")
                            address=input("Enter address (address/city/state): ")
                            phone=input("Enter phone no : ")
                            date=input("Enter date of confirmation of covid: ")
                            mycursor.execute("select * from sno") #[patients,staff]
                            for i in mycursor:
                                patient,staff=i
                                patient=int(patient)+1
                            string="insert into patients values("+"'"+str(patientid)+"'"+","+"'"+str(name)+"'"+","+"'"+str(age)+"'"+","+"'"+str(gender)+"'"+","+"'"+str(weight)+"'"+","+"'"+str(height)+"'"+","+"'"+str(address)+"'"+","+"'"+str(phone)+"'"+","+"'"+str(date)+"'"+")"
                            mycursor.execute(string)
                            mycursor.execute("update sno set patients=' "+str(patient)+" ' ")
                            mydb.commit()
                            print("Data of patient has been save succesfully ................")
                            mycursor.execute("select * from patients")
                            t=0
                            for i in mycursor:
                                t+=1
                                patientid1,name1,age1,gender1,weight1,height1,address1,phone1,date1=i
                            print("==========================================================")
                            print(f"Total number of infected patients ------>>>>{patient}")
                            print("==========================================================")
                            print(f"Active cases------------------>>>>>>>>>>>>>>>>{t}")
                            print("==========================================================")
                            print(f"This patient with {patientid1} will be in quarantine upto 14 days from {date1}")
                            print("==========================================================")
                            loop3=input("Do you want to enter more Data  of more patients (y/n):   ")
                            print("==========================================================")
                        loop2=input("Do you Want to Logout(y/n):  ")
                    elif(ch2=='2'):
                        loop3="y"
                        while (loop3=='y' or loop3 =='Y'):
                             name=input("Enter new staff name: ")
                             age=input("Enter age :  ")
                             gender=input("Enter gender (m/f):  ")
                             post=input("Enter (His/Her) post:  ")
                             salary= input("Enter (His/Her) Salary:  ")
                             staffid=randomid()
                             specialist=input("Enter staff specialist :  ")
                             dob=input("Enter date of birth : ")
                             aadhar_no=input("Enter adhar car no [for security reason]: ")
                             address=input("Enter Address : ")
                             phone=input("Enter phone no : ")
                             
                             mycursor.execute("select * from sno")
                             for i in mycursor:
                                 patient,staff=i
                                 staff=int(staff)+1
                                 
                             string1="insert into staff values ('"+staffid+"','"+name+"','"+age+"','"+gender+"','"+post+"','"+specialist+"','"+dob+"','"+aadhar_no+"','"+address+"','"+phone+"','"+salary+"')"
                             mycursor.execute(string1)
                             mycursor.execute("update sno set staff=' " + str(staff)+"'")
                             mydb.commit()
                             print("=====================================================================")
                             print(f"The staff with staff id  {staffid} has ben saved successfully.........")
                             print("=====================================================================")
                             mycursor.execute("select * from staff")
                             t=0
                             for i in mycursor:
                                 t+=1
                             print(f"Active Staff Members  ---->>>{t}")
                             print("====================================================================")
                             loop3=input("Do you want to enter more staff Data (y/n): ")
                             print("====================================================================")
                        loop2=input("Do u want to logout (y/n): ")
                    elif(ch2=='3'):
                        idd=input("Enter patients id : ")
                        patientid2,name2,age2,gender2,weight2,height2,address,phone2,date2=["","","","","","","","",""]
                        mycursor.execute("select * from patients where patientid='"+idd+"'")
                        for i in mycursor:
                            patientid2,name2,age2,gender2,weight2,height2,address,phone2,date2=i
                        if patientid2=="":
                            print("Sorry sir / maam u had entered wrong patients id . Please check again !! ")
                        else:
                            print("| NAME | AGE | GENDER | CORONA POSITIVE DATE |")
                            print(f"| {name2} | {age2} | {gender2} | {date2}|")
                    elif(ch2=='4'):#working here
                        idd = input("Enter staff id : ")
                        staffid3,name3, age3, gender3,post3, specialist3,dob3,adhar3,address3,phone3,salary3= ["", "", "","","","","","","","",""]
                        mycursor.execute("select * from staff where staffid='" +idd+"'")
                        for i in mycursor:
                            staffid3,name3,age3,gender3,post3,specialist3,dob3,adhar3,address3,phone3,salary3 = i
                        if staffid3=="":
                            print("Sorry sir / maam u had entered wrong staff id . Please check again !!")
                        else:
                            print("|            NAME           |      AGE        |     GENDER      |          POST        |        SALARY         |")
                            print(f"| {name3} | {age3} | {gender3} | {post3}| |{salary3}")
                    elif (ch2=='5'):
                        pas=input("Enter Old Password: ")
                        mycursor.execute("select * from login")
                        for i in mycursor:
                            username,passwordd=i
                        if (pas==password):
                            npas=input("Enter New Password: ")
                            mycursor.execute("update login set password='"+npas+"'")
                            mydb.commit()
                        else:
                            print("Old password is wrong......")
                    elif(ch2=='6'):
                        loop3='y'
                        while (loop3=='y' or loop3=='Y'):
                            idd=input("Enter patient id: ")
                            mycursor.execute("delete from patients where patientid='"+idd+"'")
                            mydb.commit()
                            print("Patient has been removed succesfully")
                            loop3=input("Do you want to remove more patients (y/n): ")

                    elif(ch2=='7'):
                        loop3='y'
                        while(loop3=='y' or loop3=='Y'):
                            idd=input("Enter Staff id: ")
                            mycursor.execute("delete from staff where sno='"+idd+"'")
                            mydb.commit()
                            print("Staff has been removed succesfully....")
                            loop3=input("Do you want to remove more staff (y/n): ")
                    elif(ch2=='8'):
                        break
                    else:
                        print("Please enter correct choice ")
            else:
                print("Sorry your password is incorrect , please enter again .....")
        elif(ch1=='2'):
            print("Thank you for coming forward for your test .....")
            icough=input("Are you feeling cough?(y/n): ").lower()
            dry_cough='n'
            cough='n'
            if (icough=='y' or icough=='Y'):
                dry_cough=input("Are you feeling dry cough (y/n): ").lower()
                cough = input("Are you feeling normal cough (y/n): ").lower()

            sneeze=input("Are you feeling sneeze? (y/n): ")
            pain=input("Are you feeling pain in your body? (y/n): ")
            weakness=input("Are you feeling weakness? (y/n)")
            mucus=input("Are you feeling any mucus? (y/n): ")
            itemp=int(input("Please enter your body temperature : "))
            if(itemp<=100):
                temp='low'
            else:
                temp='high'
            breath=input("Are you having difficulty un breathing? (y/n)").lower()
            if (dry_cough=='y'and sneeze=='y'and weakness=='y' and temp=='high' and breath=='y'):
                print("sorry to say that but according to our research and knowledge u are suffering from corona ....")
                patientid=randomid()
                name=input("Enter your name : ")
                age=input("enter your age :")
                gender = input("Enter your gender (m/f): ")
                address=input("Enter you Adress: ")
                phone=input("Enter Your Mobile: ")
                weight=input("Enter Your weight : ")
                height=input("Enter your height: ")
                date1=str(date.today())
                date=date1.replace('-',"")
                mycursor.execute("select * from sno")
                for i in mycursor:
                    patient,staff=i
                    patient=int(patient)+1
                string5="insert into patients values("+"'"+str(patientid)+"'"+","+"'"+str(name)+"'"+","+"'"+str(age)+"'"+","+"'"+str(gender)+"'"+","+"'"+str(weight)+"'"+","+"'"+str(height)+"'"+","+"'"+str(address)+"'"+","+"'"+str(phone)+"'"+","+"'"+str(date)+"'"+")"
                mycursor.execute(string5)
                mycursor.execute("update sno set patients='"+str(patient)+"'")
                mydb.commit()
                print("Data of Patient has been saved succesfully....")
                print(f"Total number of Corona Infected Patients --> {patient}")
                mycursor.execute("select * from patients")
                
                mycursor.execute("select * from patients")
                for i in mycursor:
                    patientid5,name5,age5,gender5,weight5,height5,address5,phone5,date5=i
                print(f"This patient with id {patientid5} / {name5} will be in quaratine upto 14 days from {date5}")
            elif (dry_cough=='y' and sneeze=='y' and pain=='n' and weakness=='n' and temp=='low' and breath=='n'):
                print("Nothing to worry , its just due to Air Pollution .....")
            elif (cough=='y' and mucus=='y' and sneeze=='y' and pain=='n' and weakness=='n' and temp=='low' and breath=='n'):
                print("Nothing to worry , its just Common cold....")
            else:
                print("You are not corona infected , if u are feeling something wrong, you just need to rest.....")
                print("If then also you cant feel better , please consult to your doctor. ")
                #===============================================================================================================================================================================
        elif(ch1=='3'):
            pas=input("enter your password:  ")
            mycursor.execute("select * from login1")
            for i in mycursor :
                username,password=i
            if (pas==password):
                loop2='n'
                while (loop2=='n' or loop2=='N'):
                    print("======================================================")
                    print("1.Add Entry ")
                    print("2.Add Exit ")
                    print("3.Change password ")
                    print("4.Logout")
                    print("======================================================")
                    ch2=input("Enter your choice :")
                    if (ch2=='1'):
                        loop3='y'
                        while (loop3=='y' or loop3=='Y'):
                            mode=input("""Please select an entry mode :
1.    Walking
2.   One wheeler
3.   Two wheeler
4.   Three wheeler
5.   Four wheeler
6.   More than four wheeler like truck or others
7.   Hospital Ambulance
8.   Quit
: """)
                            if mode=="1":
                                mode="Walking"
                                token=randomid()
                                name=str(input("Please enter name of the person entrying: "))
                                number="null"
                                statement="insert into Watchman_records values ('"+str(token)+"','"+str(mode)+"','"+str(number)+"','"+str(name)+"','"+str(dateandtime())+"',"+"null"+")"
                                mycursor.execute(statement)
                                print("=====================================================================")
                                print(name, "his/her token id is", token)
                                print("=====================================================================")
                                loop3=input("Do you want to add more entries (y/n) :" )
                            elif mode=="2":
                                mode="One wheeler"
                                token=randomid()
                                name=input("Please enter name of driver: ")
                                loop='y'
                                while (loop=='y' or loop=='Y' or loop=='yes'):
                                    number=input("Please Enter vehicle number : ")
                                    if (len(number)<=10):
                                        statement="insert into Watchman_records values ('"+str(token)+"','"+str(mode)+"','"+str(number)+"','"+str(name)+"','"+str(dateandtime())+"',"+"null"+")"
                                        mycursor.execute(statement)
                                        print("=====================================================================")
                                        print(name, "his/her token id is", token)
                                        print("=====================================================================")
                                        loop='n'
                                        loop3=input("Do you want to add more entries (y/n) :" )
                                        
                                    else:
                                        print("Please check number plate again because the length of the character in number plate is too long...")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        print("Note : Entry will not be register if you didnt enter vehicle number ..... ")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        loop=input("Do you want to add vehicle number without changing his/her name:")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        if loop == "n" or loop=="no" or loop ==" N" :
                                            loop3=input("Do you want to add entries again (y/n) :" )

                            elif mode=="3":
                                mode="Two wheeler"
                                token=randomid()
                                name=input("Please enter name of driver: ")
                                loop='y'
                                while (loop=='y' or loop=='Y' or loop=='yes'):
                                    number=input("Please Enter vehicle number : ")
                                    if (len(number)<=10):
                                        statement="insert into Watchman_records values ('"+str(token)+"','"+str(mode)+"','"+str(number)+"','"+str(name)+"','"+str(dateandtime())+"',"+"null"+")"
                                        mycursor.execute(statement)
                                        print("=====================================================================")
                                        print(name, "his/her token id is", token)
                                        print("=====================================================================")
                                        loop='n'
                                        loop3=input("Do you want to add more entries (y/n) :" )
                                        
                                    else:
                                        print("Please check number plate again because the length of the character in number plate is too long...")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        print("Note : Entry will not be register if you didnt enter vehicle number ..... ")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        loop=input("Do you want to add vehicle number without changing his/her name:")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        if loop == "n" or loop=="no" or loop ==" N" :
                                            loop3=input("Do you want to add entries again (y/n) :" )
                            elif mode=="4":
                                mode="Three wheeler"
                                token=randomid()
                                name=input("Please enter name of driver: ")
                                loop='y'
                                while (loop=='y' or loop=='Y' or loop=='yes'):
                                    number=input("Please Enter vehicle number : ")
                                    if (len(number)<=10):
                                        statement="insert into Watchman_records values ('"+str(token)+"','"+str(mode)+"','"+str(number)+"','"+str(name)+"','"+str(dateandtime())+"',"+"null"+")"
                                        mycursor.execute(statement)
                                        print("=====================================================================")
                                        print(name, "his/her token id is", token)
                                        print("=====================================================================")
                                        loop='n'
                                        loop3=input("Do you want to add more entries (y/n) :" )
                                        
                                    else:
                                        print("Please check number plate again because the length of the character in number plate is too long...")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        print("Note : Entry will not be register if you didnt enter vehicle number ..... ")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        loop=input("Do you want to add vehicle number without changing his/her name:")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        if loop == "n" or loop=="no" or loop ==" N" :
                                            loop3=input("Do you want to add entries again (y/n) :" )

                            elif mode=="5":
                                mode="Four wheeler"
                                token=randomid()
                                name=input("Please enter name of driver: ")
                                loop='y'
                                while (loop=='y' or loop=='Y' or loop=='yes'):
                                    number=input("Please Enter vehicle number : ")
                                    if (len(number)<=10):
                                        statement="insert into Watchman_records values ('"+str(token)+"','"+str(mode)+"','"+str(number)+"','"+str(name)+"','"+str(dateandtime())+"',"+"null"+")"
                                        mycursor.execute(statement)
                                        print("=====================================================================")
                                        print(name, "his/her token id is", token)
                                        print("=====================================================================")
                                        loop='n'
                                        loop3=input("Do you want to add more entries (y/n) :" )
                                        
                                    else:
                                        print("Please check number plate again because the length of the character in number plate is too long...")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        print("Note : Entry will not be register if you didnt enter vehicle number ..... ")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        loop=input("Do you want to add vehicle number without changing his/her name:")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        if loop == "n" or loop=="no" or loop ==" N" :
                                            loop3=input("Do you want to add entries again (y/n) :" )

                            elif mode=="6":
                                mode="vehicle more than 4 tyres"
                                token=randomid()
                                name=input("Please enter name of driver: ")
                                loop='y'
                                while (loop=='y' or loop=='Y' or loop=='yes'):
                                    number=input("Please Enter vehicle number : ")
                                    if (len(number)<=10):
                                        statement="insert into Watchman_records values ('"+str(token)+"','"+str(mode)+"','"+str(number)+"','"+str(name)+"','"+str(dateandtime())+"',"+"null"+")"
                                        mycursor.execute(statement)
                                        print("=====================================================================")
                                        print(name, "his/her token id is", token)
                                        print("=====================================================================")
                                        loop='n'
                                        loop3=input("Do you want to add more entries (y/n) :" )
                                        
                                    else:
                                        print("Please check number plate again because the length of the character in number plate is too long...")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        print("Note : Entry will not be register if you didnt enter vehicle number ..... ")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        loop=input("Do you want to add vehicle number without changing his/her name:")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        if loop == "n" or loop=="no" or loop ==" N" :
                                            loop3=input("Do you want to add entries again (y/n) :" )

                            elif mode=="7":
                                mode="Hospital ambulance"
                                token=randomid()
                                name=input("Please enter name of driver: ")
                                loop='y'
                                while (loop=='y' or loop=='Y' or loop=='yes'):
                                    number=input("Please Enter vehicle number : ")
                                    if (len(number)<=10):
                                        statement="insert into Watchman_records values ('"+str(token)+"','"+str(mode)+"','"+str(number)+"','"+str(name)+"','"+str(dateandtime())+"',"+"null"+")"
                                        mycursor.execute(statement)
                                        print("=====================================================================")
                                        print(name, "his/her token id is", token)
                                        print("=====================================================================")
                                        loop='n'
                                        loop3=input("Do you want to add more entries (y/n) :" )
                                        
                                    else:
                                        print("Please check number plate again because the length of the character in number plate is too long...")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        print("Note : Entry will not be register if you didnt enter vehicle number ..... ")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        loop=input("Do you want to add vehicle number without changing his/her name:")
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        if loop == "n" or loop=="no" or loop ==" N" :
                                            loop3=input("Do you want to add entries again (y/n) :" )
                            elif mode=="8" or mode=="quit" or mode=="quit/8":
                                break
                            else:
                                print("Wrong option selected .Please select a correct option or type quit/8 to 'quit' ")
                    #=================================================================
                    elif (ch2=="2"):
                        loop3='y'
                        while (loop3=='y' or loop3=='Y'):
                            token=input("Please enter his or her token id: ")
                            if len(token)==10 :
                                if token.isalpha:
                                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                    print("Sorry invalid token id : None of the token id is provided with the letter . PLease check again  .")
                                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                    loop3=input("Do you want to try again (y/n) :" )
                                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                else:                                    
                                    statement="update watchman_records set exit_date_and_time='"+str(dateandtime())+"' where Entry_token='"+str(token)+"'"
                                    mycursor.execute(statement)
                                    print("=====================================================================")
                                    print("Exit date and time has been noted ")
                                    print("=====================================================================")
                                    loop3=input("Do you want to add more exits (y/n) :" )
                            elif len(token)>=11 :
                                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                print("token id is too long ")
                                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                loop3=input("Do you want to try again (y/n) :" )
                                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            elif len(token)<10:
                                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                print("token id is too short")
                                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                loop3=input("Do you want to try again (y/n) :" )
                                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                                            
                    elif (ch2=="3"):
                        pas=input("Enter Old Password: ")
                        mycursor.execute("select * from login1")
                        for i in mycursor:
                            username,passwordd=i
                        if (pas==password):
                            npas=input("Enter New Password: ")
                            mycursor.execute("update login1 set password='"+npas+"'")
                            mydb.commit()
                        else:
                            print("Sorry ur old password is wrong")
                    elif (ch2=="4"):
                            break
            else:
                print("your password is wrong please try again")
        elif(ch1=='4'):
                break
    else:
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("Please enter correct choice between 1,2 ,3 and 4!!!!!!!!!!!!!!!!!!" )
