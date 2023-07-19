import piexif
from PIL import Image

exif_dict = piexif.load("qwert.tiff")
exif_dict["Exif"][piexif.ExifIFD.UserComment] = "YoooooVroooo".encode("utf-8")
exif_bytes = piexif.dump(exif_dict)
img = Image.open("qwert.tiff")
img.save("qwerty_Yo.tiff", exif=exif_bytes)


