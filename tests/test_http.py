import pytest
import allure
import json
from utils.checks import CheckStatusCode, CheckHeaders
from api.api_client import ApiClient

checkHeaders = CheckHeaders()
checkStatusCode = CheckStatusCode()

apiClient = ApiClient(host='httpbin.org')


@pytest.mark.parametrize('header', [{'Testheader': 'some value'}], ids=['Testheader:someValue'])
@allure.title('Проверка метода headers')
def test_headers(header):
    with allure.step('Выполняем запрос headers'):
        response = apiClient.getHeaders(headers=header)

    checkStatusCode.isSuccess(response=response)

    with allure.step('Проверяем наличие заголовка в ответе'):
        checkHeaders.checkHeaderIn(header=header, response=response)


@pytest.mark.parametrize('code, method, check', [
    (200, apiClient.getStatus, checkStatusCode.isSuccess),
    (202, apiClient.putStatus, checkStatusCode.isAccepted),
    (204, apiClient.postStatus, checkStatusCode.isNoContent),
    (400, apiClient.patchStatus, checkStatusCode.isClientError),
    (500, apiClient.deleteStatus, checkStatusCode.isServerError)
], ids=['200 get',
        '202 put',
        '204 post',
        '400 patch',
        '500 delete'])
@allure.title('Проверка метода status')
def test_statusCode(code, method, check):
    with allure.step(f'Выполняем запрос status/{code}'):
        response = method(code)  

    check(response)


@pytest.mark.parametrize('redirectTimes, allowRedirects, check', [
    (2, False, checkStatusCode.isRedirect),
    (3, True, checkStatusCode.isSuccess)
], ids=['Redirect allowed',
        'Redirect not allowed'])
@allure.title('Проверка метода redirects/n')
def test_redirects(redirectTimes, allowRedirects, check):
    with allure.step(f'Выполняем запрос redirects/{redirectTimes} Редиректы разрешены: {allowRedirects}'):
        response = apiClient.getRedirects(redirectTimes=redirectTimes, allowRedirects=allowRedirects)
    check(response)
