PLACE YOUR CODE HERE

import csv

def read_data(data):
    with open(data) as csvfile:

        rows = []
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            rows.append(', '.join(row))

        for r in rows:
            r.split(',')

        emails = []
        for r in rows:
            temp = r.split(",")
            emails.append(temp[3].strip())

    outfile = open('emails.csv', 'w')
    wr = csv.writer(outfile)
    wr.writerows(zip(emails[1:]))

read_data('faculty.csv')

