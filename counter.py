from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'sec'
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def ma():
    if 'counter' in session:
        session['counter'] = session.get('counter') + 1
    else:
        session['visits'] = 1
    return "Total visits: {}".format(session.get('counter'))

@app.route('/destroy')
def clear():
    session.pop('counter', None)
    return redirect("/")


if __name__=="__main__":    
    app.run(debug=True)    

