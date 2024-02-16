from openerp import models, fields, api, _
from openerp import tools, _
from datetime import datetime,timedelta



class Employee(models.TransientModel):
	_name = 'hr.employee.wizard'

 
	user_category = fields.Selection([('admin','Super User'),
									('driver','Taurus Driver'),
									('eicher_driver','Eicher Driver'),
									('pickup_driver','Pick Up Driver'),
									('lmv_driver','Light Motor Vehicle Driver'),
									('directors','Directors'),
									('project_manager','Project Manager'),
									('office_manger','Office Manager'),
									('project_eng','Project Engineer'),
									('cheif_acc','Cheif Accountant'),
									('sen_acc','Senior Accountant'),
									('jun_acc','Junior Accountant'),
									('cashier','Cashier'),
									('project_cordinator','Project Cordinator'),
									('technical_team','Technical Team'),
									('telecome_bill','Telecome Billing'),
									('survey_team','Survey Team'),
									('quality','Quality'),
									('tendor','Tendor'),
									('interlocks','Interlocks'),
									('liaisoning','Liaisoning'),
									('hr','HR'),
									('district_manager','District Manager'),
									('site_eng','Captain/Site Engineer'),
									('supervisor','Supervisor(Civil)'),
									('super_telecome','Supervisor(Telecome)'),
									('super_trainee','Supervisor(Trainee)'),
									('operators','Operators'),
									('helpers','Helpers'),
									('vehicle_admin','Vehicle Administration'),
									('purchase','Purchase'),
									('civil_store','Civil Store'),
									('telecome_store','Telecome Store'),
									('security','Security'),
									('labour','Labour'),
									('civil_workshop','Civil Workshop'),
									('vehicle_workshop','Vehicle Workshop'),
									('all','All')
									], default="all", string='User Category',required=True)
		


	@api.multi
	def action_employee_open_window(self):
			print 'a------------------------------------------------'
		 

			datas = {
				 'ids': self._ids,
				 'model': self._name,
				 'form': self.read(),
				 'context':self._context,
			}
		 
			return{
				 'name' : 'Employee Report',
				 'type' : 'ir.actions.report.xml',
				 'report_name' : 'hiworth_hr_attendance.report_employee_details_template',
				 'datas': datas,
				 'report_type': 'qweb-pdf'
			}

	@api.multi
	def action_employee_open_window1(self):
			print 'b------------------------------------------------'
		 

			datas = {
				 'ids': self._ids,
				 'model': self._name,
				 'form': self.read(),
				 'context':self._context,
			}
		 
			return{
				 'name' : 'Employee Report',
				 'type' : 'ir.actions.report.xml',
				 'report_name' : 'hiworth_hr_attendance.report_employee_details_template',
				 'datas': datas,
				 'report_type': 'qweb-html'
			}

 

	@api.multi
	def get_details(self):        
		list = []
		if self.user_category == 'all':
			employees = self.env['hr.employee'].search([])
		else:
			employees = self.env['hr.employee'].search([('user_category','=',self.user_category)])
		for empl_id in employees:
			esi = ''
			mediclaim = ''
			pf = ''
			qualification = ''
			training = ''
			if empl_id.esi == True:
				esi = "OK"
			if empl_id.pf == True:
				pf = "OK"
			if empl_id.mediclaim == True:
				mediclaim = "OK"
			for val in empl_id.edu_qualify:
				qualification += val.qualification + ','
			for val in empl_id.tech_training:
				training += val.name + ','

			basic_salary = self.env['hr.contract'].search([('employee_id','=', empl_id.id),('state','=','active')], limit=1).wage
			list.append({
							'id_no': empl_id.emp_code,
							'old_id_no': empl_id.emp_code_old,
							'company': empl_id. company_contractor_id.name,
							'employee_name': empl_id.name,
							'gender': empl_id.gender,
							'contact_no': empl_id.mobile_phone,
							'qualification': qualification,
							'technical_training': training,
							'designation': empl_id.user_category,
							'department': empl_id.department_id.name,
							'date_joining': empl_id.joining_date,
							'no_months_job': empl_id.no_mnth_job,
							'year_service': empl_id.year_service,
							'age': empl_id.age,
							'dob': empl_id.birthday,
							'blood_group': empl_id.blood_group,
							# 'level': empl_id.name,
							'basic_salary': basic_salary,
							# 'da': basic_salary,
							# 'bata': 0,
							# 'gross_salary': basic_salary,
							'pf': pf,
							'mediclaim': mediclaim,
							'esi': esi,
							'esi_no': empl_id.esi_no,
							# 'nominee': empl_id.name,
							# 'insurance': empl_id.name,
							# 'policy_no': empl_id.name,
							# 'insurance_renewal_date': empl_id.name,
							# 'previous_appraisal_month': empl_id.name,
							# 'gross_salary_before_appraisal': empl_id.name,
							# 'gross_salary_after_appraisal': empl_id.name,
							# 'remarks': empl_id.notes,
							})

		return list




