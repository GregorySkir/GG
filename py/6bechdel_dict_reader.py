import csv
from collections import defaultdict
from pathlib import Path

def bechder_read_write(input_filename, output_filename):
    years_gross = defaultdict(int)
    years_count = defaultdict(int)

    with open(input_filename, 'r') as bachdel:
        csv_reader = csv.DictReader(bachdel)
        
        for row in csv_reader:
            if row['intgross'].isdigit() and row['domgross'].isdigit():
                years_gross[(row['year'], row['binary'])] += int(row['intgross']) + int(row['domgross'])
                years_count[(row['year'], row['binary'])] += 1

    with open(output_filename, 'w', newline='') as output:
        header = ['year', 'test', 'number of movies', 'average gross']
        csv_writer = csv.DictWriter(output, fieldnames=header)
        csv_writer.writeheader()
        for year, test in years_gross.keys():
            csv_writer.writerow({'year': year, 'test': test, 'number of movies': years_count[(year, test)], \
            'average gross': years_gross[(year, test)]/years_count[(year, test)]})


movies_path = Path.cwd().joinpath('movies-bechdel.csv')
output_path = Path.cwd().joinpath('bechdel_yearly_gross.csv')
bechder_read_write(movies_path, output_path)
