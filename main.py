from rembg import remove
from PIL import Image

inputImg = "man.jpg"   # your image name goes here
outputImage = "urIMGwithotBg.png"    # what do you wanna call it 

imgOpener = Image.open(inputImg)
output_image = remove(imgOpener)

output_image.save(outputImage)
