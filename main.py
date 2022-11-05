def dududu():
   try:
       num = (input('num->'))
       splitted = num.split()
       integers = map(int, splitted)
       length = len(splitted)
       summary = sum(integers)
       average = summary / length
       print(f'Summary is: {summary}\nAverage is: {average}')

   except Exception as ex:
        print(f'Error: {ex}')
dududu()