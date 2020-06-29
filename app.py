from flask import Flask
# app.py is WSGI(Web Server Gateway Interface)

# Create Flask Object
app = Flask(__name__)

# Assign a URL route
# Tell flask when to call view
@app.route("/")
def hello():
    return "Hello"

# Run app in main
if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port = 3000)