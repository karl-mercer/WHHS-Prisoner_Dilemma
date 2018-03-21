import random
####
# Each team's file must define four tokens:
team_name = 'LoneNotSkylarWolf'
strategy_name = 'The bet strategy'
strategy_description = 'beats everyone'
#move = A function that returns 'c' or 'b'
####

moves = 1 #sets move to 1, to check the count of moves


def move(my_history, their_history, my_score, their_score):
    global moves #sets moves to global variables
    if their_history[-1:] is my_history[-1:]: #checks if their last output is my last output
        moves = moves + 1 #adds one to the move count
        return (my_history[-1:]) #returns the last output the code has given
    elif their_history[-1] is 'c' and my_history[-1:] is 'b': #checks to see if their history is 'c' and my history is 'b'
        moves = moves + 1 #adds 1 to the move count
        return ('c') #returns c as output
    elif (moves%2 is 0) and (moves is not 0): #Checks to see if the number of moves is even
        moves = moves + 1 #adds 1 to the move count
        return (their_history[-1]) #returns their last output
    else: #if none of the above criteria are met, return a random output 'bc'
        moves = moves + 1 #adds 1 to the move count
        return random.choice('bc') #selects a random letter 'bc'
               
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             