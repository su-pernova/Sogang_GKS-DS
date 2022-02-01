def boxPrint(symbol, width, height):
   if len(symbol) != 1:
      raise Exception('Symbol must be a single character')
   if width <= 2:
      raise Exception('Width must be grater than 2')
   if height <= 2:
      raise Exception('Height must be greater than 2')
    
   print(symbol * width)
   for i in range(height -2):
      print(symbol + (' ' * (width-2)) + symbol)
   print(symbol * width)

#main
try: boxPrint('*', 4, 4)
except Exception as e:
   print("Excpetion is", e)
try: boxPrint('X', 2, 3)
except Exception as e:
   print("Exception is", e)
