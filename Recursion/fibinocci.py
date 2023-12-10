def fibinocci(n):
  if n == 2:
    return [0,1]
  else:
    array = fibinocci(n-1)
    l = len(array)
    third = array[l-1]+ array[l-2]
    array.append(third)
    return array

def main():
  n=int(input("Enter the number of terms"))
  array = fibinocci(n)
  for  i in array:
    print(i)

main()