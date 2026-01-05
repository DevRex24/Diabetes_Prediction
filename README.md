# Diabetes Prediction App 
## 📋 Overview

This application uses the Pima Indians Diabetes Dataset to train an XGBoost classifier that can predict whether a person is likely to have diabetes based on eight medical input parameters. The app provides real-time predictions with probability scores through an intuitive web interface.

## ✨ Features

- **Real-time Predictions**: Instant diabetes risk assessment based on user inputs
- **Probability Scores**: Get confidence levels for each prediction
- **User-Friendly Interface**: Clean and intuitive Streamlit UI
- **Efficient Caching**: Model training and data loading are cached for optimal performance
- **Color-Coded Results**: Easy-to-understand visual feedback (green for negative, red for positive)

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or download this repository**

2. **Install required dependencies**:
   ```bash
   pip install streamlit numpy pandas xgboost
   ```

   Or create a `requirements.txt` file with:
   ```
   streamlit
   numpy
   pandas
   xgboost
   ```
   
   Then install:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Navigate to the project directory**:
   ```bash
   cd PROJECT
   ```

2. **Run the Streamlit app**:
   ```bash
   streamlit run Diabetes_predict.py
   ```

3. **Open your browser** and go to:
   - Local URL: `http://localhost:8501`
   - Network URL: `http://192.168.29.172:8501` (accessible from other devices on your network)

## 📊 Input Parameters

The app requires the following medical parameters:

| Parameter | Description | Range |
|-----------|-------------|-------|
| **Pregnancies** | Number of times pregnant | 0-20 |
| **Glucose** | Plasma glucose concentration | 0-200 mg/dL |
| **Blood Pressure** | Diastolic blood pressure | 0-140 mm Hg |
| **Skin Thickness** | Triceps skin fold thickness | 0-100 mm |
| **Insulin** | 2-Hour serum insulin | 0-900 mu U/ml |
| **BMI** | Body mass index | 0.0-70.0 kg/m² |
| **Diabetes Pedigree Function** | Diabetes heredity score | 0.0-3.0 |
| **Age** | Age in years | 0-120 |

## 🧠 Model Information

- **Algorithm**: XGBoost (Extreme Gradient Boosting)
- **Dataset**: Pima Indians Diabetes Dataset
- **Features**: 8 medical parameters
- **Target**: Binary classification (Diabetic/Non-Diabetic)
- **Evaluation Metric**: Log Loss

## 📁 Project Structure

```
PROJECT/
│
├── Diabetes_predict.py    # Main Streamlit application
└── README.md             # Project documentation
```

## 🔧 How It Works

1. **Data Loading**: The app loads the Pima Indians Diabetes dataset from GitHub
2. **Model Training**: An XGBoost classifier is trained on the dataset (cached for efficiency)
3. **User Input**: Users enter their medical parameters through the web interface
4. **Prediction**: The model predicts diabetes likelihood with probability scores
5. **Results Display**: Color-coded results show the prediction and confidence level

## 📈 Example Usage

1. Enter your medical parameters in the input fields
2. Click the "Predict" button
3. View your prediction result:
   - **Green (Success)**: Negative - Low diabetes risk
   - **Red (Error)**: Positive - High diabetes risk
4. Check the probability score for confidence level

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)**: Web application framework
- **[XGBoost](https://xgboost.readthedocs.io/)**: Machine learning algorithm
- **[Pandas](https://pandas.pydata.org/)**: Data manipulation
- **[NumPy](https://numpy.org/)**: Numerical computing

## ⚠️ Disclaimer

This application is for **educational and informational purposes only**. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📧 Contact

For questions or feedback, please reach out through GitHub.

---

**Made with ❤️ using Streamlit and XGBoost**
