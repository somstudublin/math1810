import math
import numpy as np
import time
import time
import os.path
import getpass
from IPython.display import Markdown, display



def pj(oldj,newj):
#    from subprocess import call
#    call(["passj",oldj,newj])
#    print("\nPassword should be changed.\nClose all notebooks, log out, and log in again with new password to confirm.")
        print("\nPasswords may not be changed using this notebook at present.")


#global parameter list
ps=[]
wd=''
rid=0
encoff1= 34
encoff2= 567


#############
#TEMPLATE CA FUNCTION

#Naming convention: <x><n>
#Module     x   
#MATH1810   a
#MATH1811   b
#n=ca task number

#1. def vala1(M,K):
#2. ftrycount=".a1_counter.npy"
#3. tol=0.0

#############

def a1():

    global ps
#USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO    
#   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
    ftrycount=".a1_counter.npy"
    arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file

    tol=0
    a0=ps[0]
    a1=ps[1]
    
    if(waiter()):
        while True:
            try:
                printmd('**CA** (2%)')
                print(a0,"+",a1)
                print('tester')
                value = float(input("Please enter your answer here: "))
                actual=a0+a1
                succ=np.isclose(value,actual,tol)
                if succ:
                    print("Well done, right answer is ",actual)                
                else:
                    print("Not right yet. Take another look then run this cell again.")
                    
                arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                score=100-(arec[0]-1)*10
                if arec[1]:
                    print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")
                    print("Enter this code into Brightspace:\n\n",genenc(1+encoff1,score+encoff2),'\n')
                else:
                    print("You have had ",arec[0]," tries.")
                    print("If next try is accepted you will achieve ",score-10,"% on this exercise.")

                break

            except ValueError:
                print("I didn't understand that.")
                continue

        return
        
######
#END OF TEMPLATE CA FUNCTION
######

#############
# CA2 FUNCTION

def a2(prompt):

    global ps
#USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO    
#   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
    ftrycount=".a2_counter.npy"
    arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file

    # Vary these indices for varied problem parameters
    ia0=6
    ia1=7
    #Set tolerance for testing result here (0 for exact integer calcs)
    tol=0
    
    a0=(ps[ia0])%6+1
    a1=(ps[ia1])%6+1
    while a0+a1==7 or a0==a1:
        a1+=1
        a1=a1%6+1

    if(prompt):
        printmd('**CA** (2%)')
        print("Run your program (when you are happy it is working correctly) for a=",a0," and b=",a1)
        print('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')
        return

    if(waiter()):
        while True:
            try:
                print("Enter your program's result for a=",a0," and b=",a1)
                print('(If you are not ready to enter an answer stop the kernel and go back to your program.)')
                value = float(input("Please enter your answer here: "))
                actual=(3*(a0**3*a1-a0*a1**3))%7
                succ=np.isclose(value,actual,tol)
                if succ:
                    print("Well done, right answer is ",actual)                
                else:
                    print("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")
                    
                arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                score=100-(arec[0]-1)*10
                if arec[1]:
                    print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")            
                    print("Enter this code into Brightspace:\n\n",genenc(2+encoff1,score+encoff2),'\n')                    
                else:
                    print("You have had ",arec[0]," tries.")
                    print("If next try is accepted you will achieve ",score-10,"% on this exercise.")

                break

            except ValueError:
                print("I didn't understand that.")
                continue

        return
        
######
#END OF CA2 FUNCTION
######

#############
# CA3 FUNCTION

def a3(prompt):

    global ps
#USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO    
#   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
    ftrycount=".a3_counter.npy"
    arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file

    # Vary these indices for varied problem parameters
    ia0=23
    ia1=24
    a0=(ps[ia0])%6+1
    a1=(ps[ia1])%6+1
    #Set tolerance for testing result here (0 for exact integer calcs)
    tol=0
    
    a0=10*a0+a1;

    if(prompt):
        printmd('**CA** (6%)')
        print("Run your program for ",a0,"people")
        print('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')
        return

    if(waiter()):
        while True:
            try:
                print("Enter your program's result for",a0,"people")
                print('(If you are not ready to enter an answer stop the kernel and go back to your program.)')
                value = float(input("Please enter your answer here: "))
                actual=a0+2*a0+2*a0+10*a0
                succ=np.isclose(value,actual,tol)
                if succ:
                    print("Well done, right answer is ",actual)                
                else:
                    print("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")
                    
                arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                score=100-(arec[0]-1)*10
                if arec[1]:
                    print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")            
                    print("Enter this code into Brightspace:\n\n",genenc(3+encoff1,score+encoff2),'\n')
                else:
                    print("You have had ",arec[0]," tries.")
                    print("If next try is accepted you will achieve ",score-10,"% on this exercise.")

                break

            except ValueError:
                print("I didn't understand that.")
                continue

        return
        
