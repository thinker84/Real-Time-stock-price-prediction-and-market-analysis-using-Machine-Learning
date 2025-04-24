import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from tensorflow.keras.models import load_model

import streamlit as st



start ='2010-01-01'
end = '2023-12-31'

st.title('Real-Time Stock Price Prediction and Market Analysis using Machine Learning')

user_input=st.text_input('Enter Stock Ticker','AAPL')
df=data.DataReader(user_input,'stooq',start,end)
if df.empty:
    st.subheader('NO RECORD FOUND')
else:
    # Describing Data
    st.subheader('Data from 2010 - 2023')
    st.write(df.describe())

    # Visualization
    st.subheader('Closing Price vs Time Chart')
    fig = plt.figure(figsize=(12, 6))
    plt.plot(df.Close)
    st.pyplot(fig)

    st.subheader('Closing Price vs Time Chart with 100MA')
    ma100 = df.Close.rolling(100).mean()
    fig = plt.figure(figsize=(12, 6))
    plt.plot(ma100)
    plt.plot(df.Close)
    st.pyplot(fig)

    st.subheader('Closing Price vs Time Chart with 100MA & 200MA')
    ma100 = df.Close.rolling(100).mean()
    ma200 = df.Close.rolling(200).mean()
    fig = plt.figure(figsize=(12, 6))
    plt.plot(ma100, 'r')
    plt.plot(ma200, 'g')
    plt.plot(df.Close, 'b')
    st.pyplot(fig)

    # splitting data into training and Testng

    data_training = pd.DataFrame(df['Close'][0:int(len(df) * 0.70)])
    data_testing = pd.DataFrame(df['Close'][int(len(df) * 0.70):int(len(df))])

    print(data_training.shape)
    print(data_testing.shape)

    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler(feature_range=(0, 1))

    data_training_array = scaler.fit_transform(data_training)
    # data_testing_array=scaler.fit_transform(data_testing)

    # Load my model
    model = load_model('keras_model.h5')

    # Testing part
    past_100_days = data_training.tail(100)
    # final_df=past_100_days.append(data_testing,ignore_index=True)
    final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
    input_data = scaler.fit_transform(final_df)

    x_test = []
    y_test = []

    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i - 100:i])
        y_test.append(input_data[i, 0])

    x_test, y_test = np.array(x_test), np.array(y_test)
    y_predicted = model.predict(x_test)
    scaler = scaler.scale_

    scale_factor = 1 / scaler[0]
    y_predicted = y_predicted * scale_factor
    y_test = y_test * scale_factor

    # Final Graph

    st.subheader('Predictions vs Original')
    fig2 = plt.figure(figsize=(12, 6))
    plt.plot(y_test, 'b', label='Original Price')
    plt.plot(y_predicted, 'r', label='Predicted Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(fig2)

    import datetime

    # Determine the number of future days to predict
    future_days = 10  # Example: Predicting prices for the next 10 days

    # Retrieve the last 100 days of data
    last_100_days = input_data[-100:]

    # Predict the stock prices for the future days
    predicted_prices = []
    predicted_dates = []
    for i in range(future_days):
        x_input = np.reshape(last_100_days, (1, last_100_days.shape[0], 1))
        predicted_price = model.predict(x_input)
        predicted_price = predicted_price[0][0]
        predicted_prices.append(predicted_price)

        # Update last_100_days for the next prediction
        last_100_days = np.append(last_100_days[1:], [[predicted_price]], axis=0)

        # Calculate the predicted date
        predicted_date = pd.Timestamp.today() + pd.DateOffset(days=i + 1)
        predicted_dates.append(predicted_date)

    # Create a new MinMaxScaler object for the predicted prices
    price_scaler = MinMaxScaler(feature_range=(0, 1))
    price_scaler.fit(df['Close'].values.reshape(-1, 1))

    # Inverse transform the predicted prices
    predicted_prices = np.array(predicted_prices).reshape(-1, 1)
    predicted_prices = price_scaler.inverse_transform(predicted_prices).flatten()

    # Create a DataFrame to store the predicted prices and dates
    predicted_df = pd.DataFrame({'Date': predicted_dates, 'Price': predicted_prices})

    # Display the predicted prices for the future days
    st.subheader(f'Predicted Prices for the Next {future_days} Days')
    st.dataframe(predicted_df)

