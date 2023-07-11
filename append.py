import logging
logging.basicConfig(filename='append.log',level=logging.DEBUG,format='%(asctime)s %(message)s %(name)s %(level)s')

try:
    def appendNew(l,a):
        l=l+[a]
        return(l)
except Exception as e:
    print(e)
l=[1,0,7,5,8]
print(appendNew(l,9))

l.sort()
print(l)

arr=[2,3,1,2,1]
for i in arr:
    if arr.count(i)%2==0:
        continue
    else:
        print(i)
s=[1,3,3,4,5,3]

s1="0100010"
ans="1110111"