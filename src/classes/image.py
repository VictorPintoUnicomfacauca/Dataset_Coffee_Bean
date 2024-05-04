import cv2
import numpy as np



class ImageOperations:
  def __init__(self):
    pass
   

  def otsu_threshold(self, gray):
    thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    _, image_thresholded = cv2.morphologyEx(thresholded, cv2.MORPH_OPEN, kernel, iterations=50)
    return image_thresholded


  def adaptative_threshold(self, gray):
    # th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)
    thresholded = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)
    kernel = np.ones((3, 3), np.uint8)
    image_thresholded = cv2.morphologyEx(thresholded, cv2.MORPH_OPEN, kernel, iterations=50)
    return image_thresholded


  def find_image_contours(self, frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Aplicamos el umbral de OTSU para hallar una estimación aproximada de los objetos en la imagen.
    image_thresholded = self.adaptative_threshold(gray)
    contours,hierarchy=cv2.findContours(image_thresholded,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow('Desconocido', image_thresholded)
    return contours
  
  def load_image_from_path(image_path):
    image = cv2.imread(image_path)
    return image 
    
  def resize_image(self, image, size):

    pass





  
