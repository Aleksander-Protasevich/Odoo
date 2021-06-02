# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields

class ProductManufacturer(models.Model):
    # _inherit = "product.template"
    _name = "product.manufacturer"
    _description = "Product Manufacturer"
    _rec_name = 'manufacturer'
    _order = 'manufacturer'

    manufacturer = fields.Char('Manufacturer', index=True, required=True)


class ProductModel(models.Model):
    _name = "product.model"
    _description = "Product Model"
    _parent_name = "parent_id"
    _rec_name = 'model'
    _order = 'model'

    model = fields.Char('Model', index=True, required=True)
    parent_id = fields.Many2one('product.manufacturer', 'Product Manufacturer', index=True, ondelete='cascade')
