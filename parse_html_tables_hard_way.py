import requests
import bs4  # Beautiful soup

URL = "https://www.zillow.com/cumming-ga-30040/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2230040%22%2C%22mapBounds%22%3A%7B%22west%22%3A-84.27754540283203%2C%22east%22%3A-84.08734459716797%2C%22south%22%3A34.186772458482295%2C%22north%22%3A34.23546441452508%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A70825%2C%22regionType%22%3A7%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D"


response = requests.get(URL)

soup = bs4.BeautifulSoup(response.content, 'lxml')

for table in soup.findAll('div'):
    print(table)
    print('-' * 60)
