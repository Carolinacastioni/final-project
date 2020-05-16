import cv2
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
import os
import sys
import face_recognition
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns

def importPath(folder):
    path = f"../OUTPUT/images/{folder}/*.jpg"
    list_paths = glob.glob(path)
    return list_paths


def resizeImages(lst, folder_name, dim):
    for i,e in enumerate(lst):
        imge = cv2.imread(e, cv2.IMREAD_UNCHANGED)
        resized = cv2.resize(imge, dim)
        path = f"../OUTPUT/treated_images/{folder_name}"
        cv2.imwrite(os.path.join(path , f'image_{i}.jpg'), resized)
    return 'All images were resized and saved into the new folder'

