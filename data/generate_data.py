# generate_dataset.py

import pandas as pd
import numpy as np

np.random.seed(42)

n_samples = 500

# Generate synthetic features
ages = np.random.randint(20, 80, n_samples)
cholesterol = np.random.randint(150, 300, n_samples)

# Basic rule for risk (not perfectly linear to add some noise)
risk = [
    1 if (a > 50 and c > 220) or (c > 250) else 0
    for a, c in zip(ages, cholesterol)
]

df = pd.DataFrame({
    "age": ages,
    "cholesterol_level": cholesterol,
    "risk_level": risk
})

df.to_csv("health_data.csv", index=False)
print("✅ Dataset saved to data/health_data.csv")

