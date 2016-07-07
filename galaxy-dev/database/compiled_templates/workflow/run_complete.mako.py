# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467201194.951106
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/workflow/run_complete.mako'
_template_uri = 'workflow/run_complete.mako'
_source_encoding = 'ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        scheduled = context.get('scheduled', UNDEFINED)
        workflow = context.get('workflow', UNDEFINED)
        h = context.get('h', UNDEFINED)
        invocations = context.get('invocations', UNDEFINED)
        util = context.get('util', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<div class="donemessagelarge">\n')
        if scheduled:
            __M_writer(u'    Successfully ran workflow "')
            __M_writer(filters.html_escape(unicode(util.unicodify( workflow.name ))))
            __M_writer(u'". The following datasets have been added to the queue:\n')
            for invocation in invocations:
                __M_writer(u'        <div class="workflow-invocation-complete">\n')
                if invocation['new_history']:
                    __M_writer(u'                ')

                    encoded_new_history = trans.security.encode_id(invocation['new_history'].id)
                                    
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['encoded_new_history'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n                <p>These datasets will appear in a new history:\n                <a class=\'new-history-link\' data-history-id="')
                    __M_writer(filters.html_escape(unicode(encoded_new_history)))
                    __M_writer(u'" target=\'_top\' href="')
                    __M_writer(h.url_for( controller='history', action='switch_to_history', hist_id=encoded_new_history ) )
                    __M_writer(u'">\n                    \'')
                    __M_writer(filters.html_escape(unicode(h.to_unicode(invocation['new_history'].name))))
                    __M_writer(u"'.\n                </a></p>\n")
                __M_writer(u'            <div style="padding-left: 10px;">\n')
                for step_outputs in invocation['outputs'].itervalues():
                    for data in step_outputs.itervalues():
                        if not invocation['new_history'] or data.history == invocation['new_history']:
                            __M_writer(u'                            <p><strong>')
                            __M_writer(filters.html_escape(unicode(data.hid)))
                            __M_writer(u'</strong>: ')
                            __M_writer(filters.html_escape(unicode(util.unicodify( data.name ))))
                            __M_writer(u'</p>\n')
                __M_writer(u'            </div>\n        </div>\n')
        else:
            __M_writer(u'    The requested workflows have been queued and datasets will appear\n    as jobs are created - you will need to refresh your history panel\n    to see these.\n')
        __M_writer(u'</div>\n\n<script type="text/javascript">\n    if(parent.Galaxy && parent.Galaxy.currHistoryPanel){\n        parent.Galaxy.currHistoryPanel.refreshContents();\n    }\n    $(\'a.new-history-link\').click(function(event){\n        if(parent.Galaxy && parent.Galaxy.currHistoryPanel){\n            event.preventDefault();\n            parent.Galaxy.currHistoryPanel.switchToHistory($(this).data(\'history-id\'));\n        }\n    });\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 2, "38": 1, "39": 2, "40": 5, "41": 6, "42": 6, "43": 6, "44": 7, "45": 8, "46": 9, "47": 10, "48": 10, "54": 12, "55": 14, "56": 14, "57": 14, "58": 14, "59": 15, "60": 15, "61": 18, "62": 19, "63": 20, "64": 21, "65": 22, "66": 22, "67": 22, "68": 22, "69": 22, "70": 26, "71": 29, "72": 30, "73": 34, "79": 73}, "uri": "workflow/run_complete.mako", "filename": "templates/webapps/galaxy/workflow/run_complete.mako"}
__M_END_METADATA
"""
