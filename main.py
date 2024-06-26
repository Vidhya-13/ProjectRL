from TestEnv import HydroElectric_Test
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--excel_file', type=str, default='validate.xlsx') # Path to the excel file with the test data
args = parser.parse_args()

env = HydroElectric_Test(path_to_test_data=args.excel_file)
total_reward = []
cumulative_reward = []

observation = env.observation()
for i in range(730*24 -1): # Loop through 2 years -> 730 days * 24 hours
    # Choose a random action between -1 (full capacity sell) and 1 (full capacity pump)
    action = env.continuous_action_space.sample()
    # Or choose an action based on the observation using your RL agent!:
    # action = RL_agent.act(observation)
    # The observation is the tuple: [volume, price, hour_of_day, day_of_week, day_of_year, month_of_year, year]
    next_observation, reward, terminated, truncated, info = env.step(action)
    total_reward.append(reward)
    cumulative_reward.append(sum(total_reward))

    done = terminated or truncated
    observation = next_observation

    if done:
        print('Total reward: ', sum(total_reward))
        # Plot the cumulative reward over time
        plt.plot(cumulative_reward)
        plt.xlabel('Time (Hours)')
        plt.show()




