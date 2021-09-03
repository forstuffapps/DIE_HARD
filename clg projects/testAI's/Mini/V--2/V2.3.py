import gym
import random
import numpy as np
'''import tflearn
from tflearn.layers.core import input_data,dropout,fully_connected
from tflearn.layers.estimator import regression'''
from statistics import mean,median
from collections import Counter


LR=1e-3
env=gym.make('CartPole-v0')
env.reset()
goal_steps=200
score_requirement=50
initial_games=10000

