# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PluginProject(models.Model):

	"""This class extends Project class and provides implements the projects statuses
	
	Attributes:
	    m_stage (selection): Statu sof the project. Can be building, inProgress or done
	"""
	
	_inherit = 'project.project'
	m_stage = fields.Selection([('building', 'En construction'), ('inProgress', 'En cours'), ('done', 'Réalisé')], string="Étape du projet", default="building", group_expand="_read_group_stage_ids", store=True, track_visibility='onchange')

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