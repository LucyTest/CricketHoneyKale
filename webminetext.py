#This dumps 

from os.path import exists
import sys
from pickle import dump, load
from pattern.web import URL, plaintext
 
#replace theURL with the URL you wan to evaluate 
theURL = 'http://www.foodnetwork.com/recipes/food-network-kitchens/spanish-chicken-and-potato-roast-recipe.html'
s = URL(theURL).download()
s = plaintext(s, keep={'h1':[], 'h2':[], 'strong':[], 'a':['href']})
#print s

file_name = "recipe.html"                  #replace the file extension with whatever kind of save you want (subl,txt,html...)
if exists(file_name):                   
	data = load(open(file_name, "r+"))  
	data = s                            
else:                                   
	data = s                            
	
dump (data, open(file_name, "w+"))         # write the info in data to the file   
#return data  
