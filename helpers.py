import os, glob
import pandas as pd

LABEL_MAPPING = {'PNEUMONIA_DOC_YES': 1, 'PNEUMONIA_DOC_NO': 0}

def read_pneumonia_data(directory):
    
    text_files = glob.glob(os.path.join(directory, 'subject*.txt'))
    
    record_data = []
    for text_file in text_files:
        d = {}

        record_id = os.path.splitext(os.path.basename(text_file))[0]
        anno_file = os.path.join(directory, f'{record_id}.ann')
        d['record_id'] = record_id


        with open(text_file) as f:
            d['text'] = f.read()
        with open(anno_file) as f:
            lines = f.readlines()
            d['annotations'] = lines
            for line in lines:
                anno = line.split('\t')[1]
                anno_label = anno.split(' ')[0]
                if anno_label not in LABEL_MAPPING:
                    continue
                
                d['label'] = LABEL_MAPPING[anno_label]

        record_data.append(d)
        
    return pd.DataFrame(record_data)