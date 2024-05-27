''' This is the code for NLP analyzing of text sentiment using 
    the Watson Embedded AI Libraries. For this project, 
    we're using the BERT based Sentiment Analysis function 
    of the Watson NLP Library.
'''

import json
import requests

def sentiment_analyzer(text_to_analyse):
    ''' This function returns a dict response, 
        which consists of a label and a score.
        There are 3 labels: 
            'SENT_POSITIVE'
            'SENT_NEGATIVE'
            and 'SENT_NEUTRAL'.
    '''
    url = 'https://sn-watson-sentiment-bert.labs.skills'\
            +'.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id"\
                : "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header, timeout=60)
    json_dict = json.loads(response.text)
    label = None
    score = None
    if response.status_code == 200:
        label = json_dict['documentSentiment']['label']
        score = json_dict['documentSentiment']['score']
    return {'label': label, 'score': score}
