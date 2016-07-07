# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1466779956.793607
_enable_loop = True
_template_filename = 'templates/admin/view_datatypes_registry.mako'
_template_uri = 'admin/view_datatypes_registry.mako'
_source_encoding = 'ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f8dcd1d5290', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8dcd1d5290')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8dcd1d5290')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if message:
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        __M_writer(u'\n')

        import galaxy.util
        from galaxy.web.base.controller import sort_by_attr, Datatype
        ctr = 0
        datatypes = []
        for elem in trans.app.datatypes_registry.datatype_elems:
            # Build a list of objects that can be sorted.
            extension = elem.get( 'extension', None )
            dtype = elem.get( 'type', None )
            type_extension = elem.get( 'type_extension', None )
            mimetype = elem.get( 'mimetype', None )
            display_in_upload = galaxy.util.string_as_bool( elem.get( 'display_in_upload', False ) )
            datatypes.append( Datatype( extension, dtype, type_extension, mimetype, display_in_upload ) )
        sorted_datatypes = sort_by_attr( datatypes, 'extension' )
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['type_extension','mimetype','extension','ctr','Datatype','dtype','elem','display_in_upload','sorted_datatypes','sort_by_attr','datatypes','galaxy'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n<div class="toolForm">\n    <div class="toolFormTitle">Current data types registry contains ')
        __M_writer(unicode(len( sorted_datatypes )))
        __M_writer(u' data types</div>\n    <div class="toolFormBody">\n        <table class="manage-table colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n            <tr>\n                <th bgcolor="#D8D8D8">Extension</th>\n                <th bgcolor="#D8D8D8">Type</th>\n                <th bgcolor="#D8D8D8">Mimetype</th>\n                <th bgcolor="#D8D8D8">Display in upload</th>\n            </tr>\n')
        for datatype in sorted_datatypes:
            if ctr % 2 == 1:
                __M_writer(u'                    <tr class="odd_row">\n')
            else:
                __M_writer(u'                    <tr class="tr">\n')
            __M_writer(u'                    <td>')
            __M_writer(filters.html_escape(unicode(datatype.extension)))
            __M_writer(u'</td>\n                    <td>')
            __M_writer(filters.html_escape(unicode(datatype.dtype)))
            __M_writer(u'</td>\n                    <td>\n')
            if datatype.mimetype:
                __M_writer(u'                            ')
                __M_writer(filters.html_escape(unicode(datatype.mimetype)))
                __M_writer(u'\n')
            __M_writer(u'                    </td>\n                    <td>\n')
            if datatype.display_in_upload:
                __M_writer(u'                            ')
                __M_writer(filters.html_escape(unicode(datatype.display_in_upload)))
                __M_writer(u'\n')
            __M_writer(u'                    </td>\n                </tr>\n                ')
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
{"source_encoding": "ascii", "line_map": {"23": 2, "29": 0, "41": 1, "42": 2, "43": 4, "44": 5, "45": 5, "46": 5, "47": 7, "48": 8, "66": 22, "67": 25, "68": 25, "69": 34, "70": 35, "71": 36, "72": 37, "73": 38, "74": 40, "75": 40, "76": 40, "77": 41, "78": 41, "79": 43, "80": 44, "81": 44, "82": 44, "83": 46, "84": 48, "85": 49, "86": 49, "87": 49, "88": 51, "89": 53, "93": 53, "94": 55, "100": 94}, "uri": "admin/view_datatypes_registry.mako", "filename": "templates/admin/view_datatypes_registry.mako"}
__M_END_METADATA
"""
