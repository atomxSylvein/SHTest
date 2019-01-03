from odoo import models, fields, api

class Stage(models.Model):

	"""This class is for the tickets statuses
	
	Attributes:
	    m_asResolved (bool): True if this stage/status can consider the ticket as resolved
	    m_sequence (int): Allows the stages order
	    m_stageName (str): Name of this stage
	"""
	
	_name = 'ticket_management.stage'
	_description = "Ticket Status"
	_rec_name = 'm_stageName'
	_order = "m_sequence, m_stageName, id"

	#_inherit = 'base.kanban.abstract'
	

	m_stageName = fields.Char(string='Stage name', required=True)
	m_sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
	m_asResolved = fields.Boolean(string='This stage consider the ticket as resolved')
	