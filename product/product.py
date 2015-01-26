# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2014 Andrea Cometa All Rights Reserved.
#                       www.andreacometa.it
#                       openerp@andreacometa.it
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, orm
from tools.translate import _


class product_alternative_code(orm.Model):

    _name = "product.alternative_code"
    _description = "Alternative codes for product"

    _columns = {
        'name': fields.char('Code', size=16, required=True),
        'product_id': fields.many2one('product.product', 'Product'),
        }


class product_product(orm.Model):

    _name = "product.product"
    _inherit = "product.product"

    def name_search(self, cr, user, name, args=None, operator='ilike',
                    context=None, limit=100):
        if name:
            args = args + ['|',
                    ('alternative_code', operator, '%' + name + '%')]
        res = super(product_product, self).name_search(
            cr, user, name, args, operator='ilike', context=None, limit=100)
        return res

    def _alternative_code(self, cr, uid, ids, name, arg, context=None):
        res = {}
        prds = self.browse(cr, uid, ids)
        for prd in prds:
            code = ''
            for line in prd.alternative_code_ids:
                code = '%s %s' % (code, line.name)
            res[prd.id] = code
        return res

    _columns = {
        'alternative_code': fields.function(
            _alternative_code, string="Alternative Code", type='char',
            size=256, store=True),
        'alternative_code_ids': fields.one2many(
            'product.alternative_code', 'product_id', 'Alternative Codes'),
        }
