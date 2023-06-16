from flask import Flask, render_template, request

app=Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
    
    return render_template('login.html')

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])

    return render_template('signup.html')


if __name__=="__main__":
    app.run(debug=True)