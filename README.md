# Sales Analytics Dashboard 

  An interactive **Sales Analytics Dashboard** built with **Streamlit + Plotly**, integrated with a **Machine Learning model** to predict future sales and uncover actionable business insights.
---

## Features Overview 

### Dashboard

- Sales by Region

- Sales by Category

- Monthly Sales Trend

- Discount vs Profit Analysis

- Correlation Heatmap 

### Machine Learning 

- Model: **Random Forest Regressor**
- Feature Engineering:
  - Month & Year extraction
  - One-hot encoding
- Evaluation Metrics:
  - R² Score
  - Mean Absolute Error (MAE)

### Prediction

- Input business parameters

- Get instant sales prediction

---

## Tech Stack

- Python
- Streamlit
- Plotly
- Pandas
- Scikit-learn

---

## Screenshots

### Main Dashboard & KPIs

![alt text](<Main Dashboard & KPIs.png>)



### Advanced Analytics Charts

 ![alt text](<Advanced Analytics Charts.png>)

 ![alt text](<Discount vs Profit.png>)

 ![alt text](<Correlation Heatmap.png>)

 ![alt text](<Monthly Trend.png>)


### ML Prediction Interface

 ![alt text](<ML Prediction Interface.png>)

---

##  Quick Start Guide Prerequisites

- Python 3.11.9

- Git

- pip

---

## Installation & Setup
 
 git clone https://github.com/your-username/sales-dashboard.git
cd sales-dashboard
pip install -r requirements.txt
streamlit run app.py

>Local URL: http://localhost:8501

--- 

## Dependencies

> Create a requirements.txt file with:

- streamlit
- pandas
- plotly
- scikit-learn
- numpy==1.24.3

--- 

## Project Structure

>sales-dashboard/
├── app.py
├── sales.csv
├── requirements.txt
├── screenshots/
│   ├── dashboard.png
│   ├── charts.png
│   └── prediction.png
└── README.md

---

## Technology Stack

| Component       | Technology        | Purpose                                  |
| --------------- | ----------------- | ---------------------------------------- |
| Frontend        | Streamlit, Plotly | Interactive dashboard and charts         |
| ML Model        | Scikit-learn      | RandomForestRegressor for prediction     |
| Data Processing | Pandas            | Cleaning, filtering, feature engineering |
| Deployment      | Streamlit Cloud   | Live hosting                             |

 ---

## Advanced Visualizations

 | Chart Type                     | Business Insight                                |
| ------------------------------ | ----------------------------------------------- |
| Monthly Sales and Profit Trend | Tracks performance over time                    |
| Regional Sales Bar Chart       | Compares regional contribution                  |
| Category Profit Chart          | Shows profitable categories                     |
| Treemap                        | Displays order breakdown by region and category |
| Correlation Heatmap            | Shows numeric relationships in data             |
| Year-wise Sales Chart          | Highlights growth patterns                      |

---

## Machine Learning Pipeline

- Model: Random ForestRegressor( n_estimators=150) .

- Features include: Month, Year,Region, Category, Discount, Quantity

- Uses train- test split for more realistic evaluation.

- Reports R² score and Mean Absolute Error (MAE).

---

## Usage Workflow

1.  Upload a CSV file from the sidebar or use **Sales. csv**.

2.  Apply filters for Region, Category, and Date Range.

3.  Explore the charts and KPI cards.

4.  Use the prediction form to estimate future sales.

5.  Deploy on Streamlit Cloud and share the live app link.

---

## Sample Dataset Schema

| Order Date | Region | Category    | Sales | Profit | Discount | Quantity |
|------------|--------|-------------|-------|--------|----------|----------|
| 2023-01-15 | West   | Electronics | 25000 | 4500   | 0.10     | 5        |

- Required columns: Order Date, Region, Category, Sales, Proﬁt.

---

##  Author Information

> Simhadri Itrajula

> Artificial intelligence and Data Science Student

---

- LinkedIn: **www.linkedin.com/in/simhadri-itrajula-19366b405**

- GitHub: **https://github.com/simhadri118**

- Email: **simhadriitrajula2006@gmail.com**

---

##  License

> This project is Licensed under the MIT License - free to use, modify,and distribute.

---

## Deployment

1.  Push the code to GitHub.

2.  Connect the repository to Streamlit Cloud.

3.  Deploy and get a public app link for internship or portfolio use.

---

## Future Enhancements

- CSV upload feature

- Model tuning & optimization

- Cloud deployment (Streamlit Cloud / AWS)

- Time-series forecasting

---

## Notes

- Model is trained on available dataset for demonstration purposes

- Ensure Sales.csv is present in the project folder
