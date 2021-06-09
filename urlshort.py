import pyshorteners, random

#Input Link Here
link = ["youtube.com/hansengianto","instagram.com/fgmindonesia"]


s = pyshorteners.Shortener()

#Converter List
list_url = [s.dagd,s.isgd,s.osdb,s.qpsru,s.tinyurl]

if link is None:
	url = input("Paste Url : ")
	rand = random.choice(list_url)
	print(rand.short(url))
else:
	for x in link:
		rand = random.choice(list_url)
		print(rand.short(x))
