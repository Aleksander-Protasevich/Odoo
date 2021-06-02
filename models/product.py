# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields

class ProductTemplateManufacturer(models.Model):
    _inherit = "product.template"
   
    product_manufacturer = fields.Reference('product_manufacturer.manufacturer')


