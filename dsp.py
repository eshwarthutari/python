#2nd march thursday 9.10
#print 'vandemataram' using class
""" class Display:
    def __init__(self):
        print("vandematharam")
#instantiate object
a=Display() """
#print vandemataram 10 times using class
'''
class Displayten():
    def __init__(self):
        self.i=1
    def process(self):
        while self.i<=10:
            print("vandemataram #",self.i)
            self.i+=1
#instantiate object
b=Displayten()
b.process()
'''
#program to display vandematharam n times
'''
class DisplayN():
    def __init__(self):
        self.N=int(input('enter n value: '))
    def intialcounter(self):
        self.i=1
    def main(self):
        while self.i<=self.N:
            print("vandematharam #",self.i)
            self.i+=1
c=DisplayN()
c.intialcounter()
c.main()
'''
#program to print n numbers
'''
class Displaynum():
    def __init__(self):
        self.n=int(input("enter n value: "))
    def inc(self):
        self.i=1
    def main(self):
        while self.i<=self.n:
            print(self.i,end=' ')
            self.i+=1
d=Displaynum()
d.inc()
d.main()
'''
#program to display numbers in the given range
'''
class Displayrange():
    def __init__(self):
        self.a=int(input("enter starting value: "))
        self.b=int(input("enter ending value: "))
    def main(self):
        if self.a<self.b:
            for i in range(self.a,self.b+1):
                print(i,end=" ")
e=Displayrange()
e.main()'''
#program to display numbers in given range reverse:
'''
class Displayrangerev():
    def __init__(self):
        self.a=int(input("enter starting value: "))
        self.b=int(input("enter ending value: "))
    def main(self):
        if self.a>self.b:
            for i in range(self.a,self.b-1,-1):
                print(i,end=" ")
e=Displayrangerev()
e.main()
'''
#odd numbers in given range
'''
class Displayrangeodd():
    def __init__(self):
        self.a=int(input("enter starting value: "))
        self.b=int(input("enter ending value: "))
    def main(self):
        if self.a<self.b:
            for i in range(self.a,self.b+1):
                if i%2!=0:
                    print(i,end=" ")
f=Displayrangeodd()
f.main()
'''
#sum of odd numbers in given range
'''
class Displayrangesumodd():
    def __init__(self):
        self.a=int(input("enter starting value: "))
        self.b=int(input("enter ending value: "))
    def main(self):
        if self.a<self.b:
            sum=0
            for i in range(self.a,self.b+1):
                if i%2!=0:
                    sum=sum+i
        print(sum)
g=Displayrangesumodd()
g.main()
'''
#program to read and check whether it is divisible by 2&5
'''
class Divisible2nd5():
    def __init__(self):
        self.n=int(input("enter your number: "))
    def main(self):
        if (self.n%2==0) & (self.n%5==0):
            print("yes,{} is divisble by 2 &5".format(self.n))
        else:
            print("no")
h=Divisible2nd5()
h.main()
'''
#3rd march friday 1.30pm
#program to find factorrs of a given number
'''
class Factors():
    def __init__(self):
        self.n=int(input("enter your number: "))
    def main(self):
        self.i=1
        while(self.i<=self.n):
            if self.n%self.i==0:
                print(self.i,end=" ")
            self.i+=1
i=Factors()
i.main()
'''
#program to find sum of factors
'''
class Factorsum():
    def __init__(self):
        self.n=int(input("enter your number: "))
    def main(self):
        self.i=1
        self.sum=0
        while(self.i<=self.n):
            if self.n%self.i==0:
                print(self.i,end=" ")
                self.sum+=self.i
            self.i+=1
        print("\n sum of the facctors of {0} is {1}".format(self.n,self.sum))
j=Factorsum()
j.main()'''
#program to check perfecct number
'''
class perfectnum():
    def __init__(self):
        self.n=int(input("enter your number: "))
    def main(self):
        self.i=1
        self.sum=0
        while(self.i<self.n):
            if self.n%self.i==0:
                print(self.i,end=" ")
                self.sum+=self.i
            self.i+=1
        if self.sum==self.n:
            print("\n {} is a perfecr number ".format(self.n))
        else:
            print("\n {} is not a perfecr number ".format(self.n))
k=perfectnum()
k.main()
'''
#program to print sum of digits of a given number
'''class Sumdigits():
    def __init__(self):
        self.n=int(input("enter your number:"))
    def main(self):
        self.sum=0
        while self.n!=0:
            r=self.n%10
            self.sum+=r
            self.n=self.n//10
        print("sum of digits of the number {0} is {1}".format(self.n,self.sum))
l=Sumdigits()
l.main()
'''
#program to find the sum of squares of the digits of the number
'''class Sumsqrdigits():
    def __init__(self):
        self.n=int(input("enter ur number: "))
    def main(self):
        self.sum=0
        while self.n>0:
            r=self.n%10
            self.sum+=r*r
            self.n=self.n//10
        print("sum of the squares of the digits of the given number : ",self.sum)
m=Sumsqrdigits()
m.main()
'''
#program to count digits
'''
class Countdigits():
    def __init__(self):
        self.n=int(input("enter ur number: "))
    def main(self):
        self.count=0
        while self.n>0:
            self.count=self.count+1
            self.n=self.n//10
        print("number of the digits in the given number : ",self.count)
n=Countdigits()
n.main()
'''
#program to evaluate b to the power p
'''
class Bpowerp():
    def __init__(self):
        self.b=int(input("enter b value:"))
        self.p=int(input("enter p value:"))
    def main(self):
        result=1
        c=1
        while c<=self.p:
            result=result*self.b
            c+=1
        print(result)
o=Bpowerp()
o.main()
'''
#program for ARMSTRONG number
'''
class Armstrong():
    def __init__(self):
        self.n=int(input("enter the number : "))
        self.x=self.n
    def counting(self):
        num=self.n
        self.count=0
        while num>0:
            self.count=self.count+1
            num=num//10
        return self.count
    def powerfn(self,b,p):
        result=1
        c=1
        while c<=p:
            result=result*b
            c+=1
        return result
    def main(self):
        sum=0
        p=self.counting()
        while self.n>0:
            r=self.n%10
            sum+=self.powerfn(r,p)
            self.n=self.n//10
        print("sum of the digits of {} is {}".format(self.x,sum))
        if self.x==sum :
            print("{} is a armstrong number".format(self.x))
        else:
            print("{} is NOT a armstrong number".format(self.x))
p=Armstrong()
p.main()
'''
#PROGRAM TO FIND FACTORIAL OF A GIVEN NUMBER BY USING FOR LOOP
'''
class Factorial():
    def __init__(self):
        self.n=int(input("enter your number:"))
    def main(self):
        fact=1
        for i in range(1,self.n+1):
            fact=fact*i
        print("factorial of {} is {}".format(self.n,fact))
q=Factorial()
q.main()'''
#PROGRAM TO PRINT MATHEMAICAL TABLE OF THE GIVEN NUMBER
'''
class table():
    def __init__(self):
        self.n=int(input("enter the number:"))
    def main(self):
        i=1
        while i<=20:
            print("{1} x {0} = {2}".format(i,self.n,self.n*i))
            i=i+1
r=table()
r.main()'''
#PROGRAM TO CHECK WHETHER THE GIVEN NUMBER IS PRIME OR NOT
'''class Primecheck():
    def __init__(self):
        self.n=int(input("enter a number: "))
    def counters(self):
        self.c=2
        self.r=1
    def main(self):
        while self.c<=self.n/2 and self.r!=0:
            self.r=self.n%self.c
            self.c+=1
        if  self.r!=0:
            print("{} is a prime number".format(self.n)) #print("str(self.n)+is a prime number")
        else:
            print("{} is not a prime number".format(self.n))
s=Primecheck()
s.counters()
s.main()
'''
#PROGRAM TO FIND THE G.C.D OF TWO NUMBERS
class lcf():
    def __init__(self):
        self.a=int(input("enter your first number: "))
        self.n2=int(input("enter your second number: "))
    def main(self):
        while (self.a != self.n2):
            if self.a>self.n2:
                self.a=self.a-self.n2
            else:
                self.n2=self.n2-self.a
        print("The Greatest Common Divisor is "+str(self.a))
t=lcf()
t.main()
