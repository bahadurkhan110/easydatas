import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


def evaluate_classification_model(model, X_test, y_test):
    predictions = model.predict(X_test)

    # Calculate accuracy (existing code)
    accuracy = model.score(X_test, y_test)

    return accuracy

def get_confusion_matrix(model, y_test, predictions):
     # Generate and visualize the confusion matrix
    cm = confusion_matrix(y_test, predictions)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', annot_kws={"size": 16})
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()

    

