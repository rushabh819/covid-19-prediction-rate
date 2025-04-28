# COVID-19 Death Rate Prediction

## 📚 Project Description
Predicting COVID-19 death rates per 100,000 population for different countries based on healthcare capacity, vaccination coverage, and socioeconomic indicators.  
We also explore using free open-source LLMs (Large Language Models) to summarize country-level COVID-19 policy responses.

## 📂 Data Sources
- WHO COVID-19 Global Daily Dataset
- World Bank GDP per Capita (manually added)
- Sample country reports (for text summarization)

## 🔧 Methodology
- **Data Wrangling**: Aggregated deaths, engineered deaths per 100k.
- **EDA**: Scatter plots and bar plots to visualize death rates.
- **LLM Summarization**: Summarized policy responses using `facebook/bart-large-cnn`.
- **Modeling**: Linear Regression to predict death rate.
- **Evaluation**: Mean Absolute Error (MAE), Mean Squared Error (MSE), R² Score.

## 📈 Results
- MAE: *xx.xx*
- MSE: *xxx.xx*
- R²: *0.xx*

## 🛠 Technologies Used
- Python 3.8+
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- HuggingFace Transformers

## 🚀 Future Improvements
- Incorporate more features (stringency index, mobility data)
- Try Random Forest, XGBoost for better predictions
- Deploy as a simple web dashboard (optional)

---

## 👨‍💻 Author
Rushabh Parmar  
(Feel free to add your LinkedIn / GitHub profile here.)

---

> This project is for educational purposes as part of a Data Science Final Assignment.
