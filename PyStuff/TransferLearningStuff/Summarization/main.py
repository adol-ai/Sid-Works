from transformers import pipeline
import pprint

s = str(input("Enter Content: "))
x = int(input("\nMinimal Word Count: "))
summarizer = pipeline(task="summarization", model="facebook/bart-large-cnn")
ans = summarizer(s, min_length=x)

pprint.pprint(ans)