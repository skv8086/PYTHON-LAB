import  calendar
current_year=2024
final_year = int(input("Enter final year:"))
leap_year=[]
for year in range(current_year,final_year+1):
 if calendar.isleap(year):
   leap_year.append(year)

print(f"leap year from{current_year}to{final_year}:")

for year in leap_year:

 print(year)		