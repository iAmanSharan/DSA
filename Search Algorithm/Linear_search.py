def linear_search(arr,item):
  for i in arr:
    if arr[i] == item:
      return "item found"

  return "Not found"

arr = [1,2,3,45,4,5,]
item = 12
linear_search(arr,item)