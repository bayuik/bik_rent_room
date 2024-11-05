from odoo import fields, models, api
from odoo.exceptions import ValidationError
import re


class RoomReservation(models.Model):
    _name = "room.reservation"
    _description = "Room Reservation"
    _order = "id desc"

    name = fields.Char('Nomor Pemesanan', required=True, default='/')
    room_master_id = fields.Many2one('room.master', 'Ruangan', required=True, ondelete='restrict')
    reservation_name = fields.Char('Nama Pemesanan', required=True)
    reservation_date = fields.Date('Tanggal Pemesanan', default=lambda self: fields.Date.today(), required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('on_going', 'On Going'),
        ('done', 'Done'),
    ], string='Status', default='draft')
    notes = fields.Text('Catatan Pemesanan')

    def _sequence_name(self):
        if self.name == '/':
            sequence = self.env['ir.sequence'].next_by_code('room.reservation.sequence')
            room_master_id = self.room_master_id
            room_type_value = dict(room_master_id.fields_get(['room_type'])['room_type']['selection']).get(
                room_master_id.room_type, '')
            reservation_date = self.reservation_date.strftime('%d/%m/%Y')

            return f"{room_master_id.name}/{room_type_value}/{reservation_date}/{sequence}"

    @api.model
    def create(self, vals):
        if 'reservation_name' in vals:
            existing_reservation = self.search([('reservation_name', '=', vals['reservation_name'])], limit=1)
            if existing_reservation:
                raise ValidationError("Nama Pemesanan tidak boleh sama.")

        if 'room_master_id' in vals and 'reservation_date' in vals:
            existing_reservation = self.search([
                ('room_master_id', '=', vals['room_master_id']),
                ('reservation_date', '=', vals['reservation_date'])
            ], limit=1)
            if existing_reservation:
                raise ValidationError("Tidak boleh memesan ruangan dan tanggal pemesanan yang sama.")

        if 'notes' in vals:
            if not re.match(r"^[a-zA-Z0-9\s.,'-]+$", vals['notes']):
                raise ValidationError("Input pada 'Catatan Pemesanan' mengandung karakter tidak valid.")

        res = super(RoomReservation, self).create(vals)
        res.name = res._sequence_name()
        return res

    @api.constrains('reservation_name')
    def _check_reservation_name_unique(self):
        for record in self:
            if self.search_count([('reservation_name', '=', record.reservation_name)]) > 1:
                raise ValidationError("Nama Pemesanan harus unik.")

    @api.constrains('room_master_id', 'reservation_date')
    def _check_room_and_date_unique(self):
        for record in self:
            if self.search_count([
                ('room_master_id', '=', record.room_master_id.id),
                ('reservation_date', '=', record.reservation_date),
                ('id', '!=', record.id)
            ]) > 0:
                raise ValidationError("Tidak boleh memesan ruangan dan tanggal pemesanan yang sama.")

    def action_on_going(self):
        self.state = 'on_going'

    def action_done(self):
        self.state = 'done'
