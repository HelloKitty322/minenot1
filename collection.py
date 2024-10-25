import csv

RACES = ['империя', 'альянс', 'доминион', 'орда', 'союз', 'легион', 'белатто']
CLASSES = {'чародеи': 'debaff', 'тяжелые воины': 'hdd', 'легкие воины': 'ldd', 'маги': 'mage',
           'мастера войны': 'master_war', 'рыцари': 'shield', 'убийцы': 'assassin', 'стрелки': 'bow', 'лекари': 'medic',
           'менталисты': 'mental'}

with open('professions.csv', 'r', encoding='UTF-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    file_list = list(reader)
    all_professions = list(map(lambda x: x['Название профессии'].lower(), file_list))

with open('pics.csv', 'r', encoding='UTF-8') as file:
    reader = csv.DictReader(file)
    pics_list = list(reader)
