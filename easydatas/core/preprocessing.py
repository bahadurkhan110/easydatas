from sklearn.preprocessing import StandardScaler

def preprocess_data(data, numerical_cols):
    scaler = StandardScaler()
    data[numerical_cols] = scaler.fit_transform(data[numerical_cols])
    return data
