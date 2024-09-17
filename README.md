# **Insurance Analytics Project README**

## **Overview**

This project involves analyzing historical insurance claim data to optimize marketing strategies and identify low-risk targets for premium reduction. The analyses include exploratory data analysis (EDA), A/B hypothesis testing, and version control using Data Version Control (DVC). The goal is to provide actionable insights to enhance marketing strategies and attract new clients by identifying risk patterns and potential savings.

## **Contents**

1. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
2. [Data Version Control (DVC)](#data-version-control-dvc)
3. [A/B Hypothesis Testing](#ab-hypothesis-testing)
4. [StatisticalModeling]
5. [Readme File for Tasks and Analysis](#readme-file-for-tasks-and-analysis)

## **Exploratory Data Analysis (EDA)**

### **1. Data Summarization**

- **Descriptive Statistics**: Calculated variability for numerical features such as `TotalPremium` and `TotalClaims`.
- **Data Structure**: Reviewed the data types of each column to ensure proper formatting.

```python
print(df.describe())
print(df.info())
```

### **2. Data Quality Assessment**

- **Missing Values**: Checked for and addressed missing values.

```python
print(df.isnull().sum())
```

### **3. Univariate Analysis**

- **Distribution of Variables**: Plotted histograms for numerical columns and bar charts for categorical columns.

```python
sns.histplot(df['TotalPremium'])
sns.countplot(x='Gender', data=df)
```

### **4. Bivariate and Multivariate Analysis**

- **Correlations and Associations**: Explored relationships between `TotalPremium` and `TotalClaims` as a function of `PostalCode` using scatter plots and correlation matrices.

```python
sns.scatterplot(x='TotalPremium', y='TotalClaims', hue='PostalCode', data=df)
```

### **5. Data Comparison**

- **Trends Over Geography**: Compared changes in insurance cover type, premium, auto make, etc., across provinces and postal codes.

```python
sns.boxplot(x='Province', y='TotalPremium', data=df)
```

### **6. Outlier Detection**

- **Box Plots**: Used to detect outliers in numerical data.

```python
sns.boxplot(x='TotalClaims', data=df)
```

### **7. Visualization**

- **Key Plots**: Created plots that capture insights gained from the EDA.

```python
sns.heatmap(province_contingency_table, annot=True, cmap='coolwarm', fmt='d')
```

## **Data Version Control (DVC)**

### **1. Install DVC**

- Install DVC using pip.

```bash
pip install dvc
```

### **2. Initialize DVC**

- Initialize DVC in your project directory.

```bash
dvc init
```

### **3. Set Up Local Remote Storage**

- **Create a Storage Directory**:

  ```bash
  mkdir /path/to/your/local/storage
  ```

- **Add the Storage as a DVC Remote**:

  ```bash
  dvc remote add -d localstorage /path/to/your/local/storage
  ```

### **4. Add Your Data**

- **Track Datasets**:

  ```bash
  dvc add <data.csv>
  ```

### **5. Commit Changes to Version Control**

- **Commit the .dvc Files**:

  ```bash
  git add <data.csv>.dvc .gitignore
  git commit -m "Add raw data with DVC"
  ```

### **6. Push Data to Local Remote**

- **Push Data**:

  ```bash
  dvc push
  ```

## **A/B Hypothesis Testing**

### **1. Hypotheses**

- **Hypothesis 1**: There are no risk differences across provinces.
- **Hypothesis 2**: There are no risk differences between postal codes.
- **Hypothesis 3**: There are no significant margin (profit) differences between postal codes.
- **Hypothesis 4**: There are no significant risk differences between men and women.

### **2. Data Segmentation**

- **Group A (Control)**: Plans without the feature.
- **Group B (Test)**: Plans with the feature.

### **3. Statistical Testing**

- **Chi-Square Test**: For categorical variables.

  ```python
  chi2_stat_province, p_value_province, dof_province, expected_province = chi2_contingency(province_contingency_table)
  ```

- **t-Test**: For continuous variables.

  ```python
  t_stat_premium, p_value_premium = ttest_ind(group_A, group_B)
  ```

- **Interpretation**: Analyze p-values to determine whether to reject or fail to reject the null hypotheses.

### **4. Statistical Equivalence**

- Ensure that other key variables (e.g., VehicleType, InsurancePlan) are statistically similar across groups before testing the hypotheses.

```python
# Chi-Square test for VehicleType across provinces
chi2_stat_vehicle, p_value_vehicle, dof_vehicle, expected_vehicle = chi2_contingency(vehicle_type_contingency_table)
```

---

## **Summary**

This project involved analyzing a dataset with over 1 million records to optimize insurance marketing strategies and identify low-risk targets. The analysis included exploratory data analysis (EDA), data version control using DVC, and hypothesis testing using Chi-Square tests and t-tests. Key insights from the data were visualized, and statistical methods were employed to ensure robust and reliable results.

Feel free to adjust any details or add more specifics based on your actual implementation or needs!
