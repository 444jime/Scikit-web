# MindTree: Personality Predictor 🧠🤖

An interactive web application that leverages **Machine Learning** to classify personality types (Introvert vs. Extrovert). This project demonstrates the integration of a **Scikit-learn** model within a **Flask** web environment, providing a practical implementation of data science concepts.

## ✨ Key Features

* **Decision Tree Classification**: Utilizes the `DecisionTreeClassifier` from Scikit-learn for accurate personality prediction.
* **Interactive Web Interface**: A clean, user-friendly frontend built with HTML5 and CSS3.
* **Dynamic Visualization**: Generates and displays decision tree diagrams based on the processed dataset.
* **Modular Backend**: Follows a clean architecture with a clear separation between business logic, data management, and presentation.

## 🏗️ Architecture

The project is structured to ensure scalability and code readability:
* **Presentation Layer**: Flask templates and static assets for an intuitive user experience.
* **Business Logic**: Python services that handle model training, prediction, and image generation.
* **Data Layer**: CSV-based dataset management for training the classification model.

## 🛠️ Tech Stack

* **Language**: Python
* **Machine Learning**: Scikit-learn, Pandas, NumPy
* **Web Framework**: Flask
* **Visualization**: Matplotlib / Graphviz
* **Frontend**: HTML5, CSS3

## 🚀 Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/444jime/Scikit-web.git](https://github.com/444jime/Scikit-web.git)
    cd scikit-web
    ```

2.  **Install dependencies**:
    ```bash
    pip install flask scikit-learn pandas matplotlib
    ```

3.  **Run the application**:
    ```bash
    python main.py
    ```

---
*Developed by Tania as part of her Associate Degree in Systems Analysis.*
