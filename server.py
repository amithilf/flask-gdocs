from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/get_additional_information', methods=['GET'])
# def get_additional_information(account):
#     return account

@app.route('/test')
def test():
    return redirect("https://www.intsights.com"), 302

if __name__ == '__main__':
    app.run()