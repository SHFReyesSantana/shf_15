from odoo import models, fields, api
from odoo.exceptions import UserError
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    def preview_sale_angular(self):
        self.ensure_one()
        self.rename_sequence_shf()
        #return
        url = 'preview_sale_angular/'+str(self.id)
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': url ,
        }

    def rename_sequence_shf(self):
        parent_lines = []

        lines = self.env['sale.order.line'].search([('order_id','=',self.id)],order='sequence asc , id desc ')
        #lines = self.order_line
        for l in lines:
            if not l.parent_section_id:
                parent_lines.append(l)

        #raise UserError(str(parent_lines))

        csequence = 0

        if parent_lines:
            for p in parent_lines:
                csequence += 1
                p.sequence = csequence
                #self.env.cr.execute("UPDATE sale_order_line SET sequence  = "+str(csequence)+" WHERE id = "+str(p.id))
                #raise ValueError(p.childrens_line_ids)
                csequence = p.validate_childrens(csequence)


    #new new

    def write(self, values):
        res = super(SaleOrder, self).write(values)
        self.rename_sequence_shf()
        return res



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    # _order = 'order_id,  sequence_save ,sequence, sequence_seccion1 , id'

    total = fields.Monetary(compute='_compute_total', string='Total Amount ')
    unit = fields.Float(compute="_compute_unit", string="unit")
    product_quantity = fields.Float(compute="_compute_quantity", string="quantity")
    # yo agregue
    state_hidden = fields.Selection([('show', 'show'), ('hidden', 'hidden')], default='show')
    #section_parent_id = fields.Many2one('sale.order.line', compute="get_section_parent_id")
    #state_hidden_parent = fields.Selection(related="section_parent_id.state_hidden")
    # section_parent_parent_id = fields.Many2one('sale.order.line', compute="get_section_parent_id")
    #field_previous = fields.Many2one('sale.order.line', compute="get_section_parent_id")
    #nivel_section = fields.Integer(string="NS")


    def validate_childrens(self,csequence):
        if self.childrens_line_ids:
            for ch in self.childrens_line_ids:
                csequence += 1
                ch.sequence = csequence
                csequence = ch.validate_childrens(csequence)
                #ch.sequence = csequence

            return csequence
        else:
            csequence += 1
            self.sequence = csequence
            return csequence


    # @api.depends('sequence')
    def get_section_parent_id(self):
        for record in self:
            record.section_parent_id = False

            record.field_previous = False

            for l in record.order_id.order_line:
                # search line previus
                if l.sequence < record.sequence:
                    record.field_previous = l.id

                # search line previus and
                if l.sequence < record.sequence and l.display_type in ['line_section']:
                    if record.display_type not in ['line_section']:
                        record.section_parent_id = l.id
                    else:
                        if l.nivel_section == 0:
                            record.section_parent_id = l.id
                        if record.nivel_section == 0:
                            record.section_parent_id = False
                else:
                    pv = record.field_previous
                    if pv.display_type in ['line_section'] and pv.display_type == 0:
                        record.section_parent_id = pv.id

            '''
            for l in record.order_id.order_line:
                if record.display_type in ['line_section', 'line_note']:
                    if l.sequence < record.sequence:
                        pv = l.field_previous
                        if pv.display_type in ['line_section', 'line_note']:
                            record.section_parent_id = l.id
            '''

    # yo agregue

    @api.depends('product_id')
    def _compute_total(self):
        for rec in self:
            rec.total = 0

    @api.depends('product_id')
    def _compute_unit(self):
        for rec in self:
            rec.unit = 0

    @api.depends('product_id')
    def _compute_quantity(self):
        for rec in self:
            rec.product_quantity = 0


    '''
        def action_hidden(self):

            record = self
            if 1 == 1:
                state_hidden = 'show'
                tmp_state_hidden = None
                for l in record.order_id.order_line:
                    if l.section_parent_id == record:
                        if not tmp_state_hidden:
                            tmp_state_hidden = l.state_hidden

                        if tmp_state_hidden == 'hidden':
                            l.state_hidden = 'show'
                            state_hidden = 'show'

                        if tmp_state_hidden == 'show':
                            l.state_hidden = 'hidden'
                            state_hidden = 'hidden'

                        for lx in record.order_id.order_line:

                            if lx.section_parent_id == l:
                                # raise ValueError(record.section_parent_id)
                                if tmp_state_hidden == 'hidden':
                                    lx.state_hidden = 'show'
                                    state_hiddenx = 'show'

                                if tmp_state_hidden == 'show':
                                    lx.state_hidden = 'hidden'
                                    state_hiddenx = 'hidden'
                                l.state_hidden = state_hiddenx if tmp_state_hidden else 'show'

                record.state_hidden = state_hidden if tmp_state_hidden else 'show'
                parent = record.section_parent_id
                if parent:
                    if parent.display_type == 'line_section' and parent.nivel_section == 0:
                        if parent.state_hidden == 'show':
                            record.state_hidden = 'show'
        '''

    # new new
    parent_section_id = fields.Many2one('sale.order.line', string="PS", domain="[('order_id','=', order_id.id)]")
    childrens_line_ids = fields.One2many('sale.order.line','parent_section_id')



    def action_hidden(self,state_init=None):
        #childres = self.env['sale.order.line'].search([('parent_section_id','=',self.id)])
        childres = self.childrens_line_ids
        if childres:
            ch_o = childres[0]
            state_init = ch_o.state_hidden if ch_o.state_hidden else 'hidden'
            state_init = 'hidden' if state_init == 'show' else 'show'
            for ch in childres:
                ch.state_hidden = state_init
                ch.action_hidden(state_init)



