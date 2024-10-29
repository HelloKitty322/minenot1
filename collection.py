import csv

RACES = ['империя', 'альянс', 'доминион', 'орда', 'союз', 'легион', 'белатто']
CLASSES = {'чародеи': 'debaff', 'тяжелые воины': 'hdd', 'легкие воины': 'ldd', 'маги': 'mage',
           'мастера войны': 'master_war', 'рыцари': 'shield', 'убийцы': 'assassin', 'стрелки': 'bow', 'лекари': 'medic',
           'менталисты': 'mental'}

with open('professions.csv', 'r', encoding='UTF-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    jobs_data = list(reader)
    all_professions = [i['Название профессии'].lower() for i in jobs_data]

with open('pics.csv', 'r', encoding='UTF-8') as file:
    reader = csv.DictReader(file)
    pics_list = {}
    for i in reader:
        pics_list.setdefault(i['Название профессии'], i['Ссылка на картинку'])