######
#END OF CA3 FUNCTION
######

######
#START OF CA4 FUNCTION
######                                                                                                                                                        


def a4(prompt):
        
        import random
        import requests
        
        global ps
        global wd
        #USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO
        #   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
        ftrycount=".a4_counter.npy"
        arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file
        
        # Vary these indices for varied problem parameters
        ia0=60
        ia1=61
        ia2=62
        ia3=63
        ia4=64
        
        #Set tolerance for testing result here (0 for exact integer calcs)
        tol=0
        
        if(prompt):
                #word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
                word_site = "https://users.cs.duke.edu/~ola/ap/linuxwords"

                # response = requests.get(word_site) # Use two lines below for expired cert
                requests.packages.urllib3.disable_warnings()
                response = requests.get(word_site,verify=False)

                WORDS = response.content.splitlines()
                random.seed(10*ps[62]+ps[63])
                mykey=4+(10*ps[64]+ps[65])%4   #between 4 and 7 inclusive
                seek=True
                while seek:
                        myword=WORDS[random.randint(0,len(WORDS)-1)].decode("utf-8")
                        #print(myword)
                        if len(myword)>7 and len(myword)<14 and myword[0].islower(): # between 7 and 13 letters, first letter lower case
                                seek=False
                                for c in myword:
                                        if chr(ord(c)+mykey)>'z': # check encoding stays in regular alphabet
                                                seek=True
                #print(myword,mykey)
                mylen=len(myword)
                mycode=''
                for i in range(0,mylen):
                        #print(myword[i],ord(myword[i])+mykey)
                        mycode+=chr(ord(myword[i])+mykey)
                #print('Your encoded word is',mycode,'\nYour key is',mykey,'\n')
                print('Your encoded word is',mycode)
                print('Write your program in the cell below this one.\n')
                print('When you have decoded the word (it should be a real word if you are correct),\n', \
                      'run the CA cell underneath and enter the word into the dialogue box.')
                wd=myword
                return

        if(waiter()):
                while True:
                        try:
                                printmd('**CA** (6%)')
                                value = str(input("Enter your DECODED word here: "))
                                actual=wd
                                succ=value==actual
                                if succ:
                                        print("Well done, right answer is ",actual)                
                                else:
                                        print("Not right yet. Take another look then run this cell again.")                    

                                arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                                score=100-(arec[0]-1)*10
                                if arec[1]:
                                        print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")            
                                        print("Enter this code into Brightspace:\n\n",genenc(4+encoff1,score+encoff2),'\n')
                                else:
                                        print("You have had ",arec[0]," tries.")
                                        print("If next try is accepted you will achieve ",score-10,"% on this exercise.")
                                break

                        except ValueError:
                                print("I didn't understand that.")
                                continue
                
                return        
                        
######
#END OF CA4 FUNCTION
######                                                                                                                                                        

######
#START OF CA5 FUNCTION
######
# differentiate polynomial
def a5(prompt):
        
        import random
        import requests
        
        global ps
        global P0
        
        #USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO
        #   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
        ftrycount=".a5_counter.npy"
        arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file
        
        # Vary these indices for varied problem parameters
        ia0=70
        ia1=71
        ia2=72
        ia3=73
        ia4=74
        
        #Set tolerance for testing result here (0 for exact integer calcs)
        tol=0

        if(prompt):
                P0=[]
                deg=7+(10*ps[ia0]+ps[ia1])%4   #between 7 and 11 inclusive
                for i in range(deg):
                        P0.append(max(0,ps[ia2+i]-1))
                print('Run your program for the list below:\n',P0)

                print('Run the next cell and copy and paste your result, as a list of the same length, into the dialogue box.')

        elif(waiter()):
                while True:
                        try:

                                #Testing answer from here
                                printmd('**CA** (6%)')
                                value = eval(input("Enter your list here: "))



                                #Solution determined here
                                D=3
                                Pd=P0.copy()
                                Pd.append(0)
                                print(Pd)
                                deg=len(P0)
                                for d in range(D):
                                        for i in range(deg):
                                                #print(deg,i,Pd)
                                                Pd[i]=Pd[i+1]*(i+1)
                                Pd.pop()

                                #Setting actual answer and testing
                                actual=Pd

                                if not type(value) == type(actual):
                                        print('You need to enter answer as a list (not counted as an attempt).')
                                elif not len(value) == len(actual):
                                        print('You need to enter answer as list of same length (not counted as an attempt).')
                                else:
                                        succ=value==actual
                                        if succ:
                                                print("Well done, right answer is ",actual)                
                                        else:
                                                print("Not right yet. Take another look then run this cell again.")                    

                                        arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                                        score=100-(arec[0]-1)*10
                                        if arec[1]:
                                                print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")            
                                                print("Enter this code into Brightspace:\n\n",genenc(5+encoff1,score+encoff2),'\n')
                                        else:
                                                print("You have had ",arec[0]," tries.")
                                                print("If next try is accepted you will achieve ",score-10,"% on this exercise.")
                                        break
                                # Prevent querying of stored internal solution from calling routing
                                #print('Setting to None')
                                Pd=None 
                                actual=None                                
                        except ValueError:
                                print("I didn't understand that.")
                                continue

        return        
                        
