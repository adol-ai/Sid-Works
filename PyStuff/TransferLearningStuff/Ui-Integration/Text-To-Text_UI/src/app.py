from flask import Flask, request, jsonify
from transformers import pipeline
from colorama import Fore, Style
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_text():
    data = request.json
    input_text = data.get('inputText', '')
    print(Fore.CYAN + Style.BRIGHT + "\nJus' Got the Text Content In !" + Fore.RESET)
    min_word_count = int(data.get('min_word_count', 0)) 
    max_length = min(len(input_text.split(' ')) + 50, 512)

    summarizer = pipeline(task="summarization", model="facebook/bart-large-cnn")
    summary = summarizer(input_text, max_length=max_length, min_length=min_word_count)
    generated_summary = summary[0]['summary_text']
    print(Fore.WHITE + Style.BRIGHT + "\tThe Content is Out !" + Fore.RESET)

    return jsonify({'summary': generated_summary})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
