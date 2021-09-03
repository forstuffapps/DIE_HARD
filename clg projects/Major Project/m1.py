
import gym
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from collections import namedtuple
from time import sleep

RIGHT_CMD = [0, 1]
LEFT_CMD = [1, 0]

# Define Reward Config
BEST_GAMES_TO_EVOLVE = 10

# Define Game Commands
GAME_ACTIONS_MAPPING_TO_ARRAY = [
    [1, 0, 0],  # Movement 0
    [0, 1, 0],  # Movement 1
    [0, 0, 1]   # Movement 2
]

# Initialize Game Environment
env = gym.make('MountainCar-v0')

# Define Structures
GameData = namedtuple('GameData', 'reward data')


def compute_reward(position):
    """
    Compute Reward for Current Position.
    position:
    return:
    """
    # Update Best Position
    if position >= -0.1000000:
        return 6
    if position >= -0.1100000:
        return 5
    if position >= -0.1300000:
        return 4
    if position >= -0.1500000:
        return 3
    if position >= -0.1700000:
        return 2
    if position >= -0.2000000:
        return 1

    return -1


def play_random_games(games=100):
    """
    Play Random Games to Get Some Observations
    games:
    return:
    """

    # Storage for All Games Movements
    all_movements = []

    for episode in range(games):

        # Reset Game Reward
        episode_reward = 0

        # Define Storage for Current Game Data
        current_game_data = []

        # Reset Game Environment
        env.reset()

        # Get First Random Movement
        action = env.action_space.sample()

        while True:

            # Play
            observation, reward, done, info = env.step(action)  # observation=position, velocity

            # Update Reward Value
            reward = compute_reward(observation[[0]])

            # Get Random Action (On Real, its get a "Next" movement to compensate Previous Movement)
            action = env.action_space.sample()

            # Store Observation Data and Action Taken
            current_game_data.append(
                np.hstack((observation, GAME_ACTIONS_MAPPING_TO_ARRAY[action]))
            )

            if done:
                break

            episode_reward += reward

        # Compute Reward
        if episode_reward > -199.0:
            print(f'Reward={episode_reward}')

            # Save All Data
            all_movements.append(
                GameData(episode_reward, current_game_data)
            )

    # Sort Movements Array
    all_movements.sort(key=lambda item: item.reward, reverse=True)

    # Filter the best N games
    all_movements = all_movements[BEST_GAMES_TO_EVOLVE] if len(all_movements) > BEST_GAMES_TO_EVOLVE else all_movements

    # Retrieve only the Game Movements
    movements_only = []
    for single_game_movements in all_movements:
        movements_only.extend([item for item in single_game_movements.data])

    # Create DataFrame
    dataframe = pd.DataFrame(
        movements_only,
        columns=['position', 'velocity', 'action_0', 'action_1', 'action_2']
    )

    return dataframe


def generate_ml(dataframe):
    """
    Train and Generate NN Model
    dataframe:
    return:
    """

    # Define Neural Network Topology
    model = Sequential()
    model.add(Dense(64, input_dim=2, activation='relu'))
    # model.add(Dense(128,  activation='relu'))
    # model.add(Dense(128,  activation='relu'))
    model.add(Dense(64,  activation='relu'))
    model.add(Dense(32,  activation='relu'))
    model.add(Dense(3,  activation='sigmoid'))

    # Compile Neural Network
    model.compile(optimizer='adam', loss='categorical_crossentropy')

    # Fit Model with Data
    model.fit(
        dataframe[['position', 'velocity']],
        dataframe[['action_0', 'action_1', 'action_2']],
        epochs=80
    )

    return model


def play_game(ml_model, games=100):
    """
    Play the Game
    ml_model:
    games:
    return:
    """

    for i_episode in range(games):

        # Define Reward Var
        episode_reward = 0

        # Reset Env for the Game
        observation = env.reset()

        while True:
            #render = env.render()
            #sleep(0.01)

            # Predict Next Movement
            current_action_pred = ml_model.predict(observation.reshape(1, 2))[0]

            # Define Movement
            current_action = np.argmax(current_action_pred)

            # Make Movement
            observation, reward, done, info = env.step(current_action)
            #if 0.5000000<=observation[0]<=0.6000000:
                #w[0]+=1

            # Update Reward Value
            episode_reward += compute_reward(observation[[0]])

            if done:
                if 0.5000000<=observation[0]<=0.6000000:
                    w[0]+=1
                print(f"Episode finished after {i_episode+1} steps", end='')
                break

        print(f" Score = {episode_reward}")
        l.append(episode_reward)


print("[+] Playing Random Games")
df = play_random_games(games=1000)

print("[+] Training NN Model")
ml_model = generate_ml(df)

l=[]
w=[0]
print("[+] Playing Games with NN")
play_game(ml_model=ml_model, games=30)

print(l)


def z1(l):
    q,w,e=0,0,0
    for i in l:
        if i>0:
            q+=1
        if i<0:
            w+=1
        if i==0:
            e+=1
        
    return [q,w,e]

def z2(l):
    q,w,e=0,0,0
    for i in l:
        if i>0:
            q+=i
        if i<0:
            w+=i
        if i==0:
            e+=i
        
    return [q,w,e],q-w,(q-w)/len(l)

def zx(q1):
    #print(sum(q1),len(q1),sum(q1)/len(q1),z1(q1),z2(q1))
    print('Total Average reward ',z2(q1)[2])

zx(l)
print('The total no. of times we won',w)
