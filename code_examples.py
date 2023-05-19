from var_voltage_control.voltage_control_env import VoltageControl
import numpy as np


def main():

    # define envs
    env = VoltageControl()

    n_agents = env.get_num_of_agents()
    n_actions = env.get_total_actions()

    n_episodes = 10

    for e in range(n_episodes):
        state, global_state = env.reset()
        max_steps = 100
        episode_reward = 0

        for t in range(max_steps):
            obs = env.get_obs()
            state = env.get_state()

            actions = []
            for agent_id in range(n_agents):
                avail_actions = env.get_avail_agent_actions(agent_id)
                avail_actions_ind = np.nonzero(avail_actions)[0]
                action = np.random.normal(0, 0.5, n_actions)
                action = action[avail_actions_ind]
                actions.append(action)

            actions = np.concatenate(actions, axis=0)
            
            reward, _, info = env.step(actions)

            episode_reward += reward

        print (f"Total reward in epsiode {e} = {episode_reward:.2f}")

    env.close()

if __name__ == '__main__':
    main()