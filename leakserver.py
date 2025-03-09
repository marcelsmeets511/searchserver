from flask import Flask, render_template, request
from supabase import create_client
import os

app = Flask(__name__)

# Initialize Supabase client
url = "https://wxwxtdgvubhrpdhczgfj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind4d3h0ZGd2dWJocnBkaGN6Z2ZqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE1MTUyMTgsImV4cCI6MjA1NzA5MTIxOH0.YpWVZuNIIGQ8bJi5cMgG-2KtkZKoFaKYVAtaguAdX3k"
supabase = create_client(url, key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = supabase.table('profiles').select('*')
    
    # Add filters for each non-empty field
    for field in request.form:
        if request.form[field]:
            query = query.ilike(field, f'%{request.form[field]}%')
    
    results = query.execute()
    return render_template('index.html', results=results.data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))