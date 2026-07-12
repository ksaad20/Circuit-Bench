import nbformat as nbf

nb = nbf.v4.new_notebook()

cells = [

("# Hyperparameter Optimization\n\nCircuitBench optimization benchmark.", "markdown"),

("""
import json
from pathlib import Path

import numpy as np
import pandas as pd

from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV,
    train_test_split
)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

SEED = 42
""", "code"),

("""
df = pd.DataFrame({
    "Voltage":[3.65,3.72,3.81,3.95,4.05],
    "Current":[2.1,1.8,1.5,1.1,0.8],
    "Temperature":[25,27,29,31,34],
    "SOC":[18,35,54,76,95]
})

X = df.drop(columns=["SOC"])
y = df["SOC"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=SEED
)
""", "code"),

("""
model = RandomForestRegressor(
    random_state=SEED
)

params = {
    "n_estimators":[50,100,200],
    "max_depth":[None,5,10],
    "min_samples_split":[2,5]
}
""", "code"),

("""
grid = GridSearchCV(
    model,
    params,
    cv=5,
    scoring="neg_root_mean_squared_error"
)

grid.fit(X_train,y_train)

prediction = grid.predict(X_test)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        prediction
    )
)

r2 = r2_score(
    y_test,
    prediction
)

print(grid.best_params_)
print(rmse)
print(r2)
""", "code"),

("""
results = {
    "best_parameters": grid.best_params_,
    "RMSE": float(rmse),
    "R2": float(r2)
}

Path("results").mkdir(exist_ok=True)

with open(
    "results/optimization_report.json",
    "w"
) as f:
    json.dump(
        results,
        f,
        indent=4
    )

print("Optimization completed")
""", "code"),

]

for source, cell_type in cells:
    if cell_type == "markdown":
        nb.cells.append(
            nbf.v4.new_markdown_cell(source)
        )
    else:
        nb.cells.append(
            nbf.v4.new_code_cell(source)
        )

nb.metadata = {
    "kernelspec":{
        "display_name":"Python 3",
        "language":"python",
        "name":"python3"
    }
}

with open(
    "notebooks/7_Hyperparameter_Optimization.ipynb",
    "w",
    encoding="utf-8"
) as f:
    nbf.write(nb,f)

print("Created valid notebook")
