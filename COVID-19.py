import pickle
import os
import getpass
print('**************************')
print(' COVID INFORMATION SYSTEM')
print('**************************')
def covidinfo():
            print('''COVID IS A AIRBORNE VIRUS WHICH SPREADS THROUGH AIR PHYSICAL CONTACT,THIS VIRUS WAS FIRST FOUND IN NOVEMBER 2019 IN WUHAN,CHINA.
                  IT IS SAID THAT IT SPREAD FROM A BAT AND DAY BY DAY CASES GOT HIGHER IN CHINA AND THE VIRUS STARTED TO SPREAD RAPIDLY ACCROSS THE WORLD AS IT WAS AIRBORNE.
                  NO VACCINES HAVE BEEN FOUND YET BUT THERE IS HOPE IT WILL BE FOUND SOON. THIS VIRUS MAINLY DAMAGES OUR LUNGS WHICH CAUSES BREATHING PROBLEMS.

                  SYMPTOMS:

                  (i)COLD.
                  (ii)FEVER.
                  (iii)SEVRE HEADACHE.
                  (iv)BREATHING PROBLEMS.
                  (v)TIREDNESS.

                  IF YOU FEEL ANY OF THESE PLEASE GO AND DO A TEST(IT IS FREE)
                  
                  STEPS TO PREVENT COVID:

                  (i)DO NOT TOUCH OTHERS.
                  (ii)WEAR MASKS.
                  (iii)SANITIZE AND WASH YOUR HANDS WHEN YOU COME HOME.
                  (iv)DO NOT GO OUT OF YOUR HOMES WITHOUT A CAUSE''')
            
def covid():
        print("\n********************")
        print("WELCOME TO MAIN MENU")
        print("********************")
        print('1.ADMIN')
        print('2.VISITOR')
        print('3.EXIT')
        opt=int(input("Enter Your Option:"))
        if opt==1:
           g=input("Enter Password:")
           if g=='COVID':
                 admin()
           else:
                  print('WRONG PASSWORD')
        if opt==2:
              print('YOU HAVE ENTERED THE VISITORS MENU')
              visitor()
        if opt==3:
              print('THANK YOU')
        

def admin():
            print("*********************")
            print("WELCOME TO ADMIN MENU")
            print("*********************")
            print('1.ENTER NEW HOSPITALS')
            print('2.VIEW HOSPITALS')
            print('3.Search Hospitals')
            print('4.Update Hospital details')
            print('5.Delete Hospital')
            print('6.Enter New Patient Detail')
            print('7.View Patients')
            print('8.Search Patient')
            print('9.Delete Patient') 
            b=int(input('ENTER NUMBER CORRESPONDING TO THE OPTION:'))
            if b==1:
                newhospitals()
            elif b==2:
                 View_hos()                   
            elif b==3:
                 Search_hos()
            elif b==4:
                 Update_hos()
            elif b==5:
                 Del_hos()
            elif b==6:
                 New_Pat()
            elif b==7:
                View_Pat()
            elif b==8:
                 Search_Pat()
            elif b==9:
                 Del_Pat()

           
def newhospitals():
    f=open('hospitals.dat','ab+')
    opt='y'
    Hospital={}
    print("**************************************")
    print("WELCOME TO HOPITAL'S REGISTRATION MENU")
    print("**************************************")
    while opt=='y':
          Hospital['Hos_ID']=int(input("Enter Hospital ID:"))
          Hospital['Hos_Name']=input('ENTER HOSPITAL NAME:')
          Hospital['Non_Covid_Rooms']=int(input('ENTER NO.OF ROOMS FOR NON-COVID PATIENTS:'))
          Hospital['Covid_Rooms']=int(input('ENTER NO OF ROOMS FOR COVID TREATMENT:'))
          Hospital['Hos_Pat']=int(input('ENTER TOTAL COUNT OF EXISTING  PATIENTS IN THE HOSPITAL:'))
          Hospital['Hos_No']=input('ENTER HOSPITAL PHONE NUMBER:')
          pickle.dump(Hospital,f)
          print("Hospitals details are stored successfully")
          opt=input('DO YOU WANT TO ENTER ANOTHER HOSPITAL(y/n):')
    o=input('ENTER y TO ENTER ADMIN MENU')
    f.close()
    if o=='y':
       admin()
    else:
        e=input('DO YOU WANT TO ENTER MAIN MENU y/n:')
        if e=='y':
           covid()  
    f.close()
       
    
         
