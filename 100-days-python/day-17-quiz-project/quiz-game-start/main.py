from question_model import Question
from data import QuizData
from quiz_brain import QuizBrain
from html import unescape

if __name__ == "__main__":

    question_bank = []

    quiz_data_loader = QuizData()
    quiz_data_loader.load_questions()
    question_data = quiz_data_loader.questions_list["results"]

    for entry in question_data:
        question = Question(unescape(entry["question"]), entry["correct_answer"])
        question_bank.append(question)


    brain = QuizBrain(question_bank)
    brain.question_iteration()