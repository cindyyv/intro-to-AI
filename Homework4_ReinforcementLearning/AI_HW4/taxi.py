import numpy as np
import os

# from sympy import Q
import gym
import random
from tqdm import tqdm

total_reward = []


class Agent():
    def __init__(self, env, epsilon=0.05, learning_rate=0.8, gamma=0.9):
        """
        Parameters:
            env: target enviornment.
            epsilon: Determinds the explore/expliot rate of the agent.
            learning_rate: Learning rate of the agent.
            gamma: discount rate of the agent.
        """
        self.env = env

        self.epsilon = epsilon
        self.learning_rate = learning_rate
        self.gamma = gamma

        # Initialize qtable  -- Q-table content are all 0
        self.qtable = np.zeros((env.observation_space.n, env.action_space.n))

        # Values for Q Table = state_size (500) * action_size (6)

        # # comment (modification)
        # self.max_epsilon = 1.0
        # self.min_epsilon = 0.01
        # self.decay_rate = 0.01

        self.qvalue_rec = [] # wont be used

    def choose_action(self, state):
        """
        Choose the best action with given state and epsilon.

        Parameters:
            state: A representation of the current state of the enviornment.
            epsilon: Determines the explore/expliot rate of the agent.

            # Epsilon is our way to balance actions between Exploration and Exploitation, 
            # the idea here is according the epsilon number decrease, 
            # our agent will take more Exploitation actions and vice versa.

        Returns:
            action: The action to be evaluated.
        """
        # Begin your code
        randnum = random.uniform(0,1)                   # numpy.random.uniform takes number between 0 and 1
        if randnum > self.epsilon:                      # do exploitation
            action = np.argmax(self.qtable[state])      # take the action with the biggest value of Q-table for current state
        else:                                           # do random choice
            action = env.action_space.sample()

        return action
        pass
        # End your code

    def learn(self, state, action, reward, next_state, done):
        """
        Calculate the new q-value base on the reward and state transformation observered after taking the action.

        Parameters:
            state: The state of the enviornment before taking the action.
            action: The exacuted action.
            reward: Obtained from the enviornment after taking the action.
            next_state: The state of the enviornment after taking the action.
            done: A boolean indicates whether the episode is done.

        Returns:
            None (Don't need to return anything)
        """
        # Begin your code

        if not done:
            self.qtable[state, action] = (1-self.learning_rate)*self.qtable[state, action] + \
                self.learning_rate*(reward + self.gamma*np.max(self.qtable[next_state]))
        else:
            self.qtable[state, action] = (1-self.learning_rate)*self.qtable[state, action] + \
                self.learning_rate*(reward + 0)                 # if done, next state = 0

        pass
        # End your code
        
        # You can add some conditions to decide when to save your table
        if done:
            np.save("./Tables/taxi_table.npy", self.qtable)

    def check_max_Q(self, state):
        """
        - Implement the function calculating the max Q value of given state.
        - Check the max Q value of initial state

        Parameter:
            state: the state to be check.
        Return:
            max_q: the max Q value of given state
        """
        # Begin your code
        max_q = max(self.qtable[state])                       # take the maximum value of qtable using numpy
        # print(self.qtable[state])
        return max_q
        pass
        # End your code


def extract_state(ori_state):
        state = []
        
        if ori_state % 4 == 0:
            state.append('R')
        else:
            state.append('G')
        
        ori_state = ori_state // 4

        if ori_state % 5 == 2:
            state.append('Y')
        else:
            state.append('B')
        
        print(f"Initial state:\ntaxi at (2, 2), passenger at {state[1]}, destination at {state[0]}")
        

def train(env):
    """
    Train the agent on the given environment.

    Paramenters:
        env: the given environment.

    Returns:
        None (Don't need to return anything)
    """
    training_agent = Agent(env)
    episode = 3000
    rewards = []

    # An episode start when you start the environment and 
    # end when your agent arrives in a terminal action such lost the game.
    for ep in tqdm(range(episode)):
        state = env.reset()
        done = False

        count = 0
        while True:
            action = training_agent.choose_action(state)
            next_state, reward, done, _ = env.step(action)

            training_agent.learn(state, action, reward, next_state, done)
            count += reward

            if done:                                    # if done, finish the episode
                rewards.append(count)
                break

            state = next_state                          # new state

        # after updating the q-values using our formula and verify if we finish the episode or not
        # if yes, we increment 1 in the number of episodes and reduce our epsilon number using:
        # training_agent.epsilon = training_agent.min_epsilon + \
        #     (training_agent.max_epsilon - training_agent.min_epsilon) * \
        #     np.exp(-training_agent.decay_rate*(ep + 1))

    total_reward.append(rewards)
    # after running all above code, we have the Q-table ready to be used by agent -> go to test agent


def test(env):
    """
    Test the agent on the given environment.

    Paramenters:
        env: the given environment.

    Returns:
        None (Don't need to return anything)
    """
    testing_agent = Agent(env)
    testing_agent.qtable = np.load("./Tables/taxi_table.npy")
    rewards = []                                                # array to store total reward and visualize it in the end of train

    # exploitation!!
    for _ in range(100):
        state = testing_agent.env.reset()                       # first, reset our environment to make sure agent start from the beginning
        count = 0                                               # store total reward
        while True:
            action = np.argmax(testing_agent.qtable[state])
            next_state, reward, done, _ = testing_agent.env.step(action)
            count += reward
            if done == True:                                    # if episode finishes
                rewards.append(count)
                # print('Score: ', count)
                break

            state = next_state
    # Please change to the assigned initial state in the Google sheet
    # state = 248
    state = 249

    print(f"average reward: {np.mean(rewards)}")
    extract_state(state)
    print(f"max Q:{testing_agent.check_max_Q(state)}")


def seed(seed=118):
    '''
    It is very IMPORTENT to set random seed for reproducibility of your result!
    '''
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    random.seed(seed)


if __name__ == "__main__":
    '''
    The main funtion
    '''
    # Please change to the assigned seed number in the Google sheet
    # SEED = 20
    SEED = 118

    env = gym.make("Taxi-v3")
    seed(SEED)
    env.seed(SEED)
    env.action_space.seed(SEED)
        
    if not os.path.exists("./Tables"):
        os.mkdir("./Tables")

    # training section:
    for _ in range(5):
        train(env)   
    # testing section:
    test(env)
        
    if not os.path.exists("./Rewards"):
        os.mkdir("./Rewards")

    np.save("./Rewards/taxi_rewards.npy", np.array(total_reward))

    env.close()