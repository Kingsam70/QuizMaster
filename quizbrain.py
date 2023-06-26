import html


class QuizBrain:
    def __init__(self, data):
        self.data = data
        self.length_data = len(self.data["results"])
        self.question_no = 0

        self.question_text = html.unescape(self.data["results"][self.question_no]["question"])
        self.answer = self.data["results"][self.question_no]["correct_answer"]

    def check_answer(self, value):
        if value == self.answer:
            return True

    def next_question(self):
        self.question_no += 1
        self.question_text = html.unescape(self.data["results"][self.question_no]["question"])
        self.answer = self.data["results"][self.question_no]["correct_answer"]
