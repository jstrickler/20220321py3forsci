from dataclasses import dataclass
import requests
# from pprint import pprint


@dataclass
class Movie:
    title: str
    year: int
    director: str
    plot: str
    rotten_tomatoes_score: int

class OMDB:
    OMDB_URL = "http://www.omdbapi.com"

    def __init__(self, api_key):
        self.api_key = api_key

    def title_search(self, title, full_plot=False):
        return self.single_search(title, search_type="title", full_plot=full_plot)

    def imdb_id_search(self, imdb_id, full_plot=False):
        return self.single_search(imdb_id, search_type="imdb_id", full_plot=full_plot)

    def single_search(self, search_key, search_type, full_plot=False):
        search_param = 't' if search_type == 'title' else 'i'
        requests_params = {search_param: search_key, "apikey": self.api_key}

        if full_plot:
            requests_params['plot'] = 'full'

        response = requests.get(
            self.OMDB_URL,
            params=requests_params,
        )

        if response.status_code == requests.codes.OK:
            raw_data = response.json()
            return self.parse_movie(raw_data)
        else:
            raise Exception(f"Request failed: {response.status_code}")

    def keyword_search(self, keyword, full_plot=False):
        requests_params = {'s': keyword, "apikey": self.api_key}

        if full_plot:
            requests_params['plot'] = 'full'

        response = requests.get(
            self.OMDB_URL,
            params=requests_params,
        )

        if response.status_code == requests.codes.OK:
            raw_data = response.json()
            # pprint(raw_data)
            movies = []
            for movie_data in raw_data['Search']:
                if 'imdbID' in movie_data:
                    movies.append(self.imdb_id_search(movie_data['imdbID']))
        else:
            raise Exception(f"Request failed: {response.status_code}")
        return movies

    def parse_movie(self, raw_data):
        rt_rating = None
        if 'Ratings' in raw_data:
            for rating in raw_data['Ratings']:
                if rating.get('Source') == "Rotten Tomatoes":
                    rt_rating = int(rating['Value'].rstrip('%'))
                    break
        movie = Movie(
            raw_data.get('Title'),
            raw_data.get('Year'),
            raw_data.get('Director'),
            raw_data.get('Plot'),
            rt_rating,
        )
        return movie


if __name__ == '__main__':
    def display_movie(m):
        print(f"{m.title} ({m.year}): {m.director}")
        print('-' * len(m.title))
        print(m.plot, '\n')


    omdb = OMDB('b87452b6')

    m1 = omdb.title_search("The GodFather", full_plot=True)
    display_movie(m1)

    m2 = omdb.imdb_id_search("tt3896198", full_plot=True)
    display_movie(m2)

    print("=" * 60)
    print("=" * 60)

    movie_list = omdb.keyword_search('avengers')
    for movie in movie_list:
        display_movie(movie)
        print("-" * 10)
