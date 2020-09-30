#Write a program to calculate the total salary of a person.
#The user has to enter the basic salary (an integer) and the grade (an uppercase character),
#and depending upon which the total salary is calculated as -'''

#totalSalary = basic + hra + da + allow – pf

#hra   = 20% of basic
#da    = 50% of basic
#allow = 1700 if grade = ‘A’
#allow = 1500 if grade = ‘B’
#allow = 1300 if grade = ‘C' or any other character
#pf    = 11% of basic.'''


EMP = input().strip().split(' ')

basic = int(EMP[0])
grade = EMP[1]

hra = 0.20 * basic
da = 0.50 * basic

allowance = 0

if (grade == 'A'):
    allowance = 1700
elif (grade == 'B'):
    allowance = 1500
else:
    allowance = 1300

pf = 0.11 * basic
totalsalary = basic + hra + da + allowance - pf

ans = round(totalsalary)
print(ans)
