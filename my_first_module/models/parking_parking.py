from odoo import fields, models


class Parking_Parking(models.Model):
    _name = 'parking.parking'
    _description = 'Parking Parking'

    name = fields.Char(string='Name', required=True)
    car_ids = fields.One2many('car.car', 'parking_id', string='Car')
