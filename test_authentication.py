
from lecta_api_ammo.test_lecta import *

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-us,en;q=0.8",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "_gat=1; _ga=GA1.2.1994786266.1453794507",
}

auth = Authentication_helper('https://id.demo.cognita.ru/api/', headers)

login = "golubenkov_test@mail.ru"
password = "igor-igor"


resp_aut = auth.req_sessionid(login, password)

if resp_aut.status_code != 200:
    raise ConnectionError('Status error ( getting sesssionId ) : %s' % resp_aut.status_code, 'Response : %s' % resp_aut.json())
print('Received sessionId: %s' % resp_aut.json()['sessionId'])


# getting sessionId
ses_id = resp_aut.json()['sessionId']


headers.update({"X-Session-Id": ses_id})


resp_oauth = auth.req_code(headers)

if resp_oauth.status_code != 200:
    raise ConnectionError('Status error ( getting code ) : %s' % resp_oauth.status_code, 'Response : %s' % resp_oauth.json())
print('Received code: %s' % resp_oauth.json()['code'])


# getting code
ses_code = resp_oauth.json()['code']


resp_oauth_token = auth.req_oauth_token(headers, ses_code)

if resp_oauth_token.status_code != 200:
    raise ConnectionError('Status error ( getting token ) : %s' % resp_oauth.status_code, 'Response : %s' % resp_oauth_token.json())
print('Received oauth token: %s' % resp_oauth_token.json()["token"])


# getting & print token
ses_token = resp_oauth_token.json()["token"]
print("\nToken", ses_token)
# getting & print refreshToken
ses_refreshToken = resp_oauth_token.json()['refreshToken']
print("refreshToken", ses_refreshToken)
# getting & print refreshTokenExpirationDate
ses_refreshTokenExpirationDate = resp_oauth_token.json()['refreshTokenExpirationDate']
print("refreshTokenExpirationDate\n", ses_refreshTokenExpirationDate)


headers.update({"X-Access-Token": ses_token})


resp_user_me = auth.req_user_me(headers)
if resp_user_me.status_code != 200:
    raise ConnectionError('Status error ( getting information about the logged in user ) : %s' % resp_user_me.status_code, 'Response : %s' % resp_user_me.json())
print('Received information about the logged in user: %s' % resp_user_me.json())


resp_user_me_accounts = auth.req_user_me_accounts(headers)
if resp_user_me_accounts.status_code != 200:
    raise ConnectionError('Status error ( getting detailed information about the user accounts ) : %s' % resp_user_me_accounts.status_code, 'Response : %s' % resp_user_me_accounts.json())
print('Received detailed information about the user accounts: %s' % resp_user_me_accounts.json())


# getting & print "X-Account"
preparation_x_account = resp_user_me_accounts.json()[0]
x_account = preparation_x_account['id']
print("\nX-account\n", x_account)


headers.update({"X-Account": x_account})
print(headers)


