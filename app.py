import numpy as np
import re, math, copy
from collections import OrderedDict
from collections import Counter
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    doc1 = request.form["Text1"]
    doc2 = request.form["Text2"]
    doc_text = [doc1, doc2]
    
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    for i in range(len(symbols)):
        doc_files = np.char.replace(doc_text, symbols[i], ' ')
        doc_files = np.char.replace(doc_text, "  ", " ")
    doc_text = np.char.replace(doc_text, ',', '')
    doc_text = np.char.replace(doc_text, "'", "")
    doc_text = list(doc_text)
    
    tokenized_documents = [re.findall(r'\w+', d.lower()) for d in doc_text]
    lexicon = sorted(set(sum(tokenized_documents, [])))
    vector_template = OrderedDict((token, 0) for token in lexicon)
    
    doc_tfidf_vectors = []
    for doc_tokens in tokenized_documents:
        vec = copy.copy(vector_template)
        token_counts = Counter(doc_tokens)
        for key, value in token_counts.items():
            docs_containing_key = 0
            for _doc_tokens in tokenized_documents:
                if key in _doc_tokens:
                    docs_containing_key += 1
            tf = value / len(doc_tokens)
            if docs_containing_key:
                idf = len(tokenized_documents) / docs_containing_key
            else:
                idf = 0
            vec[key] = tf * idf
        doc_tfidf_vectors.append(vec)
        
    vec1 = list(doc_tfidf_vectors[0].values())
    vec2 = list(doc_tfidf_vectors[1].values())
    
    dot_prod = 0
    for i, v in enumerate(vec1):
        dot_prod += v * vec2[i]
    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))
    sim = dot_prod / (mag_1 * mag_2)

    output = sim

    return render_template('index.html', prediction_text='Cosine Similarity is {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)