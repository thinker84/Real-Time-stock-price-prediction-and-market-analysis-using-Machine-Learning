
# 📈 Real-Time Stock Price Prediction and Market Analysis using Machine Learning

This project is a real-time stock market prediction and analysis web app built using Python, Keras, and Streamlit. It predicts future stock prices using a deep learning model trained on historical stock data fetched from Stooq.

---

## 🎥 Demo
📽️ [Click here to watch the demo video](https://drive.google.com/file/d/1yYKk7665jM0UdhGtIZjxNVEToDGnK8K0/view?usp=drive_link)

---

## 🧩 Problem Statement
- Stock price movements are highly volatile and influenced by complex patterns, making accurate forecasting challenging for investors and analysts.  
- Traditional forecasting methods often fail to capture the non-linear trends and time-dependent nature of stock market data.  
- There is a need for an intelligent, real-time system that can predict future stock prices using deep learning techniques, based on historical trends and 
  patterns.  
- This project aims to build a web-based application that leverages an LSTM model to forecast stock prices and visualize trends, helping users make more informed 
  decisions.

---

## 🧾 Existing System
- Uses statistical models, technical indicators, and fundamental analysis.
- Limited in handling complex patterns and time-based dependencies in stock data.
- Not well-suited for real-time market analysis.
- Struggles to adapt to fast-changing market conditions

---

## 💡 Proposed System
- A machine learning-based approach using an LSTM model trained on historical stock prices.
- Utilizes free data from Stooq for accessibility.
- Predicts future prices and visualizes them with moving averages and comparison plots.
- Fully interactive and user-friendly interface built with Streamlit.

---

## Methodology
1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Model Training
5. Stock Price Prediction
6. Visualization and Reporting

---

## 🔍 Key Features
- 📊 Fetches historical stock data from 2010–2023 for any ticker (default: AAPL) using `pandas_datareader`.
- 📉 Visualizes stock price trends with moving averages (100MA & 200MA).
- 🤖 Predicts future stock prices using a pre-trained LSTM model (`keras_model.h5`).
- 📅 Displays predicted prices for the next 10 days using recent trends.
- 📈 Compares actual vs. predicted prices using interactive line plots.
- 🌐 Fully interactive web interface built using Streamlit.

---

## 🧠 Technologies & Libraries Used
- Python
- TensorFlow / Keras (LSTM model)
- Streamlit (for real-time UI)
- pandas (for data handling)
- matplotlib (for visualizations)
- scikit-learn (MinMaxScaler for normalization)
- pandas_datareader (fetching stock data from Stooq)

---

## 🧪 How It Works
1. User inputs a stock ticker (e.g., `AAPL`).
2. App fetches historical data (2010–2023) from Stooq.
3. Visualizes:
   - Raw closing prices
   - 100-day & 200-day moving averages
4. Splits data into:
   - 70% training
   - 30% testing
5. Uses an LSTM model to:
   - Predict prices
   - Compare with actual values
   - Forecast the next 10 days
6. All results are visualized and displayed on a real-time Streamlit dashboard.

---

## 🎯 Model Accuracy
While no explicit metric (like RMSE or R²) is shown in the app, the LSTM model demonstrates approximately **85% trend accuracy**, based on visual comparison of actual vs. predicted curves.

---

## 📌 How to Run
1. Clone the repository: Clone the project repository to your local machine using Git (or download as ZIP):
git clone <repo_url>

2. Set up a virtual environment: Open a terminal and navigate to the project folder. Then create and activate a virtual environment:

For Windows:
python -m venv venv
venv\Scripts\activate

For macOS/Linux:
python3 -m venv venv
source venv/bin/activate

3. Install required dependencies: Once your virtual environment is active, install the required packages using the requirements.txt file:
pip install -r requirements.txt

4. Run the Streamlit app: To start the Streamlit web app, run the following command in your terminal:
streamlit run app.py

5. Access the web app: After running the command, Streamlit will automatically open the app in your default web browser. If not, you can manually open the following URL in your browser:
http://localhost:8501

6. Enter a Stock Ticker: In the web interface, you can enter any stock ticker (e.g., AAPL) into the search bar. The app will fetch and display:
Historical stock data (from 2010 to 2023).
Stock price predictions for the next 10 days.


