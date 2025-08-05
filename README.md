
# 📈 Sales Forecasting App (Gradient Boosting + Flask)

This is a simple web application that predicts **monthly sales** for a store using a **Gradient Boosting Regression** model.  
The dataset used is **synthetic** and includes store-level sales data with seasonality and promotions.

---

## 📊 Dataset

The dataset (`monthly_sales.csv`) contains:
- `store_id` → Store identifier (1–10)
- `year` → Year of sales data
- `month` → Month of sales
- `promo` → Whether a promotion was running that month (0 = no, 1 = yes)
- `sales` → Actual monthly sales (target variable)
- `prev_month_sales` → Sales from the previous month
- `month_sin`, `month_cos` → Seasonal encoding for month

---

## 🛠 Tech Stack

- **Python 3**
- **Flask** (web framework)
- **scikit-learn** (GradientBoostingRegressor)
- **pandas**, **numpy** (data processing)
- **HTML/CSS** (frontend UI)

---

## 📁 Project Structure

```
sales-forecasting-app/
│
├── static/
│   └── style.css            
│
├── templates/
│   └── index.html             
│
├── app.py                  
├── train_model.py       
├── model.pkl           
├── scaler.pkl                 
├── monthly_sales.csv            
└── README_Sales_Forecasting.md  
```

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install flask scikit-learn pandas numpy
```

### 2. (Optional) Re-train the model
```bash
python train_model.py
```
This will regenerate:
- `monthly_sales.csv`
- `model.pkl`
- `scaler.pkl`

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
Go to:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖥 Example Usage

1. Select **Store ID** (1–10)  
2. Enter **Year** (e.g., 2024)  
3. Enter **Month** (1–12)  
4. Select **Promotion** (0 or 1)  
5. Enter **Previous Month Sales** (estimate if unknown)  
6. Click **Predict Sales**

<img width="769" height="626" alt="image" src="https://github.com/user-attachments/assets/65b1d733-4e56-42b5-9a1c-7a1c3df613a6" />


You’ll get:
- **Predicted monthly sales** (₹ by default)

<img width="769" height="626" alt="image" src="https://github.com/user-attachments/assets/ed87d0bb-374a-4512-b615-31b41c266a24" />

---

## 📌 Notes
- The dataset is synthetic for demonstration purposes.
- Replace `monthly_sales.csv` with your own real sales data for production use.
- Feature engineering includes seasonality (`month_sin`, `month_cos`), which helps model monthly patterns.
- To improve accuracy, add more features like holidays, regional events, marketing campaigns, or prices.

---

## 🙋 Author
**Hari Prasath S**  
GitHub: [@hariprasath2105](https://github.com/hariprasath2105)
