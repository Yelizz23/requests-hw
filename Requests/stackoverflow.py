from datetime import datetime
import requests
import time

time.sleep(5)


def get_questions(tags, past_days):
    url = 'https://api.stackexchange.com/2.3/questions'
    current_date = int(time.time())
    from_date = current_date - past_days * 24 * 60 * 60
    page = 1
    counter = 0

    for i in range(1, 26):
        params = {'fromdate': from_date,
                  'todate': current_date,
                  'order': 'desc',
                  'sort': 'creation',
                  'tagged': tags,
                  'page': page,
                  'pagesize': 60,
                  'site': 'stackoverflow'
                  }
        result = requests.get(url, params=params).json()
        if result['items']:
            for item in result['items']:
                counter += 1
                print(f'Вопрос номер: {counter}; {datetime.utcfromtimestamp(item["creation_date"])}')
                print(item['tags'])
                print(item['title'])
                print(item['link'])
                print()
        else:
            print(f'Некорректный запрос!')

    page += 1


get_questions(tags='python', past_days=2)
