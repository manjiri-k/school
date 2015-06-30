from openerp.osv import fields, osv

class school_school(osv.osv):
    _name="school.school"
    
    _columns={'name':fields.char(string='Name of school'),
              'school_id':fields.integer(string='School ID'),
              'cbse':fields.boolean(string="CBSE"),
              'icse':fields.boolean(string="ICSE"),
              'students':fields.one2many('student.student','school_id',string="No. of students"),
              'school_courses':fields.many2many('courses.courses','school_courses_rel','school_id_rel','courses_id_rel',string="List of Courses")
              }
    _defaults={'name':"School 1"
               }
    
    
    
