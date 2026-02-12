# Using crime.csv:
# • Load the dataset into a pandas DataFrame.
# • Create a new column called risk based on ViolentCrimesPerPop:
# – If ViolentCrimesPerPop is greater than or equal to 0.50, set risk = "High-
# Crime".
# – Otherwise, set risk = "LowCrime".
# • Group the data by the risk column.
# • For each group, calculate the average value of PctUnemployed.
# • Print the average unemployment rate for both HighCrime and LowCrime groups in a

# clear format
import pandas as pd

# load the dataset
data_frame_of_all_of_the_students = pd.read_csv("C:/Users/zaint/Downloads/crime1.csv")

def risk_of_the_violent_crime(ViolentCrimesPerPop):
    if ViolentCrimesPerPop >= 0.50:
        return 'High-Crime'
    else:
        return 'LowCrime'


data_frame_of_all_of_the_students['risk'] = (data_frame_of_all_of_the_students['ViolentCrimesPerPop'].apply(risk_of_the_violent_crime))

comparison = (data_frame_of_all_of_the_students.groupby('risk')['PctUnemployed'].mean())

print(f"Average unemployment rate in HighCrime areas: {comparison['High-Crime']:.2f}")
print(f"Average unemployment rate in LowCrime areas: {comparison['LowCrime']:.2f}")


