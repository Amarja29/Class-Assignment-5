import logging
logging.basicConfig(filename='pop.log',level=logging.DEBUG,format='%(asctime)s %(message)s %(name)s %(level)s')

try:
    def popNew(l):
        l[:]=l[:-1]

except Exception as e:
    print(e)

l=[6,8,9,7]
popNew(l)
print(l)