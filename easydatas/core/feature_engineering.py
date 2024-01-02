from sklearn.feature_selection import SelectKBest, f_classif

def select_best_features(X_train, y_train, k=5):
    selector = SelectKBest(score_func=f_classif, k=k)
    X_train_selected = selector.fit_transform(X_train, y_train)
    return X_train_selected
