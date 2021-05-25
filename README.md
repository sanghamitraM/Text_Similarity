## Text-Similarity-Model
This is a project which takes two texts as input and uses the cosine similarity metric on the TF-IDF values to determine how similar they are.

### Prerequisites
Flask (for API) and Numpy. Check Requirements.txt.

### Project Structure
This project has four major parts :
1. app.py - This contains Flask APIs that receives text input through GUI or API calls, computes the similarity value based on TF_IDF and cosines similarity and returns it.
3. request.py - This uses requests module to call APIs defined in app.py and displays the output value.
4. templates - This folder contains the HTML template to allow user to enter two text inputs and displays the similarity value.

### Running the project deployed on Heroku using Flask
1. Navigate to the URL: https://text-similarity-cosine-api.herokuapp.com/

2. Enter valid text values in both the two input boxes and hit Calculate button.

### Running the project locally
1. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

2. Navigate to URL http://localhost:5000

3. Enter valid text values in both the two input boxes and hit Calculate button.
