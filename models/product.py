# -*- coding: utf-8 -*-
from odoo import api, models, fields


class ProductTemplateManufacturerModel(models.Model):
    _inherit = "product.template"
       
    product_manufacturer = fields.Many2one("product.manufacturer", 'Manufacturer')
    product_model = fields.Many2one("product.model", 'Model')

