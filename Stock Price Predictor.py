"""
Stock Price Predictor (Dummy)

Predict next day's price based on previous days using linear regression.

Requirements:
pip install numpy scikit-learn

"""

import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    # Dummy stock prices (last 5 days)
    prices = np.array([100, 102, 101, 105, 110])
    X = np.arange(len(prices)).reshape(-1, 1)
    y = prices

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[len(prices)]])
    prediction = model.predict(next_day)[0]

    print(f"Predicted price for next day: {prediction:.2f}")

if __name__ == "__main__":
    main()
