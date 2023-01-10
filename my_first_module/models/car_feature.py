from odoo import fields, models


class CarFeature(models.Model):
    _name = 'car.feature'
    _description = 'Car Feature'

    name = fields.Char(string='Name', required=True)
