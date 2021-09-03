import gym

LR=1e-3
env=gym.make('MountainCar-v0')
env.reset()
goal_steps=200
score_requirement=50
initial_games=10000


def some_random_games_first():
    for episode in range(10):
        env.reset()
        for t in range(goal_steps):
            env.render()
            action=env.action_space.sample()
            observation,reward,done,info=env.step(action)
            if done:
                break
    env.close()

some_random_games_first()
