from odoo import api, fields, models


class PurchaseOrderType(models.Model):
    _name = 'purchase.order.type'
    _description = 'Type of purchase order'
    _order = 'sequence'

    @api.model
    def _get_domain_sequence_id(self):
        seq_type = self.env.ref('purchase.seq_purchase_order')
        return [('code', '=', seq_type.code)]

    @api.model
    def _default_sequence_id(self):
        seq_type = self.env.ref('purchase.seq_purchase_order')
        return seq_type.id

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    description = fields.Text(string='Description', translate=True)
    sequence_id = fields.Many2one(
        comodel_name='ir.sequence', string='Entry Sequence', copy=False,
        domain=_get_domain_sequence_id, default=_default_sequence_id,
        required=True)
    payment_term_id = fields.Many2one(
        comodel_name='account.payment.term', string='Payment Terms')
    incoterm_id = fields.Many2one(
        comodel_name='account.incoterms', string='Incoterm')
    sequence = fields.Integer(default=10)
