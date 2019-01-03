from odoo import http
from odoo.http import request, Response

from odoo.addons.website.controllers.main import Website

class Main(Website):

    #Homepage
    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        return request.render('atomx_portal.atomx_home', {})


    #HTML tickets list
    @http.route('/rawtickets/', type='http', auth='public')
    def raw_tickets(self):
        #récupération de tous les records de tickets
        records = http.request.env['ticket_management.ticket_management'].sudo().search([]) 

        #construction de la page
        result = '<html><body><table><tr><td>' 
        result += '</td></tr><tr><td>'.join(records.mapped('m_title'))
        result += '</td></tr></table></body></html>'

        #http.request.session['hello']= 'world'
        #http.request.session.get('hello')

        return result


    @http.route('/tickets', type='http', auth="user", website=True)
    def view_ticket_list(self, **post):
        current_id = http.request.env.context.get('uid') 
        
        user_environment = request.env['res.users']
        
        domain = [('id', '=', int(current_id))]

        user_logged = user_environment.search(domain) 

        public_user = False

        #on récupère les groupe dont il fait partie
        user_groups = user_logged.groups_id

        #on cherche à voir s'il est dans le groupe "Public"
        for group in user_groups:
            if group.name == "Public":
                public_user = True

        ticket_environment = request.env['ticket_management.ticket_management']
        ticket_list = ticket_environment.search([], order='m_resolved desc')

        if public_user == True:
            return Response("Access denied", status=403)
        else:
            return request.render('atomx_portal.tickets', { 'tickets': ticket_list, } )
        

    @http.route('/my-tickets', type='http', auth="user", website=True)
    def view_my_tickets(self):
        current_id = http.request.env.context.get('uid') 
        
        user_environment = request.env['res.users']
        
        domain = [('id', '=', int(current_id))]

        user_logged = user_environment.search(domain) 
        contact = user_logged.partner_id.id

        ticket_environment = request.env['ticket_management.ticket_management']
        domain = [('m_contact', '=', contact)]

        ticket_list = ticket_environment.search(domain, order='m_resolved desc')

        return request.render('atomx_portal.tickets', { 'tickets': ticket_list, } )


    #TO DO afficher plus d'informations 
    @http.route('/ticket_view', type='http', auth='user', csrf=False)
    def ticket_view(self, **post):
        result = '<html><body> id du ticket choisi : ' + post['id'] + '</body></html>' 
        return result


    #route to create a new ticket
    @http.route('/besoin-d-aide', type='http', auth="user", website=True)
    def besoin_d_aide(self):
        return request.render('atomx_portal.create_ticket', {} )


    @http.route('/created', type='http', auth='user', website=True)
    def create_ticket(self, **post):
        current_id = http.request.env.context.get('uid') 
        
        user = request.env['res.users']
        
        domain = [('id', '=', int(current_id))]

        user_logged = user.search(domain) 
             

        ticket = request.env['ticket_management.ticket_management'].sudo().create({
            'm_title': post.get('m_title'),
            'm_ticketDescription': post.get('m_ticketDescription'),
            'm_resolved': False,
            'm_type': post.get('m_type'),
            'm_contact': int(user_logged.partner_id.id),
        })
        return http.request.redirect('/my-tickets')


    #HTML test
    @http.route('/tickets/user/', type='http', auth='user')
    def user(self):  
        result = '<html><body>USER</body></html>'
        return result


    #JSON tickets list
    @http.route('/tickets/json', type='json', auth='public')
    def tickets_json(self):
        #récupération de tous les records de tickets
        records = http.request.env['ticket_management.ticket_management'].sudo().search([]) 

        return records.read(['m_title'])