from odoo import models, api

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    @api.model
    def create(self, vals):
        if vals.get('payment_type') == 'inbound':
            vals['name'] = self.env['ir.sequence'].next_by_code('account.payment.customer') or '/'
        elif vals.get('payment_type') == 'outbound':
            vals['name'] = self.env['ir.sequence'].next_by_code('account.payment.vendor') or '/'
        return super(AccountPayment, self).create(vals)
