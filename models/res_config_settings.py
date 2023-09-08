# -*- coding: utf-8 -*-

from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    api_username = fields.Char(string='User Name', config_parameter='ym_master_india.api_username')
    api_password = fields.Char(string='Password', config_parameter='ym_master_india.api_password')
    client_id = fields.Char(string='client_id', config_parameter='ym_master_india.client_id')
    client_secret = fields.Char(string='Client Secret', config_parameter='ym_master_india.client_secret')
    grant_type = fields.Char(string='Grant Type', config_parameter='ym_master_india.grant_type')
