from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Connect to AWS PostgreSQL Database using environment variables
def connect_db():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )
    return conn

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/job_tracker')
def job_tracker():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product_cost")
    product_cost_data = cursor.fetchall()
    conn.close()
    return render_template('job_tracker.html', product_cost_data=product_cost_data)

@app.route('/data_analytics')
def data_analytics():
    return render_template('data_analytics.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login or sign-up logic
        pass
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)