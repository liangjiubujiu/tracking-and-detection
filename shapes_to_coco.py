#!/usr/bin/env python3
#todo 补全 annotations images
import datetime
import json
import os
import re
import fnmatch
from PIL import Image
import numpy as np
from pycococreatortools import pycococreatortools
import time
import sys
import shutil

INFO = {
    "description": "Example Dataset",
    "url": "https://github.com/waspinator/pycococreator",
    "version": "0.1.0",
    "year": 2018,
    "contributor": "waspinator",
    "date_created": datetime.datetime.utcnow().isoformat(' ')
}


#todo make sure that the cat 1 and cat 10 are not conflict if there are more than 10 classes.
LICENSES = [
    {
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License",
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/"
    }
]

CATEGORIES = [
    {
        'id': 0,
        'name': 'cat0',
        'supercategory': 'shape',
    },
    {
        'id': 1,
        'name': 'cat1',
        'supercategory': 'shape',
    },
    {
        'id': 2,
        'name': 'cat2',
        'supercategory': 'shape',
    },
      {
        'id': 3,
        'name': 'cat3',
        'supercategory': 'shape',
    },
      {
        'id': 4,
        'name': 'cat4',
        'supercategory': 'shape',
    },
      {
        'id': 5,
        'name': 'cat5',
        'supercategory': 'shape',
    },
      {
        'id': 6,
        'name': 'cat6',
        'supercategory': 'shape',
    },
      {
        'id': 7,
        'name': 'cat7',
        'supercategory': 'shape',
    },
      {
        'id': 8,
        'name': 'cat8',
        'supercategory': 'shape',
    },
      {
        'id': 9,
        'name': 'cat9',
        'supercategory': 'shape',
    },
]

def get_files_list(root,dirs):
    files_path=[]
    files_name=[]
    for dir in dirs:
        dir_path=root+'/'+dir
        files=os.listdir(dir_path)
        # files_name.append(files)
        num=0
        for file in files:
            file_path=dir_path+'/'+file
            files_path.append(file_path)

            file_name=dir+'/'+file
            files_name.append(file_name)
            num+=1
        print(dir_path+':'+str(num))
    return files_path, files_name

def main():

    for d in ["tooth/train", "tooth/val"]:
        ROOT_DIR = os.getcwd() + '/dataset/' + d
        IMAGE_DIR = os.path.join(ROOT_DIR, "images")
        ANNOTATION_DIR = os.path.join(ROOT_DIR, "annotations")
        img_dirs = os.listdir(IMAGE_DIR)
        ann_dirs = os.listdir(ANNOTATION_DIR)
        coco_output = {
            "info": INFO,
            "licenses": LICENSES,
            "categories": CATEGORIES,
            "images": [],
            "annotations": []
        }
        # todo  change the idx from 0 to n so that the list append func can be operated
        image_id = 0
        segmentation_id = 0
        img_files_path, img_files=get_files_list(IMAGE_DIR,img_dirs)
        img_files_path.sort()
        img_files.sort()

        ann_files_path, ann_files=get_files_list(ANNOTATION_DIR,ann_dirs)
        ann_files_path.sort()
        ann_files.sort()

        for idx in range(len(img_files_path)):
            image_filename=img_files_path[idx]
            annotation_filename=ann_files_path[idx]
            image = Image.open(image_filename)
            # image.show()
            # image_info = pycococreatortools.create_image_info(
            #     image_id, os.path.basename(image_filename), image.size)
            image_info = pycococreatortools.create_image_info(
                image_id, img_files[idx], image.size)
            coco_output["images"].append(image_info)


            class_id = [x['id'] for x in CATEGORIES if x['name'] in annotation_filename]
            category_info = {'id': class_id, 'is_crowd': 'crowd' in image_filename}# category_info has two parts id and whether is_crowd
            binary_mask = np.asarray(Image.open(annotation_filename)
                .convert('1')).astype(np.uint8)

            annotation_info = pycococreatortools.create_annotation_info(
                segmentation_id, image_id, category_info, binary_mask,
                image.size, tolerance=2)

            if annotation_info is not None:
                coco_output["annotations"].append(annotation_info)

            segmentation_id = segmentation_id + 1
            image_id = image_id + 1
            with open('{}/instances_shape_{}2018.json'.format(ROOT_DIR,d), 'w') as output_json_file:# put annotation.json file into root=image/ documentary.
                json.dump(coco_output, output_json_file,indent=4)

if __name__ == "__main__":
    since=time.time()
    main()
    time_elapsed=time.time()-since
    print('The code in {} run {:.0f}m {:.0f}s'.format(sys.argv[0][sys.argv[0].rfind(os.sep) + 1:], time_elapsed // 60, time_elapsed % 60))
    # put the two annotated files to the root path
    for d in ["tooth/train", "tooth/val"]:
        ROOT_DIR = os.getcwd() + '/dataset'
        shutil.copy(ROOT_DIR +'/'+d+ '/instances_shape_'+d+'2018.json', ROOT_DIR)




