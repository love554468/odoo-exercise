from odoo import http
from odoo.http import request
import json

class List_Car_Controller(http.Controller):

    @http.route('/cars', auth='public', type='http')
    def list_car(self):
        # return "Hello"
        cars = request.env['car.car'].sudo().search([])

        car_list = dict()

        # i, third_prize_horsepower = 0, -1
        # one_two_horsepower = dict()

        # while i == 3:
        #     for c in cars:
        #         if c.horse_power > third_prize_horsepower:
        #             third_prize_horsepower = c.horse_power

        for car in cars:
            car_list.update({
                f'name_{car.id}': car.name,
                f'horse_power_{car.id}': car.horse_power,
                f'door_number_{car.id}': car.door_number,
                # f'driver_id_{car.id}': car.driver_id,
                # f'parking_id_{car.id}': car.parking_id,
                # f'feature_ids_{car.id}': car.feature_ids,
                f'total_speed_{car.id}': car.total_speed,
                f'status_{car.id}': car.status,
            })

        return json.dumps(car_list)

