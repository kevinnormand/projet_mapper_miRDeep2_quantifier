# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1466779946.545019
_enable_loop = True
_template_filename = 'templates/admin/view_data_tables_registry.mako'
_template_uri = 'admin/view_data_tables_registry.mako'
_source_encoding = 'ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f8dcd2e1990', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8dcd2e1990')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8dcd2e1990')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if message:
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        __M_writer(u'\n')

        ctr = 0
        sorted_data_tables = sorted( trans.app.tool_data_tables.get_tables().items() )
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['sorted_data_tables','ctr'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n<div class="toolForm">\n    <div class="toolFormTitle">Current data table registry contains ')
        __M_writer(unicode(len( sorted_data_tables )))
        __M_writer(u' data tables</div>\n    <div class="toolFormBody">\n        <table class="manage-table colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n            <tr>\n                <th bgcolor="#D8D8D8">Name</th>\n                <th bgcolor="#D8D8D8">Filename</th>\n                <th bgcolor="#D8D8D8">Tool data path</th>\n                <th bgcolor="#D8D8D8">Errors</th>\n            </tr>\n')
        for data_table_elem_name, data_table in sorted_data_tables:
            if ctr % 2 == 1:
                __M_writer(u'                    <tr class="odd_row">\n')
            else:
                __M_writer(u'                    <tr class="tr">\n')
            __M_writer(u'                    <td><a href="')
            __M_writer(unicode( h.url_for( controller="data_manager", action="manage_data_table", table_name=data_table.name ) ))
            __M_writer(u'">')
            __M_writer(unicode(data_table.name))
            __M_writer(u'</a></td>\n')
            for i, ( filename, file_dict ) in enumerate( data_table.filenames.iteritems() ):
                if i > 0:
                    __M_writer(u'                            <tr><td></td>\n')
                __M_writer(u'                        <td>')
                __M_writer(filters.html_escape(unicode( filename )))
                __M_writer(u'</td>\n                        <td>')
                __M_writer(filters.html_escape(unicode( file_dict.get( 'tool_data_path' ) )))
                __M_writer(u'</td>\n                        <td>\n')
                if not file_dict.get( 'found' ):
                    __M_writer(u'                                file missing\n')
                for error in file_dict.get( 'errors', [] ):
                    __M_writer(u'                                ')
                    __M_writer(filters.html_escape(unicode( error )))
                    __M_writer(u' <br/>\n')
                __M_writer(u'                        </td>\n                        </tr>\n')
            __M_writer(u'                ')
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
{"source_encoding": "ascii", "line_map": {"23": 2, "29": 0, "44": 1, "45": 2, "46": 4, "47": 5, "48": 5, "49": 5, "50": 7, "51": 8, "58": 11, "59": 14, "60": 14, "61": 23, "62": 24, "63": 25, "64": 26, "65": 27, "66": 29, "67": 29, "68": 29, "69": 29, "70": 29, "71": 30, "72": 31, "73": 32, "74": 34, "75": 34, "76": 34, "77": 35, "78": 35, "79": 37, "80": 38, "81": 40, "82": 41, "83": 41, "84": 41, "85": 43, "86": 46, "87": 46, "91": 46, "92": 48, "98": 92}, "uri": "admin/view_data_tables_registry.mako", "filename": "templates/admin/view_data_tables_registry.mako"}
__M_END_METADATA
"""
