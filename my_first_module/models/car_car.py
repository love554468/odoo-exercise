from odoo import fields, models, api, _


class Car_Car(models.Model):
    _name = 'car.car'
    _description = 'Car Car'

    name = fields.Char(string='Name', required=True)
    horse_power = fields.Integer(string='Horse Power')
    door_number = fields.Integer(string='Door Number')
    driver_id = fields.Many2one('res.partner', string='Driver')
    parking_id = fields.Many2one('parking.parking', string='Parking', ondelete="cascade")
    feature_ids = fields.Many2many('car.feature', string='Feature')
    total_speed = fields.Integer(string='Total Speed', compute="_compute_total_speed")
    status = fields.Selection(
        string='Status'
        , selection=[('new', 'New'), ('used', 'Used'), ('sold', 'Sold')]
        , default='new'
    )

    car_sequence = fields.Char(string='Car ID', required=True, readonly=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals_list):
        # self.car_sequence = 'New'
        # try:
        #     if vals_list.get('car_sequence', _('New')) == _('New'):
        #         vals_list['car_sequence'] = self.env['ir.sequence'].next_by_code('car.car.sequence') or _('New')
        # except Exception:
        #     print('123')
        if vals_list.get('car_sequence', _('New')) == _('New'):
            vals_list['car_sequence'] = self.env['ir.sequence'].next_by_code('car.car.sequence') or _('New')
        res = super(Car_Car, self).create(vals_list)
        return res


    @api.depends('horse_power')
    def _compute_total_speed(self):
        for record in self:
            record.total_speed = record.horse_power * 5
    # test