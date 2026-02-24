# Iris Dataset – Exploratory Data Analysis & Classification

This project explores the classic **Iris flower dataset** using Python and Jupyter Notebook.  
The goal is to understand how sepal and petal measurements differ across species and to build a simple model that can predict the species of an iris flower from these features. 

---

## 📊 Dataset Overview

The Iris dataset contains **150 samples** of iris flowers from three species:

- *Iris-setosa*
- *Iris-versicolor*
- *Iris-virginica* 

For each flower, four numeric features are recorded:

- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm) 

No missing values were found, and the dataset is **balanced** with 50 samples per species. 

---

## 🔧 Workflow

1. **Data loading & inspection**  
   - Loaded the CSV into a Pandas DataFrame.  
   - Checked shape, column types, basic statistics, and class distribution.

2. **Data cleaning & preparation**  
   - Verified absence of null values and handled any duplicates.  
   - Ensured numeric types for all measurement columns.  
   - Performed basic sanity checks for unusual values/outliers.

3. **Exploratory Data Analysis (EDA)**  
   - Histograms to inspect distributions of sepal and petal measurements.  
   - Boxplots to compare features across species and highlight outliers.   
   - Scatter plots and pairplots to visualize relationships between features and species separation.

4. **Model training & evaluation**  
   - Framed the task as a **multi‑class classification** problem with `Species` as the target.   
   - Split the data into training and test sets.  
   - Trained a simple baseline classifier (e.g., Logistic Regression / k‑NN). 
   - Evaluated performance using:
     - Accuracy score  
     - Confusion matrix  
     - Classification report (precision, recall, F1-score)

---

## 🔍 Key Insights

- **Petal measurements** (length and width) clearly separate the three species and show strong positive relationships: as petal length increases, petal width tends to increase as well.   
- **Iris-setosa** forms a well-separated cluster with much smaller petal measurements, while *versicolor* and *virginica* overlap more but are still distinguishable in petal feature space.   
- Sepal features alone provide weaker separation, but combined with petal features they support robust classification. 

The baseline classification model achieved **high accuracy** on the test set, with only a small number of misclassifications between *versicolor* and *virginica*.

---

## 🛠️ Tech Stack

- Python  
- Jupyter Notebook  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- scikit-learn 

---

## 📂 Project Structure

- `Internship_Material/Task 1.ipynb` – main notebook with EDA, modeling, and commentary  
- `Internship_Material/Iris.csv` – dataset file  

---

## 🚀 Possible Extensions

- Try alternative classifiers (k‑NN, SVM, decision trees) and compare performance.  
- Perform feature importance analysis to quantify which measurements contribute most to predictions.  
- Experiment with dimensionality reduction (e.g., PCA) for 2D/3D visualizations of the feature space. 
