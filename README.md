# iris-classification
# 🌸 Iris Flower Species Prediction App

This is a simple web application built with [Streamlit](https://streamlit.io/) that predicts the species of an Iris flower based on user-provided measurements. The model uses the **K-Nearest Neighbors (KNN)** algorithm and was trained on the classic **Iris dataset**.

## 🚀 Features

- Interactive sliders to input Sepal and Petal dimensions.
- Real-time prediction of flower species using a trained KNN model.
- User-friendly and intuitive web interface.
- Species supported:
  - **Setosa**
  - **Versicolor**
  - **Virginica**


- **Algorithm:** K-Nearest Neighbors (KNN)
- **Training Dataset:** Iris dataset from Scikit-learn
- **Model File:** `knn_model.pkl` (saved using `joblib`)

## 📦 Installation

1. **Clone this repository:**

```bash
git clone https://github.com/yourusername/iris-knn-streamlit-app.git
cd iris-knn-streamlit-app
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app:**

```bash
streamlit run app.py
```


