from arraydata import *
from pathlib import Path
from IPython import display
from flask import Flask, render_template, request
import pandas as pd
import re

app = Flask(__name__)


@app.route('/')
def my_form():
  return render_template('index.html')

def dara(city):
  data = getCrimes()
  dataframe = pd.DataFrame(data,columns=["Incident","Time","Area"])
  dataframe = dataframe.dropna()
  city = city.upper()
  dataframe = dataframe[dataframe['Area'].str.contains(city)]
  return dataframe

@app.route('/',methods=['POST'])
def get_request():
  print("AMONG US  AMONG US")
  x = request.form['text']

  html = dara(x).to_html()
  old_contents = open("./templates/dataframe.html", "r")

  print(html)

  new_contents = old_contents.read().replace("</tbody>", f"{html}\n</tbody>")

  with open("./templates/dataframe.html", "w") as text_file:
    text_file.write(new_contents)

  old_contents.close()

  return render_template('dataframe.html')




if __name__ == "__main__":
  app.run()