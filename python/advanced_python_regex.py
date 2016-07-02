import csv
import re

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
    
    multi = []
    for d in degree:
        if " " in d:
            multi.append(d)
            temp = d.split(" ")
            degree.extend(temp)
    for m in multi:
        degree.remove(m)
    del degree[0]

    degree_stats = {degree[0]:0}
    for d in degree:
        if d not in degree_stats:
            degree_stats[d] = 1
        else:
            degree_stats[d] += 1

    for keys, values in degree_stats.items():
        print(keys, ": \t", values)
    
    # Q2. Number of different titles

    titles = []
    for r in rows:
        temp = r.split(",")
        titles.append(temp[2][:-16].strip())

    del titles[0]
    count_titles, titleList = 0, {}
    for t in titles:
       if t not in titleList:
           titleList[t] = 1
           count_titles += 1
       else:
           titleList[t] += 1
    print(titleList)
    print('Total = ', count_titles)  
    
    # Q3. Print list of emails

    emails=[]
    for r in rows:
        temp = r.split(",")
        emails.append(temp[3].strip())
    print("\n".join(emails[1:]))

# Q4. Unique domains and their frequencies

    domains = []
    for r in rows:
        temp = r.split(",")
        domains.append(temp[3].split('@', 1)[-1])
    del domains[0]

    count_doms, domList = 0, {}
    for d in domains:
       if d not in domList:
           domList[d] = 1
           count_doms += 1
       else:
           domList[d] += 1
    print(domList)
    print('Total = ', count_doms)

read_data('faculty.csv')

