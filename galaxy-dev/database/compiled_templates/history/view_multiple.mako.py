# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467013896.431854
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/history/view_multiple.mako'
_template_uri = 'history/view_multiple.mako'
_source_encoding = 'ascii'
_exports = ['stylesheets', 'javascript_app', 'center_panel', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'galaxy_client', context._clean_inheritance_tokens(), templateuri=u'/galaxy_client_app.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'galaxy_client')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode( parent.stylesheets() ))
        __M_writer(u'\n    <style type="text/css">\n    /* reset */\n    html, body {\n        margin: 0px;\n        padding: 0px;\n    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_app(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        include_deleted_histories = context.get('include_deleted_histories', UNDEFINED)
        galaxy_client = _mako_get_namespace(context, 'galaxy_client')
        limit = context.get('limit', UNDEFINED)
        histories = context.get('histories', UNDEFINED)
        order = context.get('order', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<script type="text/javascript">\ndefine( \'app\', function(){\n    require([\n        \'mvc/history/history-model\',\n        \'mvc/history/multi-panel\'\n    ], function( HISTORY_MODEL, MULTI_HISTORY ){\n        $(function(){\n            histories = new HISTORY_MODEL.HistoryCollection( bootstrapped.histories, {\n                includeDeleted  : bootstrapped.includingDeleted,\n                order           : bootstrapped.order,\n                currentHistoryId: \'')
        __M_writer(unicode(histories[0][ "id" ]))
        __M_writer(u"'\n            });\n\n            multipanel = new MULTI_HISTORY.MultiPanelColumns({\n                el                          : $( '#center' ).get(0),\n                histories                   : histories,\n                perPage                     : bootstrapped.limit\n            }).render( 0 );\n        });\n    });\n});\n</script>\n")
        __M_writer(unicode( galaxy_client.load( app='app', histories=histories,
    includingDeleted=include_deleted_histories, order=order, limit=limit ) ))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(_( 'Histories' )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 3, "29": 0, "34": 1, "35": 2, "36": 3, "37": 7, "38": 19, "39": 23, "40": 50, "46": 10, "51": 10, "52": 11, "53": 11, "59": 25, "68": 25, "69": 36, "70": 36, "71": 48, "73": 49, "79": 23, "88": 5, "93": 5, "94": 6, "95": 6, "101": 95}, "uri": "history/view_multiple.mako", "filename": "templates/webapps/galaxy/history/view_multiple.mako"}
__M_END_METADATA
"""
