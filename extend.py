import logging
logging.basicConfig(filename='extend.log',level=logging.DEBUG, format='%(name)s %(asctime)s %(message)s %(level)s')

try:
    def ext(l,l1):
        for i in l1:
            l=l+[i]
        return l
except Exception as e:
    print(e)
l=[9,2,6,8]
l1=[4,5,3]
print(ext(l,l1))
