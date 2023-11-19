def selection_sort(arr,n):
  for i in range(n):
    selected = arr[i]
    pos = i
    j = i+1
    for j in range(n):
      if selected < arr[j]:
        temp = arr[j]
        arr[i] = arr[j]
        arr[j] = selected
        selected = temp

  return arr

def main():
  size = int(input("Enter the size of array :"))
  print("Enter the unsorted array elements /n")
  arr = []
  for i in range(size):
    x = int(input(f"Enter {i}st element"))
    arr.append(x)

  sorted = selection_sort(arr,size)
  print(sorted)

main()
  