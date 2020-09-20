import os
import sys
import requests
import shutil
from tqdm import tqdm

try:
    from google.colab import drive
except:
    pass

if len(sys.argv) != 2:
    print('You must enter the full checkpoint path as a parameter, e.g. /content/drive/My Drive/gpt_2_checkpoint')
    sys.exit(1)

"""Mounts the user's Google Drive in Colaboratory."""
assert 'google.colab' in sys.modules, "You must be in Colaboratory to mount your Google Drive"

drive.mount('/content/drive')

file_path = sys.argv[1]

checkpoint_folder = os.path.join('checkpoint', 'run1')
if not os.path.exists(checkpoint_folder):
    os.makedirs(checkpoint_folder)
checkpoint_folder = checkpoint_folder.replace('\\','/') # needed for Windows
print(checkpoint_folder)
shutil.copytree(file_path, checkpoint_folder)
