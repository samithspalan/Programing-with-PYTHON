import logging
logging.basicconfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug('start of program')
def factorial(n):
  logging.debug('start of factorial(%s%%)'%(n))
  total=1
  for i in range(n+1):
    total*=i
    logging.debug('i is '+str(i)+',total is'+str(total))
    logging.debug('end of factorial(%s%%)%'(n))
    return total
print(factorial(5))
logging.debug('end of program')