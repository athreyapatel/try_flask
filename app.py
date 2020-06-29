from flask import Flask
# app.py is WSGI(Web Server Gateway Interface)

# Create Flask Object
app = Flask(__name__)

# Run app in main
if __name__ == "__main__":
    app.run()


