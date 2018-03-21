####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'k. mercer' # Only 10 chars displayed.
strategy_name = 'Anatol Rapoport'
strategy_description = 'Collude, relatiate, but maybe forgive.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
#####
#
#                                Strategy 1 - Strategic
#
#####    
    betcount = 0
    if len(their_history)==0:
        return 'b'
    elif their_history[-1] == 'b': #if they have betrayed me in the last round
        for betrayals in their_history: #will examine how many betrayals they have played
            if betrayals == 'b':
                betcount +=1
        print betcount
        if betcount%5 == 0:
            return 'c' #for every 5th betrayal I will not retaliate, but forgive 
        else:
            return 'b'
    else: 
        return 'c'
#####
#
#                               Strategy 2
#
#####
    #if len(my_history)==0: #show a little trust and begin with collusion
    #    return 'c'
    #elif 25>len(my_history)>0: #for the first 25 moves return whatever move they just played
    #    if their_history[-1] == 'b':
    #        return 'b'
    #    else:
    #        return 'c'
    #else:
    #    betcount = 0 #begin counting the number of collusions and betrayals in their history
    #    colcount = 0
    #    for moves in their_history: #examine each move in their history and accumulate a total of betrayals and colludes
    #        if moves == 'b':
    #            betcount +=1
    #        else:
    #            colcount += 1
    #    total = len(their_history)
    #    if betcount/total > 0.5: #if they are betraying more than 25% of the time, then betray also
    #        return 'b'
    #    else:
    #        return 'c'
#####
#
#                               Strategy 3 - Frequency Response (no good or needs work)
#
#####
    #if len(my_history) < 10:
    #    return 'c'
    #betCount, myCount = 0, 0 #counters tracking number of betrayals by both players
    #myCount = 0
    #for bets in their_history:
    #    if bets == 'b':
    #        betCount += 1
    #total = len(their_history)
    #for bets in my_history:
    #    if bets == 'b':
    #        myCount += 1
    #myTotal = len(my_history)
    #betPercent = betCount/total
    #myBets = myCount/myTotal
    #if betPercent < 0.1:
    #    if their_history[-1] == 'b':
    #        return 'c'
    #elif 0.2 > betPercent >= 0.1:
    #    if their_history[-1] == 'b' and myBets >0.1:
    #        return 'b'
    #else:
    #    return 'c'
    
#####   
#
#                               Test Function
#
#####

#def test_move(my_history, their_history, my_score, their_score, result):
#    '''calls move(my_history, their_history, my_score, their_score)
#    from this module. Prints error if return value != result.
#    Returns True or False, dpending on whether result was as expected.
#    '''
#    real_result = move(my_history, their_history, my_score, their_score)
#    if real_result == result:
#        return True
#    else:
#        print("move(" +
#            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
#                       str(my_score), str(their_score)])+
#            ") returned " + "'" + real_result + "'" +
#            " and should have returned '" + result + "'")
#        return False
#
#if __name__ == '__main__':
#     
#    # Test 1: Betray on first move.
#    if test_move(my_history='',
#              their_history='', 
#              my_score=0,
#              their_score=0,
#              result='b'):
#         print 'Test passed'
#     # Test 2: Continue betraying if they collude despite being betrayed.
#    test_move(my_history='bbb',
#              their_history='ccc', 
#              # Note the scores are for testing move().
#              # The history and scores don't need to match unless
#              # that is relevant to the test of move(). Here,
#              # the simulation (if working correctly) would have awarded 
#              # 300 to me and -750 to them. This test will pass if and only if
#              # move('bbb', 'ccc', 0, 0) returns 'b'.
#              my_score=0, 
#              their_score=0,
#              result='b')             