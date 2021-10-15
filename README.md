
# **Would You Survive Titanic Disaster --version 1.0**
## - *Run it directly by clicking here:* [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://would-you-survive-the-titanic.herokuapp.com/)

Logistic Regression model to see if you had been on the Titanic would you had survived provided you age, sex and embarkment info.

![Annotation 2021-05-24 175631](https://user-images.githubusercontent.com/68852047/119347676-7aca9300-bcb9-11eb-957b-b622481212eb.png)


### **Running the project locally:**

>Open CMD. Ensure that you are in the project home directory. Create the machine learning model by running below command -

    python mlmodel.py

This would create a serialized version of our model into a file model.pkl

>Run app.py using below command to start Flask API

    python app.py

By default, flask will run on port 5000.

>Navigate to URL http://localhost:5000 on a browser.

You should be able to view the homepage.

Enter valid values in all 3 input boxes and hit Predict.

If everything goes well, you should be able to see the prediction on the web page and you will know your answer.
