import time
from multiprocessing.dummy import Pool
from omdb import OMDB
from nfrtitles import  get_nfr_title_list

movie_titles = get_nfr_title_list()

omdb = OMDB("b87452b6")

start_time = time.time()

thread_pool = Pool(32)

def get_rt_score(title):
    movie = omdb.title_search(title)
    return movie.rotten_tomatoes_score

ratings = thread_pool.map(get_rt_score, movie_titles)

end_time = time.time()

total_time = end_time - start_time
print("total time:", total_time)
print(len(ratings), ratings[:20], ratings[-20:])


