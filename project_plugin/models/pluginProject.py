# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PluginProject(models.Model):

	"""This class extends Project class and provides implements the projects statuses
	
	Attributes:
	    m_description (str): Project description
	    m_stage (selection): Status of the project. Can be 'building', 'inProgress' or 'done'
	    m_typologie (selection): Type of service (this provides the project color code)
	"""
	
	_inherit = 'project.project'

	m_stage = fields.Selection([('building', 'En construction'), ('inProgress', 'En cours'), ('done', 'Réalisé')], string="Étape du projet", default="building", group_expand="_read_group_stage_ids", store=True, track_visibility='onchange')
	m_description = fields.Text(string = "Description du projet")
	m_typologie = fields.Selection([('4', 'Services Développement'), ('1', 'Services Intégration ServiceNow'), ('5', 'Services Intégration Odoo'), ('0', 'Autres')], string = "Business Unit Services", required=True, default='4')

	@api.model
	def _read_group_stage_ids(self, stages, domain, order):
		"""This function allows the kanban view to get all the known file status (even if the status doesn't contain any graft)
		
		Args:
		    stages (TYPE): Not used
		    domain (TYPE): Not used
		    order (TYPE): Not used
		
		Returns:
		    Array[str]: stage
		"""
		return (["building", "inProgress", "done"])