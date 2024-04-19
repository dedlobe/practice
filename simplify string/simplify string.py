def simplify_string(input_string):
  n = len(input_string)
  
  while True:
    i = 0
    while i<n-1:
      if input_string[i] == input_string[i+1]:
        input_string = input_string[:i] + input_string[i+2:]
        n = len(input_string)
        break
      i += 1
    else: 
      break

  return input_string

input_length = int(input())
input_string = input()

print(simplify_string(input_string))