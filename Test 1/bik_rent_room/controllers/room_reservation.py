from odoo import http
from odoo.http import request, Response
import json


class RoomReservationController(http.Controller):

    def _response_success(self, reservation):
        return Response(json.dumps({
            "status": "success",
            "reservation_id": reservation.id,
            "reservation_number": reservation.name,
            "reservation_name": reservation.reservation_name,
            "room_name": reservation.room_master_id.name,
            "reservation_date": reservation.reservation_date.strftime('%Y-%m-%d'),
            "state": reservation.state,
            "notes": reservation.notes
        }), status=200, mimetype='application/json')

    def _response_error(self):
        return Response(json.dumps({
            "status": "error",
            "message": "Pemesanan tidak ditemukan."
        }), status=404, mimetype='application/json')

    @http.route('/api/room_reservation/<int:reservation_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_reservation_status(self, reservation_id, **kwargs):
        reservation = request.env['room.reservation'].sudo().search([('id', '=', reservation_id)], limit=1)

        if not reservation:
            return self._response_error()

        return self._response_success(reservation)

    @http.route('/api/room_reservation/track', type='json', auth='public', methods=['POST'], csrf=False)
    def track_reservation_status(self, **payload):
        reservation_number = payload.get('reservation_number')
        if not reservation_number:
            return {
                "status": "error",
                "message": "Nomor Pemesanan diperlukan."
            }

        reservation = request.env['room.reservation'].sudo().search([('name', '=', reservation_number)], limit=1)

        if not reservation:
            return self._response_error()

        return self._response_success(reservation)
