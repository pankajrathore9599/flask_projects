from flask import Flask,redirect,url_for,request,render_template

app = Flask(__name__)

#url 1
@app.route('/')
def hello_world():
    return 'Hello World'

# url 2 routing
@app.route('/hello')
def hello_world1():
    return 'Hello this is another url'
app.add_url_rule('/','hello')

# passsing variable value in url
@app.route('/name/<Name>')
def hello_name(Name):
    return  'Hello %s!' % Name

# URL Building for admin and guest
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

# HTTP methods with login page
@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))

# Render the templates from the folder
@app.route('/template/<user>')
def template_sample(user):
    return render_template('hello.html', name = user)

# templates rendering with using conditions
@app.route('/template/<int:score>')
def template_score(score):
    return render_template('score.html', marks = score)

# templates render using the dictionary objects
@app.route('/result')
def result():
    dict = {'physic':50, 'chemistry':60, 'maths':89}
    return render_template('result.html', result = dict)

# working with static files using html and javascript
@app.route('/js')
def index():
    return render_template("index.html")

# sending data from form to templates
@app.route('/form')
def studentform():
    return render_template('form.html')

@app.route('/studentresult', methods = ['POST', 'GET'])
def result1():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result )

if __name__ == '__main__':
    app.run(debug=True)

# app debugging for restart the server automatic if any changes were make.
app.debug = True
app.run()
app.run(debug=True)