######
#END OF CA5 FUNCTION
######                                                                                                                                                        

######
#START OF CA6 FUNCTION
######                                                                                                                                                        
def a6(prompt):
        
        import random
        import requests
        
        global ps
        global P0
        
        #USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO
        #   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
        ftrycount=".a6_counter.npy"
        arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file
        
        # Vary these indices for varied problem parameters
        ia0=11
        ia1=16
        ia2=7
        ia3=33
        ia4=21
        
        #Set tolerance for testing result here (0 for exact integer calcs)
        tol=0

        if(prompt):
                seed=ps[ia0]+ps[ia1]+ps[ia2]+ps[ia3]+ps[ia4]
                random.seed(seed)
                P0=random.randint(1000,2000)
                print('Run your program to obtain the stopping time for the value:\n',P0)

                print('Run the next cell and enter the stopping time into the dialogue box.')
 
        elif(waiter()):
                while True:
                        try:

                                #Testing answer from here
                                printmd('**CA** (6%)')
                                value = eval(input("Enter your stopping number here: "))


                                #Solution determined here
                                n=P0
                                hail=[n]
                                while not n==1:
                                        if n%2:
                                                n=3*n+1
                                        else:
                                                n=n//2
                                        hail.append(n)
                                Pd=len(hail)
                                #print('hail',hail,'stop',Pd)

                                #Setting actual answer and testing
                                actual=Pd

                                if not type(value) == type(actual):
                                        print('You need to enter answer as correct type (not counted as an attempt).')
                                #elif not len(value) == len(actual):
                                #        print('You need to enter answer of correct length (not counted as an attempt).')
                                else:
                                        succ=value==actual
                                        if succ:
                                                print("Well done, right answer is ",actual)                
                                        else:
                                                print("Not right yet. Take another look then run this cell again.")                    

                                        arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                                        score=100-(arec[0]-1)*10
                                        if arec[1]:
                                                print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")            
                                                print("Enter this code into Brightspace:\n\n",genenc(6+encoff1,score+encoff2),'\n')
                                        else:
                                                print("You have had ",arec[0]," tries.")
                                                print("If next try is accepted you will achieve ",score-10,"% on this exercise.")
                                        break
                                # Prevent querying of stored internal solution from calling routing
                                #print('Setting to None')
                                Pd=None 
                                actual=None                                
                        except ValueError:
                                print("I didn't understand that.")
                                continue

        return        
                        
