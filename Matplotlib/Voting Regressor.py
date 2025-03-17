import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor, VotingRegressor
from sklearn.linear_model import LinearRegression

# Load diabetes dataset
X, y = load_diabetes(return_X_y=True)

# Train individual regressors
reg1 = GradientBoostingRegressor(random_state=1)
reg2 = RandomForestRegressor(random_state=1)
reg3 = LinearRegression()

# Fit individual models
reg1.fit(X, y)
reg2.fit(X, y)
reg3.fit(X, y)

# Train the Voting Regressor (ensemble)
ereg = VotingRegressor([("gb", reg1), ("rf", reg2), ("lr", reg3)])
ereg.fit(X, y)

# Predict on the first 20 samples
xt = X[:20]
pred1 = reg1.predict(xt)
pred2 = reg2.predict(xt)
pred3 = reg3.predict(xt)
pred4 = ereg.predict(xt)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot predictions for each model
plt.plot(pred1, "gd", label="GradientBoostingRegressor")
plt.plot(pred2, "b^", label="RandomForestRegressor")
plt.plot(pred3, "ys", label="LinearRegression")
plt.plot(pred4, "r*", ms=10, label="VotingRegressor")

# Improve plot formatting
plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
plt.ylabel("Predicted value")
plt.xlabel("Training samples")
plt.legend(loc="best")
plt.title("Regressor Predictions and Their Average")

plt.savefig("voting regressor", dpi=300)
# Show the plot
plt.show()
