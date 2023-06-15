import json
import datetime


def load_data():
    '''распаковка файла json'''
    with open('../src/operations.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        return data



def executed_operations(data):
    ''' добавление в список только выполненные операции'''
    transactions = []
    for i in data:
        if i.get("state") == "EXECUTED":
            transactions.append(i)

    return transactions


def five_last_sorted_operations(data):
    ''' сортировка операций по дате'''

    sorted_operations = sorted(data, key=lambda x: x['date'], reverse=True)
    five_last_operations = sorted_operations[:5]
    return five_last_operations


def output_data(data):
    '''вывод 5 посл операций в соот-ии с заданием'''
    result = []
    for i in data:
        data = datetime.datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        desc = i['description']
        amount = i['operationAmount']['amount']
        currency = i['operationAmount']['currency']['name']


        to_ = i['to'].split()
        to_number = to_.pop()
        to_mask = f'**{to_number[-4:]}'
        to_type = ' '.join(to_)

        if "from" in i:
            from_ = i['from'].split()
            from_number = from_.pop()
            from_mask = f'{from_number[:4]} {from_number[4:6]}** **** {from_number[-4:]}'
            from_type = ' '.join(from_)

            result.append(f'{data} {desc}\n{from_type} {from_mask} -> {to_type} {to_mask}\n{amount} {currency}')
        else:
            result.append(f'{data} {desc}\n{to_type} {to_mask}\n{amount} {currency}')
    return result















