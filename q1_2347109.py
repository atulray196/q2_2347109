#q1
li = [3,  2, 44, 23, 42, 24, 4, 43, 322, 22]
# if the list divisible by 3 or not
for x in li:
    if x % 3 == 0:
        print("the list is divisible by 3")
        break
    else:
        print("the list is not divisible by 3")
# square of even numbers in a list
sum = 0
for x in li:
    if x % 2 == 0:
        sum = sum + (x * x)
print("the sum of even numbers are",sum)
# sum of digits of all even numbers
evensum=0
for x in li:
   if x%2==0:
       while(x>1):
           t=x%10
           evensum=evensum+t
           x=x//10
print("sum of digits of all even numbers",evensum)          
#remove duplicate numbers in a list
unique=[]
for x in li:
    if x not in unique:
        unique.append(x)
print("the list after removing duplicates:",unique) 
#q2. 
#i am adding a dictionary withe the artist name and the album release date which is related to my domain
artist_del={"theweeknd":"21 march 2022","taylorswift":"22 septemper 2021","arijitsingh":"30 april 2024","divine":"21 december 2020"}
print(artist_del)
#creating a function
def albumdate(artistname):
    if artistname in artist_del:
        releasedate=artist_del[artistname]
        print(f"{artistname}'s releasedate is {releasedate}.")
    else:
        print(f"Nno artist with the name '{artistname}' found.")
albumdate("theweeknd")


