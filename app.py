import question
import twitter

from datetime import datetime, date
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,logout_user,login_user,login_required
from flask_login import UserMixin 
from flask_bcrypt import Bcrypt 

app = Flask(__name__)

app.secret_key = 'secret key'


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.init_app(app)

@login_manager.user_loader  
def load_user(user_id):  
    return User.query.get(int(user_id))  

app.config['SECRET_KEY'] = 'cfb33786023cc152019e747a051f73c6' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

Question=[]

#todoのDBモデル
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    detail = db.Column(db.String(100))
    question1 = db.Column(db.String(50), nullable=False)
    question2 = db.Column(db.String(50), nullable=False)
    question3 = db.Column(db.String(50), nullable=False)
    answer1 = db.Column(db.String(50), nullable=False)
    answer2 = db.Column(db.String(50), nullable=False)
    answer3 = db.Column(db.String(50), nullable=False)
    twitterid = db.Column(db.String(50), nullable=False)
    due = db.Column(db.DateTime, nullable=False)

#ユーザのDBモデル
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Userid = db.Column(db.String(30), nullable=False)
    Password = db.Column(db.String(30), nullable=False)
    Twittername= db.Column(db.String(30), nullable=False)


'''
class User(db.Model, UserMixin):  
    id = db.Column(db.Integer, primary_key=True)
    Userid = db.Column(db.String(30), nullable=False)
    Password = db.Column(db.String(30), nullable=False)
    Twittername= db.Column(db.String(30), nullable=False)
'''
  


@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template("login.html")



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    elif request.method == 'POST':
        
        #ログインの可否を書く
        userid = request.form.get('userid')
        password=request.form.get('password')
        
        print(userid)
        print(password)

        Password = db.session.query(User.Userid).filter_by(Userid=userid).first()
        #print(type(Password))
        #print(Password[0])

        #ログイン成功
        if userid=="aa":
            
            '''
            print("成功")
            user = User()
            login_user(user)
            post="ログイン成功"
            '''

            return render_template('index.html')
        #ログイン失敗
        else:
            post="ログイン失敗"
            return render_template('login.html',post=post)

@app.route('/member', methods=['GET',"POST"])

def member():

    if request.method == 'GET':
        posts = Post.query.order_by(Post.due).all()
        return render_template('index.html', posts=posts)

    elif request.method == "POST":
        title = request.form.get('title')
        detail = request.form.get('detail')
        answer1 = request.form.get('question1')
        answer2 = request.form.get('question2')
        answer3 = request.form.get('question3')
        twitterid = request.form.get('twitterid')

        question1=Question[0]
        question2=Question[1]
        question3=Question[2]

        due = request.form.get('due')
        due = datetime.strptime(due, '%Y-%m-%d')
        new_post = Post(title=title, detail=detail, answer1=answer1,answer2=answer2,answer3=answer3,question1=question1, question2=question2, question3=question3, twitterid=twitterid,due=due)

        db.session.add(new_post)
        db.session.commit()

        return redirect('/member')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

def dashboard():
    return render_template('dashboard.html')

@login_manager.user_loader
def load_user(user_id):
        return User()


@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == "POST":
        userid = request.form.get('userid')
        password=request.form.get('password')
        twittername = request.form.get('twittername')
        new_post = User(Userid=userid, Password=password, Twittername=twittername)
        
        db.session.add(new_post)
        db.session.commit()

        return render_template("login.html")



@app.route('/create')
def create():
    post=question.question()
    Question.clear()
    Question.append(post[0])
    Question.append(post[1])
    Question.append(post[2])
    return render_template('create.html', post1=post[0], post2=post[1], post3=post[2])


@app.route('/detail/<int:id>')
def read(id):
    post = Post.query.get(id)

    return render_template('detail.html', post=post)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    post = Post.query.get(id)
    if request.method == 'GET':
        return render_template('update.html', post=post)
    else:
        post.title = request.form.get('title')
        post.detail = request.form.get('detail')
        post.due = datetime.strptime(request.form.get('due'), '%Y-%m-%d')

        db.session.commit()
        return redirect('/member')


@app.route('/complete/<int:id>')
def complete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return render_template('complete.html')

@app.route('/fail/<int:id>')
def fail(id):
    post = Post.query.get(id)
    str=post.twitterid
    str+="\n"
    str+=post.question1
    str+="\n"
    str+=post.answer1
    str+="\n"
    str+=post.question2
    str+="\n"
    str+=post.answer2
    str+="\n"
    str+=post.question3
    str+="\n"
    str+=post.answer3
    
    print(str)
    twitter.Tweet_Text(str)

    
    db.session.delete(post)
    db.session.commit()
    return redirect("/member")

if __name__ == "__main__":
    app.run()




