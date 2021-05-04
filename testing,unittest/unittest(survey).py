import unittest
from survey import AnonymousSurvey


# проверяем ли сохранился ответ с помощью assertIn
# начинат  всегда с Test класс
# setUp - упрощает можно создать один екземляр и не париться


# class TestAnonmySurvey(unittest.TestCase):
# """Пишем тесты для класса AnonymousSurvey"""


# def test_store_single_response(self):
# """Проверяється что один ответ сохранен в  списке"""
# question = 'Какой язык програмированния вам нравится?'
# my_survey = AnonymousSurvey(question)
# my_survey.store_response('Java')

# self.assertIn('Java', my_survey.responses)

# print(my_survey.responses)

# def test_five_responses(self):
# """Проверяет что 5 ответов были сохранены"""
# question = 'Какой язык програмированния вам нравится?'
# my_survey = AnonymousSurvey(question)
# responses1 = ['Java', 'Python', 'C#', 'Go', 'Javascript']
# for response in responses1:
# my_survey.store_response(response)

# for response in responses1:
# self.assertIn(response, my_survey.responses)


# можна и не писать
# if __name__ == '__main__':
# unittest.main()


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = 'Какой язык програмированния вам нравится?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Java', 'Python', 'C#', 'Go', 'Javascript']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[1])
        self.assertIn(self.responses[1], self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()
