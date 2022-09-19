import os
from art import Artwork

os.makedirs('exports', exist_ok=True)
for i in range(10):
    filepath = os.path.join("exports", f'test-{i + 1}.png')
    grain = i * 0.1
    art = Artwork((500, 500), grain_level=grain)
    art.save_to_file(filepath)