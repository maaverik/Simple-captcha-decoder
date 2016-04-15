from PIL import Image
import os, sys

#pass filenames as command line arguments
#print(script name: sys.argv[0])

def enhance(img):
	img = img.convert("RGB")
	pixelData = img.load()
	for x in xrange(img.size[0]):
		for y in xrange(img.size[1]):
			if pixelData[x, y][1] < 136:
				pixelData[x, y] = (0, 0, 0, 255)
	for x in xrange(img.size[0]):
		for y in xrange(img.size[1]):
			if pixelData[x, y][2] > 0:
				pixelData[x, y] = (255, 255, 255, 255)
	return img


def decode(cap):
	cap.save("cap.jpg")
	command = "tesseract cap.jpg stdout"
	os.system(command) 
	os.remove("cap.jpg")


if len(sys.argv) == 1:
	print("Enter captcha filenames as command line arguments to this script")
	sys.exit()

for file in sys.argv[1:]:
	try:
		img = Image.open(file)
	except:
		print("Invalid file" + str(file))
		continue
	print str(file) + " contains text:"	
	captcha = enhance(img)
	decode(captcha)


