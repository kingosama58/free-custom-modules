{
    'name': 'AT Odoo 18 Community Accounting',
    'version': '1.0.3',
    'category': 'Accounting',
    'summary': 'Accounting Reports, Asset Management and Budget, Recurring Payments, '
               'Lock Dates, Fiscal Year, Accounting Dashboard, Financial Reports, '
               'Customer Follow up Management, Bank Statement Import',
    'description': 'Odoo 18 Financial Reports, Asset Management and '
                   'Budget, Financial Reports, Recurring Payments, '
                   'Bank Statement Import, Customer Follow Up Management,'
                   'Account Lock Date, Accounting Dashboard',
    'live_test_url': 'https://www.youtube.com/c/OdooMates',
    'sequence': '1',
    'sequence': '1',
    'website': 'https://wa.me/966553493285',
    'author': 'AccountTechs',
    'maintainer': 'Odoo Mates, Walnut Software Solutions',
    'license': 'LGPL-3',
    'support': 'osamahalnihmi@gmail.com',
    'depends': [
        'at_accounting_pdf_reports',
        'at_account_asset',
        'at_account_budget',
        'at_fiscal_year',
        'at_recurring_payments',
        'at_account_daily_reports',
        'at_account_followup',
    ],
    'data': [
        'security/group.xml',
        'views/menu.xml',
        'views/settings.xml',
        'views/account_group.xml',
        'views/account_tag.xml',
        'views/res_partner.xml',
        'views/account_bank_statement.xml',
        'views/payment_method.xml',
        'views/reconciliation.xml',
        'views/account_journal.xml',
    ],
    'application': True,
    'images': ['static/description/banner.gif'],
}

