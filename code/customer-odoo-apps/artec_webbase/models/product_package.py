from odoo import models, fields, api

class ProductPackage(models.Model):
    _name = 'artec.product.package'
    _description = 'Artec Product Package'

    name = fields.Char(
        required=True, 
    )
    image = fields.Image()

    categ_ids = fields.Many2many(
        comodel_name='product.public.category',
        string='Category'
    )