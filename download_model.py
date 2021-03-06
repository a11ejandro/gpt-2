import os
import sys
import requests
from tqdm import tqdm

if len(sys.argv) != 2:
    print('You must enter the model name as a parameter, e.g.: download_model.py 117M')
    sys.exit(1)

model = sys.argv[1]

subdir = os.path.join('models', model)
if not os.path.exists(subdir):
    os.makedirs(subdir)
subdir = subdir.replace('\\','/') # needed for Windows
print(subdir)
for filename in ['checkpoint','hparams.json','model-282000.data-00000-of-00001','model-282000.index','model-282000.meta','sp.model','sp.vocab']:

    r = requests.get("https://bereg-fest.ru/" + subdir + "/" + filename, stream=True)

    with open(os.path.join(subdir, filename), 'wb') as f:
        file_size = int(r.headers["content-length"])
        chunk_size = 1000
        with tqdm(ncols=100, desc="Fetching " + filename, total=file_size, unit_scale=True) as pbar:
            # 1k for chunk_size, since Ethernet packet size is around 1500 bytes
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                pbar.update(chunk_size)
