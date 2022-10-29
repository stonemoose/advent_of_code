import requests

INPUT_URL = 'https://adventofcode.com/{}/day/{}/input'
SUBMIT_URL = 'https://adventofcode.com/{}/day/{}/answer'


def get_input(session, year, day):
    input_url = INPUT_URL.format(year, day)
    html_data = requests.get(input_url, cookies={'Session': session})
    print(html_data.text)


get_input(2021, 4)
