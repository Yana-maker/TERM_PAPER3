import json
from src.utils import load_data, executed_operations, five_last_sorted_operations, output_data

def test_load_data():
    transations = load_data()
    assert isinstance(transations, list)
    assert len(transations) > 0

def test_executed_operations(item):
    assert executed_operations(item) == [{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }]

def test_five_last_sorted_operations(item):
    sorted_operations = five_last_sorted_operations(item)
    dates = [elen['date'] for elen in sorted_operations]
    assert dates == ['2019-08-26T10:50:58.294041',
 '2019-07-03T18:35:29.512364',
 '2018-06-30T02:08:58.425572',
 '2018-03-23T10:45:06.972075']






def test_output_data(item):
    assert output_data(item) == ['26.08.2019 Перевод организации\n'
 'Maestro 1596 83** **** 5199 -> Счет **9589\n'
 '31957.58 руб.',
 '03.07.2019 Перевод организации\n'
 'MasterCard 7158 30** **** 6758 -> Счет **5560\n'
 '8221.37 USD',
 '30.06.2018 Перевод организации\n'
 'Счет 7510 68** **** 6952 -> Счет **6702\n'
 '9824.07 USD',
 '23.03.2018 Открытие вклада\nСчет **2431\n48223.05 руб.']
