# Here you will create a new categorical variable and generate a grouped summary table.
# Using student.csv:
# • Create a new column grade_band:
# – Low: grade ≤ 9
# Assignment No 2 Page 3
# – Medium: grade 10–14
# – High: grade ≥ 15
# • Create a grouped summary table showing for each band:
# – number of students
# – average absences
# – percentage of students with internet access
# • Save the table as student_bands.csv

import pandas as pd

# Load the dataset 
data_frame_of_all_of_the_students = pd.read_csv('C:/Users/zaint/DATA221_SEMESTER1/assignment_2/student.csv')

def categorize_grade(grade):
    if grade <= 9:
        return 'Low'
    elif 10 <= grade <= 14:
        return 'Medium'
    else:
        return 'High'

# Create grade_band column
data_frame_of_all_of_the_students['grade_band'] = data_frame_of_all_of_the_students['grade'].apply(categorize_grade)

# Manual grouped summary - NO agg or lambda
grouped_data = data_frame_of_all_of_the_students.groupby('grade_band')

# Calculate each metric 
student_count = grouped_data.size()  # Number of students per band
average_absences = grouped_data['absences'].mean()  # Average absences
percentage_of_students_with_internet_acces = grouped_data['internet'].mean() * 100  # 

# Combine into summary table manually
summary_table = pd.DataFrame({'student_count': student_count, 'avg_absences': average_absences,'pct_internet': percentage_of_students_with_internet_acces})

# Save to CSV
summary_table.to_csv('C:/Users/zaint/DATA221_SEMESTER1/assignment_2/student_bands.csv')

print(summary_table)
