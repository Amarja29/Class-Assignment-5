import logging
import sys
logging.basicConfig(filename='FunPr.log',level=logging.DEBUG,format='%(asctime)s %(message)s %(name)s %(level)s')

try:
    def print1():
        sys.stdout.write("Hello")
except Exception as e:
    print(e)
print1()