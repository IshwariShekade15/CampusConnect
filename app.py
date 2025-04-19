from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection setup
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',          # Replace with your MySQL username
        password='root123',   # Replace with your MySQL password
        database='campusconnect'  # Replace with your MySQL database name
    )

@app.route('/')
def index():
    return render_template('opportunities.html')

@app.route('/add_opportunity', methods=['POST'])
def add_opportunity():
    # Safely get form data
    title = request.form.get('title')
    description = request.form.get('description')
    link = request.form.get('link')

    # Ensure all fields are filled
    if not (title and description and link):
        return 'All fields are required!', 400

    # Connect to MySQL and insert data
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO opportunities (title, description, link)
        VALUES (%s, %s, %s)
    """, (title, description, link))
    conn.commit()
    cursor.close()
    conn.close()

    return 'Opportunity added successfully!'

if __name__ == '__main__':
    app.run(debug=True)
