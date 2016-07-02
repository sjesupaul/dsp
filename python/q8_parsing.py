#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

def read_data(data):
    with open(data) as csvfile:

        rows = []
        name = ''
        min_diff = 1000

        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            rows.append(', '.join(row))

        iterr = iter(rows)
        next(iterr)
        for r in iterr:
            r = r.split(", ")
            diff = abs(int(r[5])-int(r[6]))
            if diff < min_diff:
                min_diff = diff
                name = r[0]

        print(name)
read_data('football.csv')
