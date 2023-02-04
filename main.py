import openai

openai.api_key = "YOUR_API_KEY"

def sentiment_analysis(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='Sentiment analysis of the following text: ' + text + '\n' + '\n' + 'Label the sentiment as positive, neutral, or negative.',
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response["choices"][0]["text"].strip()
    sentiment = message.split("\n")[-1].strip()

    return sentiment

text = "This is a sample text for sentiment analysis."
sentiment = sentiment_analysis(text)
print("Sentiment:", sentiment)