def View_hos():
    f=open("hospitals.dat",'rb')
    try:
        while True:
              S=pickle.load(f)
              print("\n************************")
              print("HOSPITAL ID:",S['Hos_ID'])
              print("HOSPITAL NAME:",S['Hos_Name'])
              print("NON COVID ROOMS:",S['Non_Covid_Rooms'])
              print("COVID ROOMS:",S['Covid_Rooms'])
              print("EXISTING PATIENTS COUNT:",S['Hos_Pat'])
              print("HOSPITAL PHONE.NO:",S['Hos_No'])
              print("****************************")
    except:
            f.close()
    o=input('ENTER y TO ENTER ADMIN MENU')
    if o=='y':
          admin()
    else:
          e=input('DO YOU WANT TO ENTER MAIN MENU y/n:')
          if e=='y':
                 covid()
            
def Search_hos():
     f=open("hospitals.dat",'rb')
     ID=int(input("Enter the Hospital ID which you want to search:"))
     found=0
     try:
        while True:
               S=pickle.load(f)
               if S['Hos_ID']==ID:
                   print("\n************************")
                   print("HOSPITAL ID:",S['Hos_ID'])
                   print("HOSPITAL NAME:",S['Hos_Name'])
                   print("NON COVID ROOMS:",S['Non_Covid_Rooms'])
                   print("COVID ROOMS:",S['Covid_Rooms'])
                   print("EXISTING PATIENTS COUNT:",S['Hos_Pat'])
                   print("HOSPITAL PHONE.NO:",S['Hos_No'])
                   print("****************************")
                   found=1
                   break
     except:
            f.close()
     if found==0:
        print("Hospital Not Found")
     o=input('ENTER y TO ENTER ADMIN MENU')
     if o=='y':
          admin()
     else:
          e=input('DO YOU WANT TO ENTER MAIN MENU y/n:')
          if e=='y':
                 covid()
        
def Update_hos():
      f=open("hospitals.dat",'rb+')
      ID=int(input("Enter Hospital ID to Modify:"))
      found=0
      try:
         while True:
                pos=f.tell()
                S=pickle.load(f)
                if S['Hos_ID']==ID:
                   print("The searched hospital details are found",S)
                   S['Non_Covid_Rooms']=S['Non_Covid_Rooms']+int(input("Enter New Vacancy for non-covid patients treatment :"))
                   S['Covid_Rooms']=S['Covid_Rooms']+int(input("Enter New Vacancy  for COVID treatment:"))
                   f.seek(pos)
                   pickle.dump(S,f)
                   found=1
                   print("Details are updated successfully")
                   f.close()
                   View_hos()
                   break
      except:
             f.close()
      if found==0:
             print("The searched Hospital ID not found")
def Del_hos():
     f1=open('hospitals.dat','rb')
     f2=open('temp.dat','wb')
     w=int(input('ENTER HOSPITAL ID TO BE DELETED'))
     found=0
     try:
        while True:
             s=pickle.load(f1)
             if s['Hos_ID']==w:
                found=1
             else:
                 pickle.dump(s,f2)
     except:
             f1.close()
             
             f2.close()
     if found==0:
             print("Record Not found")
     else:
          print("Record Deleted Successfully")
          os.remove("hospitals.dat")
          os.rename("temp.dat","hospitals.dat")
     o=input('ENTER y TO ENTER ADMIN MENU')
     if o=='y':
               admin()
     else:
               e=input('DO YOU WANT TO ENTER MAIN MENU y/n:')
               if e=='y':
                          covid()

                    
        
