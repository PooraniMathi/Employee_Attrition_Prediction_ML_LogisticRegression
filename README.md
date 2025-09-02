Employee Attrition Prediction using Logistic Regression
1. Objective
This project aims to predict whether an employee is likely to leave the company (attrition) using a Logistic Regression model. Employee attrition is a critical concern for organizations, and predictive analytics can assist in developing proactive HR strategies.
2. Dataset Description
The dataset contains demographic and employment-related attributes of employees.
Key features may include:
•	Age
•	Department
•	Job Role
•	Monthly Income
•	Job Satisfaction
•	Years at Company
•	OverTime
•	Total Working Years
•	Attrition (Target variable)
3. Libraries Used
Python libraries used in this project:
•	pandas
•	numpy
•	matplotlib
•	seaborn
•	scikit-learn
4. Data Preprocessing
Data preprocessing involved handling missing values, encoding categorical variables (e.g., using Label Encoding or One-Hot Encoding), and normalizing numerical features. The dataset was split into training and testing sets using an 80-20 ratio.
5. Exploratory Data Analysis
EDA was conducted to understand patterns and correlations in the data.
Visualizations like heatmaps, bar plots, and histograms were used to uncover relationships between features and attrition.
6. Model Building
Logistic Regression was chosen due to its simplicity and interpretability for binary classification. The model was trained on the training dataset using scikit-learn's LogisticRegression() class.
7. Model Evaluation
The model was evaluated using the following performance metrics:
•	Accuracy
•	Confusion Matrix
•	Precision
•	Recall
•	F1-Score
These metrics help in understanding the classification performance, especially in identifying true positives and false positives.
8. Conclusion
The logistic regression model provides an efficient way to predict employee attrition with interpretable results. With further tuning and additional features, the model could be enhanced to support HR decision-making processes more effectively.
