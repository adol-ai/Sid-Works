import piexif
import pprint

exif_dict = piexif.load("qwerty_Yo.tiff")
exif = exif_dict["Exif"].get(piexif.ExifIFD.UserComment)
des = bytes(exif).decode("UTF-8")