######
#END OF CA6 FUNCTION
######                                                                                                                              

                          
######
#START OF CA7 FUNCTION
######                                                                                                                                                        
def a7(userfunc):
        
        #USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO
        #   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
        ftrycount=".a7_counter.npy"
        arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file

        def dummy():
                pass
        
        # Test cases
        testvals=[(30,10)]
        
        #Set tolerance for testing result here (0 for exact integer calcs)
        tol=1.0e-4

        
        if(waiter()):
                #Testing answer from here
                printmd('**CA** (6%)')
                
                if not type(userfunc) == type(dummy):
                        print('You need to enter answer as correct type (not counted as an attempt).')
                        #elif not len(value) == len(actual):
                        #        print('You need to enter answer of correct length (not counted as an attempt).')
                else:

                        #Solution determined here
                        def solfunc(nu,alpdeg):
                                import math
                                g=9.81
                                alp=math.pi*alpdeg/180.
                                R=nu**2*math.sin(2*alp)/g
                                H=nu**2*(math.sin(alp))**2/(2.*g)
                                return R,H
                        
                        #Setting actual answer and testing
                        import random as r
                        testvals=[]
                        wrongreturnform=False
                        succs=[]
                        nu0=10   # limits
                        nu1=100
                        a0=5
                        a1=85
                        for i in range(5):
                                testvals.append((r.uniform(nu0,nu1),r.uniform(a0,a1)))
                        for (nu,alp) in testvals:
                                print('Testing:',nu,alp)
                                value=userfunc(nu,alp)
                                print('Output:',*value)
                                actual=solfunc(nu,alp)
                                print('Actual:',*actual)
                                print()
                                if (not type(value) == type(actual)) or (not len(value)==len(actual)):
                                        if wrongreturnform==False:
                                           wrongreturnform=True
                                else:
                                        succs.append(all(np.isclose(value,actual,tol)))

                        if wrongreturnform:
                                print('Check the returned value format of your function (not counted as an attempt).')
                                        
                        else:
                                succ=all(succs)
                                if succ:
                                        print("Well done, all correct.")                
                                else:
                                        print("Not right yet. Take another look then run this cell again.")                    
                                
                                arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                                score=100-(arec[0]-1)*10
                                if arec[1]:
                                        print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")            
                                        print("Enter this code into Brightspace:\n\n",genenc(7+encoff1,score+encoff2),'\n')
                                else:
                                        print("You have had ",arec[0]," tries.")
                                        print("If next try is accepted you will achieve ",score-10,"% on this exercise.")
                        # Prevent querying of stored internal solution from calling routing
                        #print('Setting to None')
                        actual=None                                
                        solfunc=None
        
        return        
                        
######
#END OF CA7 FUNCTION
######                                                                                                                                                        

                          
######
#START OF CA8 FUNCTION
######                                                                                                                                                        
def a8(userfunc):
        
        #USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO
        #   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
        ftrycount=".a8_counter.npy"
        arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file

        def dummy():
                pass
        
        
        #Set tolerance for testing result here (0 for exact integer calcs)
        tol=1.0e-4

        
        if(waiter()):
                #Testing answer from here
                printmd('**CA** (6%)')
                


                if not type(userfunc) == type(dummy):
                        print('You need to enter answer as correct type (not counted as an attempt).')
                        #elif not len(value) == len(actual):
                        #        print('You need to enter answer of correct length (not counted as an attempt).')

                else:

                        #check not using loops
                        import inspect
                        lines = inspect.getsourcelines(userfunc)
                        valid=True
                        linenums=[]
                        for linenum,line in enumerate(lines[0]):
                                if 'for' in line or 'while' in line:
                                        #print(linenum,line)
                                        valid=False
                                        linenums.append(linenum)
                        if not valid:
                                print('Function needs to be written without loops (using NumPy), check lines',*linenums)
                                print('No marks lost for this attempt.')
                                return
                                
                        #Solution determined here
                        def solfunc(vertices):
                                a = np.vstack((vertices, vertices[0]))
                                S1 = sum(a[:-1,0] * a[1:,1])
                                S2 = sum(a[:-1,1] * a[1:,0])
                                return abs(S1-S2)/2
                        
                        #Setting actual answer and testing
                        import random as r
                        nvals=r.randint(6,11)
                        testvals=np.ones((nvals,2))
                        wrongreturnform=False
                        succs=[]
                        x0=1.   # limits
                        x1=20.
                        y0=x0
                        y1=x1
                        for i in range(nvals):
                                testvals[i]=[r.uniform(x0,x1),r.uniform(y0,y1)]
                        print('Testing:',testvals)
                        value=userfunc(testvals)
                        print('Output:',value)
                        actual=solfunc(testvals)
                        print('Actual:',actual)
                        print()
                        if not type(value) == type(actual) :
                                if wrongreturnform==False:
                                        wrongreturnform=True
                        else:
                                succs.append(np.isclose(value,actual,tol))

                        if wrongreturnform:
                                print('Check the returned value format of your function (not counted as an attempt).')
                                        
                        else:
                                succ=all(succs)
                                if succ:
                                        print("Well done, all correct.")                
                                else:
                                        print("Not right yet. Take another look then run this cell again.")                    
                                
                                arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                                score=100-(arec[0]-1)*10
                                if arec[1]:
                                        print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")            
                                        print("Enter this code into Brightspace:\n\n",genenc(8+encoff1,score+encoff2),'\n')
                                else:
                                        print("You have had ",arec[0]," tries.")
                                        print("If next try is accepted you will achieve ",score-10,"% on this exercise.")
                        # Prevent querying of stored internal solution from calling routing
                        #print('Setting to None')
                        actual=None                                
                        solfunc=None
        
        return        
                        
######
#END OF CA8 FUNCTION
######

