from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    product_ids  = fields.Many2many(
        comodel_name='product.template'
    )