from odoo import models, fields, api, tools, SUPERUSER_ID

from odoo import http
from odoo.http import request

#from . import stage

class TicketManagement(models.Model):

	"""Core of this module. This class describes what is a ticket
	
	Attributes:
	    m_resolved (bool): True if the ticket is resolved, false otherwise
	    m_ticketDescription (str): This is the text of the ticket (the issue)
	    m_title (str): Title of the ticket
	    m_type (str): Type of the ticket -> incident | question | request
	    m_contact (many2one): Foreign key targeting the contact id (caller)
	    m_caller_company (many2one) : company of the caller
	    m_caller_phone (str) : phone number of the caller
	    m_stage_id (many2one) : refer to the ticket status
	    m_settings (many2one) : refer to the ticket settings
	    m_multi_email_addr (str) : contains the email address of the helpers
	"""
	
	_name = 'ticket_management.ticket_management'
	_inherit = ['mail.thread']


	m_resolved = fields.Boolean(string='Le ticket est résolu', default=False, required=True)
	m_waiting = fields.Boolean(string='Le ticket est en attente', default=False)

	#m_stage_id = fields.Many2one('ticket_management.stage', string='Ticket Status', ondelete='restrict', track_visibility='onchange', index=True, group_expand='_read_group_stage_ids', default= lambda self: self.env['ticket_management.stage'].search([], order='m_sequence', limit=1).id)
	m_status = fields.Selection([("new","Nouveau"), ("inProgress","En progression"), ("resolved","Résolu")], string="Ticket status", default='new', track_visibility='onchange', group_expand='_read_stage_ids')
	
	m_title = fields.Char(string='Title', required=True)
	m_type = fields.Selection([('question','Question'), ('incident', 'Incident'), ('helpRequest', 'Demande d\'aide')], string='Type of ticket')
	m_ticketDescription = fields.Text(string='Description', required=True, help="Ticket's description")
	m_contact = fields.Many2one('res.partner', string='Caller')

	m_caller_company = fields.Many2one(related='m_contact.parent_id', store=False, readonly=True)
	m_caller_phone = fields.Char(related='m_contact.phone', store=False, readonly=True)

	m_settings = fields.Many2one('ticket_management.settings', required=True, string='Settings', ondelete='restrict', index=True, default= lambda self: self.env['ticket_management.settings'].search([], order='m_sequence', limit=1).id)
	m_multi_email_addr = fields.Char(string='A string built with all internal users\' email address')

	@api.one
	def resolved_ticket(self):
		"""Is called to resolve a ticket, mark the current ticket as resolved in the database and change its stage
		"""
		self.write({'m_resolved':True, 'm_status':"resolved"})

	@api.one
	def ticket_waiting(self):
		"""Is called to resolve a ticket, mark the current ticket as resolved in the database and change its stage
		"""
		self.write({'m_waiting':True})

	@api.model
	def create(self, values):
		"""Overrides the create default method in order to allow a mail sending when a new ticket is recorded
		
		Args:
		    values (tab): Fields of TicketManagement class (at least the required fields) 
		
		Returns:
		    TicketManagement: Class
		"""

		# Override the original create function for the this model
		record = super(TicketManagement, self).create(values)


		#mail sending to the caller
		template_caller = record.m_settings.m_caller_mail
		template_caller.send_mail(record.id)

		#mail sending to the group user
		record.m_multi_email_addr = record.m_settings.m_multi_email_addr
		template_users = record.m_settings.m_group_user_mail
		template_users.send_mail(record.id)
		
		return record

	@api.model
	def _read_stage_ids(self, stages, domain, order):
		"""This function allows the kanban view to get all the known ticket status (even if the status doesn't contain any ticket)
		
		Args:
		    stages (TYPE): Not used
		    domain (TYPE): Not used
		    order (TYPE): Not used
		
		Returns:
		    Array[str]: All status
		"""
		return (["new", "inProgress", "resolved"])