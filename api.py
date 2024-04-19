import json
import re
import time
import csv
from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [ { 'id': 1, 'name': 'Ashley' }, { 'id': 2, 'name': 'Kate' }, { 'id': 3, 'name': 'Joe' }]

@app.route('/', methods=['GET'])
def get_employees():
   header = []
   rows = []

   with open("analyzer_v1.3.py", 'r') as f:
      source_code = f.read()
      exec(source_code)

      with open('anlyzer_results.csv', newline='') as csvfile:
         csvreader = csv.reader(csvfile, delimiter=';')
         header = next(csvreader)
         for row in csvreader:
            rows.append(row)

   return jsonify(header, rows)

if __name__ == '__main__':
   app.run(debug=True, port=5000)

