# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467380797.866281
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/workflow/build_from_current_history.mako'
_template_uri = 'workflow/build_from_current_history.mako'
_source_encoding = 'ascii'
_exports = ['stylesheets', 'javascripts', 'history_item', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7fc15c6f48d0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fc15c6f48d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc15c6f48d0')._populate(_import_ns, [u'render_msg'])
        jobs = _import_ns.get('jobs', context.get('jobs', UNDEFINED))
        warnings = _import_ns.get('warnings', context.get('warnings', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        app = _import_ns.get('app', context.get('app', UNDEFINED))
        util = _import_ns.get('util', context.get('util', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        def history_item(data,creator_disabled=False):
            return render_history_item(context._locals(__M_locals),data,creator_disabled)
        n_ = _import_ns.get('n_', context.get('n_', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        history = _import_ns.get('history', context.get('history', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<p>The following list contains each tool that was run to create the\ndatasets in your current history. Please select those that you wish\nto include in the workflow.</p>\n\n<p>Tools which cannot be run interactively and thus cannot be incorporated\ninto a workflow will be shown in gray.</p>\n\n')
        for warning in warnings:
            __M_writer(u'    <div class="warningmark">')
            __M_writer(unicode(warning))
            __M_writer(u'</div>\n')
        __M_writer(u'\n<form method="post" action="')
        __M_writer(unicode(h.url_for(controller='workflow', action='build_from_current_history')))
        __M_writer(u'">\n<div class=\'form-row\'>\n    <label>')
        __M_writer(unicode(_('Workflow name')))
        __M_writer(u'</label>\n    <input name="workflow_name" type="text" value="Workflow constructed from history \'')
        __M_writer(unicode( util.unicodify( history.name )))
        __M_writer(u'\'" size="60"/>\n</div>\n<p>\n    <input type="submit" value="')
        __M_writer(unicode(_('Create Workflow')))
        __M_writer(u'" />\n    <button id="checkall" style="display: none;">Check all</button>\n    <button id="uncheckall" style="display: none;">Uncheck all</button>\n</p>\n\n<table border="0" cellspacing="0">\n\n    <tr>\n        <th style="width: 47.5%">')
        __M_writer(unicode(_('Tool')))
        __M_writer(u'</th>\n        <th style="width: 5%"></th>\n        <th style="width: 47.5%">')
        __M_writer(unicode(_('History items created')))
        __M_writer(u'</th>\n    </tr>\n\n')
        for job, datasets in jobs.iteritems():
            __M_writer(u'\n    ')

            cls = "toolForm"
            tool_name = "Unknown"
            if hasattr( job, 'is_fake' ) and job.is_fake:
                cls += " toolFormDisabled"
                disabled = True
                tool_name = getattr( job, 'name', tool_name )
            else:
                tool = app.toolbox.get_tool( job.tool_id )
                if tool:
                    tool_name = tool.name
                if tool is None or not( tool.is_workflow_compatible ):
                    cls += " toolFormDisabled"
                    disabled = True
                else:
                    disabled = False
                if tool and tool.version != job.tool_version:
                    tool_version_warning = 'Dataset was created with tool version "%s", but workflow extraction will use version "%s".' % ( job.tool_version, tool.version )
                else:
                    tool_version_warning = ''
            if disabled:
                disabled_why = getattr( job, 'disabled_why', "This tool cannot be used in workflows" )
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tool_version_warning','tool','disabled_why','disabled','tool_name','cls'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n\n    <tr>\n        <td>\n            <div class="')
            __M_writer(unicode(cls))
            __M_writer(u'">\n\n                <div class="toolFormTitle">')
            __M_writer(unicode(tool_name))
            __M_writer(u'</div>\n                <div class="toolFormBody">\n')
            if disabled:
                __M_writer(u'                        <div style="font-style: italic; color: gray">')
                __M_writer(unicode(disabled_why))
                __M_writer(u'</div>\n')
            else:
                __M_writer(u'                        <div><input type="checkbox" name="job_ids" value="')
                __M_writer(unicode(job.id))
                __M_writer(u'" checked="true" />Include "')
                __M_writer(unicode(tool_name))
                __M_writer(u'" in workflow</div>\n')
                if tool_version_warning:
                    __M_writer(u'                            ')
                    __M_writer(unicode( render_msg( tool_version_warning, status="warning" ) ))
                    __M_writer(u'\n')
            __M_writer(u'                </div>\n            </div>\n        </td>\n        <td style="text-align: center;">\n            &#x25B6;\n        </td>\n        <td>\n')
            for _, data in datasets:
                __M_writer(u'                <div>')
                __M_writer(unicode(history_item( data, disabled )))
                __M_writer(u'</div>\n')
            __M_writer(u'        </td>\n    </tr>\n\n')
        __M_writer(u'\n</table>\n\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc15c6f48d0')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(h.css( 'history', 'base' )))
        __M_writer(u'\n    <style type="text/css">\n    div.toolForm{\n        margin-top: 10px;\n        margin-bottom: 10px;\n    }\n    .list-item.dataset.history-content {\n        padding: 8px 10px;\n    }\n    .list-item.dataset.history-content .title-bar {\n        cursor: auto;\n    }\n    input[type="checkbox"].as-input {\n        margin-left: 8px;\n    }\n    th {\n        border-bottom: solid black 1px;\n    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc15c6f48d0')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n    $(function() {\n        $("#checkall").click( function() {\n            $("input[type=checkbox]").attr( \'checked\', true );\n            return false;\n        }).show();\n        $("#uncheckall").click( function() {\n            $("input[type=checkbox]").attr( \'checked\', false );\n            return false;\n        }).show();\n    });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_history_item(context,data,creator_disabled=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc15c6f48d0')._populate(_import_ns, [u'render_msg'])
        disabled = _import_ns.get('disabled', context.get('disabled', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if data.state in [ "no state", "", None ]:
            __M_writer(u'        ')
            data_state = "queued" 
            
            __M_writer(u'\n')
        else:
            __M_writer(u'        ')
            data_state = data.state 
            
            __M_writer(u'\n')
        __M_writer(u'    ')
        encoded_id = trans.app.security.encode_id( data.id ) 
        
        __M_writer(u'\n    <table cellpadding="0" cellspacing="0" border="0" width="100%">\n        <tr>\n            <td>\n                <div class="list-item dataset history-content state-')
        __M_writer(unicode( data.state ))
        __M_writer(u'" id="dataset-')
        __M_writer(unicode( encoded_id ))
        __M_writer(u'">\n                    <div class="title-bar clear">\n                        <div class="title">\n                            <span class="hid">')
        __M_writer(unicode(data.hid))
        __M_writer(u'</span>\n                            <span class="name">')
        __M_writer(unicode(data.display_name()))
        __M_writer(u'</span>\n                        </div>\n                    </div>\n')
        if disabled:
            __M_writer(u'                        <input type="checkbox" id="as-input-')
            __M_writer(unicode( encoded_id ))
            __M_writer(u'" class="as-input"\n                               name="')
            __M_writer(unicode(data.history_content_type))
            __M_writer(u'_ids" value="')
            __M_writer(unicode(data.hid))
            __M_writer(u'" checked="true" />\n                        <label for="as-input-')
            __M_writer(unicode( encoded_id ))
            __M_writer(u'" >')
            __M_writer(unicode(_('Treat as input dataset')))
            __M_writer(u'</label>\n')
        __M_writer(u'                </div>\n            </td>\n        </tr>\n    </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fc15c6f48d0')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        __M_writer(u'Extract workflow from history')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 2, "29": 0, "48": 1, "49": 2, "50": 4, "54": 4, "55": 6, "56": 28, "57": 44, "58": 72, "59": 81, "60": 82, "61": 82, "62": 82, "63": 84, "64": 85, "65": 85, "66": 87, "67": 87, "68": 88, "69": 88, "70": 91, "71": 91, "72": 99, "73": 99, "74": 101, "75": 101, "76": 104, "77": 105, "78": 106, "104": 128, "105": 132, "106": 132, "107": 134, "108": 134, "109": 136, "110": 137, "111": 137, "112": 137, "113": 138, "114": 139, "115": 139, "116": 139, "117": 139, "118": 139, "119": 140, "120": 141, "121": 141, "122": 141, "123": 144, "124": 151, "125": 152, "126": 152, "127": 152, "128": 154, "129": 158, "135": 8, "142": 8, "143": 9, "144": 9, "150": 30, "157": 30, "158": 31, "159": 31, "165": 46, "174": 46, "175": 47, "176": 48, "177": 48, "179": 48, "180": 49, "181": 50, "182": 50, "184": 50, "185": 52, "186": 52, "188": 52, "189": 56, "190": 56, "191": 56, "192": 56, "193": 59, "194": 59, "195": 60, "196": 60, "197": 63, "198": 64, "199": 64, "200": 64, "201": 65, "202": 65, "203": 65, "204": 65, "205": 66, "206": 66, "207": 66, "208": 66, "209": 68, "215": 6, "221": 6, "227": 221}, "uri": "workflow/build_from_current_history.mako", "filename": "templates/webapps/galaxy/workflow/build_from_current_history.mako"}
__M_END_METADATA
"""
