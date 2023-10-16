# -*- coding: utf-8 -*-

from odoo import models, fields, api


class norah_supermarket(models.Model):
    _name = 'fresh_start.fresh_start'
    _description = 'fresh_start.fresh_start'

    header = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    body = fields.Text()
    state = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('approval', "Approval"),

        ], default='draft',)

    @api.model
    def createfromjs(self, values):
        usnew = super(norah_supermarket, self).create(values)
        print('yes is added')
        return usnew

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def approval_b(self):
        self.state='approval'