#
# PLACE HOLDER FUNCTIONS BELOW
#
#



######
#START OF CA1 NOT LIVE FUNCTION
######
def a1_notlive():
        print('This CA test is not currently live.')
        return                        
######
#END OF CA1 NOT LIVE FUNCTION
######                                                                                                                                                        

######
#START OF CA2 NOT LIVE FUNCTION
######
def a2_notlive(prompt):
        print('This CA test is not currently live.')
        return                        
######
#END OF CA2 NOT LIVE FUNCTION
######                                                                                                                                                        

######
#START OF CA3 NOT LIVE FUNCTION
######
def a3_notlive(prompt):
        print('This CA test is not currently live.')
        return                        
######
#END OF CA3 NOT LIVE FUNCTION
######                                                                                                                                                        

######
#START OF CA4 NOT LIVE FUNCTION
######
def a4_notlive(prompt):
        print('This CA test is not currently live.')
        return                        
######
#END OF CA4 NOT LIVE FUNCTION
######                                                                                                                                                        

######
#START OF CA5 NOT LIVE FUNCTION
######
def a5_notlive(prompt):
        print('This CA test is not currently live.')
        return                        
######
#END OF CA5 NOT LIVE FUNCTION
######                                                                                                                                                        

######
#START OF CA6 NOT LIVE FUNCTION
######
def a6_notlive(prompt):
        print('This CA test is not currently live.')
        return                        
######
#END OF CA6 NOT LIVE FUNCTION
######                                                                                                                                                        

######
#START OF CA7 NOT LIVE FUNCTION
######
def a7_notlive():
        print('This CA test is not currently live.')
        return                        
######
#END OF CA7 NOT LIVE FUNCTION
######                                                                                                                                                        

######
#START OF CA8 NOT LIVE FUNCTION
######
def a8_notlive(polygon):
        print('This CA test is not currently live.')
        return                        
######
#END OF CA8 NOT LIVE FUNCTION
######                                                                                                                                                        

                                                                              




#######################
#   Semester 2 functions below here
#######################

######
#START OF b1 FUNCTION
######                                                                          

def b1():

    global ps
#USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO    
#   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
    ftrycount=".b1_counter.npy"
    arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file

    tol=0.05    #relative tolerence
    
    if(waiter()):
        while True:
            try:
                printmd('**CA**')
                value = eval(input("Please enter your answer here in the format D,k: "))
                actual=(0.025,2.0)
                succ=all(np.isclose(value,actual,rtol=tol))
                if succ:
                    print("Well done, reasonable estimate is ",actual)                
                else:
                    print("Not right yet. Take another look then run this cell again.")
                    
                arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                score=100-(arec[0]-1)*10
                if arec[1]:
                    print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")            
                    print("Enter this code into Brightspace:\n\n",genenc(1+encoff1,score+encoff2),'\n')
                else:
                    print("You have had ",arec[0]," tries.")
                    print("If next try is accepted you will achieve ",score-10,"% on this exercise.")

                break

            except ValueError:
                print("I didn't understand that.")
                continue

        return
        
######
#END OF b1 FUNCTION
######                                                                          


