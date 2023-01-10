from odoo import http
from odoo.http import request
import json

class List_Car_Controller(http.Controller):


    def get_third_largest_num(self, num_list):
        # num = [2, 3, 7, 4, 5, 6, 10, 11, 120]
        num = num_list

        # 2
        largest_num = num[0]
        second_largest_num = num[0]
        third_largest_num = num[0]

        # 3
        for i in num:
            # 4
            if i > largest_num:
                third_largest_num = second_largest_num
                second_largest_num = largest_num
                largest_num = i
            # 5
            elif i > second_largest_num:
                third_largest_num = second_largest_num
                second_largest_num = i
            # 6
            elif i > third_largest_num:
                third_largest_num = i

        # 7
        return third_largest_num
    @http.route('/cars', auth='public', type='http')
    def list_car(self):
        cars = request.env['car.car'].search([])                 #cars = request.env['car.car'].sudo().search([]) - need understanding sudo

        num_list = [i.horse_power for i in cars]
        max3horse = self.get_third_largest_num(num_list)

        car_list = dict()
        car_set = set()

        for car in cars:
            if car.horse_power < max3horse or car.horse_power in car_set:
                continue

            car_set.add(car.horse_power)

            car_list.update({
                f'name_{car.id}': car.name,
                f'horse_power_{car.id}': car.horse_power,
                f'door_number_{car.id}': car.door_number,         # f'driver_id_{car.id}': car.driver_id, # f'parking_id_{car.id}': car.parking_id, # f'feature_ids_{car.id}': car.feature_ids,
                f'total_speed_{car.id}': car.total_speed,
                f'status_{car.id}': car.status,
            })

        return json.dumps(car_list)

