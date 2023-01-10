from io import BytesIO

from odoo import api, models, fields
import xlsxwriter,base64

from odoo.http import request
import json

class CarReportWizard(models.TransientModel):
    _name = "car.report.wizard"

    horse_power_update_test = fields.Integer(string="Horse Power Max", required=True)

    def export_report_test(self):
        # print("Yeah, successfully!")
        # self.env['car.car'].browse(self._context.get("active_ids").update({'horse_power': self.horse_power_update_test}))

        file_data = BytesIO()
        workbook = xlsxwriter.Workbook(file_data)
        # for rec in self:
        #     # horse_power = rec.month_filter
        #     # year = rec.year_filter
        #     # [('month', '=', rec.month_filter), ('year', '=', rec.year_filter)])
        #     cost_lines = rec.env['car.car'].search([('horse_power', '<=', self.horse_power_update_test)])

        car_list = request.env['car.car'].search([('horse_power', '<=', self.horse_power_update_test)])

        for car in car_list:
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

        print(car_list)

        return True
    #         data_line = []
    #         range_cost = len(cost_lines.ids) + 1
    #         for data, rang in zip(cost_lines, range(1, range_cost)):
    #             line = {}
    #             line.update({
    #                 'stt': str(rang),
    #                 'name': data.hr_employee_id.name,
    #                 'email': data.work_email,
    #                 'cost': data.labor_costs
    #             })
    #             [{a: 1}, {b: 2}]
    #             data_line.append(line)
    #         style_title = rec.add_color_excel(workbook, '#ffffff', 17, 'center')
    #         style_header = rec.add_color_excel(workbook, '#2b7ac4', 12, 'center')
    #         style_content = rec.add_color_excel(workbook, '#ffffff', 12, 'center')
    #         style_content_left = rec.add_color_excel(workbook, '#ffffff', 12, 'left')
    #         style_content_right = rec.add_color_excel(workbook, '#ffffff', 12, 'right')
    #         list_style = [style_content, style_content_left, style_content_left, style_content_right]
    #         worksheet = workbook.add_worksheet('Chi phí nhân công T{}_{}'.format(month, year))
    #         worksheet.set_row(0, 20)
    #         worksheet.set_row(1, 20)
    #         worksheet.merge_range(f"A1:D3", 'Chi phí nhân công T{}/{} '.format(month, year), style_title)
    #         worksheet.write('A4', 'STT', style_header)
    #         worksheet.write('B4', 'Tên', style_header)
    #         worksheet.write('C4', 'Email', style_header)
    #         worksheet.write('D4', 'Chi phí nhân công', style_header)
    #         row = 5
    #         for data in data_line:
    #             col = 0
    #             for rec, style in zip(data, list_style):
    #                 worksheet.write(f"{chr(65 + col)}{row}", data[rec], style)
    #                 col += 1
    #             row += 1
    #         worksheet.set_column('B:D', 30)
    #         worksheet.set_column('A:A', 10)
    #         workbook.close()
    #         report_data = base64.encodebytes(file_data.getvalue())
    #         attachment_id = self.env['ir.attachment'].create({
    #             'name': 'Chi phí nhân công T%s/%s.xlsx' % (month, year),
    #             'datas': report_data,
    #             'type': 'binary',
    #         })
    #
    #         return {
    #             'type': 'ir.actions.act_url',
    #             'url': '/web/content/' + str(attachment_id.id) + '?download=true',
    #             'target': 'new',
    #         }
    #
    # def add_color_excel(self, workbook, color, size, align):
    #     return workbook.add_format({
    #         'font_size': size,
    #         'border': 1,
    #         'font_color': 'black',
    #         'align': align,
    #         'valign': 'vcenter',
    #         'fg_color': color,
    #         'num_format': '#,##0.00',
    #     })
        # return True