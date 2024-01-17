from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

'''
Function to analyse the sentiment in a text
'''
def analyze_sentiment(text):
  try:
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
  except:
    return "Error", {}

  #classification
  #https://vadersentiment.readthedocs.io/en/latest/pages/about_the_scoring.html
  if sentiment_score['compound'] >= 0.5:
    sentiment = 'Positive'
  elif -0.5 < sentiment_score['compound'] < 0.5:
    sentiment = 'Neutral'
  else:
    sentiment = 'Negative'

  return sentiment, sentiment_score

@app.route('/ana-sentiment', methods=['POST'])
def analyze_endpoint():
  text = request.json['text']
  sentiment, sentiment_score = analyze_sentiment(text)
  return jsonify({'sentiment': sentiment, 'sentiment_score': sentiment_score})


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)