import requests
import allure
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class ApiClient:

    def __init__(self, host):
        self.host = f'https://{host}/'

    def getHeaders(self, headers={}):
        url = self.host + 'headers'
        logger.info(f'Выполнение запроса: GET {url}')
        response = requests.get(url, headers=headers)
        logger.info(f'Ответ получен: {response.status_code}')
        logger.debug(f'Ответ: {response.text}')
        return response

    def getStatus(self, code):
        url = self.host + 'status/' + str(code)
        logger.info(f'Выполнение запроса: GET {url}')
        response = requests.get(url)
        logger.info(f'Ответ получен: {response.status_code}')
        logger.debug(f'Ответ: {response.text}')
        return response

    def putStatus(self, code):
        url = self.host + 'status/' + str(code)
        logger.info(f'Выполнение запроса: PUT {url}')
        response = requests.put(url)
        logger.info(f'Ответ получен: {response.status_code}')
        logger.debug(f'Ответ: {response.text}')
        return response

    def postStatus(self, code):
        url = self.host + 'status/' + str(code)
        logger.info(f'Выполнение запроса: POST {url}')
        response = requests.post(url)
        logger.info(f'Ответ получен: {response.status_code}')
        logger.debug(f'Ответ: {response.text}')
        return response

    def patchStatus(self, code):
        url = self.host + 'status/' + str(code)
        logger.info(f'Выполнение запроса: PATCH {url}')
        response = requests.patch(url)
        logger.info(f'Ответ получен: {response.status_code}')
        logger.debug(f'Ответ: {response.text}')
        return response

    def deleteStatus(self, code):
        url = self.host + 'status/' + str(code)
        logger.info(f'Выполнение запроса: DELETE {url}')
        response = requests.delete(url)
        logger.info(f'Ответ получен: {response.status_code}')
        logger.debug(f'Ответ: {response.text}')
        return response

    def getRedirects(self, redirectTimes=1, allowRedirects=True):
        url = self.host + 'redirect/' + str(redirectTimes)
        logger.info(f'Выполнение запроса: GET {url} Редиректы {"разрешены" if allowRedirects else "запрещены"}')
        response = requests.get(url, allow_redirects=allowRedirects)
        logger.info(f'Ответ получен: {response.status_code}')
        logger.debug(f'Ответ: {response.text}')
        return response




