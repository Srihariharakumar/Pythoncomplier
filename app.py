# app.py
import json
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Reading questions from file
with open(r'C:\Users\Arun\Documents\Python_assessment\questions.json', 'r') as file:
    data = json.load(file)

# logic , function to save answers in JSON file
def save_document_as_json(user_answers):
    try:
        with open('user_answers.json', 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(user_answers)

    with open('user_answers.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

# Routes
@app.route('/')
def home():
    ran_home = random.randint(0, len(data['python']) - 1)
    global initial_question
    initial_question = data['python'][str(ran_home)]
    return render_template('text_box.html', question=initial_question)

@app.route('/get_next_question')
def get_next_question():
    ran = random.randint(0, len(data['python']) - 1)
    next_question = data['python'][str(ran)]
    return jsonify({'question': next_question})

@app.route('/save_answer', methods=['POST'])
def save_answer():
    answer = request.json.get('answer')
    question = request.json.get('question')
    question_number = request.json.get('question_number')
    formatted_question = f"{question}"
    save_document_as_json({formatted_question: answer})
    return jsonify({'message': 'Answer saved successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)
