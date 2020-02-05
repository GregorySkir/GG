import os
import csv
from pathlib import Path

def read_movies(file_path):
    movies = open(file_path, 'r')
    count = 0
    header = next(movies)
    # header = movies.readline()
    # print(header)
    for row in movies:
        movie_name = row.split('\t')[0]
        print(movie_name)
        count += 1
    movies.close()
    return('number of rows', count)

def my_csv_reader(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = dir_path + '/' + filename
    movies = []
    with open(file_name, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        next(csv_reader)
        for current_row in csv_reader:
            movies.append([current_row[0]])
    return movies


def my_csv_writer(filename, movies):
    dir_path = Path.cwd()
    file_name = dir_path.joinpath(filename + '.csv')
    with open(file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Movies"]) # write headline
        csv_writer.writerows(movies) # write multiple lines

file_name = "movies.txt"
movies = my_csv_reader(file_name)
my_csv_writer("example_movies", movies)
