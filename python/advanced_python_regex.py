import csv

def read_data(data):
   # COMPLETE THIS FUNCTION
    with open(data) as csvfile:

      rows = []

      reader = csv.reader(csvfile, delimiter=',')
      print(type(reader))
      for row in reader:
        rows.append(', '.join(row))

      for r in rows:
         r.split(',')

    # Q1. Different degrees and frequencies

    degree = []
    for r in rows:
        temp = r.split(",")

        degree.append(temp[1].strip().replace(".", ""))

    del degree[0]
    print(degree)

    degree_stats = {degree[1]:1}
    for d in degree:
        if d not in degree_stats:
            degree_stats[d] = 1
        else:
            degree_stats[d] += 1

    print("\n".join(degree_stats))

    # Q3. Print list of emails

    emails=[]
    for r in rows:
        temp = r.split(",")
        emails.append(temp[3].strip())

    #print("\n".join(emails[1:]))

read_data('faculty.csv')
