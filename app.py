from flask import Flask, request, render_template_string
from sentiment_basic import analyze_text   # 👈 connects Flask to your AI file

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
  <head><title>Syna Sentiment Analyzer</title></head>
  <body style="font-family:sans-serif; text-align:center; margin-top:50px;">
    <h2>Enter text to analyze sentiment</h2>
    <form method="POST">
      <textarea name="text" rows="4" cols="60"></textarea><br><br>
      <input type="submit" value="Analyze">
    </form>
    {% if sentiment %}
      <h3>Sentiment: {{ sentiment }}</h3>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        text = request.form.get("text", "")
        sentiment = analyze_text(text)  # 👈 calls your AI logic
    return render_template_string(HTML, sentiment=sentiment)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
