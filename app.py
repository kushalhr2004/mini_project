from flask import Flask, render_template, request

app = Flask(__name__)

# ✅ Home Page
@app.route('/')
def home():
    return render_template('home.html')

# ✅ About Page
@app.route('/about')
def about():
    return render_template('about.html')

# ✅ Feedback Page
@app.route('/add', methods=['GET', 'POST'])
def add_feedback():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        return f"Feedback submitted by {name}: {message}"

    return render_template('add_feedback.html')


# ✅ Run App
if __name__ == '__main__':
    app.run(debug=True)