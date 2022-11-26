{
    'name': "Zakaria web module",
    'summary': '',
    'description': """
    """,
    'author': "SARL ARTEC-INT",
    'category': '',
    'version': '0.1',

    'depends': ['base', 'mail', 'contacts', 'product', 'website_sale', 'web', 'crm'],

    'assets': {
        'web.assets_qweb': [],
        'web.assets_frontend': [],
        'web.assets_common': [
            'artec_webbase/static/src/css/visits_style.css',
        ],
    },

    'data': [
        'views/web_home_page.xml',
        'views/web_product_list.xml',
        'views/web_product_page.xml',
        'views/crm_lead_view_form.xml',
    ],
}
