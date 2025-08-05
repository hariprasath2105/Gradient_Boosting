
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

np.random.seed(42)
months = list(range(1,13))
years = list(range(2018, 2024))
store_ids = list(range(1,11))  # 10 stores

rows = []
for store in store_ids:
    base = np.random.uniform(2000, 10000)
    trend = np.random.uniform(50, 200)
    for year in years:
        for month in months:
            t = (year - 2018) * 12 + month
            promo = np.random.choice([0,1], p=[0.7,0.3])
            month_factor = 1 + 0.1*np.sin(2*np.pi*(month/12))
            noise = np.random.normal(0, base*0.05)
            sales = base + trend * t * month_factor + promo * 500 + noise
            rows.append({
                "store_id": store,
                "year": year,
                "month": month,
                "promo": promo,
                "sales": round(max(0, sales), 2)
            })

df = pd.DataFrame(rows)
df = df.sort_values(['store_id','year','month']).reset_index(drop=True)
df['prev_month_sales'] = df.groupby('store_id')['sales'].shift(1)
df['prev_month_sales'] = df.groupby('store_id')['prev_month_sales'].transform(lambda x: x.fillna(x.median()))
df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)

df.to_csv("monthly_sales.csv", index=False)

features = ['store_id','year','month','promo','prev_month_sales','month_sin','month_cos']
X = df[features].copy()
y = df['sales'].copy()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=3, random_state=42)
model.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

