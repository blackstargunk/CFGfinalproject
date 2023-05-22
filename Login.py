# import MySQLdb.cursors
# Code to log in/create account to store user's playlists
# from flask_mysqldb import MySQL
# import MySQLdb.cursors



# app.config["MYSQL_HOST"] = 'localhost'
# app.config["MYSQL_USER"] = 	"root"
# app.config["MYSQL_PASSWORD"] = "" #whatever password is
# app.config["MYSQL_DB"] = "pythonlogin"
#
# mysql = MySQL(app)


#login page for existing accounts

# @app.route('/pythonlogin/', methods=["GET", "POST"])
# def login():
#     output_message = ""
#     if request.method == "POST" and "username" in request.form and "password" in request.form:
#         username = request.form["username"]#make sure this is the same as SQL
#         password = request.form["password"]
#         #checking account exists in SQL
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute("SELECT * FROM accounts WHERE username = %s AND password = %s", (username, password,))# ensure these match up with SQL
#         account = cursor.fetchone()
#
#     if account:
#         session["loggedin"] = True
#         session["id"] = account["id"]
#         session["username"] = account["username"]
#         #redirect to homepage
#         return "Logged in Successfully!"
#     else:
#         output_message = "Incorrect username or password combination"
#
#     return render_template("savedplaylists.html", output_message="") #html needs to match up with Liyaan's
#
#
# def logout():
#     session.pop("loggedin", None)
#     session.pop("id", None)
#     session.pop("username", None)
#
#     return redirect(url_for("login"))
#
#
# # Creating a new account
#
# def register():
#     output_message = ""
#
#     if request.method == "POST" and "username" in request.form and "password" in request.form and "email" in request.form:
#         username = request.form["username"]
#         password = request.form["password"]
#         email = request.form["email"]
#     elif request.method == "POST":
#         output_message = "Please fill out the sign up form"
#     return render_template("register.html", output_message=output_message) #make sure HTML matches with Liyaan
#
#
# email = request.form["email"]
#
# cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
# cursor.execute("SELECT * FROM accounts WHERE username = %s", (username)) # make sure matches with SQL from Renee
# account = cursor.fetchone()
#
# if account:
#     output_message = "This account already exists"
# elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#     output_message = "Invalid email address entered"
# elif not re.match(r'[A-Za=z0-9]+', username):
#     output_message = "Username must only contain letters and numbers"
# elif not username or not password or not email:
#     output_message = "Please fill out the registration form"
# else:
#     cursor.execute("INSERT INTO accounts VALUE (NULL, %s, %s, %s"), (username, password, email))
#     mysql.connection.commit()
#     output_message = "You have successfully created an account"
#
#
# #Account page that can only be seen once logged in and will contain the saved playlists
#
# def personal_page():
#         if 'loggedin' in session:
#             return render_template('savedplaylists.html', username=session["username"])#make sure same html page as Liyaan
#
#         return redirect(url_for('login'))#to redirect to login page if user is not logged in
