import openai

#need to remove the key before pushing to GitHub
openai.api_key = ""

def sentiment_analysis(texts):
    sentiments = []
    for text in texts:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt='Sentiment analysis of the following text: ' + text + '\n' + '\n' + 'Label the sentiment as positive, neutral, or negative. Do not provide any other feedback or words in your response.',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = response["choices"][0]["text"].strip()
        sentiment = message.split("\n")[-1].strip()
        sentiments.append(sentiment)
    return sentiments

texts = ["This sample text is sus.",
         "This sample text is a little ok.",
        "This third sample text is good."]
sentiments = sentiment_analysis(texts)

print(sentiments)

for sentiment in sentiments:
  print("Sentiments:", sentiment)