import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model import load_data  # noqa: E402
from utils import load_model  # noqa: E402
from evaluate import evaluate_model  # noqa: E402


def test_evaluate_model():
    model = load_model()
    data_infile = "data/protein_processed_data.pkl"
    X_train, X_test, y_train, y_test = load_data(data_infile)
    assert evaluate_model(model, X_test, y_test) is None
