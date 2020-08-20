import json
import sys

import requests


def get_data(url):
    r = requests.get(url)
    data = json.loads(r.text)
    items = data['items']
    return items


def solve(N):
    result = []
    url_api_questions = ('https://api.stackexchange.com/2.2/questions'
                         '?pagesize={}&order=desc&sort=votes'
                         '&site=stackoverflow').format(N)
    data_questions = get_data(url_api_questions)
    for question in data_questions:
        title_quest = question['title']
        id_quest = question['question_id']
        url_api_answers = ('https://api.stackexchange.com/2.2/questions'
                           '/{}/answers?pagesize=1&order=desc&sort=votes'
                           '&site=stackoverflow').format(id_quest)
        data_answers = get_data(url_api_answers)
        id_answer = data_answers[0]['answer_id']
        url_answer = 'https://stackoverflow.com/a/{}'.format(id_answer)
        result.append((title_quest, url_answer))
    return result


if __name__ == '__main__':
    N = sys.argv[1]
    quests_answers = solve(N)
    for quest in quests_answers:
        print('Question Title: ', quest[0])
        print('The Highest Voted Answer: ', quest[1])
