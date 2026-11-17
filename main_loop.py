import pandas
import numpy as np
import random

prio = pandas.read_excel("data/stacks_priority.xlsx")
draw = pandas.read_excel("data/stacks_draw.xlsx")
effects = pandas.read_excel("data/stacks_effects.xlsx")

spare_keys_thresh = 2
spare_routes_thresh = 10
more_spare_routes_thresh = 15
good_card_thresh = 20

gof_check = 0.98
shushing_check = 344/492
escape = 0.98

# book_dependent
start_hour = 1
echo_reward = 116


game_state = {
    'actions' : 0,
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
    'hand' : tuple()
    }