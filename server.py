''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer as sense

#Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    #TO DO
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze == '':
        return "Please enter some text."
    response = sense(text_to_analyze)
    label = response['label']
    score = response['score']
    if label is None:
        return "Invalid input! Please try again."
    label_1 = label.split('_')[1] # Drop 'SENT_' from label
    return f"The given text has been identified as {label_1} with a score of {score}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TO DO
    return render_template("index.html")

@app.errorhandler(500)
def invalid_input():
    ''' This is to handle errors. 
    '''
    return ({"message": "Invalid input! Please try again."}, 500)

# if __name__ == "__main__":
#     ''' This functions executes the flask app and deploys it on localhost:5000
#     '''
      #TO DO
#     app.run(host = "0.0.0.0", port = "5000")
app.run(host = "0.0.0.0", port = "5000")
