import csv
import chardet


def convert(row):
    str = ''
    # for col in row:
    split = row[3].split()
    initial = [word[0].upper() for word in split]
    initial1 = ''.join(initial)
    title_h = row[3].replace(" ", "_")
    # Course Identifier
    str = str + "ex:" + title_h + " a ex:Course;\n"
    # Course Name
    str = str + '\tex:courseName "' + row[3] + '";\n'
    # Course Label
    str = str + '\trdfs:label "' + initial1 + '";\n'
    # Course comment
    str = str + '\trdfs:comment "Vocabulary for ' + initial1 + ' course";\n'
    # Course subject
    str = str + '\tex:courseSubject "' + row[1] + '";\n'
    # Course Number
    str = str + '\tex:courseNumber "' + row[2] + '"^^xsd:integer;\n'
    # Course credit
    str = str + '\tex:courseCredit "' + row[4] + '"^^xsd:integer;\n'
    # Course Description/Pre-requisite
    str = str + '\tex:courseDescription "' + row[7] + '";\n\t.'
    
    return str


# Detect file encoding
with open('csv_to_triple_converter/CU_SR_OPEN_DATA_CATALOG.csv', 'rb') as f:
    encoding = chardet.detect(f.read())['encoding']

# Open the CSV file with detected encoding
with open('csv_to_triple_converter/CU_SR_OPEN_DATA_CATALOG.csv', newline='', encoding=encoding) as csvfile:
    write_str = ''
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)
    
    # Iterate over each row in the CSV file
    count = 0
    for row in csvreader:
        count = count + 1
        # Each row is a list of values corresponding to columns
        if count > 1:
            out = convert(row)
            write_str = write_str + out + '\n\n'
        
    # print(write_str)
    with open('csv_to_triple_converter/course_ttl.txt', 'w', encoding='utf-8') as file:
        file.write(write_str)

    print('Write Complete.')