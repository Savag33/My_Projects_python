
from survey import AnonymousSurvey



question = 'Какой язык проаграмирования вам нравится?'

my_survey = AnonymousSurvey(question)

my_survey.show_question()
print('\nНажмите "q" для вихода с опроса. ')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

print('\nСпасибо за ответ!')

my_survey.show_results()




