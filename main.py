def repeatedValue(arr):
  
  # Constraints 
  if len(arr) > 105 :
    print("The array is too long. Provide a smaller one.")
    return 1
  
  for i in range(len(arr)):
    if arr[i] < -109 or arr[i] > 109:
      print(f"Array value outside valid range [-109, 109]\nGiven Array: {arr}")
      break
    for j in range(i+1, len(arr)):
      if arr[i] == arr[j]:
        print(f"True: The number {arr[i]} is repeated at least once.")
        return True
      else:
        print("False: No repeated numbers within the array.")
        return False

  return 1

nums = [-200,-1,1,3,3,4,3,2,4,2]
repeatedValue(nums)