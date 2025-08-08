def q1():
    print("Enter 10 names:\n")
    listnames = []

    for i in range(10):
        listnames.append(input(f"Enter {i+1}th:\t"))
    
    print("\n")
    for nam in listnames:
        splitted = nam.split()
        print(f"First name:\t {splitted[0]}")
        print(f"Last name:\t {splitted[-1]}\n")


    print("\nnames from 3rd to 5th\n")

    i=3
    for nam in listnames[2:5]:
        splitted = nam.split()
        print(f"{i}:")
        i+=1
        print(f"First name:\t {splitted[0]}")
        print(f"Last name:\t {splitted[-1]}\n")

    print("\nnames in reverse\n")

    i=10
    for nam in listnames[::-1]:
        splitted = nam.split()
        print(f"{i}:")
        i-=1
        print(f"First name:\t {splitted[0]}")
        print(f"Last name:\t {splitted[-1]}\n")

    print("\nnames from 8th to 5th\n")

    i=8
    for nam in listnames[7:1:-1]:
        splitted = nam.split()
        print(f"{i}:")
        i-=1
        print(f"First name:\t {splitted[0]}")
        print(f"Last name:\t {splitted[-1]}\n")


"""
a b
c d
e f
g h
i j
k l
m n
o p
q r
s t

"""

def q2():
    print("Enter 5 names:\n")
    tupname = tuple()
    print(type(tupname))

    for i in range(5):
        tupname += ( input(f"Enter {i+1}th:\t")  , )
        
    
    print("\n")
    for nam in tupname:
        splitted = nam.split()
        print(f"First name:\t {splitted[0]}")
        print(f"Last name:\t {splitted[-1]}\n")

    

    # try:
    #     tupname.append("first last")
    # except Exception as e:
    #     print("exceptions raised:\t")
    #     print(e)
    
    # print("\n\ndeleting new names to tuple")

    # try:
    #     tupname.delete("first last")
    # except Exception as e:
    #     print("exceptions raised:\t")
    #     print(e)
    
    print("\n\nadding new names to tuple")
    
    tupname += ( input(f"Enter new name:\t")  , )
    
    print("\n")
    for nam in tupname:
        splitted = nam.split()
        print(f"First name:\t {splitted[0]}")
        print(f"Last name:\t {splitted[-1]}\n")

    
    print("\n\ndeleting new name from tuple")
    na =  input(f"Enter name to del:\t") 
    ind = tupname.index(na)
    tupname = tuple(list(tupname)[:ind]+list(tupname)[ind+1:])
    
    print("\n")
    for nam in tupname:
        splitted = nam.split()
        print(f"First name:\t {splitted[0]}")
        print(f"Last name:\t {splitted[-1]}\n")
        
        
    print("\nprinting 1st to 3rd\n")
    for nam in tupname[0:3]:
        splitted = nam.split()
        print(f"First name:\t {splitted[0]}")
        print(f"Last name:\t {splitted[-1]}\n")
        
    print("\nmodifying\n")
    try:
        tupname[1] = "g h"
    except Exception as e:
        print("exceptions raised:\t")
        print(e)
       
"""
a b
c d
e f
g h
i j
k l
a b

"""



def q3():
    print("Enter names and ages:\n")
    namedict = {}


    for i in range(3):
        namedict[input("Enter name:\t")] = int(input("Enter age:\t"))
        print("\n")
    
    print("Priting all")
    for a,b in namedict.items():
        print(a + "\t:\t" + str(b))
        
        
    
    print("\n\nPriting with age >20")
    for a,b in namedict.items():
        if b>20:
            print(a + "\t:\t" + str(b))
            
    print("\n\nAdding jkl with age 70")
    namedict["jkl"] = 70
    print("\n\nPriting all")
    for a,b in namedict.items():
        print(a + "\t:\t" + str(b))
        
    
    print("\n\nDeleting abc")
    namedict.pop("abc")
    
    print("\n\nPriting all")
    for a,b in namedict.items():
        print(a + "\t:\t" + str(b))
        
    print("\n\nAvg age:\t")
    avg = 0
    for b in namedict.values():
        avg += b
    print( float(avg) / len(namedict))

"""
12
abc
23
def
34
ghi

"""


def q4():
    n = int(input("Enter number of nums:\n"))
    nums = []
    


    for i in range(n):
        nums.append(int(input("Enter a num:\t")))
    print("\n\n\nprinting all even nums")
    for n in nums:
        if n%2 == 0:
            print(n)
    
"""
10
1
2
3
4
5
6
7
8
9
10

"""

def q5():
    n = int(input("Enter number of nums:\n"))
    nums = []
    freq = {}


    for i in range(n):
        num = int(input("Enter a num:\t"))
        nums.append(num)
        
        if freq.get(num):
            freq[num] += 1
        else:
            freq[num] = 1
        
    print("\n\n\nprinting all nums")
    for n,f in freq.items():
        if f>1:
            print(n)


"""
10
1
2
3
4
4
6
7
3
4
1

"""  



def q6():
    s = input("Enter str:\t")
    print("\nReversed str:\t")
    print(s[::-1])
    
    
def q7():
    a = 0
    b = 1
    
    print("fib till 5th\n")
    for i in range(5):
        print(a)
        temp = a
        a = b
        b = temp +a
    
    
    
def q8():
    with open("lol.txt","w") as f:
        s= "Hi, I am currently pursuing my BTech from Jaypee."
        f.write(s)
        
def q99():
    with open("lol1.txt","w") as f:
        for i in range(10): 
            s= f"this is line {i}\n"
            f.write(s)
        
def q9():
    lines = []
    with open("lol1.txt","r") as f:

        lines = f.readlines()

    for l in lines[::-1]:
        print(l)


def q10():
    n = int(input("Enter number of nums:\n"))
    nums = []


    for i in range(n):
        num = int(input("Enter a num:\t"))
        nums.append(num)
        
        
    print([num for num in nums if num % 2 != 0])

"""
10
1
2
3
4
5
6
7
8
9
10

"""
def q11():
    lines = []
    with open("lol1.txt","r") as f:

        filedata = f.read()
        print(f"Chars in file:\t {len(filedata)}")




def q12():

    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    a = {}
    for word in words:
        s = ''.join(sorted(word))
        if s in a:
            a[s].append(word)
        else:
            a[s] = [word]

    res = list(a.values())
    print(res)


if __name__ == "__main__":
    q12()