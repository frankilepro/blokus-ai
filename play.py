import gym
import random


env = gym.make("blokus:blokus-v0")  # Make sure to do: pip install -e blokus in root
observation = env.reset()
while True:
    env.render("human")
    actions = env.ai_possible_indexes()
    if len(actions) == 0:
        actions = [None]

    observation, reward, done, info = env.step(random.choice(actions))

    if done:
        print("game done")
        observation = env.reset()
env.close()
