import gym
import random
import numpy as np
'''import tflearn
from tflearn.layers.core import input_data,dropout,fully_connected
from tflearn.layers.estimator import regression'''
from statistics import mean,median
from collections import Counter


LR=1e-3
env=gym.make('MountainCar-v0')
env.reset()
goal_steps=200
score_requirement=50
initial_games=10000



def initial_population():
    training_data=[]
    scores=[]
    accepted_scores=[]
    for _ in range(initial_games):
        score=0
        prev_observation=[]
        game_memory=[]
        #env.reset()
        for _ in range(goal_steps):
            action=random.randrange(0,2)
            observation,reward,done,info=env.step(action)

            if len(prev_observation)>0:
                game_memory.append([prev_observation,action])
            prev_observation=observation
            score+=1
            if done:
                break
        if score>=score_requirement:
            accepted_scores.append(score)
            for data in game_memory:
                if data[1]==1:
                    output=[0,1]
                elif data[1]==0:
                    output=[1,0]
                training_data.append([data[0],output])
        env.reset()
        scores.append(score)
    training_data_save=np.array(training_data)
##    np.save('saved.npy',training_data_save)
    print('Average accepted scores:',mean(accepted_scores))
    print('Median accepted scores:',median(accepted_scores))
    #print(Counter(accepted_scores))
    q=Counter(accepted_scores)
    for i in sorted(q.keys()):
        print(i,':',q[i])
    return training_data
initial_population()
