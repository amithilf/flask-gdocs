from flask import Flask, redirect, jsonify, request, abort
import os 
import gspread
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)

credential = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",
                                                              ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)
gsheet = client.open("Python Server").sheet1

@app.route('/')
def main_screen():
    return "<h1>Server Main Screen </h1>"

@app.route('/get_additional_information', methods=['GET'])
def get_additional_information():
    account = request.args.get('account')
    cell = gsheet.find(account)
    acc_details = jsonify(gsheet.get_all_records()[cell.row - 2])
    
    return acc_details


if __name__ == '__main__':
    app.run()