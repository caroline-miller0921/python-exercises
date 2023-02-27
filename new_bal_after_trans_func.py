# defining a function that takes the current balance and subtracts the price

def new_bal_after_trans(cur_bal, price):
    float_bal = price.strip('$').replace(',', '')
    float_bal = float(float_bal)
    cur_bal = cur_bal.strip('$').replace(',', '')
    float_curbal = float(cur_bal)
    new_bal = float_curbal - float_bal
    print('$', new_bal)



