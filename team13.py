
team_name = 'Team 13' # Only 10 chars displayed.
strategy_name = 'The Good Strat'
strategy_description = 'How does this strategy decide?'

def move(my_history, their_history, my_score, their_score):
    if my_history == '':
        return 'b'
    else:
        if their_history[-1] == 'c':
            return 'b'
        else:
            return their_history[-1]
