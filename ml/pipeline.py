'''
This is an example of the instantiation of a Pipeline with any standardized regressor with a test size of 20%.

Inspired from the "Supervised Learning with scikit-learn" course on Datacamp.com
Author: Alex Nakagawa
'''
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Setup the pipeline
steps = [('scaler', StandardScaler()),
         ('*ANY_REGRESSOR*', '*REGRESSOR_OBJECT*')]

pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {'*REGRESSOR*__C':[1, 10, 100],
              '*REGRESSOR*__gamma':[0.1, 0.01]}

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=21)

# Instantiate the GridSearchCV object: cv
cv = GridSearchCV(pipeline, parameters, cv=3)

# Fit to the training set
cv.fit(X_train,y_train)

# Predict the labels of the test set: y_pred
y_pred = cv.predict(X_test)

# Compute and print metrics
print("Accuracy: {}".format(cv.score(X_test, y_test)))
print(classification_report(y_test, y_pred))
print("Tuned Model Parameters: {}".format(cv.best_params_))
