def is_vowel(my_let):
    if type(my_let) == str:
        if len(my_let) == 1:
            return my_let.lower() in list('aeiou')
        else:
            return False
    else: 
        return False

def calculate_tip(my_bill, my_tip=.2):
    return my_bill * my_tip

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