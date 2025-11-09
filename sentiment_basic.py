
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from colorama import Fore, Style, init

init(autoreset=True)
analyzer = SentimentIntensityAnalyzer()

print("Enter a few sentences (type 'done' when finished):")

sentences = []
while True:
    text = input("> ")
    if text.lower() == "done":
        break
    sentences.append(text)

print("\nResults:\n")
best = {"text": None, "score": -1}
worst = {"text": None, "score": 1}

for s in sentences:
    score = analyzer.polarity_scores(s)['compound']
    sentiment = "Positive" if score >= 0.05 else "Negative" if score <= -0.05 else "Neutral"

    if sentiment == "Positive":
        color = Fore.GREEN
    elif sentiment == "Negative":
        color = Fore.RED
    else:
        color = Fore.YELLOW

    print(color + f"{s} → {sentiment} (score = {score})" + Style.RESET_ALL)

    if score > best["score"]:
        best = {"text": s, "score": score}
    if score < worst["score"]:
        worst = {"text": s, "score": score}

print(Fore.CYAN + f"\nMost positive: {best['text']}")
print(Fore.MAGENTA + f"Most negative: {worst['text']}" + Style.RESET_ALL)
