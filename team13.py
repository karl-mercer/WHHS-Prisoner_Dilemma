
team_name = 'Team 13' # Only 10 chars displayed.
strategy_name = 'The Good Strat'
strategy_description = 'How does this strategy decide?'

def move(my_history, their_history, my_score, their_score):
    if my_history == '':
        return 'b'
    else:
        if my_score >= their_score:
            return their_history[-1]
        else:
            return 'b'
