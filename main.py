# First attemppt - Brute Force
def repeatedValue(arr):

  # Valid size of array: 1 <= arr <= 105
  if len(arr) > 105:
    print("The array has more than 105 values. Provide a smaller one.")
    return 2  #I chose 2 to be the value returned for the constraints error

  for i in range(len(arr)):

    # Array values must be within [-109, 109]
    if arr[i] < -109 or arr[i] > 109:
      print(
          f"Array value outside valid range [-109, 109]\n\nGiven Array: {arr}")
      return 2

    for j in range(i + 1, len(arr)):
      if arr[i] == arr[j]:
        print(
            f"True: The number {arr[i]} is repeated at least once.\n\nGiven array: {arr}"
        )
        return 1

  print(f"False: No repeated numbers within the array.\n\nGiven array: {arr}")
  return 0

# Optimized for Time Complexity 
def optimizedRepeatedValue(arr):

  # Constraint Violations
  if len(arr) > 105:
    print(2)
    return 2
  
  seen = set()
  for num in arr: 
    if num < -109 or num > 109:
      print(2)
      return 2
    if num in seen:
      print(1)
      return 1 #Found duplicate
    seen.add(num)
  print(0)
  return 0 # No dupicates

nums = [-20, -1, 1, 3, 3, 4, 3, 2, 4, 2]
optimizedRepeatedValue(nums)


