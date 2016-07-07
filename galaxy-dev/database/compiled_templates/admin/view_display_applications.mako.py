# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1466779954.587911
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/admin/view_display_applications.mako'
_template_uri = 'admin/view_display_applications.mako'
_source_encoding = 'ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f8dcd36f410', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8dcd36f410')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8dcd36f410')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        display_applications = _import_ns.get('display_applications', context.get('display_applications', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if message:
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">There are currently ')
        __M_writer(unicode(len( display_applications )))
        __M_writer(u' <a class="icon-btn" href="')
        __M_writer(unicode( h.url_for( controller='admin', action='reload_display_application' ) ))
        __M_writer(u'" title="Reload all display applications" data-placement="bottom">\n                        <span class="fa fa-refresh"></span>\n                    </a> display applications loaded.</div>\n    <div class="toolFormBody">\n        <table class="manage-table colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n            <tr>\n                <th bgcolor="#D8D8D8">Reload</th>\n                <th bgcolor="#D8D8D8">Name</th>\n                <th bgcolor="#D8D8D8">ID</th>\n                <th bgcolor="#D8D8D8">Version</th>\n                <th bgcolor="#D8D8D8">Links</th>\n                <th bgcolor="#D8D8D8">Filename</th>\n            </tr>\n            ')
        ctr = 0 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ctr'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        for display_app in display_applications.values():
            if ctr % 2 == 1:
                __M_writer(u'                    <tr class="odd_row">\n')
            else:
                __M_writer(u'                    <tr class="tr">\n')
            __M_writer(u'                    <td>\n                        <a class="icon-btn" href="')
            __M_writer(unicode( h.url_for( controller='admin', action='reload_display_application', id=display_app.id ) ))
            __M_writer(u'" title="Reload ')
            __M_writer(filters.html_escape(unicode( display_app.name )))
            __M_writer(u' display application" data-placement="bottom">\n                            <span class="fa fa-refresh"></span>\n                        </a>\n                    </td>\n                    <td>')
            __M_writer(filters.html_escape(unicode( display_app.name )))
            __M_writer(u'</td>\n                    <td>')
            __M_writer(filters.html_escape(unicode( display_app.id )))
            __M_writer(u'</td>\n                    <td>')
            __M_writer(filters.html_escape(unicode( display_app.version )))
            __M_writer(u'</td>\n                    <td><ul>\n')
            for link in display_app.links.values():
                __M_writer(u'                            <li>')
                __M_writer(filters.html_escape(unicode(  link.name )))
                __M_writer(u'</li>\n')
            __M_writer(u'                    </ul></td>\n                    <td>')
            __M_writer(filters.html_escape(unicode( display_app._filename )))
            __M_writer(u'</td>\n                </tr>\n                ')
            ctr += 1 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ctr'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        __M_writer(u'        </table>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 2, "29": 0, "42": 1, "43": 2, "44": 4, "45": 5, "46": 5, "47": 5, "48": 7, "49": 9, "50": 9, "51": 9, "52": 9, "53": 22, "57": 22, "58": 23, "59": 24, "60": 25, "61": 26, "62": 27, "63": 29, "64": 30, "65": 30, "66": 30, "67": 30, "68": 34, "69": 34, "70": 35, "71": 35, "72": 36, "73": 36, "74": 38, "75": 39, "76": 39, "77": 39, "78": 41, "79": 42, "80": 42, "81": 44, "85": 44, "86": 46, "92": 86}, "uri": "admin/view_display_applications.mako", "filename": "templates/webapps/galaxy/admin/view_display_applications.mako"}
__M_END_METADATA
"""
