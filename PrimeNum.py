import logging
logging.basicConfig(filename='prime.log',level=logging.DEBUG, format='%(asctime)s %(message)s')

try:
    for i in range(2,101):
        flag=0
        for j in range(2,101):
            if i%j==0 and j!=i:
                flag=1
                break
        if flag==0:
            print(i)
except Exception as e:
    print(e)