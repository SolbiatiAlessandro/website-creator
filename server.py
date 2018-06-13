from flask import Flask, render_template, flash, request

app = Flask(__name__)


@app.route('/')
def main():
	return render_template('index/index.html')


@app.route('/website', methods=["GET","POST"])
def website():
	print("inside website()")
	print(request)
	print(request.form["link"])
	import urllib.request
	contents = urllib.request.urlopen(request.form["link"]).read()
	
	_title = contents.find("<title>")
	title = contents[_title+7:contents.find("\xe2",_title)]

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
	urls = list(set(urls))
	l = len(urls)
	ll = l/4
	A = urls[:ll]
	B = urls[ll:ll*2]
	C = urls[ll*2:ll*3]
	D = urls[ll*3:]
	ABCD = [A,B,C,D]



	return render_template('templated-radius/index.html', torender=ABCD,title=title)
