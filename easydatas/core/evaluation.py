def evaluate_classification_model(model, X_test, y_test):
    accuracy = model.score(X_test, y_test)
    return accuracy
