from flask import jsonify

from exceptions.ATM.main import InvalidWithdraw


def get_available_ballots_value():
    return [100, 50, 20, 10, 5, 2]


def serialize_data(response):
    notas = get_available_ballots_value()
    for nota in notas:
        if nota not in response:
            response.update({nota: 0})
    return jsonify(response)


def get_ballots_number(value, response=None):
    response = {} if response is None else response
    closest_ballot = get_closest_ballot_value(value)
    number_of_notes = value // closest_ballot
    response.update({closest_ballot: number_of_notes})
    if value == closest_ballot or value == 0:
        return serialize_data(response)
    if value < closest_ballot:
        raise InvalidWithdraw()
    return get_ballots_number(value - (number_of_notes * closest_ballot), response)


def get_closest_ballot_value(value):
    notas = get_available_ballots_value()
    for index, nota in enumerate(notas):
        if nota < value:
            return notas[index if index > 0 else 0]
    return notas[-1]
