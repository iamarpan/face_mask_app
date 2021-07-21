import xml.etree.ElementTree as ET
import os
import csv
from tqdm import tqdm
import pandas as pd

def parse():
    data = []
    classes = ['with_mask','without_mask','mask_weared_incorrect']
    for file_name in tqdm(os.listdir('./annotations'),total=len(os.listdir('./annotations'))):
        xml = ET.parse(f'./annotations/{file_name}')
        xml = xml.getroot()
        image_name = xml.find('filename').text
        
        size = xml.find('size')
        width = int(size[0].text)
        height = int(size[1].text)
        depth  = int(size[2].text)
        text_file = file_name.split(".")[0]+".txt" 
        for obj in xml.findall('object'):
            dataset = {}
            class_name = obj.find('name').text
            box = obj.find('bndbox')
            xmin = int(box.find('xmin').text)
            ymin = int(box.find('ymin').text)
            xmax = int(box.find('xmax').text)
            ymax = int(box.find('ymax').text)
            x_center = round(((xmax + xmin)//2)/width,6)
            y_center = round(((ymax + ymin)//2)/height,6)
            box_width = round((xmax - xmin)/width,6)
            box_height = round((ymax - ymin)/height,6)
            class_label = classes.index(class_name)
            data = [class_label,x_center,y_center,box_width,box_height]
            with open(f'labels/{text_file}','a') as f:
                f.write(str(data[0]) + " " + str(data[1]) + " " + str(data[2]) + " " + str(data[3]) + " " + str(data[4]) + '\n') 
if __name__ == '__main__':
    os.makedirs("labels/",exist_ok=True)
    parse()

