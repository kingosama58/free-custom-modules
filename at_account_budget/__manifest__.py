{
    'name': 'AT- Odoo 18 Budget Management',
    'author': 'Odoo Mates, Odoo SA',
    'category': 'Accounting',
    'version': '1.0.1',
    'description': """Use budgets to compare actual with expected revenues and costs""",
    'summary': 'Odoo 18 Budget Management',
    'sequence': 10,
    'website': 'https://wa.me/966553493285',
    'depends': ['account'],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/account_analytic_account_views.xml',
        'views/account_budget_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'images': ['static/description/banner.gif'],
    'demo': ['data/account_budget_demo.xml'],
}
