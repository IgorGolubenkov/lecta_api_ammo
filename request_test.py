

import requests

requests.packages.urllib3.disable_warnings()

class Authentication_template:

    def req_get(self, url_lead, headers_lead):
        return requests.get(url=url_lead, headers=headers_lead, verify=False)

    def req_get_param(self, url_lead, headers_lead, params_lead):
        return requests.get(url=url_lead, headers=headers_lead, params=params_lead, verify=False)

    def req_post(self, url_lead, headers_lead, body_req):
        return requests.post(url=url_lead, headers=headers_lead,  json=body_req, verify=False)

    def req_post_not_headers(self, url_lead, body_req):
        return requests.post(url=url_lead, json=body_req, verify=False)
