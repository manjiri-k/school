from openerp.osv import fields, osv

class student_student(osv.osv):
    _name='student.student'
    
    _columns={'name123':fields.char(string='Name of student',size=20),
              'date123':fields.date(string="Date"),
              'datetime123':fields.datetime(string="Date time"),
              'marks':fields.float(string="Marks",digits=(4,2)),
              'description':fields.text(string="Description"),
              'gender':fields.selection(string="Gender",selection=[('1','Male'),('ad','Female')]),
              'school_id':fields.many2one('school.school',string='School'),
              #'school_id1':fields.many2one('school.school',string='School fake'),
              'library':fields.many2one('lib.lib',string="Library")
            }
    
    _defaults={'date123':fields.date.today(),
               'datetime123':fields.datetime.now(),
               
               }