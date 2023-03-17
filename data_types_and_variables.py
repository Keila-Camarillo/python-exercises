'''
1. Identify the data type of the following values: 
99.9, "False", False, '0', 0, True, 'True', [{}], {'a':[]}
float, str, bool, str, int, bool, str,  list, dict
'''
'''
2. What data type would best represent the following?

A term or phrase typed into a search box - str
Whether or not a user is logged in - bool
A discount amount to apply to a user's shopping cart - float
Whether or not a coupon code is valid - bool
An email address typed into a registration form - str
The price of a product - float
A matrix - list of lists
The email addresses collected from a registration form - list of strings
Information about applicants to Codeup's data science program - dict

'''
'''
3.  For each of the following code blocks:

Read the expression and predict the evaluated results

Execute the expression in a Python REPL
'1' + 2 - error

6 % 4 - 2

type(6 % 4) - int

type(type(6 % 4)) -type

'3 + 4 is ' + 3 + 4 - error

0 < 0 - False

'False' == False - False

True == 'True' - True

5 >= -5 - True

True or "42"- True

6 % 5 - 1

5 < 4 and 1 == 1 - False

'codeup' == 'codeup' and 'codeup' == 'Codeup' - False

4 >= 0 and 1 !== '1' - Error because of the extra '=' 

6 % 3 == 0 - true

5 % 2 != 0  - True

[1] + 2 - error

[1] + [2] - [1,2]

[1] * 2 - [1,1]

[1] * [2] - error

[] + [] == [] - True

{} + {} - error
'''

'''
5. You have rented some movies for your kids:

The Little Mermaid for 3 days
Brother Bear for 5 days
Hercules for 1 day
If the daily fee to rent a movie is 3 dollars, how much will you have to pay?
'''

    
print('True')
little_mermaid = 3
brother_bear = 5
hercules = 1

daily_fees = 3

print('Movie rental fee: ' + str(daily_fees * (little_mermaid + brother_bear + hercules)))

# Review
price_rate = 3
lil_mer = 3
bro_bear = 5
hercules = 1

totalrate = (lil_mer + bro_bear + hercules) * price_rate
print(totalrate)

'''
6.Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.

They pay you the following hourly rates:

Google: 400 dollars
Amazon: 380 dollars
Facebook: 350 dollars
This week you worked: 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

How much will you receive in payment for this week?
'''


work_comp = { 'google': 400, 'amazon': 380, 'facebook': 350 }

work_hrs = {'google': 6, 'amazon': 4, 'facebook': 10}

paycheck = (work_comp['google'] * work_hrs['google']) + (work_comp['amazon'] * work_hrs['amazon']) + (work_comp['facebook'] * work_hrs['facebook'])

print('Weekly paycheck: ' + str(paycheck))

# Review
g_rate = 400
a_rate = 380
fb_rate = 350

g_hrs = 6
az_hrs = 4
fb_hrs = 10

paycheck = (g_rate * g_hrs) + (a_rate * az_hrs) + (fb_rate * fb_hrs)
print(paycheck)

'''
7. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
'''
class_stat = 'not full'
class_sch =  ['monday', 'wednesday']
stu_sch = ['tuesday', 'friday']

if class_stat == 'not full' and class_sch != stu_sch:
    print('Student can enroll')
else:
    print('Student cannot enroll')


# review
class_not_full = True
sch_not_conf = True
enroll = class_not_full and sch_not_conf
print(enroll)
'''
8. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
'''
customers = {
    'cus_1': {'total cart': 3, "Premium MBR": False },
    'cus_2': {'total cart': 1, "Premium MBR": True },
    'cus_3': {'total cart': 1, "Premium MBR": False }
    }
# # customer 1
if customers['cus_1']['Premium MBR'] == True:
    print('Thank you for being a member, an offer is available ')
elif customers['cus_1']['total cart'] >= 2:
    print('Offer is available, become a member today')
else:
    print('Pay full amount')

# customer 2
if customers['cus_2']['Premium MBR'] == True:
    print('Thank you for being a member, an offer is available ')
elif customers['cus_2']['total cart'] >= 2:
    print('Offer is available, become a member today')
else:
    print('Pay full amount')

# customer 3
if customers['cus_3']['Premium MBR'] == True:
    print('Thank you for being a member, an offer is available ')
elif customers['cus_3']['total cart'] >= 2:
    print('Offer is available, become a member today')
else:
    print('Pay full amount')

# review
prem_mbr = True
more_than_2 = True
coupz_not_exp = True
print(coupz_not_exp and (more_than_2 or prem_mbr))
'''
9. Continue working in the data_types_and_variables.py file. Use the following code to follow the instructions below:
Create a variable that holds a boolean value for each of the following conditions:

The password must be at least 5 characters
The username must be no more than 20 characters
The password must not be the same as the username
Bonus Neither the username or password can start or end with whitespace
'''
username = 'codeup'
password = 'notastrongpassword'

if password.strip() == username:
    print("password cannot be username")
elif len(username) > 20:
    print("username too long")
elif len(password.strip()) > 5 and password != username:
    print("Password meets requirements")
else:
    print("Password needs to be at least 5 characters long")

# review
my_un = 'codeup'
my_pass = "blahblah"
check_1 =len(my_pass) > 4
print(check_1)

check_2 =len(my_un) <= 20

check_3 = my_un != my_pass