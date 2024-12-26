# -*- coding: utf-8 -*-
{
    'name': "Skab.custmodule",
    
    'summary': " انشاء مجموعات خاصة لشركات المقاولات وتخصيص صلاحيات مرتبطة بطبيعة هذا النشاط",
    
    'description': 
    """

انشاء مجموعات خاصة لشركات المقاولات وتخصيص صلاحيات مرتبطة بطبيعة هذا النشاط
    """,
    
    'author': "Real World Problem Solution Techniques (RWPST)",
    'website': "https://ads.rwpst.online/",
    
    # Categories can be used to filter modules in modules listing
    'category': 'Field Service',
    'version': '1.0',
    
    # any module necessary for this one to work correctly
    'depends': ['base','calendar'],

    # always loaded
    'data': [

        'security/group.xml',
#        'security/ir.model.access.csv'


    ],
   # 'assets': {
    #    'web.assets_backend': [
     #       'skab_custmodule/static/src/js/calendar_filter_override.js',
      #  ],
    },
    # only loaded in demonstration mode
    'demo': [
#        'demo/demo.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
