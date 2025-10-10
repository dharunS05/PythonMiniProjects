#==================================================
# Student Mark Analyser 
#==================================================
import pandas as pd 

#load the student data csv file 
def load_csv(file_path):
    student_data = pd.read_csv(file_path)
    return student_data

def analyser(student_data):
    student_data['total'] = student_data['Math']+student_data['Science']+student_data['English']+student_data['Computer']

    student_data['avg'] = student_data['total']/4
    return student_data


#==================================================
# Main Function
#==================================================

file_path = r'E:\linkedinProjects\BankManagementProject\PythonMiniProjects\student_performance_analyser\data\student_data.csv'
student_data=load_csv(file_path)

#clean Added Dataset
clean_data = analyser(student_data)

#print Total Student count
no_of_student = len(clean_data['Name'])

#Averages
total_avg = 0
math_avg = 0
science_avg = 0
english_avg = 0
computer_avg = 0

#top scorer
top_scorer = clean_data.loc[clean_data['avg'].idxmax()]

#low Scorer
low_scorer = clean_data.loc[clean_data['avg'].idxmin()]


#Overall averages  
total_avg = clean_data['avg'].mean()

math_avg = clean_data['Math'].mean()
science_avg = clean_data['Science'].mean()
english_avg = clean_data['English'].mean()
computer_avg =clean_data['Computer'].mean()

print("#============================================================#")
print("#Student Mark Analysis")
print("#============================================================#")
print("Total Number Of Students: ",no_of_student)
print(f"Overall Mark Average(All Subjects): {total_avg:2f}")
print(f"Top Performer: {top_scorer['Name']} average: {top_scorer['avg']:.2f}")
print(f"low Performer: {low_scorer['Name']} average: {low_scorer['avg']:.2f}")
print("#============================================================#")
print("All Subject Overall Average...")
print(f"Math:{math_avg:.2f}")
print(f"Science:{science_avg:.2f}")
print(f"English:{english_avg:.2f}")
print(f"Computer:{computer_avg:.2f}")



