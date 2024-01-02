# EasyDataS - Your Data Science Work Made Easy

EasyDS is a Python library designed to simplify common tasks in the data science workflow. It provides functionality for data loading, preprocessing, feature engineering, model training, evaluation, deployment, and more.

## Installation

You can install EasyDS using pip. Run the following command in your terminal:

```bash
pip install easyds
```

## Getting Started

Here's a quick example demonstrating how to use EasyDS:

from easyds.core.data import read_data
from easyds.core.preprocessing import preprocess_data
from easyds.core.model import train_classification_model
from easyds.core.evaluation import evaluate_classification_model

## Read data

data = read_data('path/to/your/data.csv')

## Preprocess data

numerical_cols = ['numerical_feature1', 'numerical_feature2']
preprocessed_data = preprocess_data(data, numerical_cols)

## Split data, train model, and evaluate

### (Assuming 'target_column' is your target variable)

X_train, X_test, y_train, y_test = ...

model = train_classification_model(X_train, y_train)
accuracy = evaluate_classification_model(model, X_test, y_test)

print(f'Model Accuracy: {accuracy}')

## Features

1. Data loading and saving
2. Data preprocessing and cleaning
3. Feature engineering
4. Model training and evaluation
5. Visualization and helpers for data exploration

## Contributing

We welcome contributions! If you find any issues or have ideas for improvements, please open an issue or submit a pull request on our GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact US

Bahadur Khan k201081@nu.edu.pk
Sumsam Ali k201075@nu.edu.pk
