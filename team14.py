import random

team_name = 'napes' # Only 10 chars displayed.
strategy_name = 'The RNG god'
strategy_description = 'It picks randomly unless I am losing'
                 
def move(my_history, their_history, my_score, their_score):
    if my_score < their_score:
        return random.choice('b''c')
    elif their_score > my_score:
        return ('b')
    else:
        return ('c')