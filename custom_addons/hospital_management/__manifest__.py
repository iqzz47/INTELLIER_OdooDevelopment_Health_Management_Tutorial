{
    'name': 'Hospital Management',
    'version': '1.2',
    'category': 'Hospital',
    'summary': 'Hospital management system',
    'description': """Hospital management system
    """,
    'depends': ['mail','product'],
    'data': ['security/ir.model.access.csv','data/patient_tag_data.xml','data/patient.tag.csv','wizard/cancel_appointment_view.xml','views/menu.xml','views/patient_view.xml','views/female_patient_view.xml','views/appointment_view.xml','views/patient_tag_view.xml'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': -100,
    'assets': {},
    'license': 'LGPL-3',


}
