# -*- coding: utf-8 -*-


from odoo import api, models, fields

class ProductTemplateManufacturer(models.Model):
    _inherit = "product.template"
       
    product_manufacturer = fields.Char('Manufacturer')


class ProductTemplateModel(models.Model):
    _inherit = "product.template"
   
    product_model = fields.Char('Model')
