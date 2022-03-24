import argparse
from omdb import OMDB


def main():
    args = get_args()

    omdb = OMDB('b87452b6')

    if args.title:
        movie = omdb.title_search(args.title)
        print(movie)
    elif args.imdb_id:
        movie = omdb.imdb_id_search(args.imdb_id)
        print(movie)
    else:
        movie_list = omdb.keyword_search(args.keyword)
        for movie in movie_list:
            print(movie)


def get_args():
    parser = argparse.ArgumentParser(description="Movie Search")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", dest="title", help="search by title")
    group.add_argument("-i", dest="imdb_id", help="search by IMDB ID")
    group.add_argument("-s", dest="keyword", help="keyword search")
    parser.add_argument("-full_plot", help="Show entire plot", default=False,
                        action="store_true")

    return parser.parse_args()

if __name__ == '__main__':
    main()
