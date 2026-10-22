D = int(input('Enter the total days =='))

years = D // 365
remaining_days = D % 365
weeks = remaining_days // 7
Days = remaining_days % 7

print (f' {years}Years,{Days}Days , {weeks}Weeks')
