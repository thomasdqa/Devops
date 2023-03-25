from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user, LoginManager
from .models import Service_request, User
from sqlalchemy import update
from . import db

import json


login_manager = LoginManager()

views = Blueprint('views', __name__)

#function to load a sepcific user from the database
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(first_name=user_id).first()

#function to load all users from the database
def load_all_users():
    return User.query.all()

#function to load all service requests from the database
def load_all_requests():
    return Service_request.query.all()

#This function will run whenever we go to the '/' route
@views.route('/', methods=['GET', 'POST'])
#users cannot access this route without logging in
@login_required
def home():
    #fetches data from the post request
    if request.method == 'POST':
        service_request = request.form.get('service_request')
        service_request_categoryid = request.form.get('service_request_categoryid')

        #authenticates the service request
        if len(service_request) < 1:
            flash('Please populate request body!', category='error')
        else:
            #Once the request has passed authetication, it adds the request as a new entry in the db session
            new_service_request = Service_request(data=service_request, user_id=current_user.id, status_id="1", category_id=service_request_categoryid)
            db.session.add(new_service_request)
            db.session.commit()

            #notifies user of successful entry to the request table
            flash('Request sent successfully!', category='success')

    #displays the home.html when this route is accessed
    return render_template("home.html", user=current_user)

#This function will run whenever we go to the '/admin' route
@views.route("/admin", methods=['GET', 'POST'])
#users cannot access this route without logging in
@login_required
def admin():     
    #sets value of variable users to value defined in function above
    users = load_all_requests()  
    #displays the admin.html when this route is accessed
    return render_template("admin.html", user=current_user, service_request = users )

#This function will run whenever we go to the '/adminPrivileges' route
@views.route("/adminPrivileges/", methods=['GET', 'POST'])
#users cannot access this route without logging in
@login_required
def adminPrivileges(): 
    #sets value of variable users to value defined in function above    
    users = load_all_users()   
    #displays the adminPrivileges.html when this route is accessed
    return render_template("adminPrivileges.html", user=current_user, dif_users = users )

#This function will run whenever we go to the '/delete-service_request' route
@views.route('/delete-service_request', methods=['POST'])
def delete_service_request():
    #loads json data from corrosponding JS file
    service_request = json.loads(request.data)
    service_requestId = service_request['service_requestId']
    #matches data to a service request in the databse
    service_request = Service_request.query.get(service_requestId)
    if service_request:
        #ensures users can only delete their own service request
        if service_request.user_id == current_user.id:
            #removes service request from the databse
            db.session.delete(service_request)
            db.session.commit()

    return jsonify({})

#This function will run whenever we go to the '/service-id_request' route
@views.route('/service-id_request', methods=['POST'])
def service_id_request():
    #loads json data from corrosponding JS file
    service_request = json.loads(request.data)
    service_requestId = service_request['service_requestId']
    #matches data to a service request in the databse
    service_request = Service_request.query.get(service_requestId)
    #updates the value of status_id on the corrosponding service request
    statement = update(Service_request).where(Service_request.id == service_requestId).values(status_id = 2)
    if service_request:
            db.session.execute(statement)
            db.session.commit()

    return jsonify({})

#This function will run whenever we go to the '/service-id_request2' route
@views.route('/service-id_request2', methods=['POST'])
def service_id_request2():
    #loads json data from corrosponding JS file
    service_request2 = json.loads(request.data)
    service_requestId2 = service_request2['service_requestId2']
    #matches data to a service request in the databse
    service_request2 = Service_request.query.get(service_requestId2)
    #updates the value of status_id on the corrosponding service request
    statement = update(Service_request).where(Service_request.id == service_requestId2).values(status_id = 3)
    if service_request2:
            db.session.execute(statement)
            db.session.commit()

    return jsonify({})

#This function will run whenever we go to the '/delete-user' route
@views.route('/delete-user', methods=['POST'])
def delete_user():
    #loads json data from corrosponding JS file
    user = json.loads(request.data)
    userId = user['UserId']
    #matches data to a user in the databse
    user = User.query.get(userId)
    if user:
            #deletes user from the databse
            db.session.delete(user)
            db.session.commit()

    return jsonify({})

#This function will run whenever we go to the '/make-user-admin' route
@views.route('/make-user-admin', methods=['POST'])
def make_user_admin():
    #loads json data from corrosponding JS file
    user = json.loads(request.data)
    userId = user['userId']
    #matches data to a user in the databse
    user = User.query.get(userId)
    #updates the value of admin on the corrosponding user
    statement = update(User).where(User.id == userId).values(admin = 'true')
    if user:
            db.session.execute(statement)
            db.session.commit()

    return jsonify({})

#This function will run whenever we go to the '/remove-user-admin' route
@views.route('/remove-user-admin', methods=['POST'])
def remove_user_admin():
    #loads json data from corrosponding JS file
    data = json.loads(request.data)
    dataId = data['userId']
    #matches data to a service request in the databse
    data = User.query.get(dataId)
    #updates the value of admin on the corrosponding user
    statement = update(User).where(User.id == dataId).values(admin = 'False')
    if data:
            db.session.execute(statement)
            db.session.commit()

    return jsonify({})