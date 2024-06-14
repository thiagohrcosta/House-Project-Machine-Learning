import bcrypt
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from datetime import datetime

from dotenv import load_dotenv
import os
import requests

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

import joblib 


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin123@localhost:3306/house_app'

db.init_app(app)

model_path = 'data/house_linear_regression_model.pkl'

try:
    model = joblib.load(model_path)
    print("Modelo carregado com sucesso.")
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    model = None


if __name__ == '__main__':
  app.run(debug=True)