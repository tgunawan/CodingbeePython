from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
        <h1>Welcome to Djanggo Web</h1>
        <p>This is a simple, expandable web app.</p>
        <a href="{{ url_for('about') }}">About</a>
    """)

@app.route('/about')
def about():
    return render_template_string("""
        <h1>About Page</h1>
        <p>This is the about page.</p>
        <a href="{{ url_for('home') }}">Home</a>
    """)

if __name__ == '__main__':
    app.run(debug=True)