import pandas
import numpy as np
import random

##
spare_keys_thresh = 2
spare_routes_thresh = 10
more_spare_routes_thresh = 15
start_hour = 1

game_state = {
    'prog' : 0,
    'stage' : 1,
    'keys' : spare_keys_thresh,
    'routes' : more_spare_routes_thresh,
    'echos_tp' : 0,
    'completions' : 0,
    'hour' : start_hour,
    "nightmares" : 0,
    'noises' : 0,
    'chained_counter' : 0,
    'hand' : ["A Discarded Ladder", "A Map Room"]
    }

##

draw = pandas.read_excel("data/stacks_draw.xlsx")
draw['num_conds'] = draw.shape[1] - draw.isna().sum(axis=1) - 2

##


conds = np.array([
    game_state['stage'] == 1,
    game_state['noises'] > 0,
    game_state['noises'] >= 10,
    game_state['hour'] == 10,
    game_state['routes'] >= 6,
    game_state['chained_counter'] == 0
])

while len(game_state['hand']) < 4:

    this_draw = draw[~draw['Name'].isin(game_state['hand'])]
    this_draw = this_draw.reset_index(drop = True)

    draw_mat = this_draw.iloc[:,2:-1]

    draw_mat = draw_mat.to_numpy()



    conds_met = draw_mat == conds
    conds_met = conds_met.sum(axis = 1)

    conds_met = (conds_met == this_draw.num_conds).to_numpy()





    filt_draw = this_draw[conds_met].reset_index(drop = True)
    filt_draw['cum_weight'] = filt_draw['Weight'].cumsum()

    weight_sum = sum(filt_draw['Weight'])

    roll = random.random() * weight_sum



    mask = filt_draw['cum_weight'] > roll
    card = filt_draw['Name'].iloc[np.argmax(mask)]

    game_state['hand'].append(card)

#print(filt_draw.iloc[:,[0,1,9]])
#print(roll)
#print(np.argmax(mask))
#print(card)

print(game_state['hand'])
