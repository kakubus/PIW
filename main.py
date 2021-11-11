import cv2
import random
import numpy as np
import ctypes  # An included library with Python install.   




image = cv2.imread('shapes.png', 0)

image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

image_new = image
list_of_colors = []
list_of_colors.append((64,64,64)) #poczytac o listach, bo trzeba zrobic zliczanie kolorkow
counter_without_problems = 0
counter_of_colors = 1
new_color = list(np.random.choice(range(256), size=3))

rows = image.shape[0]
cols = image.shape[1]
n_i = 0
n_j = 0
cols1 = image.shape[1]-1
for i in range(rows):
   
    for j in range(cols):
        
        if image[i][j][0] == 255 and image[i][j][1] == 255 and image[i][j][2] == 255:
            image_new[i][j] = new_color
            
            counter_without_problems = 0
            if image[i][j+1][0] == 0 and image[i][j+1][1] == 0 and image[i][j+1][2] == 0:
                new_color = list(np.random.choice(range(256), size=3)) #losuje nowy kolor jak znajdzie nowy bialy kolor
                counter_of_colors+=1
            if(i>0):
                if (image[i-1][j][0] != 0 and image[i-1][j][1] != 0 and image[i-1][j][2] != 0):
                    image[i][j] = image[i-1][j]
                elif(image[i][j-1][0] != 0 and image[i][j-1][1] != 0 and image[i][j-1][2] != 0):
                    image[i][j] = image[i][j-1] 
                elif(image[i-1][j-1][0] != 0 and image[i-1][j-1][1] != 0 and image[i-1][j-1][2] != 0):
                    image[i][j] = image[i-1][j-1] 
                elif(image[i-1][j+1][0] != 0 and image[i-1][j+1][1] != 0 and image[i-1][j+1][2] != 0):
                    image[i][j] = image[i-1][j+1]
                else:
                    counter_without_problems = 0
                
               # if image[i][j+1][0] == 255 and image[i][j+1][1] == 255 and image[i][j+1][2] == 255:
               #     counter_without_problems+=1
                              
    for k in range(cols1):
        if(k<cols1):
            if(image[i][cols1-k-1][0] == 0 and image[i][cols1-k-1][1] == 0 and image[i][cols1-k-1][2] == 0):
                continue
        if((image[i][cols1-k][0] != 0 and image[i][cols1-k][1] != 0 and image[i][cols1-k][2] != 0) and (image[i][cols1-k][0] != 255 and image[i][cols1-k][1] != 255 and image[i][cols1-k][2] != 255)):  #patrz na prawo jeśli kolor nie jest czarny lub bialy to wtedy trzeba sie cofnac kolorkami
            image[i][(cols1-k)-1] = image[i][cols1-k]
        
       ##działa kod

                  
    
                                                
     
            #while((image[i][j][0] == 255 and image[i][j][1] == 255 and image[i][j][2] == 255) and (image[i+1][j][0] == 255 and image[i+1][j][1] == 255 and image[i+1][j][2] == 255) and i < 512 and j < 512):
               # image_new[i][j] = 254,128,128
                


cv2.imshow('Image', image_new)
ctypes.windll.user32.MessageBoxW(0, "Detected objects: " + str(counter_of_colors) + "\n\nAutorzy:\tAlbert Pintera, Jakub Kaniowski\n| 2021 | Polsl | AiR TI-3 |", "Information " , 1)
cv2.waitKey(0)
cv2.destroyAllWindows()