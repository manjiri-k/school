from openerp.osv import fields, osv

class courses_courses(osv.osv):
    _name='courses.courses'
    
    _columns={'name':fields.char(string='Name of course',size=20),
              'duration':fields.integer(string="Duration"),
              'assignments':fields.integer(string="Assignments"),
              'attach':fields.binary("Bianry field"),
              'courses_school':fields.many2many('school.school','school_courses_rel','courses_id_rel','school_id_rel',string="List of Courses"),
              
              }