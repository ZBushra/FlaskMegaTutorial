#The views are the handlers that respond to requests from web browsers or 
# other clients. In Flask handlers are 
# written as Python functions. 
# Each view function is mapped to one 
# or more request URLs.
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
#two route decorators above the index () 
# function create the mappings from
#  URLs / and /index to this function
def index():
   #return 'Hello World!!!'
   user = {'nickname':'Bushra'} #fake user
   #recent posts from followed users in the home page
   posts = [#fake array of posts
        {'author':{'nickname':'John'},
         'body':'Beautiful day in Portland!'
        },
        {'author':{'nickname':'Susan'},
         'body':'The Avengers movie was so cool!'
        }
   ]
   return render_template('index.html', title='Home', user =user,posts = posts)

#not scalable option to return html code, Templates help implement this separation of logic
#of application from the layout or presentation above
#Under the covers, the render_template function 
# invokes the Jinja2 templating engine that is
#  part of the Flask framework. Jinja2 substitutes 
# {{...}} blocks with the corresponding values 
# provided as template arguments . 
# The Jinja2 templates also support control 
# statements, given inside {%...%}

