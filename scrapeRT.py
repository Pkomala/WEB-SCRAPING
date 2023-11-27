#The code has been written in Visual Studio

from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.rottentomatoes.com/browse/movies_in_theaters/")
source.raise_for_status() #to check if the link we have is good for scraping

soup = BeautifulSoup(source.text, 'html.parser')
MOVIES = soup.find('div', class_="discovery-tiles")

if MOVIES:
    for movie_div in MOVIES.find_all('div', class_="flex-container"):
        name = movie_div.a.text.strip()  # Extracting movie name
        print("Movie Name:", name)
else:
    print("Couldn't find the specified div class on the webpage.")


