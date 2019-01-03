from odoo import models, fields, api

class Settings(models.Model):

	"""This class is for the tickets statuses
	
	Attributes:
	    m_asResolved (bool): True if this stage/status can consider the ticket as resolved
	    m_sequence (int): Allows the stages order
	    m_name (str): Name of this stage
	    m_caller_mail (str): Email template of the caller
	    m_group_user_mail (str): Email template of the users
	    m_group_id (str): Id of the group including the users who are allowed to resolve a ticket
		m_multi_email_addr (str): Contains a well formed string including the helpers email address
	"""
	
	_name = 'ticket_management.settings'
	_description = "Ticket Settings"
	_order = "m_sequence"


	m_name = fields.Char(string='Setting title', required=True)
	m_sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

	m_caller_mail = fields.Many2one('mail.template', string='Caller - confirmation mail template', required=True)
	m_group_user_mail = fields.Many2one('mail.template', string='Internal users - confirmation mail template', required=True)	
	
	m_group_id = fields.Many2one('res.groups', string='Internal users who are allowed to resolve a ticket')

	m_multi_email_addr = fields.Char(string='A string built with all internal users\' email address')

	@api.model
	def create(self, values):
		"""Overrides the create default method in order to build and store a well formed string including the users email address, when a new setting is recorded
		
		Args:
		    values (tab): Fields of Settings class (at least the required fields) 
		
		Returns:
		    Settings: Class
		"""
		# Override the original create function for the this model
		record = super(Settings, self).create(values)

		emails = {}

		for user in record.m_group_id.users:
			emails[user.email] = user.id

		record.m_multi_email_addr = ', '.join(str(x) for x in emails)

		return record