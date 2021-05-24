# Would-You-Survive-Titanic-
Linear Regression model to see if you had been in the Titanic would you had survived.
Running the project

    Open CMD. Ensure that you are in the project home directory. Create the machine learning model by running below command -

python mlmodel.py

This would create a serialized version of our model into a file model.pkl

    Run app.py using below command to start Flask API

python app.py

By default, flask will run on port 5000.

    Navigate to URL http://localhost:5000

You should be able to view the homepage.

Enter valid values in all 3 input boxes and hit Predict.

If everything goes well, you should be able to see the predicted vaule on the HTML page and you know if you survived or not.
