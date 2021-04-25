import time
import pickle
import tkinter
import os
import cv2.cv2 as cv2
from unipath import Path
 
ASCII_CHARS=["@","$","#","%","!","*",";",":","."," "]

# Converting video to frames
def videoToFrames(video_path):

    video = cv2.VideoCapture(video_path)
    pic_path = Path(video_path).parent + '/frames'

    if not os.path.exists(pic_path):
        os.makedirs(pic_path)
    count = 1

    while video.isOpened():

        flag, img = video.read()
        if not flag:
            break

        cv2.imwrite(pic_path +'/'+ str(count+100000) + '.jpg',img)
        print(count, 'Succeed!')
        count += 1

# Resize function
def resize(img, new_width = 50):

    width,height = img.shape
    ratio = width/height
    new_height = int(new_width * ratio)
    dim = (new_width,new_height)
    resized_image = cv2.resize(img, dim)
    return(resized_image)

# ASCII interpreter
def pixelsToASCII(img):

    characters = []
    for i in img:
        temp = []
        for j in i:
            temp.append(ASCII_CHARS[j//25])
        characters.append(temp)

    return(characters)
    
# Array -> string
def arrayToString(arr):

    ascii = ''
    for i in arr:
        ascii+= ' '.join(i)
        ascii+='\n'

    return ascii

# Main
def main(new_width = 100):

    path = input("Enter a valid pathname:\n")
    
    try:
        videoToFrames(path)
    except:
        print(path,"is not a valid pathname.") 
    
    total = []
    dirlist = os.listdir(Path(path).parent+"/frames/")
    count = 1
    for eachFile in dirlist:
        eachFile = cv2.imread(Path(path).parent+"/frames/" + eachFile,0)
        try:
            # Format
            ASCII_converted = arrayToString(pixelsToASCII(resize(eachFile))) + "\n"
            total.append(ASCII_converted)
            print(count, "yeet")
            count +=1

        except:
            print("Not it")

    # Save result
    with open(Path(path).parent+'/0.dat', 'wb') as fp:
        pickle.dump(total, fp)

if __name__ == "__main__":
    main()


