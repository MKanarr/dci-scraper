import requests
import csv
from bs4 import BeautifulSoup
from threading import Thread

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

def Finals2019():
    page = requests.get('https://www.dci.org/scores/recap/2019-dci-world-championship-finals')
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

    CreateCSV('2019finals.csv', corpsList, generalEffect, visual, music, finalTotal)

def Finals2018():
    page = requests.get('https://www.dci.org/scores/recap/2018-dci-world-championship-finals')
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

    CreateCSV('2018finals.csv', corpsList, generalEffect, visual, music, finalTotal)

def Finals2017():
    page = requests.get('https://www.dci.org/scores/recap/2017-dci-world-championship-finals')
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

    CreateCSV('2017finals.csv', corpsList, generalEffect, visual, music, finalTotal)

def Finals2016():
    page = requests.get('https://www.dci.org/scores/recap/2016-dci-world-championships-finals')
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

    CreateCSV('2016finals.csv', corpsList, generalEffect, visual, music, finalTotal)

def Finals2015():
    page = requests.get('https://www.dci.org/scores/recap/2015-dci-world-championship-world-class-finals')
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

    CreateCSV('2015finals.csv', corpsList, generalEffect, visual, music, finalTotal)

def Finals2014():
    page = requests.get('https://www.dci.org/scores/recap/2014-dci-world-championships-world-class-finals')
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

    CreateCSV('2014finals.csv', corpsList, generalEffect, visual, music, finalTotal)

def Finals2013():
    page = requests.get('https://www.dci.org/scores/recap/2013-dci-world-championship-finals')
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

    CreateCSV('2013finals.csv', corpsList, generalEffect, visual, music, finalTotal)

Thread(target=Finals2013).start()
Thread(target=Finals2014).start()
Thread(target=Finals2015).start()
Thread(target=Finals2016).start()
Thread(target=Finals2017).start()
Thread(target=Finals2018).start()
Thread(target=Finals2019).start()