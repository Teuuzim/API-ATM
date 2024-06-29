from flask import Flask, request, jsonify, Response

from exceptions.ATM.main import InvalidWithdraw
from services.ATM.main import get_ballots_number

app = Flask(__name__)


# allow both GET and POST requests
class SaqueInputValidator:

    def validate(self, value):
        if not value:
            raise ValueError("Value cannot be empty")
        if type(value) is not int:
            raise ValueError("Value must be an integer")
        if value < 0:
            raise ValueError("Value cannot be negative")


@app.route('/api/saque', methods=['POST'])
def saque():
    try:
        body = request.json['valor']
        SaqueInputValidator().validate(body)
        response = get_ballots_number(body)
        return response
    except InvalidWithdraw:
        return Response(status=400, response='Saque Inválido')
    except Exception as e:
        response = Response(status=400,
                     response='Ocorreu um erro durante o saque. Por favor tente outro valor. Erro: ' + str(e))
        print(response.data)
        return response

if __name__ == '__main__':
    app.run()
