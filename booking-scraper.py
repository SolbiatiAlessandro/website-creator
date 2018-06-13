import urllib.request
contents = urllib.request.urlopen("https://www.booking.com/hotel/it/bilocale-appennini.it.html").read()
images = []
urls = []
start = -1 
while True:
    start = contents.find('images', start + 1)
    if start== -1:
        break
    end = contents.find('"',start)
    images.append(contents[start:end])

for image in images:
	if(image.find("max1024")!=-1 and len(image)<50):
		end = image.find(".jpg")
		urls.append("https://s-ec.bstatic.com/"+image[0:(end+4)])