from flask import Flask, redirect, jsonify, request, abort
import os 
import gspread
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)

credential = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",
                                                              ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)
gsheet = client.open("Python Server").sheet1


# @app.route('/all_reviews', methods=["GET"])
# def all_reviews():
#     return jsonify(gsheet.get_all_records())

# @app.route('/all_values', methods=["GET"])
# def all_values():
#     return jsonify(gsheet.get_all_values())


@app.route('/')
def hello_world():
    return "Server Main Screen"

@app.route('/get_additional_information/<account_name>', methods=['GET'])
def get_additional_information(account_name):

    cell = gsheet.find(account_name)
    acc_details = jsonify(gsheet.get_all_records()[cell.row - 2])
    return acc_details


if __name__ == '__main__':
    app.run()