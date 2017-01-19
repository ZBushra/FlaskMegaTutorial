from flask import Flask

app = Flask(__name__) #Flask instance
from app import views #app the package where we get the views module                      
# the import statement is at the end and not at the beginning of the script as it is always done, the reason is to avoid circular references, because you are going to see that the views module needs to import the app variable defined in this script. Putting the import at the end avoids the circular import error


