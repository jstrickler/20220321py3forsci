import time
from omdb import OMDB
from nfrtitles import  get_nfr_title_list

movie_titles = get_nfr_title_list()

omdb = OMDB("b87452b6")

start_time = time.time()

ratings = []
for title in movie_titles:
    movie = omdb.title_search(title)
    ratings.append(movie.rotten_tomatoes_score)

end_time = time.time()

total_time = end_time - start_time
print("total time:", total_time)
print(ratings[:20])


