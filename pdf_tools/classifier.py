from .feature_extraction import feature_extraction

import joblib


def predict(path):
    features = feature_extraction(path)
    clf = joblib.load('pdf_tools/model.joblib')
    result = clf.predict(features)
    return result[0] == "yes"
