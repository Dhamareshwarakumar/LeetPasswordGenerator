import math
import random
import os
import platform
from jimner import jimner
import cowsay



def combination(n,r):
    if n==0 or r==0:
        return 0
    else:
        ran=(math.factorial(n))/((math.factorial(n-r))*(math.factorial(r)))
        return int(ran)



def leet(crc):
    if crc=="A" or crc=="a":
        return ['4','/\\','@','/-\\','^','aye','(L','Д']

    elif crc=="B" or crc=="b":
        return ["I3","8","13","|3","ß","!3","(3","/3",")3","|-]","j3","6"]

    elif crc=="C" or crc=="c":
        return ["[","¢","{","<","(","©",]

    elif crc=="D" or crc=="d":
        return [")","|)","(|","[)","I>","|>","?","T)","I7","cl","|}",">","|]"]

    elif crc=="E" or crc=="e":
        return ["3","&","£","€","ë","[-","|=-"]

    elif crc=="F" or crc=="f":
        return ["|=","ƒ","|#","ph","/=","v"]

    elif crc=="G" or crc=="g":
        return ["&","6","(_+","9","C-","gee","(?,","[,","{,","<-","(."]

    elif crc=="H" or crc=="h":
        return ["#","/-/","[-]","]-[",")-(","(-)",":-:","|~|","|-|","]~[","}{","!-!","1-1","\\-/","I+I","/-\\"]

    elif crc=="I" or crc=="i":
        return ["1","[]","|","!","eye","3y3","]["]

    elif crc=="J" or crc=="j":
        return [",_|","_|","._|","._]","_]",",_]","]",";","1",]

    elif crc=="K" or crc=="k":
        return [">|","|<","/<","1<","|c","|(","|{"]

    elif crc=="L" or crc=="l":
        return ["1","£","7","|_","|"]

    elif crc=="M" or crc=="m":
        return ["/\\/\\","/V\\","JVI","[V]","[]V[]","|\\/|","^^","<\\/>","{V}","(v)","(V)","|V|","nn","IVI","|\\|\\","]\\/[","1^1","ITI","JTI"]

    elif crc=="N" or crc=="n":
        return ["^/","|\\|","/\\/","[\\]","<\\>","{\\}","|V","/V","И","^","ท"]

    elif crc=="O" or crc=="o":
        return ["0","Q","()","oh","[]","p","<>","Ø"]

    elif crc=="P" or crc=="p":
        return ["|*","|o","|º","?","|^","|>","|","9","[]D","|°","|7"]

    elif crc=="Q" or crc=="q":
        return ["(_,)","9","()_","2","0_","<|","&"]

    elif crc=="R" or crc=="r":
        return["I2","|`","|~","|?","/2","|^","lz","|9","2","12","®","[z","Я",".-","|2","|-"]

    elif crc=="S" or crc=="s":
        return ["5","$","z","§","ehs","es","2"]

    elif crc=="T" or crc=="t":
        return ["7","+","-|-","']['","†","\"|\"","~|~"]

    elif crc=="U" or crc=="u":
        return ["(_)","|_|","v","L|","µ","บ"]

    elif crc=="V" or crc=="v":
        return ["\\/","|/","\\|"]

    elif crc=="W" or crc=="w":
        return ["\\/\\/","VV","\\N","'//","\\\\'","\\^/","(n)","\\V/","\\X/","\\|/","\\_|_/","\\_:_/","Ш","Щ","uu","2u","\\\\//\\\\//","พ","v²"]

    elif crc=="X" or crc=="x":
        return ["><","Ж","}{","ecks","×","?",")(","]["]

    elif crc=="Y" or crc=="y":
        return ["j","`/","Ч","7","\\|/","¥","\\//"]

    elif crc=="Z" or crc=="z":
        return ["2","7_","-/_","%",">_","s","~/_","-\_","-|_"]

    else:
         return crc



def combinationsGenerator(length):
    arr=[[i] for i in range(length)]
    b=0
    for k in range(length-1):
        c=b
        b=combination(length,k+1)+c
        for i in range(c,b):
            for j in range(arr[i][-1]+1,length):
                arr[i].append(j)
                arr.append(arr[i].copy())
                arr[i].pop()
    return arr



# def product(arr1,arr2):
#     ar=[]
#     for i in arr1:
#         for j in arr2:
#             ar.append([i,j])
#     return ar



def product(a):

    if(len(a)==1):
        return [[i] for i in a[0]]
    arr=[]
    for i in a[0]:
        for j in a[1]:
            arr.append([i,j])

    del(a[0])
    del(a[0])

    while(a!=[]):
        temp=arr.copy()
        arr=[]
        for i in temp:
            for j in a[0]:
                i.append(j)
                temp2=i.copy()
                i.pop()
                arr.append(temp2)
        del(a[0])
        res=[]
    return arr



def asciiArt():
    title=jimner()
    title.get_banner_from_text('Big','Leet')
    title.get_banner_from_text('Big','Password')
    title.get_banner_from_text('Big','Cracker')
    print("=========================================================================================")

    cowsay.cheese("Leet Password Cracker prints all the strings that can be made from given string by replacing with leet speak codes...")



def lencalc(str):
    length=1
    for i in str:
        length*=(len(leet(i))+1)
    return length




def clear():
    if(platform.system()=="Windows"):
        os.system("cls")
    elif(platform.system()=="Linux"):
        os.system("clear")
    else:
        print("Clear Fail")

def cracker(inp):

    a=combinationsGenerator(len(inp))

    for i in a:
        temp=list(inp)
        for j in i:
            temp[j]=leet(temp[j])

        for k in product(temp):
            print(''.join(k))
            print()

    print(lencalc(inp))



def generator(inp):
    ar=[]
    for i in inp:
        ar.append(random.choice(leet(i)))
    return ''.join(ar)

if __name__=="__main__":

    asciiArt()

    inp=input("\n\nEnter a password ")

    print("Select the Below choices to proceed\n")

    print("1. Leet Password Cracker")
    print("2. Leet Password Generator")

    choice=input("\nEnter Your Choice Here: ")

    if(choice=="1"):
        clear()
        cracker(inp)
    elif(choice=="2"):
        clear()
        print(generator(inp))
    else:
        exit()
