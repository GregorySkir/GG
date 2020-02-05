#Q1
"""Write the function read_bechdel(file_path) that process the file content for the file movies-bechdel.csv.
 The file can be found in Class examples week 6.

Extract and return the following information as a tuple: total number of movies and average budget.

As this is a csv file, it is better to read it using the csv library (though this is not a must).
You should open the file with a text editor to see its content. You can use visual studio code for that.
Notice that we are printing the results for testing in a different way than the way it is returned by your
 function. """
import csv
def read_bechdel(file_path):
    n=0
    k=0
    a=0
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            n+=1
            k+=int(line[6])
        a=k/n
    return (n,a)
read_bechdel('movies-bechdel.csv')#Total movies: 1794 Average budget: 44826462.61
#Q2
"""Write the function calculate_mean_year(file_path) that processes the file content for the file 
movies-bechdel.csv. 
For each year calculate the following information: number of movies, and average revenues (rounded
 to 2 digits after a period).
The function should return 2 dictionaries: the first would contain the number of movies for each
 year (used as a key). The second would contain the average revenues for each year.
* Noticed that the revenue is the sum of 2 columns: domgross and intgross.
* Pay attention: the columns domgross and intgross contains also null values (called #N/A). 
You should decide what to do with the null values. You can ignore the whole line or only ignore these 
movies when calculating the average revenues, but this is more complicated (you should use a list for that).
* We suggest that you use the years as keys for both dictionaries. Please use them as strings (not int). 
This way, you can go over the keys of one dictionary and get the values from both dictionaries.
* We suggest that you would use the round and sum functions.
For our test, we would check specific years."""
import csv
def calculate_mean_year(file_path):
    mpy = {}
    arpy = {}
    rpy = {}
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            year = line["year"]
            mpy.setdefault(year, 0)
            mpy[year]+=1
            if line["domgross"].isdigit():
                domgross = int(line["domgross"])
            else:
                domgross=0
            if line["intgross"].isdigit():
                intgross = int(line["intgross"]) 
            else:
                intgross=0
            revenue = domgross+intgross
            rpy.setdefault(year, 0)
            rpy[year]+=revenue
        for year in mpy.keys():
            average = rpy[year]/mpy[year]
            arpy[year] = round(average, 2)
    return mpy, arpy
movies_counts, movies_revenues = calculate_mean_year('movies-bechdel.csv')
print(movies_counts['2012'] == 86 and movies_revenues['2012'] == 290968859.77)#True
#Q3
"""Write a function write_revenues_to_file(file_path, movies_counts, movies_revenues) that writes the 
results of question 2 into a csv file with three columns: Year, Number of movies, Average revenues. 
Sort the results by year.
The function has 3 arguments, the first is the path of the new file, the second is the dictionary 
of the counts and the third is a dictionary of the revenues (as returned from question 2).
You should write the columns name (the header) in the first line.
* To sort, user the sorted function.
* Remeber the dictionaries have the same keys, so you can loop over the keys of one dictionary to 
write the values from both of the dictionaries. 
* make sure that your columns are separated by a ',' (without a space).
The tester checks if the file was written and its' content."""
def write_revenues_to_file(file_path, movies_counts, movies_revenues):
    with open(file_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Year","Number of movies","Average revenues"])
        for key in sorted(movies_counts.keys()):
            writer.writerow([key,movies_counts[key],movies_revenues[key]])
        return()
	
write_revenues_to_file(file_path, movies_counts, movies_revenues)#Great!