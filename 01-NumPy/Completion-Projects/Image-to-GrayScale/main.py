from PIL import Image
import numpy as np
from pathlib import Path

while True:
    imgName = input("Enter Image name with ext: ")

    filePath = Path(f"01-NumPy/Completion-Projects/Image-to-GrayScale/{imgName}")
                    
    if (filePath.exists()):
        break

img = Image.open(f"01-NumPy/Completion-Projects/Image-to-GrayScale/{imgName}")

img_array = np.array(img)

weights = np.array([0.299,0.587,0.114])
grayScaled = np.dot(img_array[:,:,:3], weights)

grayScaled =  grayScaled.astype(np.uint8)

finalImg = Image.fromarray(grayScaled)
finalImg.save(f"01-NumPy/Completion-Projects/Image-to-GrayScale/grayscaled.png")
print("GrayScale Successful")