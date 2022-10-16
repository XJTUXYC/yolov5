import os
import random

root_path = '/home/xyc/datasets/robot/images/'
txt_save_path = 'data/robot/'
train_name = os.listdir(root_path + 'train')
train_name.sort()
val_name = os.listdir(root_path + 'val')
val_name.sort()
train_txt = open(txt_save_path + 'train.txt', 'w')
val_txt = open(txt_save_path + 'val.txt', 'w')

for name in train_name:
    train_txt.write(root_path + 'train/' + name + '\n')
for name in val_name:
    val_txt.write(root_path + 'val/' + name + '\n')
    
train_txt.close()
val_txt.close()
