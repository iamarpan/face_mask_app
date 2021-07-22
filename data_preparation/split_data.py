import os
import random
from shutil import copyfile
from tqdm import tqdm
PATH = './images'

def prepare_data():
    train_dataset = random.sample(os.listdir(PATH),int(len(os.listdir('./images'))*0.9))
    test_dataset = [a for a in os.listdir(PATH) if a not in train_dataset]
    os.makedirs('dataset/images/train/',exist_ok=True)
    os.makedirs('dataset/images/val/',exist_ok=True)
    os.makedirs('dataset/labels/train/',exist_ok=True)
    os.makedirs('dataset/labels/val/',exist_ok=True)
    for file_name in tqdm(train_dataset):
        txt_file = file_name.split(".")[0] + '.txt'
        copyfile(f'images/{file_name}',f'dataset/images/train/{file_name}')
        copyfile(f'labels/{txt_file}',f'dataset/labels/train/{txt_file}')

    for file_name in tqdm(test_dataset):
        txt_file = file_name.split(".")[0] + '.txt'
        copyfile(f'images/{file_name}',f'dataset/images/val/{file_name}')
        copyfile(f'labels/{txt_file}',f'dataset/labels/val/{txt_file}')


if __name__ == '__main__':
    prepare_data()
