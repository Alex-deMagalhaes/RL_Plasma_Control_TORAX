import gymnasium as gym
from gymnasium.wrappers import RecordVideo
import gymtorax

# Setup video recording wrapper
env = gym.make('gymtorax/IterHybrid-v0', render_mode="rgb_array")
env = RecordVideo(
    env,
    video_folder="./videos",
    episode_trigger=lambda x: True,  # Record every episode
    name_prefix="plasma_simulation"
)

# Run simulation with automatic video recording
observation, info = env.reset()
terminated = False
while not terminated:
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        break

env.close()
# Video saved automatically to ./videos/plasma_simulation-episode-0.mp4