def New_Pat():
            opt='y'
            found=0
            Patient={}
            while opt=='y':
                  f=open('newpatients.dat','ab')
                  f2=open('hospitals.dat','rb+')
                  pid=int(input('ENTER PATIENT ID:'))
                  pname=input('ENTER PATIENT NAME:')
                  page=int(input('ENTER PATIENT AGE:')) 
                  padd=input('ENTER PATIENT ADDRESS:')
                  phos=input('ENTER HOSPITAL NAME:')
                  pward=int(input('ENTER PATIENT WARD NUMBER:'))
                  pdate=input("ENTER PATIENT ADMITTED DATE:")
                  pprob=input('ENTER PROBLEM OF PATIENT')
                  found=0
                  Patient['P_ID']=pid
                  Patient['P_NAME']=pname
                  Patient['P_AGE']=page
                  Patient['P_ADDRESS']=padd
                  Patient['P_HOS']=phos
                  Patient['P_WARD']=pward
                  Patient['P_DATE']=pdate
                  Patient['P_DIS']=pprob
                  try:
                      while True:
                            pos=f2.tell()
                            S=pickle.load(f2)
                            if S['Hos_Name']==Patient['P_HOS']:
                               found=1
                               if Patient['P_DIS']=='COVID-19' or Patient['P_DIS']=='CORONA':
                                  S['Covid_Rooms']=S['Covid_Rooms']-1
                                  S['Hos_Pat']=S['Hos_Pat']+1
                               else:
                                   S['Non_Covid_Rooms']=S['Non_Covid_Rooms']-1
                                   S['Hos_Pat']=S['Hos_Pat']+1
                               pickle.dump(Patient,f)
                               f2.seek(pos)
                               pickle.dump(S,f2)
                               print("Patient Details are stored successfully")
                               opt=input('DO YOU WANT TO ENTER ANOTHER PATIENT NAME:(y/n)')
                        
                          
                  except:
                        f.close()
                  if found==0:
                        print('HOSPITAL NOT FOUND')
                        print('ABOVE DETAILS ARE NOT STORED SUCCESSFULY')
                 
            
                  o=input('ENTER y TO ENTER ADMIN MENU')        
                  if o=='y':
                            admin()
                  else:
                            e=input('DO YOU WANT TO ENTER MAIN MENU y/n:')
                            if e=='y':
                                  covid()
                            else:
                                 print('THANK YOU')
               
              
def View_Pat():
    f=open('newpatients.dat','rb')
    try:
        while True:
             s=pickle.load(f)
             print('*******************')
             print("PATIENT_ID:",s['P_ID'])
             print("NAME:",s['P_NAME'])
             print("AGE:",s['P_AGE'])
             print("ADDRESS:",s['P_ADDRESS'])
             print("ADDMITED IN:",s['P_HOS'])
             print("DATE OF ADMISSION:",s['P_DATE'])
             print("WARD NO:",s['P_WARD'])
             print("DISEASE:",s['P_DIS'])
             print('*******************')
    except:
            f.close()
             
    o=input('ENTER y TO ENTER ADMIN MENU')
    if o=='y':
       admin()
    else:
       e=input('DO YOU WANT TO ENTER MAIN MENU y/n:')
       if e=='y':
          covid()
def Search_Pat():
    f=open('newpatients.dat','rb')
    a=int(input('ENTER PATIENT ID TO SEARCH'))
    found=0
    try:
       while True:
             s=pickle.load(f)
             if s[0]==a:
                print('*******************')
                print("PATIENT_ID:",s['P_ID'])
                print("NAME:",s['P_NAME'])
                print("AGE:",s['P_AGE'])
                print("ADDRESS:",s['P_ADDRESS'])
                print("ADDMITED IN:",s['P_HOS'])
                print("WARD NO:",s['P_WARD'])
                print('*******************')
                found=1
                break
    except:
           f.close()
    if found==0:
            print('PATIENT ID NOT FOUND')
    o=input('ENTER y TO ENTER ADMIN MENU')
    if o=='y':
       admin()
    else:
       e=input('DO YOU WANT TO ENTER MAIN MENU y/n:')
       if e=='y':
          covid()

