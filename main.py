import sys
import os
from PIL import Image
from tqdm import tqdm
import time


files = os.listdir('img') # list  of file in the directory
print(str(len(files)) +" Images")
total_iterations = len(files)   # Set the total number of iterations
progress_bar = tqdm(total=total_iterations, unit='iteration') # Create a progress bar
for i,file in zip(range(total_iterations),files):    # Perform your task in a loop
    time.sleep(0.1)                                  # Simulate some work being done  
    if file.endswith(('.jpg','.png')):
        imgDir = os.getcwd()+"\img"+'\\'+file
        img = Image.open(imgDir)
        img.thumbnail(size=(1050,1050))
        try:
            os.makedirs("OutFile")
        except:
            pass # print("OutFile already Exist")
        img.save(os.getcwd()+"\\OutFile\\"+file,optimize=True)
    else :
        pass # print(file +"is Not Image")
    progress_bar.update(1)   # Update the progress bar
progress_bar.close() # Close the progress bar
        