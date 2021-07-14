for i in range(1,101):
  #print(i)
  #z= str(i)
  #z= int('FizzBuzz')
  if i%15 == 0:
    z= str(i)
    z = 'FizzBuzz'
    #print(i)
    print(z)
  elif i%3 == 0:
    z= str(i)
    z='Fizz'
    print(z)
  elif i% 5 == 0:
    c = str(i)
    c = 'Buzz'
    print(c)
    #print("Buzz")
  else:
    print(i)