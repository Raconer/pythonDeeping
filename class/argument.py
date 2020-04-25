# Argument == 인자, KeyWord Argument


#인자 무한대로 받기 == *args, KeyWord Argument == **kwargs
# ex) plus(1, 2, 3, 4, 5, 6, 7, 8, 9, a=1, b="temp" )
# def plus(*args, **kwargs):
#   print(args) # Tuple 형태
#   print(kwargs) # Dictionary 
#   return a + b

def plus(*args):
  result = 0
  for number in args:
    result += number 

  print(result)


plus(1, 2, 3, 4, 5, 6, 7, 8 ,9)
