from PIL import Image


img = Image.open("pic.jpg")
if "Raw profile type exif" in img.info:
	rawProfileTypeExif = bytes.fromhex(
		"".join(img.info["Raw profile type exif"].split("\n")[3:])
	)
	if rawProfileTypeExif[:6] != "Exif\x00\x00":
		print("Fix missing EXIF prefix")
		img.info["exif"] = b"Exif\x00\x00"+rawProfileTypeExif
exif = img.getexif()
print(exif)
