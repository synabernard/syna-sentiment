from flask import Flask, request, render_template_string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

HTML = """
<!DOCTYPE html>
<html>
  <head><title>Sentiment Analyzer</title></head>
  <body style="font-family:sans-serif; text-align:center; margin-top:50px;">
    <h2>Enter text to analyze sentiment</h2>
    <form method="POST">
      <textarea name="text" rows="4" cols="60"></textarea><br><br>
      <input type="submit" value="Analyze">
    </form>
    {% if sentiment is not none %}
      <h3>Sentiment: {{ sentiment }}</h3>
      <p>Score: {{ score }}</p>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment, score = None, None
    if request.method == "POST":
        text = request.form.get("text", "")
        scores = analyzer.polarity_scores(text)
        score = scores["compound"]
        if score >= 0.05:
            sentiment = "Positive"
        elif score <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
    return render_template_string(HTML, sentiment=sentiment, score=score)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
