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

    # Q6: create new dictionary for faculty info

    faculty_dict = {'Name': [['Degree', 'Title', 'Email']]}
    name = []
    for r in rows:
        temp = r.split(",")
        name.append(temp[0].strip().replace(".", ""))

    del name[0]
    first_name, last_name = [], []
    for n in name:
        temp = n.split(" ")
        last_name.append(temp[len(temp)-1])
        first_name.append(temp[0])

    for i in range(len(last_name)):
        for r in rows:
            faculty_dict[last_name[i]] = [r.split(',')[1:4]]
    #print (faculty_dict)

    # Q7: new dictionary with better keys
    
    professor_dict = {('First Name', 'Last Name'): ['Degree', 'Title', 'Email']}
    names = []
    for j in range(len(first_name)):
        names.append((first_name[j], last_name[j]))

    i=0
    del rows[0]
    for r in rows:
        if i < len(names):
            professor_dict[names[i]] = [r.split(',')[1].strip()]
            professor_dict[names[i]].append(r.split(',')[2][:-16].strip())
            professor_dict[names[i]].append(r.split(',')[3])
            i+=1
    #print(professor_dict)

    # Q8: sort new dictionary by last name

    del professor_dict[(('First Name', 'Last Name'))]
    for k, v in sorted(professor_dict.items(), key=lambda x: x[0][1]):
        print(k, ':', v)

read_data('faculty.csv')
