from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the Excel sheet into a pandas DataFrame
df = pd.read_csv('students.csv')  # Replace with your actual Excel file path

# Convert the Id column to string to handle large numbers properly
df['Student Code'] = df['Student Code'].astype(str)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_student', methods=['POST'])
def get_student():
    # Get the ID from the form submission
    input_id = request.form['id']
    
    # Find the student details based on the provided Id
    student = df[df['Student Code'] == input_id]

    if not student.empty:
        # Extract details and convert to Python native types
        student_email = student['E-mail'].values[0]
        student_password = str(student['password'].values[0]) # Ensure int64 is cast to int
        return render_template('index.html', student_name=student_email, student_id=student_password)
    else:
        return render_template('index.html', error='Student not found')

if __name__ == '__main__':
    app.run(debug=True)