######
#START OF b2 FUNCTION
######                                                                                                                                                        
def b2(userfunc):

        #USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO
        #   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
        ftrycount=".b2_counter.npy"
        arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file

        def dummy():
                pass
                
        #Set tolerance for testing result here (0 for exact integer calcs)
        rtol=1.0e-2
        atol=0.0 
        
        if(waiter()):
                #Testing answer from here
                printmd('**CA**')
                
                if not type(userfunc) == type(dummy):
                        print('You need to enter answer as correct type (not counted as an attempt).')
                        #elif not len(value) == len(actual):
                        #        print('You need to enter answer of correct length (not counted as an attempt).')
                else:

                        #Solution determined here

                        def solfunc(thetas):
                                ximpacts=[] # landing distances 
                                v0=20.0
                                m=58.1e-3
                                g=9.81
                                x0=0.0
                                y0=0.0
                                t0=0.0
                                t1=10 # terminal time
                                r=3.35e-2
                                C=0.51
                                rho=1.25
                                A=math.pi*r**2
                                D=0.5*C*A*rho
                                # Variable arrays
                                nn=100000 # number of points in sol 
                                t = np.zeros(nn,float)
                                ax = np.zeros(nn,float)
                                ay = np.zeros(nn,float)
                                vx = np.zeros(nn,float)
                                vy = np.zeros(nn,float)
                                x = np.zeros(nn,float)
                                y = np.zeros(nn,float)
                                t,dt=np.linspace(t0,t1,nn,retstep=True)
                                #vary initial angle
                                for theta in thetas:
                                        vx0=v0*math.cos(theta)
                                        vy0=v0*math.sin(theta)
                                        #numerical solution
                                        x[0]=x0
                                        y[0]=y0
                                        vx[0]=vx0
                                        vy[0]=vy0
                                        for i in range(nn-1):      # Euler-Cromer
                                                v=math.sqrt(vx[i]**2+vy[i]**2)
                                                fx = -D*v*vx[i]              # Set x force here
                                                ax[i] = fx/m
                                                vx[i+1] = vx[i] + ax[i]*dt
                                                x[ i+1] = x[ i] + vx[i+1]*dt
                                                fy = -m*g-D*v*vy[i]           # Set y force here
                                                ay[i] = fy/m
                                                vy[i+1] = vy[i] + ay[i]*dt
                                                y[ i+1] = y[ i] + vy[i+1]*dt
                                                if (y[i+1]<0):
                                                        break
                                        imax=i
                                        ximpacts.append(x[imax])
                                        #print('t_impact=',t[imax], 'x_impact=',x[imax])
                                return(ximpacts);
                        
                        #Setting actual answer and testing
                        import random as r
                        testvals=[]
                        wrongreturnform=False
                        succs=[]
                        theta0=0.1   # limits
                        theta1=1.5
                        for i in range(5):
                                testvals.append(r.uniform(theta0,theta1))
                        testvals.sort()
                        print('Testing thetas=',testvals)
                        value=userfunc(testvals)
                        print('Output ximpacts=',value)
                        actual=solfunc(testvals)
                        print('Actual ximpacts=',actual)
                        print()
                        if (not type(value) == type(actual)) or (not len(value)==len(actual)):
                                if wrongreturnform==False:
                                        wrongreturnform=True
                        else:
                                succs.append(all(np.isclose(value,actual,rtol=rtol,atol=atol)))

                        if wrongreturnform:
                                print('Check the returned value format of your function (not counted as an attempt).')
                                        
                        else:
                                succ=all(succs)
                                if succ:
                                        print("Well done, all correct.")                
                                else:
                                        print("Not close enough. Take another look then run this cell again.")                    
                                
                                arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                                score=100-(arec[0]-1)*10
                                if arec[1]:
                                        print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")            
                                        print("Enter this code into Brightspace:\n\n",genenc(2+encoff1,score+encoff2),'\n')
                                else:
                                        print("You have had ",arec[0]," tries.")
                                        print("If next try is accepted you will achieve ",score-10,"% on this exercise.")
                        # Prevent querying of stored internal solution from calling routing
                        #print('Setting to None')
                        actual=None                                
                        solfunc=None
        
        return        
                        
######
#END OF b2 FUNCTION
######                                                                                                                                                        

######
#START OF b3 FUNCTION
######                                                                          

def b3():

    global ps
#USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO    
#   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
    ftrycount=".b3_counter.npy"
    arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file

    #Set tolerance for testing result here (0 for exact integer calcs)
    atol=0.01 
    
    if(waiter()):
        while True:
            try:
                printmd('**CA**')
                value = float(input("Enter a real number here: "))
                actual=0.5
                succ=np.isclose(value,actual,atol=atol)
                if succ:
                    print("Well done. Actual value is ",actual)                
                else:
                    print("Not right yet. Take another look then run this cell again.")
                    
                arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                score=100-(arec[0]-1)*10
                if arec[1]:
                    print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")            
                    print("Enter this code into Brightspace:\n\n",genenc(3+encoff1,score+encoff2),'\n')
                else:
                    print("You have had ",arec[0]," tries.")
                    print("If next try is accepted you will achieve ",score-10,"% on this exercise.")

                break

            except ValueError:
                print("I didn't understand that.")
                continue

        return
        
######
#END OF b3
######




######
#START OF b1 NOT LIVE FUNCTION
######
def b1_notlive():
        print('This CA test is not currently live.')
        return                        
######
#END OF b1 NOT LIVE FUNCTION
######                                                                                                                                                        



######
#START OF b2 NOT LIVE FUNCTION
######
def b2_notlive(userfunc):
        print('This CA test is not currently live.')
        return                        
######
#END OF b2 NOT LIVE FUNCTION
######                                                                                                                                                        
######
#START OF b3 NOT LIVE FUNCTION
######
def b3_notlive():
        print('This CA test is not currently live.')
        return                        
######
#END OF b2 NOT LIVE FUNCTION
######                                                                                                                                                        






def printmd(string):
    display(Markdown(string))

