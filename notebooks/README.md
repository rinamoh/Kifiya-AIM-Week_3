AB_hypothesisTestingHypothesis --- Testing for Car Insurance Data

1. Importing Necessary Packages
   The code begins by importing essential Python libraries:

pandas and numpy are used for data manipulation and numerical operations.
scipy.stats provides functions for statistical tests.
seaborn and matplotlib.pyplot are used for data visualization.
sklearn.model_selection.StratifiedShuffleSplit is used to create balanced splits of data based on categorical features. 2. Loading the Dataset
The dataset is loaded from a CSV file into a Pandas DataFrame. This is where all subsequent data manipulations and analyses will be performed.

3. Ensuring Correct Data Types
   The code converts certain columns to categorical types. This is crucial because categorical data needs to be handled differently from numerical data in statistical tests.

4. Creating Additional Features
   New columns are added to the dataset:

ProfitMargin: This column calculates the difference between the total premium paid and the total claims made. It's useful for evaluating profitability.
RiskCategory: This column classifies TotalClaims into risk categories ('Low', 'Medium', 'High') based on claim amounts. This classification helps in segmenting data for further analysis. 5. Hypothesis Testing
Hypothesis 1: Risk Differences Across Provinces
Select Metrics and Segment Data

Total claims are summed by province to understand the distribution of claims across different geographical areas.

Feature Selection and Segmentation

The dataset is split into two groups based on provinces (e.g., Gauteng vs. Western Cape). This segmentation allows for comparison between the selected provinces.

Statistical Equivalence Check

Chi-Square Test: This test is used to determine if there are significant differences in categorical features (e.g., MaritalStatus, VehicleType) between the two provinces. A contingency table is created for each feature, and the Chi-Square test is applied to check for differences.
T-Test: This test compares the mean values of numerical features (e.g., SumInsured) between the two provinces to see if there are significant differences.
Adjust Groups

If significant differences are found in the features between the groups, the groups are adjusted to ensure they are similar with respect to those features. This is done using StratifiedShuffleSplit to ensure that the distributions of categorical features are balanced between the groups.

Re-check Adjustments

After adjusting the groups, the tests are re-run to ensure that the adjustments worked and that the groups are now statistically similar for the features being tested.

Hypothesis 2: Risk Differences Between Zip Codes
Segment Data

The dataset is split based on postal codes. This allows for comparing risk profiles between specific zip codes.

Perform Statistical Tests

A T-test is used to compare the TotalClaims between the selected postal codes to see if there are significant differences in risk profiles.

Hypothesis 3: Profit Margin Differences Between Zip Codes
Calculate Profit

Profit is calculated for both groups (postal codes) as the difference between TotalPremium and TotalClaims.

Perform T-test on Profit

A T-test is performed on the calculated profit to determine if there are significant differences in profit margins between the zip codes.

Hypothesis 4: Risk Differences Between Men and Women
Data Segmentation

The dataset is split by gender, creating two groups: male and female.

Perform Hypothesis Testing

T-Test: This test is applied to TotalClaims to check if there are significant differences in risk profiles between men and women.

# Model Interpretation with LIME

This repository provides an example of using LIME (Local Interpretable Model-agnostic Explanations) for interpreting a regression model trained with XGBoost.

## Prerequisites

Ensure you have the following packages installed:

- `numpy`
- `pandas`
- `xgboost`
- `lime`
- `scikit-learn`

You can install the necessary packages using pip:

```bash
pip install numpy pandas xgboost lime scikit-learn
```

## Overview

This example demonstrates how to:

1. **Train a regression model using XGBoost.**
2. **Use LIME to interpret the model's predictions.**
3. **Explain individual predictions and visualize the explanations.**

## Implementation

### Training the Model

First, ensure you have a trained XGBoost model (`model_xgb`) and a test dataset (`X_test`). This README assumes that these have been prepared as part of your workflow.

### Explanation with LIME

1. **Import Required Libraries**

   ```python
   import numpy as np
   import pandas as pd
   import lime
   import lime.lime_tabular
   from xgboost import XGBRegressor
   ```

2. **Initialize the LIME Explainer**

   ```python
   explainer = lime.lime_tabular.LimeTabularExplainer(
       training_data=np.array(X_train),  # Training data used to fit the model
       feature_names=X_train.columns,    # Feature names
       mode='regression'                 # Mode for regression task
   )
   ```

3. **Choose a Sample to Explain**

   ```python
   i = 0  # Index of the sample you want to explain
   sample = X_test.iloc[i]
   ```

4. **Explain the Prediction for the Selected Sample**

   ```python
   explanation = explainer.explain_instance(
       data_row=np.array(sample),
       predict_fn=model_xgb.predict
   )
   ```

5. **Display the Explanation**

   ```python
   explanation.show_in_notebook(show_table=True, show_all=False)
   ```

   - Alternatively, you can save the explanation to an HTML file:

   ```python
   explanation.save_to_file('lime_explanation.html')
   ```

## Example

After running the code above, you should be able to view an interactive explanation of how different features contributed to the model’s prediction for the selected sample. This can be particularly useful for understanding model behavior and gaining insights into feature importance.

## Notes

- Ensure that `X_train` and `X_test` are preprocessed similarly and that they include the same features.
- The `predict_fn` used in `explain_instance` should match the model’s prediction method.

## Troubleshooting

If you encounter issues, verify the following:

- Your `X_train` and `X_test` have the correct shape and feature names.
- The model is trained and able to make predictions.
- All dependencies are installed and up-to-date.

---

Feel free to adjust the README according to your specific setup or additional details about your project.
