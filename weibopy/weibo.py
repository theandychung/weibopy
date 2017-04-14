# encoding:utf-8
import requests

from .exceptions import WeiboAPIError


class WeiboClient(object):
    """
    weibo client base 
    """
    base = "https://api.weibo.com/2/"

    def __init__(self, access_token):
        """
        """
        self.access_token = access_token
        self.session = requests.Session()

    def request(self, method, suffix, params, data=None):
        """
        request weibo api 
        :param suffix: str,
        :param method: str,http method: GET,POST,PUT.etc
        :param params: dict, url query parameters 
        :param data: dict, 
        :return: 
        """
        url = self.base + suffix
        params["access_token"] = self.access_token

        response = self.session.request(method=method, url=url, params=params, data=data)
        json_obj = response.json()
        if json_obj.get("error_code"):
            raise WeiboAPIError(data["error_code"], data["error"])
        else:
            return json_obj
