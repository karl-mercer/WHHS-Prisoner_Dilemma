import random

team_name = 'napes' 
strategy_name = 'RNG GOD'
strategy_description = 'It is random unless I am losing'
                 
def move(my_history, their_history, my_score, their_score):
    if my_score < their_score:
        return random.choice('b''c')
    elif their_score > my_score:
        return ('b')
    else:
        return ('c')