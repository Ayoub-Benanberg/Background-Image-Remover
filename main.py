from rembg import remove
from PIL import Image

inputImg = "man.jpg"
outputImage = "urIMGwithotBg.png"

imgOpener = Image.open(inputImg)
output_image = remove(imgOpener)

output_image.save(outputImage)
