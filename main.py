def repeatedValue(arr):
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] == arr[j]:
        print("true")
        return True
  print("false")
  return False

arr = [1,1,1,3,3,4,3,2,4,2]
repeatedValue(arr)