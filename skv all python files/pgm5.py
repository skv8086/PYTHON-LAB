user_input=input("Enter the list of integers separater by speaces:")
result = []

for num in user_input.split():
   if int(num) > 100:
      result.append("over")
   else:
      result.append(int(num))

print("Modified list:",result)

     