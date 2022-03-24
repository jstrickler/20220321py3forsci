import time
import asyncio
import aiohttp
from omdb import OMDB
from nfrtitles import  get_nfr_title_list

movie_titles = get_nfr_title_list()

omdb = OMDB("b87452b6")

start_time = time.time()

def get_rt_score(title):
    movie = omdb.title_search(title)
    return movie.rotten_tomatoes_score

def main():



end_time = time.time()

total_time = end_time - start_time
print("total time:", total_time)
print(len(ratings), ratings[:20], ratings[-20:])


