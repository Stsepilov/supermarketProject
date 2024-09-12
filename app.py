from flask import Flask, request, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Groceries

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///groceries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'
db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    groceries = Groceries.query.all()
    return render_template('index.html', groceries=groceries)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        details = request.form['details']
        weight = request.form['weight']
        quantity = request.form['quantity']
        price = request.form['price']
        new_item = Groceries(name=name, details=details, weight=weight, quantity=quantity, price=price)
        db.session.add(new_item)
        db.session.commit()
        flash(f'Товар {name} успешно добавлен!', 'success')
        return redirect('/')
    return render_template('add.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        name = request.form['name']
        db.session.query(Groceries).filter(Groceries.name == name).delete(synchronize_session="fetch")
        db.session.commit()
        flash(f'Товар {name} успешно удален!', 'success')
        return redirect('/')
    return render_template('delete.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
