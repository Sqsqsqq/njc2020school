from flask import *
import sqlite3

#Instantiates a flask object and assigns it to app
app = Flask(__name__)

@app.route('/')  #decorator for home page
def home():
    return render_template("index.html")

@app.route('/search', methods = ["POST"])  #decorator for search page

def search():

    data = request.form
    school = data["school"]
    department = data["department"]
    connection = sqlite3.connect("schools.db")
    results = connection.execute("SELECT SCHOOL.Name, STAFF.name, Department, Contact, Address " +
                                 "FROM STAFF, SCHOOL WHERE SCHOOL.Name LIKE '%'||?||'%' AND STAFF.Department = ?", (school, department))
    
    lst = []
    for row in results:
        lst.append(row)
    
    connection.commit()
    connection.close()
    return render_template("information.html", lst = lst)

if __name__ == '__main__':
    app.run(port = 5678)
