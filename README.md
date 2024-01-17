Web Scraping Rotten Tomatoes Movies in Theaters with BeautifulSoup :

This Python script, developed in Visual Studio, utilizes the BeautifulSoup library to scrape real-time data from Rotten Tomatoes. The objective is to extract information about currently playing movies from the "Movies in Theaters" section on the Rotten Tomatoes website.

The script begins by making an HTTP request to the targeted webpage, ensuring the link is suitable for scraping. BeautifulSoup is then employed to parse the HTML content, focusing on the "discovery-tiles" div class, where the information about movies resides.

For each movie found within this div, the script extracts and prints the movie name. The extraction is performed by navigating through the HTML structure to locate the relevant elements.

This tool provides a basic foundation for web scraping and data extraction from Rotten Tomatoes, showcasing how Python and BeautifulSoup can be employed for such tasks. Users can further customize and extend the script to collect additional details or integrate it into larger projects involving data analysis, visualization, or automation of movie-related tasks.