def Del_Pat():
     f1=open('newpatients.dat','rb')
     f2=open('temp.dat','wb')
     f3=open('hospitals.dat','rb+')
     w=int(input('ENTER PATIENT ID TO BE DELETED'))
     found=0
     try:
        while True:
              s=pickle.load(f1)
              if s['P_ID']==w:
                 found=1
              else:
                  pickle.dump(s,f2)
     except:
           f1.close()
           f2.close()
     if found==0:
             print("Record Not found")
     else:
          print("Record Deleted Successfully")
          os.remove("newpatients.dat")
          os.rename("temp.dat","newpatients.dat")
     o=input('ENTER y TO ENTER ADMIN MENU')
     if o=='y':
               admin()
     else:
               e=input('DO YOU WANT TO ENTER MAIN MENU y/n:')
               if e=='y':
                          covid()

                
def visitor():
    print("\n*********************")
    print("WELCOME TO VISITOR MENU")
    print("***********************")
    print('1.HOSPITALS AVAILABLE TO TREAT COVID')
    print('2.VACANCIES IN EACH HOSPITAL')
    print('3.INFORMATION ABOUT COVID-19')
    print('4.ACTIVE CASES')
    c=int(input('ENTER THE OPTIONS CORRESPONDING NUMBER'))
    if c==1:
       hospitalsname()
    elif c==2:
       vacancies()
    elif c==3:
         covidinfo()
    elif c==4:
         activecases()

def hospitalsname():
    f=open('hospitals.dat','rb')
    S=pickle.load(f)
    print("\n************************")
    print("HOSPITAL ID:",S['Hos_ID'])
    print("HOSPITAL NAME:",S['Hos_Name'])
    print("NON COVID ROOMS:",S['Non_Covid_Rooms'])
    print("COVID ROOMS:",S['Covid_Rooms'])
    print("EXISTING PATIENTS COUNT:",S['Hos_Pat'])
    print("HOSPITAL PHONE.NO:",S['Hos_No'])
    print("****************************")
    
    o=input('ENTER y TO ENTER VISITOR MENU')
    if o=='y':
       visitor()
    else:
        e=input('DO YOU WANT TO ENTER MAIN MENU y/n:')
        if e=='y':
           covid()
            
def vacancies():
    f=open('hospitals.dat','rb')
    name=input('ENTER HOSPITAL NAME:')
    found=0
    try:
       while True:
             R=pickle.load(f)
             if R['HOS_NAME']==name:
                 print('VACANCIES FOR TREATING NON COVID PATIENTS',R['Non_Covid_Rooms'])
                 print('VACANCIES FOR COVID:',R['Covid_Rooms'])
                 found=1
                 break
        
                 
             
    except:
        f.close()
    if found==0:
            print('HOSPITAL NOT FOUND')
            
    o=input('ENTER y TO ENTER VISITOR MENU')
    if o=='y':
       visitor()
    else:
        e=input('DO YOU WANT TO ENTER MAIN MENU y/n:')
    if e=='y' or e=='Y':
       covid()


                      
def activecases():
    f=open('newpatients.dat','rb')
    count=0
   
    try:
        while True:
                 s=pickle.load(f)
                 count=count+1
    except:
        f.close()
    
   
    print('ACTIVE CASES',count)
    o=input('ENTER y TO ENTER VISITOR MENU')
    if o=='y':
       visitor()
    else:
        e=input('DO YOU WANT TO ENTER MAIN MENU y/n:')
        if e=='y':
           covid()
        

covidinfo()
covid()
print('THANK YOU')
print('STAY SAFE')







          

    



    
            

        
