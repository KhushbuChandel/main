from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#intialise the sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Todo(db.Model):
    
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def _repr_(self):
        return "Hello"
    
@app.route('/')
def hello_world():

    todo = Todo(title="First Todo", desc="Start investing in Stock market")
    db.session.add(todo) 
    db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html')

# @app.route('/products')
@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'this is products page'

if __name__ == "_main_":
    # with app.app_context():
    #     # Create the database tables if they don't exist
    #     db.create_all()
    app.run(debug=True)