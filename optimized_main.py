def optimizedRepeatedValue(arr):

  # Constraint Violations
  if len(arr) > 105:
    return 2
  
  seen = set()
  for num in arr: 
    if num in seen:
      return 0 #Found duplicate
    seen.add(num)
  return 1 # No dupicates

