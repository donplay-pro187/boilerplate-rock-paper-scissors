# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def abbey_play(count,last_move):
    play = {'S':'P','P':'R','R':'S'}
    if count == 1:
        return (2,last_move)
    else:
        return (1,play[last_move])
    
def kris_play(last_move):
    beat = {'S':'P','P':'R','R':'S'}
    return beat[last_move]

def mrugesh_play(count,last_move):
    play = {'S':'P','P':'R','R':'S'}
    if count<5:
        return (count+1,last_move)
    else:
        return (1,play[last_move])

def quincy_play(count):
    moves = ['P','P','S','S','R']
    return (count+1,moves[(count+1)%5])
    
def player(prev_opponent_play, opponent_history=[], my_history=[],predict_opp=[]):
    if not prev_opponent_play:
        predict_opp.clear()
        my_history.clear()
        opponent_history.clear()
    if prev_opponent_play:
        opponent_history.append(prev_opponent_play)
    if(len(opponent_history)<10):
        return 'S'
    elif len(opponent_history)==10:
        s_count,r_count,p_count = 0,0,0 
        for i in opponent_history:
            if i=='R':
                r_count+=1
            elif i=='S':
                s_count+=1
            else:
                p_count+=1
        if r_count == len(opponent_history):
            my_history.clear()
            predict_opp.append({'name':'mrugesh','count':1})
            my_history.append('P')
            return 'P'
        
        elif r_count == (len(opponent_history)-1):
            my_history.clear()
            predict_opp.append({'name':'kris'})
            my_history.append('P')
            return 'P'
        
        elif s_count == 0 and r_count>(len(opponent_history)-3):
            my_history.clear()
            predict_opp.append({'name':'abbey','count':1})
            my_history.append('S')
            return 'S'
        
        else:
            my_history.clear()
            predict_opp.append({'name':'quincy','count':11})
            return 'P'
    else:
        if predict_opp[0]['name'] == 'abbey':
            count,my_move = abbey_play(predict_opp[0]['count'],my_history[-1])
            predict_opp[0]['count'] = count 
            my_history.append(my_move)
            return my_move
        
        elif predict_opp[0]['name'] == 'kris':
            my_move = kris_play(my_history[-1])
            my_history.append(my_move)
            return my_move
        
        elif predict_opp[0]['name'] == 'mrugesh':
            count,my_move = mrugesh_play(predict_opp[0]['count'],my_history[-1])
            my_history.append(my_move)
            predict_opp[0]['count'] = count 
            return my_move
        
        else:
            count,my_move = quincy_play(predict_opp[0]['count'])
            my_history.append(my_move)
            predict_opp[0]['count'] = count 
            return my_move