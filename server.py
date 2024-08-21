from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)


class Tasks(db.Model)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"Task {self.id}"

#using a context manager:
with app.app_context():
    db.create_all()



@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        task_name = request.form['task_name']
        task_desc = request.form['task_desc']
        new_task_entry = Tasks(name=task_name, description=task_desc)
        try:
            db.session.add(new_task_entry)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"Error: {e}")
            return f'{e}'
    else:
        tasks = Tasks.query.order_by(Tasks.date.desc()).all()
        return render_template("index.html", tasks=tasks)
    

#edit
@app.route('/edit/<int:id>', methods=["POST", "GET"])
def edit(id:int):
    task = Tasks.query.get_or_404(id)
    if request.method == "POST":
        task.name = request.form['task_name']
        task.description = request.form['task_desc']
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"Error: {e}"
    else:
        return render_template("edit.html", task=task)


#delete
@app.route('/delete/<int:id>')
def delete(id:int):
    del_task = Tasks.query.get_or_404(id)
    try:
        db.session.delete(del_task)
        db.session.commit()
        return redirect('/')
        
    except Exception as e:
        return f"Error: {e}"
    
    
if __name__ == "__main__":
    app.run(debug=True)
