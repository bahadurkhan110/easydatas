import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_importance(model, feature_names):
    # Plot feature importance for tree-based models
    feature_importance = model.feature_importances_
    sorted_idx = feature_importance.argsort()

    plt.barh(range(len(sorted_idx)), feature_importance[sorted_idx], align='center')
    plt.yticks(range(len(sorted_idx)), [feature_names[i] for i in sorted_idx])
    plt.xlabel('Feature Importance')
    plt.title('Feature Importance Plot')
    plt.show()
