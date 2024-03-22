import csv
import chardet
import re


def convert(row):
    

    row_split = row[3].split()
    course_initial = [word[0].upper() for word in row_split]
    course_initial_join = ''.join(course_initial)
    title_h = row[3]
   
    triple_identifier = re.sub(r'[^a-zA-Z]+', '_', title_h)

    triple_string = ''
    
    # Course Identifier
    triple_string = triple_string + "ex:" + triple_identifier + " a ex:Course;\n"
    # Course Name
    triple_string = triple_string + '\tex:courseName "' + row[3] + '";\n'
    # Course Label
    triple_string = triple_string + '\trdfs:label "' + course_initial_join + '";\n'
    # Course comment
    triple_string = triple_string + '\trdfs:comment "Vocabulary for ' + course_initial_join + ' course";\n'
    # Course subject
    triple_string = triple_string + '\tex:courseSubject "' + row[1] + '";\n'
    # Course Number
    triple_string = triple_string + '\tex:courseNumber "' + row[2] + '"^^xsd:integer;\n'
    # Course credit
    triple_string = triple_string + '\tex:courseCredit "' + row[4] + '"^^xsd:integer;\n'
    # Course Description/Pre-requisite
    triple_string = triple_string + '\tex:courseDescription "' + row[5] + '";\n\t.'
    
    return str



with open('csv_to_triple_converter/CU_SR_OPEN_DATA_CATALOG.csv', 'rb') as f:
    encoding = chardet.detect(f.read())['encoding']


with open('csv_to_triple_converter/CU_SR_OPEN_DATA_CATALOG.csv', newline='', encoding=encoding) as csvfile:
    write_str = ''

    csvreader = csv.reader(csvfile)
    

    count = 0
    for row in csvreader:
        count = count + 1

        if count > 1:
            out = convert(row)
            write_str = write_str + out + '\n\n'
        
    # print(write_str)
    with open('csv_to_triple_converter/course_ttl.txt', 'w', encoding='utf-8') as file:
        file.write(write_str)

    print('Write Complete.')