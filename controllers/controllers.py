# -*- coding: utf-8 -*-
from odoo import http

class cipwebsite(http.Controller):
    # @http.route('/cipwesite/cipwesite/', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"

    # @http.route('/cipwesite/cipwebsite/home/', auth='public')
    # def index(self, **kw):
    #     return http.request.render('cipwebsite.index', {
    #         'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
    #     })

    # @http.route('/cipwebsite/cipwebsite/home/model/', auth='public')
    # def index(self, **kw):
    #     Teachers = http.request.env['cipwebsite.teachers']
    #     return http.request.render('cipwebsite.model', {
    #         'teachers': Teachers.search([])
    #     })

    @http.route('/cipwebsite/cipwebsite/website/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['cipwebsite.teachers']
        return http.request.render('cipwebsite.website', {
            'teachers': Teachers.search([])
        })

    @http.route('/cipwebsite/<name>/', auth='public', website=True)
    def teacher(self, name):
        return '<h1>{}</h1>'.format(name)
    

    @http.route('/cipwebsite/<int:id>/', auth='public', website=True)
    def teacher(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    
    @http.route('/cipwebsite/<model("cipwebsite.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('cipwebsite.biography', {
            'person': teacher
        })



#     @http.route('/cipwebsite/cipwebsite/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cipwebsite.listing', {
#             'root': '/cipwebsite/cipwebsite',
#             'objects': http.request.env['cipwebsite.cipwebsite'].search([]),
#         })

#     @http.route('/cipwebsite/cipwebsite/objects/<model("cipwebsite.cipwebsite"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cipwebsite.object', {
#             'object': obj
#         })