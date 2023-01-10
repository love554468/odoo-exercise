from odoo import api, fields, models


class HrEmployeePrivate(models.Model):
    _inherit = "hr.employee"

    pincode = fields.Char(string='Pincode')
    password = fields.Char(string='Password')