from odoo import fields, models


class RoomMaster(models.Model):
    _name = "room.master"
    _description = "Room Master"
    _order = "id desc"

    name = fields.Char('Nama Ruangan', required=True)
    room_type = fields.Selection([
        ('small', 'Meeting Room Kecil'),
        ('large', 'Meeting Room Besar'),
        ('aula', 'Aula'),
    ], 'Tipe Ruangan', required=True)
    room_location = fields.Selection([
        ('1a', '1A'),
        ('1b', '1B'),
        ('1c', '1C'),
        ('2a', '2A'),
        ('2b', '2B'),
        ('2c', '2C'),
    ], 'Lokasi Ruangan', required=True)
    image = fields.Binary('Foto Ruangan', required=True)
    room_capacity = fields.Integer('Kapasitas Ruangan', required=True)
    description = fields.Text('Keterangan')
