n=int(input())
s=input()
l=s.split()

b={}
suff={}
c=''
for j in range(n):
    for i in range(len(l[j])):
        a=l[j]
        c=a[i:]
        b.update({i:c})
    q=sorted(b.items(), key=lambda x: x[1])
    suff.update({j:q})


# print(suff)



#the following creates a suffix array for a list of strings
#input
#3
#banana apple orange


#dictionary sort by key and value

# d1={3:"apple",2:"cherry"}

# d1.update({1:"banana"})

# for i in d1:
#     print(i)

# for i in d1:
#     print(d1[i])

# d2={}

# for i in sorted(d1):
#     d2[i]=d1[i]
    
# print(d2)

# d2=dict(sorted(d1.items(),key=lambda x:x[1]))
# print(d2)





d1={3:"apple",2:"cherry"}
d1.update({1:"banana"})

d2=dict(sorted(d1.items())) #sort according to keys
d2=dict(sorted(d1.items(), key = lambda x:x[1])) #sort according to values
print(d2)





s="anagram"
hashS={}
for i in range(len(s)):
    hashS[s[i]]= hashS.get(s[i],0) + 1
print(hashS)

# the above code inserts each character of string s and their occurences
# get function helps to appends the element to dictionary if not found in the dictionary