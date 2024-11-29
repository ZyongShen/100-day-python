import requests
class QuizData:

    def __init__(self):
        self.questions_list = [];

    def load_questions(self):
        url = "https://opentdb.com/api.php?amount=10&type=boolean"

        try:
            response = requests.get(url)
            if (response.status_code == 200):
                self.questions_list = response.json()
        except requests.exceptions.RequestException as e:
            print("Error", e)
            return None

    

    