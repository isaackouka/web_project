from odoo.http import request
from odoo import http, tools
import json
from odoo.addons.website.controllers.main import QueryURL
from odoo.osv import expression
from odoo.addons.website.models.ir_http import sitemap_qs2dom
from odoo.addons.http_routing.models.ir_http import slug
from werkzeug.exceptions import Forbidden, NotFound


class WebController(http.Controller):

    @http.route('/', auth='public', type='http', website=True, csrf=False)
    def home_page(self,**kw):
        category = http.request.env['product.public.category'].sudo().search([('product_tmpl_ids','!=',False)])
        return request.render("artec_webbase.artec_web_home",{
            "category":category
        })

    @http.route('/categ/<int:categ_id>',  auth='public', type='http', website=True, csrf=False)
    def product_by_categ(self, categ_id):
        products = http.request.env['product.template'].sudo().search_read([('public_categ_ids','in',categ_id)],['id','name','image_1920','list_price'])
        return request.render("artec_webbase.website",{
            "products":products
        })

    @http.route('/product/<int:product_id>',  auth='public', type='http', website=True, csrf=False)
    def product_page(self, product_id):
        products = http.request.env['product.template'].sudo().search_read([('id','=',product_id)],['id','name','image_1920'])
        return request.render("artec_webbase.product_page",{
            "products":products
        })

    @http.route('/product/send/', auth='public', type='http', website=True, csrf=True)
    def get_data(self, **kw):
        errors = list()
        list_product = []
        if kw:
            for x in kw.items():
                try:
                    list_product.append(int(x[0]))
                except:
                    pass
            products = http.request.env['product.template'].sudo().search([('id','in',list_product)])
            value={
                'name':'Command'+' '+kw.get('name'),
                'phone':kw.get('phone'),
                'email_from':kw.get('email_from'),
                'description':kw.get('description'),
                'product_ids': products
            }
            if errors == []:
                new_partner = http.request.env['crm.lead'].sudo().create(value)
                return request.render("artec_webbase.artec_web_home")
            else:
                return "<div class='alert alert-warning' role='alert'>ERROR : INVALIDE DATA </div>"
        else:
            return "<div class='alert alert-warning' role='alert'> SOMETHING WENT WRONG </div>"


    # def _get_pricelist_context(self):
    #     pricelist_context = dict(request.env.context)
    #     pricelist = False
    #     if not pricelist_context.get('pricelist'):
    #         pricelist = request.website.get_current_pricelist()
    #         pricelist_context['pricelist'] = pricelist.id
    #     else:
    #         pricelist = request.env['product.pricelist'].browse(pricelist_context['pricelist'])

    #     return pricelist_context, pricelist

    # def _get_search_order(self, post):
    #     # OrderBy will be parsed in orm and so no direct sql injection
    #     # id is added to be sure that order is a unique sort key
    #     order = post.get('order') or 'website_sequence ASC'
    #     return 'is_published desc, %s, id desc' % order

    # def _get_search_domain(self, search, category, attrib_values, search_in_description=True):
    #     domains = [request.website.sale_product_domain()]
    #     if search:
    #         for srch in search.split(" "):
    #             subdomains = [
    #                 [('name', 'ilike', srch)],
    #                 [('product_variant_ids.default_code', 'ilike', srch)]
    #             ]
    #             if search_in_description:
    #                 subdomains.append([('description', 'ilike', srch)])
    #                 subdomains.append([('description_sale', 'ilike', srch)])
    #             domains.append(expression.OR(subdomains))

    #     if category:
    #         domains.append([('public_categ_ids', 'child_of', int(category))])

    #     if attrib_values:
    #         attrib = None
    #         ids = []
    #         for value in attrib_values:
    #             if not attrib:
    #                 attrib = value[0]
    #                 ids.append(value[1])
    #             elif value[0] == attrib:
    #                 ids.append(value[1])
    #             else:
    #                 domains.append([('attribute_line_ids.value_ids', 'in', ids)])
    #                 attrib = value[0]
    #                 ids = [value[1]]
    #         if attrib:
    #             domains.append([('attribute_line_ids.value_ids', 'in', ids)])

    #     return expression.AND(domains)

    # def sitemap_shop(env, rule, qs):
    #     if not qs or qs.lower() in '/shop':
    #         yield {'loc': '/shop'}

    #     Category = env['product.public.category']
    #     dom = sitemap_qs2dom(qs, '/shop/category', Category._rec_name)
    #     dom += env['website'].get_current_website().website_domain()
    #     for cat in Category.search(dom):
    #         loc = '/shop/category/%s' % slug(cat)
    #         if not qs or qs.lower() in loc:
    #             yield {'loc': loc}

    # # @http.route('/categ/<int:category>',  auth='public', type='http', website=True, csrf=False, sitemap=sitemap_shop)
    # def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
    #     add_qty = int(post.get('add_qty', 1))
    #     try:
    #         min_price = float(min_price)
    #     except ValueError:
    #         min_price = 0
    #     try:
    #         max_price = float(max_price)
    #     except ValueError:
    #         max_price = 0

    #     Category = request.env['product.public.category']
    #     if category:
    #         category = Category.search([('id', '=', int(category))], limit=1)
    #         if not category or not category.can_access_from_current_website():
    #             raise NotFound()
    #     else:
    #         category = Category

    #     if ppg:
    #         try:
    #             ppg = int(ppg)
    #             post['ppg'] = ppg
    #         except ValueError:
    #             ppg = False
    #     if not ppg:
    #         ppg = request.env['website'].get_current_website().shop_ppg or 20

    #     ppr = request.env['website'].get_current_website().shop_ppr or 4

    #     attrib_list = request.httprequest.args.getlist('attrib')
    #     attrib_values = [[int(x) for x in v.split("-")] for v in attrib_list if v]
    #     attributes_ids = {v[0] for v in attrib_values}
    #     attrib_set = {v[1] for v in attrib_values}

    #     keep = QueryURL('/shop', category=category and int(category), search=search, attrib=attrib_list, min_price=min_price, max_price=max_price, order=post.get('order'))

    #     pricelist_context, pricelist = self._get_pricelist_context()

    #     request.context = dict(request.context, pricelist=pricelist.id, partner=request.env.user.partner_id)

    #     filter_by_price_enabled = request.website.is_view_active('website_sale.filter_products_price')
    #     if filter_by_price_enabled:
    #         company_currency = request.website.company_id.currency_id
    #         conversion_rate = request.env['res.currency']._get_conversion_rate(company_currency, pricelist.currency_id, request.website.company_id, fields.Date.today())
    #     else:
    #         conversion_rate = 1

    #     url = "/shop"
    #     if search:
    #         post["search"] = search
    #     if attrib_list:
    #         post['attrib'] = attrib_list

    #     options = {
    #         'displayDescription': True,
    #         'displayDetail': True,
    #         'displayExtraDetail': True,
    #         'displayExtraLink': True,
    #         'displayImage': True,
    #         'allowFuzzy': not post.get('noFuzzy'),
    #         'category': str(category.id) if category else None,
    #         'min_price': min_price / conversion_rate,
    #         'max_price': max_price / conversion_rate,
    #         'attrib_values': attrib_values,
    #         'display_currency': pricelist.currency_id,
    #     }
    #     # No limit because attributes are obtained from complete product list
    #     product_count, details, fuzzy_search_term = request.website._search_with_fuzzy("products_only", search,
    #         limit=None, order=self._get_search_order(post), options=options)
    #     search_product = details[0].get('results', request.env['product.template']).with_context(bin_size=True)

    #     filter_by_price_enabled = request.website.is_view_active('website_sale.filter_products_price')
    #     if filter_by_price_enabled:
    #         # TODO Find an alternative way to obtain the domain through the search metadata.
    #         Product = request.env['product.template'].with_context(bin_size=True)
    #         domain = self._get_search_domain(search, category, attrib_values)

    #         # This is ~4 times more efficient than a search for the cheapest and most expensive products
    #         from_clause, where_clause, where_params = Product._where_calc(domain).get_sql()
    #         query = f"""
    #             SELECT COALESCE(MIN(list_price), 0) * {conversion_rate}, COALESCE(MAX(list_price), 0) * {conversion_rate}
    #               FROM {from_clause}
    #              WHERE {where_clause}
    #         """
    #         request.env.cr.execute(query, where_params)
    #         available_min_price, available_max_price = request.env.cr.fetchone()

    #         if min_price or max_price:
    #             # The if/else condition in the min_price / max_price value assignment
    #             # tackles the case where we switch to a list of products with different
    #             # available min / max prices than the ones set in the previous page.
    #             # In order to have logical results and not yield empty product lists, the
    #             # price filter is set to their respective available prices when the specified
    #             # min exceeds the max, and / or the specified max is lower than the available min.
    #             if min_price:
    #                 min_price = min_price if min_price <= available_max_price else available_min_price
    #                 post['min_price'] = min_price
    #             if max_price:
    #                 max_price = max_price if max_price >= available_min_price else available_max_price
    #                 post['max_price'] = max_price

    #     website_domain = request.website.website_domain()
    #     categs_domain = [('parent_id', '=', False)] + website_domain
    #     if search:
    #         search_categories = Category.search([('product_tmpl_ids', 'in', search_product.ids)] + website_domain).parents_and_self
    #         categs_domain.append(('id', 'in', search_categories.ids))
    #     else:
    #         search_categories = Category
    #     categs = Category.search(categs_domain)

    #     if category:
    #         url = "/shop/category/%s" % slug(category)

    #     pager = request.website.pager(url=url, total=product_count, page=page, step=ppg, scope=7, url_args=post)
    #     offset = pager['offset']
    #     products = search_product[offset:offset + ppg]

    #     ProductAttribute = request.env['product.attribute']
    #     if products:
    #         # get all products without limit
    #         attributes = ProductAttribute.search([
    #             ('product_tmpl_ids', 'in', search_product.ids),
    #             ('visibility', '=', 'visible'),
    #         ])
    #     else:
    #         attributes = ProductAttribute.browse(attributes_ids)

    #     layout_mode = request.session.get('website_sale_shop_layout_mode')
    #     if not layout_mode:
    #         if request.website.viewref('website_sale.products_list_view').active:
    #             layout_mode = 'list'
    #         else:
    #             layout_mode = 'grid'

    #     values = {
    #         'search': fuzzy_search_term or search,
    #         'original_search': fuzzy_search_term and search,
    #         'category': category,
    #         'attrib_values': attrib_values,
    #         'attrib_set': attrib_set,
    #         'pager': pager,
    #         'pricelist': pricelist,
    #         'add_qty': add_qty,
    #         'products': search_product,
    #         'search_count': product_count,  # common for all searchbox
    #         'ppg': ppg,
    #         'ppr': ppr,
    #         'categories': categs,
    #         'attributes': attributes,
    #         'keep': keep,
    #         'search_categories_ids': search_categories.ids,
    #         'layout_mode': layout_mode,
    #     }
    #     if filter_by_price_enabled:
    #         values['min_price'] = min_price or available_min_price
    #         values['max_price'] = max_price or available_max_price
    #         values['available_min_price'] = tools.float_round(available_min_price, 2)
    #         values['available_max_price'] = tools.float_round(available_max_price, 2)
    #     if category:
    #         values['main_object'] = category
    #     return request.render("artec_webbase.website", {"search_product":search_product})
