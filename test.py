from nltk.corpus import stopwords
from flask import Flask, jsonify, request, redirect, url_for
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd
from openpyxl import load_workbook
import re
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import string
import nltk
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('stopwords')
nltk.download('punkt')


app = Flask(__name__)

api = Api(app)

CORS(app)


class TrendResource(Resource):
    def get(self):
        response = {"msg": "hallo"}
        return response


api.add_resource(TrendResource, "/api", methods=["GET"])


if __name__ == "__main__":
    app.run(debug=True)
