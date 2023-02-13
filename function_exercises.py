#!/usr/bin/env python
# coding: utf-8

# ### 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
# 

# In[6]:


def is_two(num):
    if (num == 2) or (num == '2'):
        return True
    else:
        return False


# In[ ]:


# Could also do the following


# In[10]:


is_two(2)


# In[ ]:


# boolean function

def is_two(num):
    return num == 2 or num == '2'

# will return True or False


# ### 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[5]:


4 in [1, 2, 3, 4]


# In[14]:


def is_vowel(my_let):
    if type(my_let) == str:
        if len(my_let) == 1:
            return my_let.lower() in list('aeiou')
        else:
            return False
    else: 
        return False


# In[16]:


assert is_vowel("A") == True


# ### 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[18]:


def is_consonant(my_let):
    if type(my_let) == str:
        if len(my_let) == 1 and not is_vowel(my_let) and my_let.isalpha():
            return True
        else:
            return False
    else: 
        return False


# ### 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[19]:


def capitalize_starting_consonant(some_word):
    if is_consonant(some_word[0]):
        return some.word.capitalize()
    else:
        return some_word


# ### 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[ ]:


def calcualte_tip(my_bill, my_tip=.2):
    return my_bill * my_tip


# ### 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[ ]:


def apply_discount(og_price, dis_percent=0):
    discount_value == og_price * dis_percent
    new_price = og_price - discount_value
    return new_price


# In[ ]:


# example of a lambda function 


# In[20]:


disc_20_off = lambda x: x - (x*.2)


# In[21]:


'2,000,000,000'.replace(',','')


# ### 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[25]:


def handle_commas(my_string_num):
    # must remove commas first
    my_new_num = my_string_num.replace(',', '')
    return int(my_new_num)  


# In[26]:


handle_commas('1,000,000')


# In[23]:


my_num = input('Enter a number: ')
my_new_num = ''
for digit in my_num:
    if digit == ',':
        continue
    if digit == '.':
        break
    else:
        my_new_num += digit


# ### 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
# 

# In[28]:


def get_letter_grade(my_num_grade):
    if my_num_grade >= 90:
        return 'A'
    elif my_num_grade >= 80:
        return 'B'
    elif my_num_grade >= 70:
        return 'C'
    elif my_num_grade < 60:
        return 'D'
    else:
        return 'F'


# In[29]:


get_letter_grade(54)


# ### 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[31]:


#initialize no_vowels as a empty string

def remove_vowels(some_stuff):
    no_vowels = ''
    for n in some_stuff:
        if is_vowel(n):
            continue
        else:
            no_vowels += n
    return no_vowels


# In[32]:


some_stuff = 'I will take four large pizzas.'
some_stuff += 'a'


# In[33]:


remove_vowels(some_stuff)


# In[ ]:


# OR


# In[ ]:


def remove_vowels(some_word):
    new_string = []
    [new_string.append(letter) fir letter in some_word if not is_vowel():


# ### 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#     - Name will become name
#     - First Name will become first_name
#     - % Completed will become completed

# In[35]:


# in 'abcdefghijklmnopqrstuvwxyz1234567890'

# 'abcdefg'.isidentifier()


# In[ ]:


def normalize_name(n):
    n = n.strip().lower()
    n = 
    new_n = ''
    
    for let in n:
        if let.isdigit() or let.isalpha():
            continue
        
        


# ### 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

# In[41]:


def cumulative_sum(some_list):
    count_sum = 0
    new_list = []
    for i in some_list:
        count_sum += i
        new_list.append(count_sum)
    return new_list


# In[43]:


cumulative_sum([1, 2, 3, 4])


# In[ ]:




