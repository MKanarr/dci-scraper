import requests
import csv
import time
import threading
from bs4 import BeautifulSoup

start = time.perf_counter()

def Corps(corpsList, soup):
    for corps in soup.find_all('div', class_='sticky-corps'):
        for ul in corps.find_all('li'):
            corpsList.append(ul.text)

    return corpsList

def SubCaptions(rawScores, soup):
    for line in soup.find_all('div', class_='column-total'):
        for total_score in line.find_all('div', class_='line'):
            if total_score.div.span is not None:
                if total_score.div.span.text != '---':
                    rawScores.append(float(total_score.div.span.text))

    return rawScores

def CreateCSV(filename, corpsList, generalEffect, visual, music, finalTotal):
    fields = ['corps', 'general_effect', 'visual', 'music', 'total']
    rows = []

    for i in range(len(corpsList)):
        row_data = [corpsList[i], generalEffect[i], visual[i], music[i], finalTotal[i]]
        rows.append(row_data) 

    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    corpsList = []
    rawScores = []

    # corps names
    corpsList = Corps(corpsList, soup)

    # subcaption scores
    rawScores = SubCaptions(rawScores, soup)

    subTotal = rawScores[3::5]
    finalTotal = rawScores[4::5]
    generalEffect = rawScores[0::5]
    visual = rawScores[1::5]
    music = rawScores[2::5]

    corpsList.reverse()
    subTotal.reverse()
    finalTotal.reverse()
    generalEffect.reverse()
    visual.reverse()
    music.reverse()

    filename = url.split('/')[-1] + '.csv'

    CreateCSV(filename, corpsList, generalEffect, visual, music, finalTotal)

urls = ['https://www.dci.org/scores/recap/2019-dci-world-championship-finals', 'https://www.dci.org/scores/recap/2018-dci-world-championship-finals',
        'https://www.dci.org/scores/recap/2017-dci-world-championship-finals', 'https://www.dci.org/scores/recap/2016-dci-world-championships-finals',
        'https://www.dci.org/scores/recap/2015-dci-world-championship-world-class-finals', 'https://www.dci.org/scores/recap/2014-dci-world-championships-world-class-finals',
        'https://www.dci.org/scores/recap/2013-dci-world-championship-finals'
        ]

threads = []

# for url in urls:
#     scrape(url)

for url in urls:
    t = threading.Thread(target=scrape, args=[url])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')