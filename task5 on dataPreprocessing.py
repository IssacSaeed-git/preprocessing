import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import joblib

# 1. Load Data
df = pd.read_csv(r'C:\Users\Royal\OneDrive\Desktop\NLP\database files\canada_per_capita_income.csv')
print(df.head())

# 2. Prepare Data
X = df[['year']]           # feature
y = df['per capita income (US$)']           # target

# 3. Build the model
model = LinearRegression()
model.fit(X, y)

# 4. Plot the data
plt.xlabel('Year')
plt.ylabel('Per Capita Income ($)')
plt.scatter(df['year'], df['per capita income (US$)'])
plt.plot(df['year'], model.predict(X))
plt.show()

# 5. Predict income in year 2020
pred_2020 = model.predict([[2020]])
print("Predicted income for 2020 =", pred_2020[0])

# 6. Predict income for 2025 (optional)
pred_2025 = model.predict([[2025]])
print("Predicted income for 2025 =", pred_2025[0])

# save
joblib.dump(model, 'canda_predict_model.pkl')
print("\nModel saved successfully to 'canda_predict_model.pkl'")
