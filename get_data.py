from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import json
import time

global json_data
json_data = []


def save_question(q, a):
    question = q[0][3:].strip()
    options = []

    for i in q[1:]:
        i = i.replace("\n", '')
        options.append(i)

    query = {
        "question": question,
        "options": options,
        "answer": a.split(':')[1].strip(),
    }

    json_data.append(query)


def parse(data, ans):
    question = data.split('<br>')
    answer = ans.split('<br>')[0]
    if len(question) > 1:
        question.pop()
        save_question(question, answer)


options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(
    executable_path='./driver/chromedriver', options=options)

links = [
    'https://www.sanfoundry.com/rdbms-questions-answers-views-transactions/',
    'https://www.sanfoundry.com/database-mcqs-query-processing/',
    'https://www.sanfoundry.com/database-mcqs-physical-storage-media/',
    'https://www.sanfoundry.com/database-mcqs-transactions/',
    'https://www.sanfoundry.com/database-mcqs-triggers/',
    'https://www.sanfoundry.com/rdbms-questions-answers-dynamic-hashing/',
    'https://www.sanfoundry.com/rdbms-questions-answers-static-hashing/',
    'https://www.sanfoundry.com/database-mcqs-ordered-indices/',
    'https://www.sanfoundry.com/database-mcqs-index-definition/'

]

for link in links:
    driver.get(link)
    time.sleep(10)
    data = driver.find_element_by_css_selector(
        'div.entry-content').find_elements_by_tag_name('p')
    ans = driver.find_element_by_css_selector(
        'div.entry-content').find_elements_by_css_selector('div.collapseomatic_content ')

    for i, j in zip(data, ans):
        parse(i.get_attribute('innerHTML'), j.get_attribute('innerHTML'))

with open('./data/data.json', 'w') as outfile:
    json.dump(json_data, outfile)
