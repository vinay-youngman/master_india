from odoo import models,_

import logging, requests
import json

_logger = logging.getLogger(__name__)


class YmMasterIndia(models.TransientModel):
    _name = 'ym.master.india'
    _description = 'Use Master India Api to fetch distance'

    def get_master_india_access_token(self):
        url = "https://pro.mastersindia.co/oauth/access_token"
        payload = json.dumps({
            "username": self.env['ir.config_parameter'].sudo().get_param('ym_master_india.api_username'),
            "password": self.env['ir.config_parameter'].sudo().get_param('ym_master_india.api_password'),
            "client_id": self.env['ir.config_parameter'].sudo().get_param('ym_master_india.client_id'),
            "client_secret": self.env['ir.config_parameter'].sudo().get_param('ym_master_india.client_secret'),
            "grant_type": "password"
        })
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()['access_token']

    def get_distance(self, from_pincode, to_pincode):
        if not (from_pincode and to_pincode) or from_pincode == '' or to_pincode == '':
            return False

        cast_to_int = lambda string: int(string) if string.strip() else False

        from_pincode = cast_to_int(str(from_pincode))
        to_pincode = cast_to_int(str(to_pincode))

        access_token = self.get_master_india_access_token()
        url = f"https://pro.mastersindia.co/distance?access_token={access_token}&fromPincode={from_pincode}&toPincode={to_pincode}"
        response = requests.request("GET", url)
        data = response.json()

        if data['results']['code'] == 200:
            return data['results']['distance']
        else:
            raise Exception("Could not fetch distance: " + data['results']['message'])
