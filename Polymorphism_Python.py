#Function Overloading
def add(a,b):
    return a+b


def add(a,b,c):
    return a+b+c

#add(2,3) will throw an error


def check(a:str):
    print(a)
def check(a:int):
    print(a)

#check("2") WILL GIVE ERROR

#Then how to achive Function Overloading

def add(*args):
    result=0
    for item in args:
        result+=item
    return result
print(add(6,7,8,9))

#OR you can achieve method overloading using

def add_variables(a,b,c=0,d=0):
    print(a+b+c+d)

add_variables(1,2,3,5)   #will result in 11
add_variables(1,2)       #will result in 3
