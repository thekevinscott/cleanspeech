from pathlib import Path
import os
import urllib.request

MODEL_DIR = 'models/research/audioset'
HTTP_DIR = 'https://storage.googleapis.com/audioset'

def downloadIfNotExist(file_name, url):
    config = Path(file_name)
    if not config.is_file():
        print('file %s does not exist, downloading it from %s' % (file_name, url))
        urllib.request.urlretrieve(url, file_name)

downloadIfNotExist('%s/vggish_model.ckpt' % MODEL_DIR, '%s/vggish_model.ckpt' % HTTP_DIR)

downloadIfNotExist('%s/vggish_pca_params.npz' % MODEL_DIR, '%s/vggish_pca_params.npz' % HTTP_DIR)


os.chdir(MODEL_DIR)
os.system('python3 vggish_smoke_test.py')
