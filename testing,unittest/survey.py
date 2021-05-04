

class AnonymousSurvey():
    """Сбор анонимных ответов на опросы"""

    def __init__(self, question):

        self.question = question
        self.responses = []

    def show_question(self):
        """Виводит опрос"""

        print(self.question)


    def store_response(self, new_response):
        """Сохранения одного ответа"""

        self.responses.append(new_response)

    def show_results(self):
        """Вивод получениых оветов"""
        print('\nОтветы на опросы: ' )

        for response in self.responses:
            print("- " + response)


