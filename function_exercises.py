import re
'''1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise. '''
def is_two(str_input):
    if str_input == 2 or str_input == '2':
        return True
    return False

print(is_two(2.0))



'''2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.'''
vowels = 'aeiou'
def is_vowel(str_vowel):
    for char in str_vowel:
        if char in vowels:
            return True
            continue
    return False
            
    
print(is_vowel('mabd'))


'''3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.'''
consonants = 'bcdfghjklmnpqrstvwxyz'
def is_consonant(str_consonant):
    if str_consonant.isalpha() == True:
        for char in str_consonant:
            if char in consonants:
                return True
        return False
    
print(is_consonant('cambodia'))


'''4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.'''
consonants = 'bcdfghjklmnpqrstvwxyz'
def cap_consonant(word):
    if word.isalpha() == True:
        if word[0] in consonants:
            return word.capitalize()
        return 'First letter is not a consonant'
        
print(cap_consonant("keila"))

'''5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.'''
def calculate_tip(tip_per bill_total):
    if 0 < tip_per < 1:
        return tip_per * bill_total
    elif tip_per > 1:
        total_bill = round((tip_per/100) * bill_total, 2)
        return total_bill
    return 'Not valid entry'
    
calculate_tip(20, 28)

'''6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.'''
def apply_discount(original_price, discount_percentage):
    if 0 < discount_percentage < 1:
        discount_amt = discount_percentage * original_price
        return round(original_price - discount_amt, 2) 
    elif discount_percentage > 1:
        discount_amt = (discount_percentage/100) * original_price   
        return round(original_price - discount_amt, 2)
apply_discount(25,0.25)

'''7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.'''

def handle_commas(str_num):
    for char in str_num:
        if char in (','):
            x = re.sub(",", "", str_num)
            if x.isdigit():
                return int(x)
    return "Not a valid entry"

handle_commas('1,000')
    
    
'''8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).'''
def get_letter_grade(grade):
    if isinstance(grade, int) or isinstance(grade, float):
        if grade >= 88:
            return 'A'
        elif 87 >= grade >= 80:
            return 'B'
        elif 79 >= grade >= 67:
            return 'C'
        elif 66 >= grade >= 60:
            return 'D'
        else:
            return 'F'
    return 'Invalid entry'
print(get_letter_grade(88))

'''9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.'''
vowels = 'aeiouAEIOU'
def remove_vowels(word):
    for char in word:
        if char in vowels:
            strip_word = re.sub(r"[aeiouAEIOU]", "", word)
            return strip_word
    return 'No vowels present'
print(remove_vowels('jacksOn'))

'''10. Define a function named normalize_name. It should accept a str+ing and return a valid python identifier, that is:
anything that is not a valid python identifier should be removed
leading and trailing whitespace should be removed
everything should be lowercase
spaces should be replaced with underscores
for example:
Name will become name
First Name will become first_name
% Completed will become completed'''
def normalize_name(name):
    strip_name = name.strip().lower()
    remove_char = re.sub(r"[!@#$%^&*)(><,./?}{\|+=~`]", "", strip_name)
    normal_name = re.sub(r" ", "_", remove_char)
    normal_name = normal_name.strip('_')
    return normal_name
print(normalize_name('% Completed'))

'''11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
cumulative_sum([1, 1, 1]) returns [1, 2, 3]
cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]'''
my_list = [1,2,3,4]

def cumulative_sum(ls):
    total = 0
    some_sums = []
    for num in ls:
        total = total + num
        some_sums.append(total)
    return some_sums

cumulative_sum(my_list)
    