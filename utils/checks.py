import allure
import json


class CheckStatusCode:
    def isSuccess(self, response):
        allure.step('Проверяем http code ответа')
        with allure.step('http code ответа 200'):
            allure.attach(f'Код ответа {response.status_code}')
            assert response.status_code == 200
        return

    def isAccepted(self, response):
        allure.step('Проверяем http code ответа')
        with allure.step('http code ответа 202'):
            allure.attach(f'Код ответа {response.status_code}')
            assert response.status_code == 202
        return
    def isNoContent(self, response):
        allure.step('Проверяем http code ответа')
        with allure.step('http code ответа 204'):
            allure.attach(f'Код ответа {response.status_code}')
            assert response.status_code == 204
        return

    def isRedirect(self, response):
        allure.step('Проверяем http code ответа')
        with allure.step('http code ответа 302'):
            allure.attach(f'Код ответа {response.status_code}')
            assert response.status_code == 302
        return

    def isClientError(self, response):
        allure.step('Проверяем http code ответа')
        with allure.step('http code ответа 400'):
            allure.attach(f'Код ответа {response.status_code}')
            assert response.status_code == 400
        return

    def isServerError(self, response):
        allure.step('Проверяем http code ответа')
        with allure.step('http code ответа 500'):
            allure.attach(f'Код ответа {response.status_code}')
            assert response.status_code == 500
        return

class CheckHeaders:
    def checkHeaderIn(self, header, response):
        key, value = header.popitem()
        responseJson = json.loads(response.text)     
        with allure.step('Проверяем наличие header в ответе'):
            allure.attach(f'header: {header} ')
            allure.attach(f'Ответ: {responseJson}')
            # Заголовок есть в ответе
            assert key in responseJson['headers']            
            # Значение заголовока верное
            assert value == responseJson['headers'][key]
        return            