class JoiningEmployees(models.Model):
		_name = 'employee.joinees.wizard'

	 
		date_from = fields.Date('Date From',required=True)
		date_to = fields.Date('Date To',required=True)
		user_category = fields.Selection([('admin','Super User'),
																		('driver','Taurus Driver'),
																		('eicher_driver','Eicher Driver'),
																		('pickup_driver','Pick Up Driver'),
																		('lmv_driver','Light Motor Vehicle Driver'),
																		('directors','Directors'),
																		('project_manager','Project Manager'),
																		('office_manger','Office Manager'),
																		('project_eng','Project Engineer'),
																		('cheif_acc','Cheif Accountant'),
																		('sen_acc','Senior Accountant'),
																		('jun_acc','Junior Accountant'),
																		('cashier','Cashier'),
																		('project_cordinator','Project Cordinator'),
																		('technical_team','Technical Team'),
																		('telecome_bill','Telecome Billing'),
																		('survey_team','Survey Team'),
																		('quality','Quality'),
																		('tendor','Tendor'),
																		('interlocks','Interlocks'),
																		('liaisoning','Liaisoning'),
																		('hr','HR'),
																		('district_manager','District Manager'),
																		('site_eng','Captain/Site Engineer'),
																		('supervisor','Supervisor(Civil)'),
																		('super_telecome','Supervisor(Telecome)'),
																		('super_trainee','Supervisor(Trainee)'),
																		('operators','Operators'),
																		('helpers','Helpers'),
																		('vehicle_admin','Vehicle Administration'),
																		('purchase','Purchase'),
																		('civil_store','Civil Store'),
																		('telecome_store','Telecome Store'),
																		('security','Security'),
																		('labour','Labour'),
																		('civil_workshop','Civil Workshop'),
																		('vehicle_workshop','Vehicle Workshop'),
																		('all','All')
																		], default="all", string='User Category',required=True)
		


		@api.multi
		def action_open_window(self):
			 

			 datas = {
					 'ids': self._ids,
					 'model': self._name,
					 'form': self.read(),
					 'context':self._context,
			 }
			 
			 return{
					 'name' : 'Site Joinees',
					 'type' : 'ir.actions.report.xml',
					 'report_name' : 'hiworth_hr_attendance.report_employee_site_joinees_template',
					 'datas': datas,
					 'report_type': 'qweb-pdf'
			 }

		@api.multi
		def action_open_window1(self):
			 

			 datas = {
					 'ids': self._ids,
					 'model': self._name,
					 'form': self.read(),
					 'context':self._context,
			 }
			 
			 return{
					 'name' : 'Site Joinees',
					 'type' : 'ir.actions.report.xml',
					 'report_name' : 'hiworth_hr_attendance.report_employee_site_joinees_template',
					 'datas': datas,
					 'report_type': 'qweb-html'
			 }


		@api.multi
		def get_details(self):
				
				list = []
				if self.user_category == 'all':
						employees = self.env['hr.employee'].search([('joining_date','>=',self.date_from),('joining_date','<=',self.date_to)],order='joining_date asc')
				else:
						employees = self.env['hr.employee'].search([('user_category','=',self.user_category),('joining_date','>=',self.date_from),('joining_date','<=',self.date_to)],order='joining_date asc')
				for empl_id in employees:
						list.append({
										'id_no': empl_id.emp_code,
										'employee_name': empl_id.name,
										'designation': empl_id.user_category,
										'joining_date': datetime.strptime(empl_id.joining_date,"%Y-%m-%d").strftime("%d-%m-%Y"),
										})

				return list


