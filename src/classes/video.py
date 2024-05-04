import os
import numpy as np
import cv2
import os
from image import *

class VideoOperations:
    def __init__(self,
            dataset_path='./src/dataset1', 
            ):
        self.dataset_path=dataset_path

    def get_url_videos(self, url_folder):
        content = os.listdir(url_folder)
        url_videos = np.array(content)
        return url_videos

    def save_images_from_url_video(self, url_video, video_name):
        video = cv2.VideoCapture(url_video)
        im_operations = ImageOperations()
        
        img_height = 300
        img_width = 300
        index_image = 0
        index_frame = -1

        img_height = int(img_height / 2)
        img_width = int(img_width / 2)

        while (video.isOpened()):

            ret, frame = video.read()

            if ret == True:
                contours = im_operations.find_image_contours(frame)
                for contour in contours:
                    if len(contour)>5:
                        index_frame += 1
                        M = cv2.moments(contour)
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        if(cY> 210 and cY<1000 and ((index_frame % 1) == 0)):

                            try:
                                
                                # cv2.imshow('Desconocido', frame[cY-img_height:cY+img_height, cX-img_width:cX+img_width, :])
                                cv2.imwrite(f'{self.dataset_path}/{video_name}_{index_image}.jpg', frame[cY-img_height:cY+img_height, cX-img_width:cX+img_width, :])
                            except:
                                print('error Traceback...')
                            index_image += 1
                if cv2.waitKey(1) & 0xff ==ord('q'):
                  break
            else: 
                break

        video.release()
        # cv2.destroyAllWindows()

    

