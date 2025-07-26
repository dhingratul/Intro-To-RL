import gymnasium as gym

env = gym.make("FrozenLake-v1", render_mode="rgb_array", map_name="4x4", is_slippery=False)

print(f"Observation space: {env.observation_space}")
print(f"Action space: {env.action_space}")
print(f"Observation space sample: {env.observation_space.sample()}")
print(f"Action space sample: {env.action_space.sample()}")

obs, info = env.reset()
print(f"Initial observation: {obs}")
print(f"Initial info: {info}")

for i in range(10):
    action = env.action_space.sample()