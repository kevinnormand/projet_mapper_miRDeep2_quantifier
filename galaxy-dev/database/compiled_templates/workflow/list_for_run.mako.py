# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467200915.914424
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/workflow/list_for_run.mako'
_template_uri = 'workflow/list_for_run.mako'
_source_encoding = 'ascii'
_exports = ['title']


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
        shared_by_others = context.get('shared_by_others', UNDEFINED)
        h = context.get('h', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        len = context.get('len', UNDEFINED)
        workflows = context.get('workflows', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<h2>Your workflows</h2>\n\n<ul class="manage-table-actions">\n    <li>\n        <a class="action-button" href="')
        __M_writer(unicode(h.url_for( controller='workflow', action='index' )))
        __M_writer(u'" target="_parent">\n            <span>Switch to workflow management view</span>\n        </a>\n    </li>\n</ul>\n  \n')
        if workflows:
            __M_writer(u'    <table class="manage-table colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n        <tr class="header">\n            <th>Name</th>\n            <th># of Steps</th>\n')
            __M_writer(u'            <th></th>\n        </tr>\n')
            for i, workflow in enumerate( workflows ):
                __M_writer(u'            <tr>\n                <td>\n                    <a href="')
                __M_writer(unicode(h.url_for(controller='workflow', action='run', id=trans.security.encode_id(workflow.id) )))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(h.to_unicode( workflow.name ) )))
                __M_writer(u'</a>\n                    <a id="wf-')
                __M_writer(unicode(i))
                __M_writer(u'-popup" class="popup-arrow" style="display: none;">&#9660;</a>\n                </td>\n                <td>')
                __M_writer(unicode(len(workflow.latest_workflow.steps)))
                __M_writer(u'</td>\n')
                __M_writer(u'            </tr>    \n')
            __M_writer(u'    </table>\n')
        else:
            __M_writer(u'\n    You have no workflows.\n\n')
        __M_writer(u'\n<h2>Workflows shared with you by others</h2>\n\n')
        if shared_by_others:
            __M_writer(u'    <table class="colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n        <tr class="header">\n            <th>Name</th>\n            <th>Owner</th>\n            <th># of Steps</th>\n            <th></th>\n        </tr>\n')
            for i, association in enumerate( shared_by_others ):
                __M_writer(u'            ')
                workflow = association.stored_workflow 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['workflow'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n            <tr>\n                <td>\n                    <a href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='run', id=trans.security.encode_id(workflow.id) )))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(workflow.name )))
                __M_writer(u'</a>\n                    <a id="shared-')
                __M_writer(unicode(i))
                __M_writer(u'-popup" class="popup-arrow" style="display: none;">&#9660;</a>\n                </td>\n                <td>')
                __M_writer(filters.html_escape(unicode(workflow.user.email )))
                __M_writer(u'</td>\n                <td>')
                __M_writer(unicode(len(workflow.latest_workflow.steps)))
                __M_writer(u'</td>\n            </tr>    \n')
            __M_writer(u'    </table>\n')
        else:
            __M_writer(u'\n    No workflows have been shared with you.\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'Workflow home')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 0, "38": 1, "39": 3, "40": 9, "41": 9, "42": 15, "43": 16, "44": 21, "45": 23, "46": 24, "47": 26, "48": 26, "49": 26, "50": 26, "51": 27, "52": 27, "53": 29, "54": 29, "55": 31, "56": 33, "57": 34, "58": 35, "59": 39, "60": 42, "61": 43, "62": 50, "63": 51, "64": 51, "68": 51, "69": 54, "70": 54, "71": 54, "72": 54, "73": 55, "74": 55, "75": 57, "76": 57, "77": 58, "78": 58, "79": 61, "80": 62, "81": 63, "87": 3, "91": 3, "97": 91}, "uri": "workflow/list_for_run.mako", "filename": "templates/webapps/galaxy/workflow/list_for_run.mako"}
__M_END_METADATA
"""