class ResigningEmployees(models.Model):
		_name = 'employee.resign.wizard'

	 
		date_from = fields.Date('Date From',required=True)
		date_to = fields.Date('Date To',required=True)
		user_category = fields.Selection([('admin','Super User'),
																		('driver','Taurus Driver'),
																		('eicher_driver','Eicher Driver'),
																		('pickup_driver','Pick Up Driver'),
																		('lmv_driver','Light Motor Vehicle Driver'),
																		('directors','Directors'),
																		('project_manager','Project Manager'),
																		('office_manger','Office Manager'),
																		('project_eng','Project Engineer'),
																		('cheif_acc','Cheif Accountant'),
																		('sen_acc','Senior Accountant'),
																		('jun_acc','Junior Accountant'),
																		('cashier','Cashier'),
																		('project_cordinator','Project Cordinator'),
																		('technical_team','Technical Team'),
																		('telecome_bill','Telecome Billing'),
																		('survey_team','Survey Team'),
																		('quality','Quality'),
																		('tendor','Tendor'),
																		('interlocks','Interlocks'),
																		('liaisoning','Liaisoning'),
																		('hr','HR'),
																		('district_manager','District Manager'),
																		('site_eng','Captain/Site Engineer'),
																		('supervisor','Supervisor(Civil)'),
																		('super_telecome','Supervisor(Telecome)'),
																		('super_trainee','Supervisor(Trainee)'),
																		('operators','Operators'),
																		('helpers','Helpers'),
																		('vehicle_admin','Vehicle Administration'),
																		('purchase','Purchase'),
																		('civil_store','Civil Store'),
																		('telecome_store','Telecome Store'),
																		('security','Security'),
																		('labour','Labour'),
																		('civil_workshop','Civil Workshop'),
																		('vehicle_workshop','Vehicle Workshop'),
																		('all','All')
																		], default="all", string='User Category',required=True)
		


		@api.multi
		def action_open_window(self):
			 

			 datas = {
					 'ids': self._ids,
					 'model': self._name,
					 'form': self.read(),
					 'context':self._context,
			 }
			 
			 return{
					 'name' : 'Site Resignation',
					 'type' : 'ir.actions.report.xml',
					 'report_name' : 'hiworth_hr_attendance.report_employee_site_resign_template',
					 'datas': datas,
					 'report_type': 'qweb-pdf'
			 }

		@api.multi
		def action_open_window1(self):
			 

			 datas = {
					 'ids': self._ids,
					 'model': self._name,
					 'form': self.read(),
					 'context':self._context,
			 }
			 
			 return{
					 'name' : 'Site Resignation',
					 'type' : 'ir.actions.report.xml',
					 'report_name' : 'hiworth_hr_attendance.report_employee_site_resign_template',
					 'datas': datas,
					 'report_type': 'qweb-html'
			 }


		@api.multi
		def get_details(self):
				
				list = []
				if self.user_category == 'all':
						employees = self.env['hr.employee'].search([('resigning_date','>=',self.date_from),('resigning_date','<=',self.date_to)],order='resigning_date asc')
				else:
						employees = self.env['hr.employee'].search([('user_category','=',self.user_category),('resigning_date','>=',self.date_from),('resigning_date','<=',self.date_to)],order='resigning_date asc')
				for empl_id in employees:
						list.append({
										'id_no': empl_id.emp_code,
										'employee_name': empl_id.name,
										'designation': empl_id.user_category,
										'resigning_date': datetime.strptime(empl_id.resigning_date,"%Y-%m-%d").strftime("%d-%m-%Y"),
										})

				return list


