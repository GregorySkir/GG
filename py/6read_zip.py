import datetime
import zipfile
import csv

def print_info(archive_name):
    if not zipfile.is_zipfile(archive_name):
        return ('not a zipfile')
    zf = zipfile.ZipFile(archive_name, 'r')
    for info in zf.infolist():
        print (info.filename)
        print ('\tComment:\t', info.comment)
        print ('\tModified:\t', datetime.datetime(*info.date_time))
        print ('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
        print ('\tZIP version:\t', info.create_version)
        print ('\tCompressed:\t', info.compress_size, 'bytes')
        print ('\tUncompressed:\t', info.file_size, 'bytes', '\n')


def average_word_count(archive_name):

    with zipfile.ZipFile(archive_name) as zf:
        for filename in zf.namelist():
            if filename.endswith('.csv'):
                with zf.open(filename, 'r') as open_file:
                    count = 0
                    words = 0
                    for line in open_file:
                        count += 1
                        words += len(line.split())
                    # data = zf.read(filename)
                if count > 0:
                    print('file {0:s} has {1:d} lines with an average words count of {2:6.2f}'.format(repr(filename),
                count, words/count))
                else:
                    print('file {!r} is empty'.format(filename))



if __name__ == '__main__':

    my_example = 'Yelp'
    if my_example == 'Gutenberg':
        archive_name = '/Users/Neta/Documents/Teaching/Machine Learning 2018/Assignments/Gutenberg.zip'
        print_info(archive_name)
    else:
        archive_name = '/Users/Neta/Documents/Teaching/Introduction to Data Science /2019-2020/Exercises/yelp.csv.zip'
        average_word_count(archive_name)

