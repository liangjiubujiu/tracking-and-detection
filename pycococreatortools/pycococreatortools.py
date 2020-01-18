#!/usr/bin/env python3

import os
import re
import datetime
import numpy as np
from itertools import groupby
from skimage import measure
from PIL import Image
from pycocotools import mask
import cv2
import matplotlib.pyplot as plt
import operator

convert = lambda text: int(text) if text.isdigit() else text.lower()
natrual_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]

#todo　显示轮廓
def show_contour(binary_mask,contours):
    fig, axes = plt.subplots(1, 2, figsize=(8, 8))
    ax0, ax1 = axes.ravel()
    ax0.imshow(binary_mask, plt.cm.gray)
    ax0.set_title('original image')

    rows, cols = binary_mask.shape
    ax1.axis([0, rows, cols, 0])
    for n, contour in enumerate(contours):
        ax1.plot(contour[:, 1], contour[:, 0], linewidth=2)
    ax1.axis('image')
    ax1.set_title('contours')
    plt.show()
    return


def resize_binary_mask(array, new_size):
    image = Image.fromarray(array.astype(np.uint8)*255)
    image = image.resize(new_size)
    return np.asarray(image).astype(np.bool_)

def close_contour(contour):

    if not np.array_equal(contour[0], contour[-1]):#判断是否首尾闭合
        contour = np.vstack((contour, contour[0]))

    return contour

def binary_mask_to_rle(binary_mask):
    rle = {'counts': [], 'size': list(binary_mask.shape)}
    counts = rle.get('counts')
    for i, (value, elements) in enumerate(groupby(binary_mask.ravel(order='F'))):
        if i == 0 and value == 1:
                counts.append(0)
        counts.append(len(list(elements)))

    return rle

def binary_mask_to_polygon(binary_mask, tolerance=0):
    """Converts a binary mask to COCO polygon representation

    Args:
        binary_mask: a 2D binary numpy array where '1's represent the object
        tolerance: Maximum distance from original points of polygon to approximated
            polygonal chain. If tolerance is 0, the original coordinate array is returned.

    """
    global binary_mask_copy
    binary_mask_copy=binary_mask
    polygons = []
    # pad mask to close contours of shapes which start and end at an edge
    padded_binary_mask = np.pad(binary_mask, pad_width=1, mode='constant', constant_values=0)#在周围填一圈0
    contours = measure.find_contours(padded_binary_mask, 0.5)# 二值图像，在图像中查找轮廓的级别值,返回多个列表，元素是坐标位置
    # print(contours)
    contours = np.subtract(contours, 1)#　全图矩阵所有元素与１的差值，弥补padding引入的平移误差
    # 显示轮廓
    # show_contour(binary_mask,contours)

    for contour in contours:
        contour = close_contour(contour)
        contour = measure.approximate_polygon(contour, tolerance)#近似具有指定公差tolerance的曲线
        if len(contour) < 3:
            continue
        contour = np.flip(contour, axis=1)#从里向外数，将第二层中按照列表层级进行逆序
        segmentation = contour.ravel().tolist()#ravel将多维数组降成一维　tolist使得数组array->列表list
        # after padding and subtracting 1 we may get -0.5 points in our segmentation，事实证明这一猜测无效
        segmentation = [0 if i < 0 else i for i in segmentation]
        # print(operator.eq(segmentation,segmentation_new))
        polygons.append(segmentation)

    return polygons

def create_image_info(image_id, file_name, image_size, 
                      date_captured=datetime.datetime.utcnow().isoformat(' '),
                      license_id=1, coco_url="", flickr_url=""):

    image_info = {
            "id": image_id,
            "file_name": file_name,
            "width": image_size[0],
            "height": image_size[1],
            "date_captured": date_captured,
            "license": license_id,
            "coco_url": coco_url,
            "flickr_url": flickr_url
    }

    return image_info

def create_annotation_info(annotation_id, image_id, category_info, binary_mask, 
                           image_size=None, tolerance=2, bounding_box=None):
    # binary_mask_copy=binary_mask

    if image_size is not None:
        binary_mask = resize_binary_mask(binary_mask, image_size)


    binary_mask_encoded = mask.encode(np.asfortranarray(binary_mask.astype(np.uint8)))
    area = mask.area(binary_mask_encoded)
    if area < 1:
        return None

    if bounding_box is None:
        bounding_box = mask.toBbox(binary_mask_encoded)
    # plt.figure()
    # plt.imshow(binary_mask)
    # plt.show()

    if category_info["is_crowd"]:
        is_crowd = 1
        segmentation = binary_mask_to_rle(binary_mask)
    else :
        is_crowd = 0
        segmentation = binary_mask_to_polygon(binary_mask, tolerance)
        if not segmentation:
            return None

    annotation_info = {
        "id": annotation_id,
        "image_id": image_id,
        "category_id": category_info["id"],
        "iscrowd": is_crowd,
        "area": area.tolist(),
        "bbox": bounding_box.tolist(),
        "segmentation": segmentation,
        "width": binary_mask.shape[1],
        "height": binary_mask.shape[0],
    } 

    return annotation_info
