from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Generate random data for demonstration
np.random.seed(42)
num_samples = 100
data = {
    f"Feature_{i+1}": np.random.rand(num_samples) for i in range(9)
}
data["Target_Variable"] = 2 * data["Feature_1"] + 3 * data["Feature_2"] + np.random.normal(0, 0.1, num_samples)

# Convert the data dictionary to a DataFrame
df = pd.DataFrame(data)

# Split data into features (X) and target variable (y)
X = df.drop("Target_Variable", axis=1)
y = df["Target_Variable"]

# Build the model
model = LinearRegression()
model.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the input values from the form
        input_values = [float(request.form[f"feature_{i+1}"]) for i in range(9)]
        
        # Convert the input values to a DataFrame with the same columns as the training data
        input_data = pd.DataFrame([input_values], columns=X.columns)
        
        # Make the prediction using the model
        prediction = model.predict(input_data)
        
        # Display the result in the result template
        return render_template('result.html', prediction=prediction[0])
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
