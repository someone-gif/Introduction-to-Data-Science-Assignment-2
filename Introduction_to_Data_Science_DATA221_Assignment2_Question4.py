# Load the dataset into a DataFrame.
# • Filter students where studytime ≥ 3, internet = 1, and absences ≤ 5.
# • Save the filtered data to high_engagement.csv.
# • Print the number of students saved and their average grade.

import pandas as pd
import csv

# load the dataset
data_frame_of_all_of_the_students = pd.read_csv('C:/Users/zaint/Downloads/student.csv')

# filter: studytime >= 3, internet == 1, absences <= 5
filtered_student_data_frame = data_frame_of_all_of_the_students[(data_frame_of_all_of_the_students['studytime'] >= 3) & (data_frame_of_all_of_the_students['internet'] == 1) & (data_frame_of_all_of_the_students['absences'] <= 5)]

# save to new file
filtered_student_data_frame.to_csv('C:/Users/zaint/Downloads/high_engagement.csv', index=False)

# Print results
print(f"Number of students saved: {len(filtered_student_data_frame)+1}")
average_grade_of_the_filtered_students = filtered_student_data_frame['grade'].mean()
print(f"Final Grade: {average_grade_of_the_filtered_students}")