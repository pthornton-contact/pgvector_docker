from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/new-post')
def new_post():
    return render_template('new-post.html')

@app.route('/blog-post')
def blog_post():
    return render_template('blog-post.html')  

@app.route('/about')
def about():
    return render_template('about.html')   

@app.route('/chatapp')
def chatapp():
    return render_template('chatapp.html') 

@app.route('/create-post', methods=['POST'])
def create_post(): # create new post here return redirect(url_for('index')) if __name__ == '__main__': app.run()
    return render_template('create-post.html')

    #from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello Peter!'


