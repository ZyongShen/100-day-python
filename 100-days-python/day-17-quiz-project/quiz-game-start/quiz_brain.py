class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.correct_answers = 0

    def question_iteration(self):
        
        # iterate through the question bank
        for question_entry in self.questions_list:
            # get user answer
            user_answer = input(f"Q.{self.question_number+1}: {question_entry.text} (True/False)? ")

            # track the number of correct answers
            self.check_answer(question_entry.answer, user_answer)

            # increment the question number
            self.question_number += 1

        self.check_score(self.correct_answers, len(self.questions_list))
        


    def check_answer(self, expected_answer, actual_answer):

        if (actual_answer.lower() == expected_answer.lower()):
            self.correct_answers += 1
            print("Correct!")
        else:
            print("Incorrect!")

    def check_score(self, number_correct, total_questions):

        if (total_questions > 0):
            percent = round(number_correct/total_questions * 100, 2)
            print(f"\nYour score is {number_correct}/{total_questions} for {percent}%")
        else:
            print("Result is 0/0 with no questions asked")

    # def next_question(self):
    #     # iterate through each question in the list
    #     for question_entry in self.question_list:
    #         # get user answer
    #         user_answer = input(f"Q.{self.question_number + 1}: {question_entry.text} (True/False)? ")
            
    #         # increment question number
    #         self.question_number += 1

    # def check_answer(self):
        
        
        