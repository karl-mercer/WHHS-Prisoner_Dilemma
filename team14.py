team_name = 'napes' 
strategy_name = 'Pavlov'
strategy_description = 'It chooses b or c depending on rewards'
                 
def move(my_history, their_history, my_score, their_score):
    if my_history == '':
        return 'c'
    if my_score < their_score:
        if their_history [-1] == 'b':
            return 'b'
        else:
            return 'c'
    if my_score > their_score:
        if their_history [-1] == 'b':
            return 'c'
        else:
            return 'b'
    if my_score == their_score:
        return 'b'
    
        