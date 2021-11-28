from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "abc123"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()



@app.route('/')
def redirect():
    """redirect to list of users"""
    return redirect('/users')

@app.route('/users')
def user_listing():
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/listing.html', users=users)

@app.route('/users/new', methods=["GET"])
def users_new_form():
    """Show a form to create a new user"""

    return render_template('users/create_user.html')

@app.route('/users/new', methods=['POST'])
def create_new_user():
    """submit the form for creating a new user"""
    fname = request.form['first_name']
    lname = request.form['last_name']
    img = request.form['img_url'] or None
    
    new_user = User(first_name=fname, last_name=lname, image_url=img)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    """show detail about a specific user"""
    user = User.query.get_or_404(user_id)
    return render_template('users/user_detail.html', user=user)


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Show form to edit existing user"""
    user = User.query.get_or_404(user_id)

    return render_template('users/edit_user.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    """submit the form for updating user info"""
    user = User.query.get_or_404(user_id)

    fname = request.form['first_name']
    lname = request.form['last_name']
    img = request.form['img_url']
    
    user.first_name = fname
    user.last_name = lname
    user.image_url = img

    db.session.add(user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """Delete an existing user."""
    user = User.query.get_or_404(user_id)
    
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')



