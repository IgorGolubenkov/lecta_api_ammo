
from lecta_api_ammo.request_test import Authentication_template

request = Authentication_template()

class Authentication_helper:

    def __init__(self, base_url, base_headers):
        self.base_url = base_url
        self.base_headers = base_headers

    def _url(self, path):
        return '%s%s' % (self.base_url, path)

    def req_sessionid(self, login, password):
        ''' метод запроса на получение session ID '''
        aut_sessionId_body = {
            "login": login,
            "password": password
            }
        return request.req_post(self._url('auth/local'), self.base_headers, aut_sessionId_body)

    def req_code(self, headers_X_sessionId):
        ''' метод запроса на получения кода '''
        oauth_code_body = {
            "clientId": 0,
            "credentials": {"id": ["main","accounts","groups"]
                }
            }
        return request.req_post(self._url('oauth/code'), headers_X_sessionId, oauth_code_body)

    def req_oauth_token(self, headers_X_sessionId, ses_code):
        ''' метод зарпос на получение токена, рефрештокена... clientId:0 '''
        oauth_token_body = {
                "clientId": "0",
                "clientSecret": "@Mqb8Xh7m5N5~eW",
                "grantType": "code",
                "code": ses_code,
                "refreshToken": "null"
                }
        return request.req_post(self._url('oauth/token'), headers_X_sessionId, oauth_token_body)

    def req_user_me(self, secured_X_Acces_Token_headers):
        ''' метод запроса на получение информации залогиненного пользователя '''
        return request.req_get(self._url('users/me'), secured_X_Acces_Token_headers)

    def req_user_me_accounts(self, secured_X_Acces_Token_headers):
        ''' метод запроса на получение информации об аккаунтах пользователя '''
        return request.req_get(self._url('users/me/accounts'), secured_X_Acces_Token_headers)

    def req_two_code(self, headers_X_token_accounts):
        ''' Запрос на получение кода после подтверждения авторизация '''
        oauth_two_body = {
            "clientId": "2",
            "credentials": {
                "id": ["main","accounts"],
                "distribution": ["main"],
                "storage": ["mian"],
                "social": ["main"]
                }
            }
        return request.req_post(self._url('oauth/code'), headers_X_token_accounts, oauth_two_body)

    def req_two_token(self, ses_code_two):
        '''метод зарпос на получение токена, рефрештокена... clientId:2 после подтверждения авторизации'''
        oauth_two_token_body = {
                "clientId": "2",
                "clientSecret": "2o1XmaNlHm",
                "grantType": "code",
                "code": ses_code_two,
                "refreshToken": "null"
                    }
        return request.req_post_not_headers(self._url('oauth/token'), oauth_two_token_body)


class Distribution_helper:

    def __init__(self, base_url):
        self.base_url = base_url

    def _url(self, path):
        return '%s%s' % (self.base_url, path)

    def req_leases_value(self, headers_X_token_accounts):
        '''Получение всех лицензий выданных данному пользователю'''
        extension_leases = {
            "extend": "catalog,keys"
            }
        return request.req_get_param(self._url('client/leases'), headers_X_token_accounts, extension_leases)

    def req_unbind_leases(self, leases_id_unbind, key_unbind, headers_X_token_accounts):
        ''' Метод для отвязки устройства '''
        unbind_leases_body = {"keyNumber": key_unbind}
        return request.req_post(self._url('client/leases/%s/unbind') % leases_id_unbind, headers_X_token_accounts, unbind_leases_body)



class Bundles_helper:

    def __init__(self, base_url, secured_headers):
        self.base_url = base_url
        self.secured_headers = secured_headers

    def _url(self, path):
        return '%s%s' % (self.base_url, path)

    def req_get_all_bundles(self):
        return request.req_get(self._url('client/leases'), self.secured_headers)


