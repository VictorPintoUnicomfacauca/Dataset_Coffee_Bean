
from matplotlib import pyplot as plt
import numpy as np
from classes.image import *
from classes.video import *

url_folder = './repo/dulce_cam/'

## Creamos un objeto de la clase VideoOperations
video_operations = VideoOperations()



url_videos = video_operations.get_url_videos(url_folder)

for video_url in url_videos:
   video_operations.save_images_from_url_video(f'./repo/dulce_cam/{video_url}', video_url)
