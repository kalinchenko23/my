import itertools
import collections
import re
import sympy
import multiprocessing

# def solve(n):
#     for i in range(1,100):
#         for b in range(1,100):
#             if i**2+n==b**2:
#                 return i**2
#             else:
#                 print(-1)
# print(solve(4))

# Task number 2 rotate latters to make an other word.
# l=['Tokyo', 'Okyot', 'Rome', 'Donlon', 'Kyoto', 'Paris','London']
# def rotate(l):
#     x=[]
#     z=[]
#     for i in l:
#         y=sorted(i.lower())
#         q="".join(y)
#         x.append(q)
#     count=Counter(x)


# print(rotate(l))

#print the highest 5 consecutive numbers
# st=number = "7316717653133062491922511967442657474235534919493496983520368542506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753123457977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257540920752963450"
# def consecutive_numbers(st):
#     result=[]
#     x=list(st)
#     for a,b,c,d,e in zip(x,x[1:],x[2:],x[3:],x[4:]):
#         r=a+b+c+d+e
#         result.append(r)
#     return int(max(result))

# print(consecutive_numbers(st))

#progran that calculates value of the word

# def word_value(string):
#     x={"Q":10, "Z":10,"J":8, "X":8, "k":5,"F":4, "H":4, "V":4, "W":4, "Y":4,"B":3, "C":3, "M":3, "P":3 ,"A":1, "E":1, "D":2,"I":1, "O":1, "U":1, "G":2, "L":1, "N":1, "R":1, "S":1, "T":1}
#     value_of_the_word=0
#     for i in  string:
#         for key,value in x.items():
#             if i.upper()==key:
#                 value_of_the_word+=value
#             elif string=="":
#                 return value_of_the_word
#     return value_of_the_word,len(x)
# print(word_value("return value_of_the_word"))


#convert curencies
# def cur_converter(num,ratio):
#     if len(ratio)>4:
#         r=int(ratio,2)
#         cur=num*r
#         print(f'here your foring currency: {cur}')
#     else:
#         cur=num*int(ratio)
#         print(f'here your foring currency: {cur}')

# cur_converter(35,"11")

#regular expressions
# coment="This website is for losers LOL!"

# def chnage_coment(coment):
#     pattern=re.compile(r'[i,o,e]')
#     matches=pattern.sub(r'',coment)
#     return matches
# print(chnage_coment(coment))


#differance_of_2
# l=[1,2,3,4,[5,6,7],8,9,0,16,14]
# def diferrance(l):
#     result=[]
#     for i in l:
#         for b in l:
#             if i-b==2:
#                 tup=i,b
#                 st=sorted(tup)
#                 result.append(st)
#     return result

# print(diferrance(l))

#best profit
# prices=[3, [10,5],2,20,256]
# def best(prices):
#     p=[]
#     l=[]
#     final=[]
#     for i in prices:
#         while type(i)==int:
#             p.append(i)
#             break
#         while type(i)==list:
#             for q in i:
#                 l.append(q)
#             break
#     if len(l)==0:
#         r=max(p)-min(p)
#         final.append(r)
#     elif len(l)>0:
#         for a in p:
#             for b in l:
#                 r=max(p)-min(p)
#                 r1=max(l)-min(l)
#                 r2=max(p)-min(l)
#                 r3=max(l)-min(p)
#                 final.append(r)
#                 final.append(r1)
#                 final.append(r2)
#                 final.append(r3)

#     return max(final)


# print(best(prices))

#get a mathematical operation out of dirty string

# s="fsdfsd234.9554s4234dfsf234442"
# def mathematical(s):
#     pattern=re.compile(r'[\d.|*|//|/|**|^|+|-]')
#     match=pattern.findall(s)
#     x="".join(match)
#     return str(round(eval(x))),x

# print(mathematical(s))

#total prime

# def total_prime(r):
#     prime=[]
#     not_prime=[]
#     final=[]
#     for i in r:
#         if sympy.isprime(i):
#             prime.append(i)
#     for i in prime:
#         x=str(i)
#         for a in x:
#             if "1" in x:
#                 not_prime.append(int(x))

#             elif "0" in x:
#                 not_prime.append(int(x))

#             y=int(a)
#             if y>1:
#                 for b in range(2, y):
#                     if (y % b) == 0:
#                         z=y
#                         if str(z) in x:
#                             not_prime.append(int(x))
#     set_not_prime=list(set(not_prime))
#     for i in set_not_prime:
#         for b in prime:
#             if b not in set_not_prime:
#                 final.append(b)
#     f=list(set(final))
#     print(f)

# t1=multiprocessing.Process(target=total_prime,args=[range(10, 10000)])

# t1.start()

#break camelcase

# def camel_case(st):


#     pattern= re.compile(r"[A-Z][a-z]*")
#     pattern2= re.compile(r"(^[a-z]*)[A-Z]")
#     match=pattern.findall(st)
#     match2=pattern2.findall(st)
#     # return matc
#     result=match2+match
#     result=" ".join(result)
#     return result



# print(camel_case("nameMax"))


titles = titles = ['The Big Bang Theory', 'How I Met Your Mother', 'Dexter', 'Breaking Bad', 'Doctor Who', 'The Hobbit', 'Pacific Rim', 'Pulp Fiction', 'The Avengers', 'Shining']
def return_match(titles,pattern):
    l=[]

    p=re.compile(r'(.+)('+pattern+'|'+pattern.lower()+')(.+)')
    p1=re.compile(r'('+pattern+'|'+pattern.lower()+')(.+)')
    p2=re.compile(r'(.+)('+pattern+'|'+pattern.lower()+')')
    p3=re.compile(r'('+pattern+'|'+pattern.lower()+')')
    for i in titles:
        match=p.findall(i)
        match1=p1.findall(i)
        match2=p2.findall(i)
        match3=p3.findall(i)
        if match:
            l.append(i)
        elif match1:
            l.append(i)
        elif match2:
            l.append(i)
        elif match3:
            l.append(i)

    return l
print(return_match(titles,"the"))



