class EmployeelnsuranceReport(models.Model):
		_name = 'employee.insurance.report'

		date_from = fields.Date('Date From')
		date_to = fields.Date('Date To')
		policy_id = fields.Many2one('policy.type', string='Type of Policy')
		state = fields.Selection([('all','All'),
							('draft','draft'),
							('paid','Paid'),
							('closed','Collected')
							], default='all')


		@api.multi
		def action_employee_insurance_open_window(self):
			print 'a------------------------------------------------'
			 

			datas = {
				 'ids': self._ids,
				 'model': self._name,
				 'form': self.read(),
				 'context':self._context,
			}
			 
			return{
				 'name' : 'Employee Report',
				 'type' : 'ir.actions.report.xml',
				 'report_name' : 'hiworth_hr_attendance.report_employee_insurance_details_template',
				 'datas': datas,
				 'report_type': 'qweb-pdf'
			}

		@api.multi
		def action_employee_open_insurance_window1(self):
			print 'b------------------------------------------------'
			 

			datas = {
				 'ids': self._ids,
				 'model': self._name,
				 'form': self.read(),
				 'context':self._context,
			}
			 
			return{
				 'name' : 'Employee Report',
				 'type' : 'ir.actions.report.xml',
				 'report_name' : 'hiworth_hr_attendance.report_employee_insurance_details_template',
				 'datas': datas,
				 'report_type': 'qweb-html'
			}


		@api.multi
		def get_details(self):
				
				list = []
				if self.state == 'all':
						insurance = self.env['employee.insurance'].search([('policy_id','=',self.policy_id.id),('commit_date','>=',self.date_from),('commit_date','<=',self.date_to)])
				else:
						insurance = self.env['employee.insurance'].search([('state','=',self.state),('policy_id','=',self.policy_id.id),('commit_date','>=',self.date_from),('commit_date','<=',self.date_to)])
				print 'insurance--------------------------------------', insurance
				for ins_id in insurance:
						list.append({
										'id_no': ins_id.employee_id.emp_code,
										'employee_name': ins_id.employee_id.name,
										'designation': ins_id.user_category,
										'mobile_no': ins_id.work_phone,
										'gender': ins_id.gender,
										'dob': ins_id.birthday,
										'age': ins_id.age,
										'policy_type': ins_id.policy_id.name,
										'claim_duration': ins_id.claim_duration,
										'premium_amt': ins_id.premium_amount,
										'company_amt': ins_id.comp_contribution,
										'staff_amt': ins_id.empol_contribution,
										'no_persons': ins_id.no_of_person,
										'policy_no': ins_id.policy_no,
										'insured_no': ins_id.insured_code,
										'commit_date': ins_id.commit_date,
										'renew_date': ins_id.renew_date,
										# 'sponsored_by': ins_id.joining_date,
										})

				return list



class EmployeelnsuranceRenewalReport(models.Model):
		_name = 'insurance.renewal.report'

		date_from = fields.Date('Date From')
		date_to = fields.Date('Date To')
		policy_id = fields.Many2one('policy.type', string='Type of Policy')



		@api.multi
		def action_employee_insurance_open_window(self):
			print 'a------------------------------------------------'
			 

			datas = {
				 'ids': self._ids,
				 'model': self._name,
				 'form': self.read(),
				 'context':self._context,
			}
			 
			return{
				 'name' : 'Employee Report',
				 'type' : 'ir.actions.report.xml',
				 'report_name' : 'hiworth_hr_attendance.report_employee_insurance_renewal_template',
				 'datas': datas,
				 'report_type': 'qweb-pdf'
			}

		@api.multi
		def action_employee_open_insurance_window1(self):
			print 'b------------------------------------------------'
			 

			datas = {
				 'ids': self._ids,
				 'model': self._name,
				 'form': self.read(),
				 'context':self._context,
			}
			 
			return{
				 'name' : 'Employee Report',
				 'type' : 'ir.actions.report.xml',
				 'report_name' : 'hiworth_hr_attendance.report_employee_insurance_renewal_template',
				 'datas': datas,
				 'report_type': 'qweb-html'
			}


		@api.multi
		def get_details(self):
				
				list = []
				insurance = self.env['employee.insurance'].search([('policy_id','=',self.policy_id.id),('renew_date','>=',self.date_from),('renew_date','<=',self.date_to)])
				print 'insurance--------------------------------------', insurance
				for ins_id in insurance:
						list.append({
										'id_no': ins_id.employee_id.emp_code,
										'employee_name': ins_id.employee_id.name,
										'designation': ins_id.user_category,
										'mobile_no': ins_id.work_phone,
										'gender': ins_id.gender,
										'dob': ins_id.birthday,
										'age': ins_id.age,
										'policy_type': ins_id.policy_id.name,
										'claim_duration': ins_id.claim_duration,
										'premium_amt': ins_id.premium_amount,
										'company_amt': ins_id.comp_contribution,
										'staff_amt': ins_id.empol_contribution,
										'no_persons': ins_id.no_of_person,
										'policy_no': ins_id.policy_no,
										'insured_no': ins_id.insured_code,
										'commit_date': ins_id.commit_date,
										'renew_date': ins_id.renew_date,
										# 'sponsored_by': ins_id.joining_date,
										})

				return list



