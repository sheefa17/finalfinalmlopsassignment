import os
import sys
import pandas as pd
import numpy as np

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from preprocess import preprocess

def test_preprocess_removes_nans():
    # Pass a DataFrame instead of NumPy array
    df = pd.DataFrame({
        "age": [25.0, 30.0],
        "cholesterol": [np.nan, 200.0]
    })

    processed = preprocess(df)

    assert isinstance(processed, np.ndarray)
    assert not np.isnan(processed).any(), "NaN values still present after preprocessing"
