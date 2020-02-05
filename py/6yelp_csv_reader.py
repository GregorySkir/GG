import zipfile
import csv
import io
from collections import defaultdict

def read_csv_from_zip(archive_name):
    """ Reads yelp zipped file and makes simple calculations
    """

    businesses = defaultdict(int)  # initialzing out dictionary
    with zipfile.ZipFile(archive_name) as my_zipfile: # opening the zipfile
        for filename in my_zipfile.namelist():  # going over all the file in the zipfile (we only have 1 file)
            yelp_file = my_zipfile.open(filename, 'r')
            yelp_file = io.TextIOWrapper(yelp_file, encoding='utf-8') # opening archived file to be read as str not bytes
            csv_reader = csv.DictReader(yelp_file)
            print(csv_reader.fieldnames)
            count = 0 # counts how many rows
            for row in csv_reader:  # readling line by line
                # print(row)
                businesses[row['business_id']] += 1  # counting how many reviews for each bussiness
                count+=1
            yelp_file.close()

    return(count, len(businesses), sum(businesses.values())/len(businesses))

def read_csv(csv_name):
    """ Reads yelp csv file and makes simple calculations
    """ 
    businesses = defaultdict(int)  # initialzing out dictionary

    with open(csv_name, 'r', encoding='utf-8') as yelp_file:
        reader = csv.DictReader(yelp_file)
        count = 0 # counts how many rows
        print(reader.fieldnames)
        for row in reader:
            businesses[row['business_id']] += 1
            count+=1
    return(count, len(businesses), sum(businesses.values())/len(businesses))


archive_name = '/Users/Neta/Documents/Teaching/Introduction to Data Science /2018-2019/Exercises/yelp.csv.zip'
csv_name = '/Users/Neta/Documents/Teaching/Introduction to Data Science /2018-2019/Exercises/yelp.csv'

# print(read_csv_from_zip(archive_name))
print(read_csv(csv_name))


