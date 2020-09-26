import os
import sys
import requests
import shutil
from tqdm import tqdm

try:
    from google.colab import drive
except:
    pass


"""Mounts the user's Google Drive in Colaboratory."""
assert 'google.colab' in sys.modules, "You must be in Colaboratory to mount your Google Drive"

drive.mount('/content/drive')

file_path = sys.argv[1]
model_name = sys.argv[2]

checkpoint_folder = os.path.join('checkpoint', 'run1')
model_folder = os.path.join('models', model_name)
# if not os.path.exists(checkpoint_folder):
#     os.makedirs(checkpoint_folder)
checkpoint_folder = checkpoint_folder.replace('\\','/') # needed for Windows
model_folder = model_folder.replace('\\','/') # needed for Windows
print(model_folder)
shutil.copytree(file_path, model_folder)
