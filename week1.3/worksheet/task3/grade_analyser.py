# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file

# open the file

# read in the data, and for each student calculate their average grade and classification

import csv

filename = input("Enter a filename")
output_filename  = filename + "_out.csv"



with open(filename, "r") as file:
    reader = csv.reader(file)
    next(reader)

    with open (output_filename, "w") as outputFile:
            writer = csv.writer(outputFile)
            for row in reader:
                studentId = row[0]
                grades = row[1:]
                total = 0
                numberOfGrades = 0
                for grade in grades:
                    if grade:
                        total += int(grade)
                        numberOfGrades += 1

                average = total / numberOfGrades
                average = round(average, 2)
                classification = "F"
                if average >= 70:
                    classification = "1"
                elif average >= 60:
                    classification = "2:1"
                elif average >= 50:
                    classification = "2:2"
                elif average >= 40:
                    classification = "3"
                else:
                    classification = "F"

            
                writer.writerow([studentId, f"{average:.2f}", classification])





# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder