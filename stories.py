import csv

all_movies = []

#universal code for character sets
with open("movie.csv", encoding = 'utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:] #all data sets will be appended to all movies when 1:

liked_movies = []

not_liked_movies = []

did_not_watch = []