class PF_ESIReport(models.Model):
		_name = 'pf_esi.wizard'

		month = fields.Selection([('January','January'),
																('February','February'),
																('March','March'),
																('April','April'),
																('May','May'),
																('June','June'),
																('July','July'),
																('August','August'),
																('September','September'),
																('October','October'),
																('November','November'),
																('December','December')], 'Month')

		year = fields.Selection([(num, str(num)) for num in range(1900, 2080 )], 'Year', default=(datetime.now().year))
		company_contractor_id = fields.Many2one('res.partner', "Contract Company",
												domain="[('company_contractor','=',True)]")

		@api.multi
		def action_employee_pf_esi_open_window(self):
			print 'a------------------------------------------------'
			 

			datas = {
				 'ids': self._ids,
				 'model': self._name,
				 'form': self.read(),
				 'context':self._context,
			}
			 
			return{
				 'name' : 'Employee Report',
				 'type' : 'ir.actions.report.xml',
				 'report_name' : 'hiworth_hr_attendance.report_employee_pf_esi_template',
				 'datas': datas,
				 'report_type': 'qweb-pdf'
			}

		@api.multi
		def action_employee_pf_esi_open_window1(self):
			print 'b------------------------------------------------'
			 

			datas = {
				 'ids': self._ids,
				 'model': self._name,
				 'form': self.read(),
				 'context':self._context,
			}
			 
			return{
				 'name' : 'Employee Report',
				 'type' : 'ir.actions.report.xml',
				 'report_name' : 'hiworth_hr_attendance.report_employee_pf_esi_template',
				 'datas': datas,
				 'report_type': 'qweb-html'
			}


		@api.multi
		def get_esi_pf_details(self):
				
				list = []
				basic = 0
				attendance = 0
				wages_due = 0
				employee_amount = 0 
				employer_amount = 0
				pf_wages = 0
				edli = 0
				employer_epf = 0 
				employee_epf = 0
				employer_eps = 0
				domain = []
				domain.append(('month', '=', self.month))
				domain.append(('year', '=', self.year))
				if self.company_contractor_id:
					domain.append(('company_contractor_id', '=', self.company_contractor_id.id))

				pf = self.env['pf.payment'].search(domain)

				for empl_id in pf:
					for line2 in empl_id.line_ids:
						basic = line2.basic
						wages_due = line2.wages_due
						pf_wages = line2.pf_wages

						employer_epf = line2.employer_epf
						employee_epf = line2.employee_epf
						employer_eps = line2.employer_eps



						list.append({
										'employee_name': line2.employee_id.name,
										'basic_pay': basic,
										'attendance': attendance,
										'wages_due': wages_due,

										'pf_wages': pf_wages,
										'edli': edli,
										'employer_epf': employer_epf,
										'employee_epf': employee_epf,
										'eps': employer_eps,
										})


				return list

		@api.multi
		def get_pf_admin_details(self):
			admin_charges_list = []
			for rec in self:

				domain = []
				domain.append(('month', '=', self.month))
				domain.append(('year', '=', self.year))
				if self.company_contractor_id:
					domain.append(('company_contractor_id', '=', self.company_contractor_id.id))

				pf = self.env['pf.payment'].search(domain, limit=1)

				for admin in pf.admin_charges_ids:
					admin_charges_list.append({'name':admin.name or '',
											   'type':admin.type or '',
											   'per_amount':admin.per_amount or '',
											   'amount':admin.amount or ''})
			return admin_charges_list

		@api.multi
		def get_final_amount(self):
				
				list = []
				esi_employee_amount = 0
				esi_employer_amount = 0
				esi_amount_total = 0
				pf_employee_amount = 0
				pf_employer_amount = 0
				eps_amount = 0
				edli_amount = 0
				admin_amount = 0
				pf_amount_total = 0
				domain = []
				domain.append(('month','=',self.month))
				domain.append(('year','=', self.year))
				if self.company_contractor_id:
					domain.append(('company_contractor_id', '=', self.company_contractor_id.id))


				pf = self.env['pf.payment'].search(domain, limit=1)
				pf_employee_amount = pf.employee_amount
				pf_employer_amount = pf.employer_amount

				eps_amount = pf.eps_amount
				for admin in pf.admin_charges_ids:

					admin_amount +=admin.amount
				pf_amount_total = pf.amount_total
				list.append({

									'employee_epf': pf_employee_amount,
									'employer_epf': pf_employer_amount,
									'employer_eps': eps_amount,

									'admin_charge': admin_amount,
									'net_epf': pf_amount_total,
									})

				return list

		@api.multi
		def get_head(self):
				
				list = []

				pf_rule = self.env['hr.salary.rule'].search([('related_type','=','pf')])
				for lin  in pf_rule.contribution_line_ids:
					list.append({

										'employee_epf': lin.emloyee_ratio,
										'employer_epf': lin.emloyer_ratio,
										'eps': lin.emloyer_eps_ratio,

										})

				return list





 