def repeat_to_length(string_to_expand, length):
   return (string_to_expand * ((length//len(string_to_expand))+1))[:length]

def getco(pslen):
    global ps

    #Code for when there is a username known
    #myname=getpass.getuser()
    #myint=int.from_bytes(myname.encode(), 'little')

    #Code for when using random id
    global rid
    myint=rid

    mystr=str(myint)
    mylongstr=repeat_to_length(mystr,pslen)
    ps = [int(i)+1 for i in mylongstr]
    #print('ps ', ps, 'rid', rid)
    
    
    
def waiter():

# SET FORCED TRIAL INTERVAL HERE    
    waittime=20
    
    fname=".ts1.txt"
    if os.path.isfile(fname):
        ts1 = np.loadtxt(fname)
#        print(ts1)
    else:
        ts1=0.0
#        print("no file")

    ts2 = time.time()        
    delt=ts2-ts1
        
    if(delt<waittime):
        print("%.1f  seconds since your last exercise answer.\nYou need to work on your estimate for %.1f seconds before you can try again!" % (delt,waittime))
        return False
    else:
        f = open(fname,'w')
        f.write(str(ts2))
        f.close()
        return True
        
def trycount(fname,succ):
    
    if os.path.isfile(fname):
        arec = np.load(fname)
        #print("Recorded itry,succ= ", arec[0],arec[1])
    else:
        arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file
        arec = [0,False]
        #print("no file")

    if not arec[1]:
        arec[0] += 1
        arec[1]=succ # update success state and count only if not already succeeded

        np.save(fname,arec)

    return arec
        
        

#############
#Damped Harmonic Oscillator
#############

def valdho(M,K):

#USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO    
#   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
    ftrycount=".dho_counter.npy"

    arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file
    
    if(waiter()):
        while True:
            try:
                value = float(input("Please enter your estimate here: "))
                Ccrit=2*np.sqrt(M*K)
                succ=np.isclose(value,Ccrit,0.2)
                if succ:
                    print("Well done, that is close to the critical damping value ",Ccrit)                
                else:
                    print("Sorry, not very close. Take another look then run this cell again.")
                    
                arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                score=100-(arec[0]-1)*10
                if arec[1]:
                    print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")            
                    print("Enter this code into Brightspace:\n\n",genenc(4+encoff1,score+encoff2),'\n')
                else:
                    print("You have had ",arec[0]," tries.")
                    print("If next try is accepted you will achieve ",score-10,"% on this exercise.")

                break

            except ValueError:
                print("I didn't understand that.")
                continue


        return
        
#############
#END Damped Harmonic Oscillator
#############

#############
#Driven Damped Harmonic Oscillator
#############

def valdrivendho(om,gam):

#USING NUMPY LOAD SAVE WITH STRUCTURED ARRAY FOR BINARY IO    
#   SET UNIQUE FILENAME FOR THIS PROBLEM'S TRY COUNTER
    ftrycount=".drivendho_counter.npy"

    arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file
    
    if(waiter()):
        while True:
            try:
                value = float(input("Please enter your estimate here: "))
                omdres= np.sqrt(om**2-2*gam**2)
                succ=np.isclose(value,omdres,0.2)
                if succ:
                    print("Well done, that is close to the resonance value ",omdres)                
                else:
                    print("Sorry, not very close. Take another look then run this cell again.")
                    
                arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful
                score=100-(arec[0]-1)*10
                if arec[1]:
                    print("First success after ",arec[0]," tries, you have ",score,"% on this exercise.")            
                    print("Enter this code into Brightspace:\n\n",genenc(5+encoff1,score+encoff2),'\n')
                else:
                    print("You have had ",arec[0]," tries.")
                    print("If next try is accepted you will achieve ",score-10,"% on this exercise.")

                break

            except ValueError:
                print("I didn't understand that.")
                continue


        return
        
#############
#END Driven Damped Harmonic Oscillator
#############

#############
#NEW NOVEMBER 2019
#CLASS QUIZ
#############



#Attendance quiz, based on https://github.com/jupyter-widgets/ipywidgets/issues/2487

import ipywidgets as widgets
import sys
from IPython.display import display
from IPython.display import clear_output

def create_multipleChoice_widget(qnum,description, options, correct_answer):
    ftrycount='.q{:d}_counter.npy'.format(qnum)
    arec = np.zeros(1,dtype='int8,bool') # itry and succrec: int and bool, output to binary .npy file                                               

    numoptions=len(options)
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        
        a = int(alternativ.value)
        
        succ=a==correct_answer_index
        arec=trycount(ftrycount,succ)  # increment arec[0] only if not already successful                                
        score=max(0,100-(arec[0]-1)*100/numoptions)
        s=alternativ.options[a][0]
        if succ:
            s+=' correct\n'
        else:
            s+=' incorrect\n'
        if arec[1]:
            s+='{:.0f}% on try {:d}'.format(score,arec[0])
        else:
            s+='{:.0f}% remaining'.format(max(0,score-100/numoptions))
   
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="submit")
    check.on_click(check_selection)
    return widgets.VBox([description_out, alternativ, check, feedback_out])
    
######
#START OF q1 FUNCTION
######                                                                                                                                                        
    
    
def runq1():
    qnum=1
    q = create_multipleChoice_widget(qnum,'Complete program:',['n*fac(n+1)','n*fac(n-1)','(n-1)*fac(n)'],'n*fac(n-1)')
    display(q)

######
#END OF q1 FUNCTION
######                                                                                                                                                        
######
#START OF q1 FUNCTION
######                                                                                                                                                        
    
    
def runQ1():
    qnum=1
    q = create_multipleChoice_widget(qnum,'1N=',['m/s^2','kg/m/s^2','kg m/s^2'],'kg m/s^2')
    display(q)

######
#END OF Q1 FUNCTION
######

######
#START OF q2 FUNCTION
######                                                                                                     
def runQ2x():
    qnum=2
    q = create_multipleChoice_widget(qnum,'',['centred','backwards','forwards'],'centred')
    display(q)

######
#END OF Q2 FUNCTION
######                                                                                                                                                        
######
#START OF q3 FUNCTION
######                                                                                                     
def runQ3x():
    qnum=3
    q = create_multipleChoice_widget(qnum,'After the Earth\'s gravity, the main effect on a falling tennis ball is: ',['moon','quantum','drag'],'drag')
    display(q)

######
#END OF Q3 FUNCTION
######                                                                                                                                                        

######
#START OF q4 FUNCTION
######                                                                                                     
def runQ4x():
    qnum=4
    q = create_multipleChoice_widget(qnum,'If position y is given by Asin(wt), then the velocity v is: ',['Acos(wt)','-Awsin(wt)','Awcos(wt)'],'Awcos(wt)')
    display(q)

######
#END OF Q4 FUNCTION
######                                                                                                                                                        
                                                   
    
######
#START OF q5 FUNCTION
######                                                                                                     
def runQ5x():
    qnum=5
    q = create_multipleChoice_widget(qnum,'Newton\'s second law states that force is proportional to ',['everything','position','acceleration'],'acceleration')
    display(q)

######
#END OF Q5 FUNCTION
######                                                                                                                                                        
                                                   
######
#START OF q6 FUNCTION
######                                                                                                     
def runQ6x():
    qnum=6
    q = create_multipleChoice_widget(qnum,'Drag force magnitude increases with ',['speed','height','gravity'],'speed')
    display(q)

######
#END OF Q6 FUNCTION
######                                                                                                                                                        
                                                   
######
#START OF q7 FUNCTION
######                                                                                                     
def runQ7x():
    qnum=7
    q = create_multipleChoice_widget(qnum,'Work has units of ',['Pascals','Newtons','Joules'],'Joules')
    display(q)

######
#END OF Q7 FUNCTION
######                                                                                                                                                        
                                                   
    

#############
#END
#NEW NOVEMBER 2019
#CLASS QUIZ
#############




### NEW GRADE ENCODING STUFF SEPTEMBER 2022 ###


pk= (283355, 839329) # see diyrsa.ipynb


def getrid():
    import random
    global rid
    rid=random.randint(100000, 999999)


def encrypt(plaintext):
    key, n = pk
    nlen=len(str(n))
    if nlen!=6:
        print('Chunk length hardcoded in format conversion to 6 characters.\n May need to adjust here and in getrid range.\n Exiting.\n')
        
    #cipher = [(int(char) ** key) % n for char in str(plaintext)]
    cipher = ['{:06d}'.format((int(char) ** key) % n) for char in str(plaintext)]
    #cipher = ['{:06d}'.format((int(char) ** key) % n for char in plaintext]
    #print(cipher)
    return ''.join(cipher)


def genenc(caid,cagr):
    global rid
    carnstr='{:06d}'.format(rid)
    caidstr='{:02d}'.format(caid)
    cagrstr='{:03d}'.format(cagr)
    #print(carnstr,caidstr,cagrstr)
    castr=carnstr+caidstr+cagrstr
    #print(castr)
    encint = '#'+encrypt(castr)+'#'
    print("Your encrypted message is: ",encint)
    return encint
