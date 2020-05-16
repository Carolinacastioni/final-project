import os
import pandas as pd
import numpy as np
from PIL import Image

def getInfo(df):
    user = list(df['user_id'])
    face = list(df['face_id'])
    image = list(df['original_image'])
    info = zip(user, face, image)
    info_set = set(info)
    return info_set