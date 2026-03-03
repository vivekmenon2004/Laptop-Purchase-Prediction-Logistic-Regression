# PredictiveAI: Laptop Purchase Prediction (Logistic Regression)

An intelligent Machine Learning web application that predicts customer buying behavior for laptops using Binary Classification mapping hardware specifications to purchase decisions.

## 🚀 Features
- **Modern AI Landing Page**: A premium, dark-themed UI built with Tailwind CSS and Material Symbols.
- **Predictive Engine**: Leverages a Logistic Regression model trained on technical hardware specifications.
- **INR Currency Support**: Input prices in Indian Rupees (₹) with automatic unit conversion.
- **Dynamic Feedback**: Real-time analysis simulation with accuracy and latency indicators.

## 🛠️ Technical Specifications Analyzed
The model uses 9 key features to determine purchase probability:
1. **Price** (Input in ₹ INR)
2. **RAM** (GB)
3. **Storage** (GB)
4. **Processor Score** (1-10)
5. **Screen Size** (Inches)
6. **Weight** (KG)
7. **Battery** (Wh)
8. **Touchscreen** (Yes/No)
9. **Dedicated GPU** (Yes/No)

## 📂 Project Structure
- `index.html`: The main web application interface.
- `Logistic_Regression.ipynb`: Jupyter Notebook containing model training and evaluation logic.
- `Laptop_Logistic_Regression_Dataset.xlsx`: High-quality curated dataset of 70 records.
- `inspect_data.py`: Utility script for dataset verification.

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/vivekmenon2004/Laptop-Purchase-Prediction-Logistic-Regression.git
   ```
2. Open `index.html` in any modern web browser to use the prediction interface.
3. Explore `Logistic_Regression.ipynb` in Jupyter Notebook or Google Colab to see the underlying ML logic.

---
Built with Python, Scikit-learn, and Tailwind CSS.
