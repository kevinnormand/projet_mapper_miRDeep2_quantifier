# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467200721.936965
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/workflow/list.mako'
_template_uri = 'workflow/list.mako'
_source_encoding = 'ascii'
_exports = ['init', 'center_panel', 'title']


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
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view="workflow"
        self.message_box_visible=False
        
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        shared_by_others = context.get('shared_by_others', UNDEFINED)
        h = context.get('h', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        len = context.get('len', UNDEFINED)
        workflows = context.get('workflows', UNDEFINED)
        message = context.get('message', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <div style="overflow: auto; height: 100%;">\n        <div class="page-container" style="padding: 10px;">\n')
        if message:
            __M_writer(u'                ')

            try:
                status
            except:
                status = "done"
                            
            
            __M_writer(u'\n                <p />\n                <div class="')
            __M_writer(unicode(status))
            __M_writer(u'message">\n                    ')
            __M_writer(unicode(h.to_unicode( message )))
            __M_writer(u'\n                </div>\n')
        __M_writer(u'\n            <h2>Your workflows</h2>\n\n            <ul class="manage-table-actions">\n                <li>\n                    <a class="action-button" href="')
        __M_writer(unicode(h.url_for( controller='workflow', action='create' )))
        __M_writer(u'">\n                        <img src="')
        __M_writer(unicode(h.url_for('/static/images/silk/add.png')))
        __M_writer(u'" />\n                        <span>Create new workflow</span>\n                    </a>\n                </li>\n                <li>\n                    <a class="action-button" href="')
        __M_writer(unicode(h.url_for( controller='workflow', action='import_workflow' )))
        __M_writer(u'">\n                        <img src="')
        __M_writer(unicode(h.url_for('/static/images/fugue/arrow-090.png')))
        __M_writer(u'" />\n                        <span>Upload or import workflow</span>\n                    </a>\n                </li>\n            </ul>\n\n')
        if workflows:
            __M_writer(u'                <table class="manage-table colored" border="0" cellspacing="0" cellpadding="0" style="width:100%;">\n                    <tr class="header">\n                        <th>Name</th>\n                        <th># of Steps</th>\n')
            __M_writer(u'                        <th></th>\n                    </tr>\n')
            for i, workflow in enumerate( workflows ):
                __M_writer(u'                        <tr>\n                            <td>\n                                <div class="menubutton" style="float: left;" id="wf-')
                __M_writer(unicode(i))
                __M_writer(u'-popup">\n                                ')
                __M_writer(filters.html_escape(unicode(h.to_unicode( workflow.name ) )))
                __M_writer(u'\n                                </div>\n                            </td>\n                            <td>')
                __M_writer(unicode(len(workflow.latest_workflow.steps)))
                __M_writer(u'</td>\n')
                __M_writer(u'                            <td>\n                                <div popupmenu="wf-')
                __M_writer(unicode(i))
                __M_writer(u'-popup">\n                                <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='editor', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'" target="_parent">Edit</a>\n                                <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='root', action='index', workflow_id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'" target="_parent">Run</a>\n                                <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='sharing', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Share or Download</a>\n                                <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='copy', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Copy</a>\n                                <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='rename', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Rename</a>\n                                <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='display_by_id', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'" target="_top">View</a>\n                                <a class="action-button" confirm="Are you sure you want to delete workflow \'')
                __M_writer(filters.html_escape(unicode(h.to_unicode( workflow.name ) )))
                __M_writer(u'\'?" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='delete', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Delete</a>\n                                </div>\n                            </td>\n                        </tr>\n')
            __M_writer(u'                </table>\n')
        else:
            __M_writer(u'                You have no workflows.\n')
        __M_writer(u'\n            <h2>Workflows shared with you by others</h2>\n\n')
        if shared_by_others:
            __M_writer(u'                <table class="colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n                    <tr class="header">\n                        <th>Name</th>\n                        <th>Owner</th>\n                        <th># of Steps</th>\n                        <th></th>\n                    </tr>\n')
            for i, association in enumerate( shared_by_others ):
                __M_writer(u'                        ')
                workflow = association.stored_workflow 
                
                __M_writer(u'\n                        <tr>\n                            <td>\n                                <a class="menubutton" id="shared-')
                __M_writer(unicode(i))
                __M_writer(u'-popup" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='run', id=trans.security.encode_id(workflow.id) )))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(h.to_unicode( workflow.name ) )))
                __M_writer(u'</a>\n                            </td>\n                            <td>')
                __M_writer(unicode(workflow.user.email))
                __M_writer(u'</td>\n                            <td>')
                __M_writer(unicode(len(workflow.latest_workflow.steps)))
                __M_writer(u'</td>\n                            <td>\n                                <div popupmenu="shared-')
                __M_writer(unicode(i))
                __M_writer(u'-popup">\n                                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='display_by_username_and_slug', username=workflow.user.username, slug=workflow.slug )))
                __M_writer(u'" target="_top">View</a>\n                                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='run', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Run</a>\n                                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='copy', id=trans.security.encode_id( workflow.id ) )))
                __M_writer(u'">Copy</a>\n                                    <a class="action-button" confirm="Are you sure you want to remove the shared workflow \'')
                __M_writer(filters.html_escape(unicode(h.to_unicode( workflow.name ) )))
                __M_writer(u'\'?" href="')
                __M_writer(unicode(h.url_for( controller='workflow', action='sharing', unshare_me=True, id=trans.security.encode_id( workflow.id ))))
                __M_writer(u'">Remove</a>\n                                </div>\n                            </td>\n                        </tr>\n')
            __M_writer(u'                </table>\n')
        else:
            __M_writer(u'                No workflows have been shared with you.\n')
        __M_writer(u'\n            <h2>Other options</h2>\n\n            <a class="action-button" href="')
        __M_writer(unicode(h.url_for( controller='workflow', action='configure_menu' )))
        __M_writer(u'">\n                <span>Configure your workflow menu</span>\n            </a>\n        </div>\n    </div>\n')
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
{"source_encoding": "ascii", "line_map": {"27": 0, "32": 1, "33": 10, "34": 12, "35": 122, "41": 3, "46": 3, "47": 4, "54": 9, "60": 14, "71": 14, "72": 17, "73": 18, "74": 18, "81": 23, "82": 25, "83": 25, "84": 26, "85": 26, "86": 29, "87": 34, "88": 34, "89": 35, "90": 35, "91": 40, "92": 40, "93": 41, "94": 41, "95": 47, "96": 48, "97": 53, "98": 55, "99": 56, "100": 58, "101": 58, "102": 59, "103": 59, "104": 62, "105": 62, "106": 64, "107": 65, "108": 65, "109": 66, "110": 66, "111": 67, "112": 67, "113": 68, "114": 68, "115": 69, "116": 69, "117": 70, "118": 70, "119": 71, "120": 71, "121": 72, "122": 72, "123": 72, "124": 72, "125": 77, "126": 78, "127": 79, "128": 81, "129": 84, "130": 85, "131": 92, "132": 93, "133": 93, "135": 93, "136": 96, "137": 96, "138": 96, "139": 96, "140": 96, "141": 96, "142": 98, "143": 98, "144": 99, "145": 99, "146": 101, "147": 101, "148": 102, "149": 102, "150": 103, "151": 103, "152": 104, "153": 104, "154": 105, "155": 105, "156": 105, "157": 105, "158": 110, "159": 111, "160": 112, "161": 114, "162": 117, "163": 117, "169": 12, "173": 12, "179": 173}, "uri": "workflow/list.mako", "filename": "templates/webapps/galaxy/workflow/list.mako"}
__M_END_METADATA
"""
