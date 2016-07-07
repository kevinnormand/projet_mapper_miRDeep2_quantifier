# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467200734.055441
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/workflow/editor.mako'
_template_uri = 'workflow/editor.mako'
_source_encoding = 'ascii'
_exports = ['left_panel', 'overlay', 'render_label', 'center_panel', 'render_module_section', 'stylesheets', 'init', 'right_panel', 'javascripts', 'render_tool']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f39c8292c10', context._clean_inheritance_tokens(), templateuri=u'/tagging_common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f39c8292c10')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f39c8292c10')._populate(_import_ns, [u'render_individual_tagging_element'])
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f39c8292c10')._populate(_import_ns, [u'render_individual_tagging_element'])
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        app = _import_ns.get('app', context.get('app', UNDEFINED))
        def render_label(label):
            return render_render_label(context,label)
        def render_module_section(module_section):
            return render_render_module_section(context,module_section)
        n_ = _import_ns.get('n_', context.get('n_', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        def render_tool(tool,section):
            return render_render_tool(context,tool,section)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from galaxy.tools import Tool
        from galaxy.tools.toolbox import ToolSection, ToolSectionLabel
            
        
        __M_writer(u'\n\n    <div class="unified-panel-header" unselectable="on">\n        <div class=\'unified-panel-header-inner\'>\n            ')
        __M_writer(unicode(n_('Tools')))
        __M_writer(u'\n        </div>\n    </div>\n\n    <div class="unified-panel-body" style="overflow: auto;">\n        <div class="toolMenu">\n            ')

        from galaxy.workflow.modules import load_module_sections
        module_sections = load_module_sections( trans )
                    
        
        __M_writer(u'\n            <div id="tool-search" style="padding-bottom: 5px; position: relative; display: block; width: 100%">\n                <input type="text" name="query" placeholder="search tools" id="tool-search-query" class="search-query parent-width" />\n                <img src="')
        __M_writer(unicode(h.url_for('/static/images/loading_small_white_bg.gif')))
        __M_writer(u'" id="search-spinner" class="search-spinner" />\n            </div>\n\n            <div class="toolSectionWrapper">\n                ')
        __M_writer(unicode(render_module_section(module_sections['inputs'])))
        __M_writer(u'\n            </div>\n\n            <div class="toolSectionList">\n')
        for val in app.toolbox.tool_panel_contents( trans ):
            __M_writer(u'                    <div class="toolSectionWrapper">\n')
            if isinstance( val, Tool ):
                __M_writer(u'                        ')
                __M_writer(unicode(render_tool( val, False )))
                __M_writer(u'\n')
            elif isinstance( val, ToolSection ) and val.elems:
                __M_writer(u'                    ')
                section = val 
                
                __M_writer(u'\n                        <div class="toolSectionTitle" id="title_')
                __M_writer(unicode(section.id))
                __M_writer(u'">\n                            <span>')
                __M_writer(unicode(section.name))
                __M_writer(u'</span>\n                        </div>\n                        <div id="')
                __M_writer(unicode(section.id))
                __M_writer(u'" class="toolSectionBody">\n                            <div class="toolSectionBg">\n')
                for section_key, section_val in section.elems.items():
                    if isinstance( section_val, Tool ):
                        __M_writer(u'                                        ')
                        __M_writer(unicode(render_tool( section_val, True )))
                        __M_writer(u'\n')
                    elif isinstance( section_val, ToolSectionLabel ):
                        __M_writer(u'                                        ')
                        __M_writer(unicode(render_label( section_val )))
                        __M_writer(u'\n')
                __M_writer(u'                            </div>\n                        </div>\n')
            elif isinstance( val, ToolSectionLabel ):
                __M_writer(u'                        ')
                __M_writer(unicode(render_label( val )))
                __M_writer(u'\n')
            __M_writer(u'                    </div>\n')
        if trans.user_is_admin() and trans.app.data_managers.data_managers:
            __M_writer(u'                   <div>&nbsp;</div>\n                   <div class="toolSectionWrapper">\n                       <div class="toolSectionTitle" id="title___DATA_MANAGER_TOOLS__">\n                           <span>Data Manager Tools</span>\n                       </div>\n                       <div id="__DATA_MANAGER_TOOLS__" class="toolSectionBody">\n                           <div class="toolSectionBg">\n')
            for data_manager_id, data_manager_val in trans.app.data_managers.data_managers.items():
                __M_writer(u'                                   ')
                __M_writer(unicode( render_tool( data_manager_val.tool, True ) ))
                __M_writer(u'\n')
            __M_writer(u'                           </div>\n                       </div>\n                   </div>\n')
        __M_writer(u'            </div>\n            <div>&nbsp;</div>\n')
        for section_name, module_section in module_sections.items():
            if section_name != "inputs":
                __M_writer(u'                    ')
                __M_writer(unicode(render_module_section(module_section)))
                __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'            <div id="search-no-results" style="display: none; padding-top: 5px">\n                <em><strong>Search did not match any tools.</strong></em>\n            </div>\n\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_overlay(context,visible=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f39c8292c10')._populate(_import_ns, [u'render_individual_tagging_element'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.overlay( "Loading workflow editor...",
                      "<div class='progress progress-striped progress-info active'><div class='progress-bar' style='width: 100%;'></div></div>", self.overlay_visible )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_label(context,label):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f39c8292c10')._populate(_import_ns, [u'render_individual_tagging_element'])
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="toolPanelLabel" id="title_')
        __M_writer(unicode(label.id))
        __M_writer(u'">\n        <span>')
        __M_writer(unicode(label.text))
        __M_writer(u'</span>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f39c8292c10')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        stored = _import_ns.get('stored', context.get('stored', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner" style="float: right">\n            <a id="workflow-options-button" class="panel-header-button" href="#"><span class="fa fa-cog"></span></a>\n        </div>\n        <div class="unified-panel-header-inner">\n            Workflow Canvas | ')
        __M_writer(filters.html_escape(unicode(h.to_unicode( stored.name ) )))
        __M_writer(u'\n        </div>\n    </div>\n    <div class="unified-panel-body">\n        <div id="canvas-viewport" style="width: 100%; height: 100%; position: absolute; overflow: hidden; background: #EEEEEE; background: white url(')
        __M_writer(unicode(h.url_for('/static/images/light_gray_grid.gif')))
        __M_writer(u') repeat;">\n            <div id="canvas-container" style="position: absolute; width: 100%; height: 100%;"></div>\n        </div>\n        <div id="overview-border" style="position: absolute; width: 150px; height: 150px; right: 20000px; bottom: 0px; border-top: solid gray 1px; border-left: solid grey 1px; padding: 7px 0 0 7px; background: #EEEEEE no-repeat url(')
        __M_writer(unicode(h.url_for('/static/images/resizable.png')))
        __M_writer(u'); z-index: 20000; overflow: hidden; max-width: 300px; max-height: 300px; min-width: 50px; min-height: 50px">\n            <div style="position: relative; overflow: hidden; width: 100%; height: 100%; border-top: solid gray 1px; border-left: solid grey 1px;">\n                <div id="overview" style="position: absolute;">\n                    <canvas width="0" height="0" style="background: white; width: 100%; height: 100%;" id="overview-canvas"></canvas>\n                    <div id="overview-viewport" style="position: absolute; width: 0px; height: 0px; border: solid blue 1px; z-index: 10;"></div>\n                </div>\n            </div>\n        </div>\n        <div id=\'workflow-parameters-box\' style="display:none; position: absolute; /*width: 150px; height: 150px;*/ right: 0px; top: 0px; border-bottom: solid gray 1px; border-left: solid grey 1px; padding: 7px; background: #EEEEEE; z-index: 20000; overflow: hidden; max-width: 300px; max-height: 300px; /*min-width: 50px; min-height: 50px*/">\n            <div style="margin-bottom:5px;"><b>Workflow Parameters</b></div>\n            <div id="workflow-parameters-container">\n            </div>\n        </div>\n        <div id="close-viewport" style="border-left: 1px solid #999; border-top: 1px solid #999; background: #ddd url(')
        __M_writer(unicode(h.url_for('/static/images/overview_arrows.png')))
        __M_writer(u') 12px 0px; position: absolute; right: 0px; bottom: 0px; width: 12px; height: 12px; z-index: 25000;"></div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_module_section(context,module_section):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f39c8292c10')._populate(_import_ns, [u'render_individual_tagging_element'])
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="toolSectionTitle" id="title___workflow__')
        __M_writer(unicode(module_section['name']))
        __M_writer(u'__">\n        <span>')
        __M_writer(unicode(module_section["title"]))
        __M_writer(u'</span>\n    </div>\n    <div id="__workflow__')
        __M_writer(unicode(module_section['name']))
        __M_writer(u'__" class="toolSectionBody">\n        <div class="toolSectionBg">\n')
        for module in module_section["modules"]:
            __M_writer(u'                <div class="toolTitle">\n                    <a href="#" onclick="workflow_view.add_node_for_module( \'')
            __M_writer(unicode(module['name']))
            __M_writer(u"', '")
            __M_writer(unicode(module['title']))
            __M_writer(u'\' )">\n                        ')
            __M_writer(unicode(module['description']))
            __M_writer(u'\n                    </a>\n                </div>\n')
        __M_writer(u'        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f39c8292c10')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'    ')
        __M_writer(unicode(h.css( "base", "autocomplete_tagging", "tool_menu", "jquery-ui/smoothness/jquery-ui" )))
        __M_writer(u'\n\n')
        __M_writer(u'    ')
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n\n    <style type="text/css">\n    body { margin: 0; padding: 0; overflow: hidden; }\n\n    #left {\n        background: #C1C9E5 url(')
        __M_writer(unicode(h.url_for('/static/style/menu_bg.png')))
        __M_writer(u') top repeat-x;\n    }\n\n    div.toolMenu {\n        margin: 5px;\n        margin-left: 10px;\n        margin-right: 10px;\n    }\n    div.toolMenuGroupHeader {\n        font-weight: bold;\n        padding-top: 0.5em;\n        padding-bottom: 0.5em;\n        color: #333;\n        font-style: italic;\n        border-bottom: dotted #333 1px;\n        margin-bottom: 0.5em;\n    }\n    div.toolTitleDisabled {\n        padding-top: 5px;\n        padding-bottom: 5px;\n        margin-left: 16px;\n        margin-right: 10px;\n        display: list-item;\n        list-style: square outside;\n        font-style: italic;\n        color: gray;\n    }\n    div.toolTitleNoSectionDisabled {\n      padding-bottom: 0px;\n      font-style: italic;\n      color: gray;\n    }\n    div.toolFormRow {\n        position: relative;\n    }\n\n    .right-content {\n        margin: 3px;\n    }\n\n    canvas { position: absolute; z-index: 10; }\n    canvas.dragging { position: absolute; z-index: 1000; }\n    .input-terminal { width: 12px; height: 12px; background: url(')
        __M_writer(unicode(h.url_for('/static/style/workflow_circle_open.png')))
        __M_writer(u'); position: absolute; top: 50%; margin-top: -6px; left: -6px; z-index: 1500; }\n    .output-terminal { width: 12px; height: 12px; background: url(')
        __M_writer(unicode(h.url_for('/static/style/workflow_circle_open.png')))
        __M_writer(u'); position: absolute; top: 50%; margin-top: -6px; right: -6px; z-index: 1500; }\n    .drag-terminal { width: 12px; height: 12px; background: url(')
        __M_writer(unicode(h.url_for('/static/style/workflow_circle_drag.png')))
        __M_writer(u'); position: absolute; z-index: 1500; }\n    .input-terminal-active { background: url(')
        __M_writer(unicode(h.url_for('/static/style/workflow_circle_green.png')))
        __M_writer(u'); }\n')
        __M_writer(u'    .unselectable { -moz-user-select: none; -khtml-user-select: none; user-select: none; }\n    img { border: 0; }\n\n    div.buttons img {\n    width: 16px; height: 16px;\n    cursor: pointer;\n    }\n\n')
        __M_writer(u'    div.toolFormInCanvas {\n        z-index: 100;\n        position: absolute;\n')
        __M_writer(u'        margin: 6px;\n    }\n\n    div.toolForm-active {\n        z-index: 1001;\n        border: solid #8080FF 4px;\n        margin: 3px;\n    }\n\n    div.toolFormTitle {\n        cursor: move;\n        min-height: 16px;\n    }\n\n    div.titleRow {\n        font-weight: bold;\n        border-bottom: dotted gray 1px;\n        margin-bottom: 0.5em;\n        padding-bottom: 0.25em;\n    }\n    div.form-row {\n      position: relative;\n    }\n\n    div.tool-node-error div.toolFormTitle {\n        background: #FFCCCC;\n        border-color: #AA6666;\n    }\n    div.tool-node-error {\n        border-color: #AA6666;\n    }\n\n    #canvas-area {\n        position: absolute;\n        top: 0; left: 305px; bottom: 0; right: 0;\n        border: solid red 1px;\n        overflow: none;\n    }\n\n    .form-row {\n    }\n\n    div.toolFormInCanvas div.toolFormBody {\n        padding: 0;\n    }\n    .form-row-clear {\n        clear: both;\n    }\n\n    div.rule {\n        height: 0;\n        border: none;\n        border-bottom: dotted black 1px;\n        margin: 0 5px;\n    }\n\n    .callout {\n        position: absolute;\n        z-index: 10000;\n    }\n\n    .pjaForm {\n        margin-bottom:10px;\n    }\n\n    .pjaForm .toolFormBody{\n        padding:10px;\n    }\n\n    .pjaForm .toolParamHelp{\n        padding:5px;\n    }\n\n    .panel-header-button-group {\n        margin-right: 5px;\n        padding-right: 5px;\n        border-right: solid gray 1px;\n    }\n\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f39c8292c10')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        stored = _import_ns.get('stored', context.get('stored', UNDEFINED))
        workflows = _import_ns.get('workflows', context.get('workflows', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')

        self.active_view="workflow"
        self.overlay_visible=True
        self.editor_config = {
            'id'      : trans.security.encode_id( stored.id ),
            'urls'    : {
                'tool_search'         : h.url_for( '/api/tools' ),
                'get_datatypes'       : h.url_for( '/api/datatypes/mapping' ),
                'load_workflow'       : h.url_for( controller='workflow', action='load_workflow' ),
                'run_workflow'        : h.url_for( controller='root', action='index', workflow_id=trans.security.encode_id(stored.id)),
                'rename_async'        : h.url_for( controller='workflow', action='rename_async', id=trans.security.encode_id(stored.id) ),
                'annotate_async'      : h.url_for( controller='workflow', action='annotate_async', id=trans.security.encode_id(stored.id) ),
                'get_new_module_info' : h.url_for(controller='workflow', action='get_new_module_info' ),
                'workflow_index'      : h.url_for( controller='workflow', action='index' ),
                'save_workflow'       : h.url_for(controller='workflow', action='save_workflow' )
            },
            'workflows' : [{
                'id'                  : trans.security.encode_id( workflow.id ),
                'latest_id'           : trans.security.encode_id( workflow.latest_workflow.id ),
                'step_count'          : len( workflow.latest_workflow.steps ),
                'name'                : h.to_unicode( workflow.name )
            } for workflow in workflows ]
        }
        
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f39c8292c10')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        stored = _import_ns.get('stored', context.get('stored', UNDEFINED))
        annotation = _import_ns.get('annotation', context.get('annotation', UNDEFINED))
        render_individual_tagging_element = _import_ns.get('render_individual_tagging_element', context.get('render_individual_tagging_element', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner">\n            Details\n        </div>\n    </div>\n    <div class="unified-panel-body" style="overflow: auto;">\n')
        __M_writer(u'        <div id="edit-attributes" class="metadataForm right-content">\n            <div class="metadataFormTitle">Edit Workflow Attributes</div>\n            <div class="metadataFormBody">\n')
        __M_writer(u'            <div id="workflow-name-area" class="form-row">\n                <label>Name:</label>\n                <span id="workflow-name" class="editable-text" title="Click to rename workflow">')
        __M_writer(filters.html_escape(unicode(h.to_unicode( stored.name ) )))
        __M_writer(u'</span>\n            </div>\n')
        __M_writer(u'            ')
        __M_writer(u'\n            <div class="form-row">\n                <label>\n                    Tags:\n                </label>\n                    <div style="float: left; width: 225px; margin-right: 10px; border-style: inset; border-width: 1px; margin-left: 2px">\n                        <style>\n                            .tag-area {\n                                border: none;\n                            }\n                        </style>\n                        ')
        __M_writer(unicode(render_individual_tagging_element(user=trans.get_user(), tagged_item=stored, elt_context="edit_attributes.mako", use_toggle_link=False, input_size="20")))
        __M_writer(u'\n                    </div>\n                    <div class="toolParamHelp">Apply tags to make it easy to search for and find items with the same tag.</div>\n                </div>\n')
        __M_writer(u'                <div id="workflow-annotation-area" class="form-row">\n                    <label>Annotation / Notes:</label>\n                    <div id="workflow-annotation" class="editable-text" title="Click to edit annotation">\n')
        if annotation:
            __M_writer(u'                        ')
            __M_writer(filters.html_escape(unicode(h.to_unicode( annotation ) )))
            __M_writer(u'\n')
        else:
            __M_writer(u'                        <em>Describe or add notes to workflow</em>\n')
        __M_writer(u'                    </div>\n                    <div class="toolParamHelp">Add an annotation or notes to a workflow; annotations are available when a workflow is viewed.</div>\n                </div>\n            </div>\n        </div>\n\n')
        __M_writer(u'        <div id="right-content" class="right-content"></div>\n\n')
        __M_writer(u'        <div style="display:none;" id="workflow-output-area" class="metadataForm right-content">\n            <div class="metadataFormTitle">Edit Workflow Outputs</div>\n            <div class="metadataFormBody"><div class="form-row">\n                <div class="toolParamHelp">Tag step outputs to indicate the final dataset(s) to be generated by running this workflow.</div>\n                <div id="output-fill-area"></div>\n            </div></div>\n        </div>\n\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f39c8292c10')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n    ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n\n    ')
        __M_writer(unicode(h.js(
        "libs/jquery/jquery.event.drag",
        "libs/jquery/jquery.event.drop",
        "libs/jquery/jquery.event.hover",
        "libs/jquery/jquery.form",
        "libs/jquery/jstorage",
        "libs/jquery/jquery.autocomplete",
    )))
        __M_writer(u"\n\n    <script type='text/javascript'>\n        workflow_view = null;\n        $( function() {\n            require(['mvc/workflow/workflow-view'], function(Workflow){\n                workflow_view = new Workflow(")
        __M_writer(unicode(h.dumps(self.editor_config)))
        __M_writer(u');\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool(context,tool,section):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f39c8292c10')._populate(_import_ns, [u'render_individual_tagging_element'])
        __M_writer = context.writer()
        __M_writer(u'\n')
        if not tool.hidden:
            if tool.is_workflow_compatible:
                if section:
                    __M_writer(u'                <div class="toolTitle">\n')
                else:
                    __M_writer(u'                <div class="toolTitleNoSection">\n')
                if "[[" in tool.description and "]]" in tool.description:
                    __M_writer(u'                    ')
                    __M_writer(unicode(tool.description.replace( '[[', '<a id="link-${tool.id}" href="workflow_view.add_node_for_tool( ${tool.id} )">' % tool.id ).replace( "]]", "</a>" )))
                    __M_writer(u'\n')
                elif tool.name:
                    __M_writer(u'                    <a id="link-')
                    __M_writer(unicode(tool.id))
                    __M_writer(u'" href="#" onclick="workflow_view.add_node_for_tool( \'')
                    __M_writer(unicode(tool.id))
                    __M_writer(u"', '")
                    __M_writer(unicode(tool.name))
                    __M_writer(u'\' )">')
                    __M_writer(unicode(tool.name))
                    __M_writer(u'</a> ')
                    __M_writer(unicode(tool.description))
                    __M_writer(u'\n')
                else:
                    __M_writer(u'                    <a id="link-')
                    __M_writer(unicode(tool.id))
                    __M_writer(u'" href="#" onclick="workflow_view.add_node_for_tool( \'')
                    __M_writer(unicode(tool.id))
                    __M_writer(u"', '")
                    __M_writer(unicode(tool.name))
                    __M_writer(u'\' )">')
                    __M_writer(unicode(tool.description))
                    __M_writer(u'</a>\n')
                __M_writer(u'            </div>\n')
            else:
                if section:
                    __M_writer(u'                <div class="toolTitleDisabled">\n')
                else:
                    __M_writer(u'                <div class="toolTitleNoSectionDisabled">\n')
                if "[[" in tool.description and "]]" in tool.description:
                    __M_writer(u'                    ')
                    __M_writer(unicode(tool.description.replace( '[[', '' % tool.id ).replace( "]]", "" )))
                    __M_writer(u'\n')
                elif tool.name:
                    __M_writer(u'                    ')
                    __M_writer(unicode(tool.name))
                    __M_writer(u' ')
                    __M_writer(unicode(tool.description))
                    __M_writer(u'\n')
                else:
                    __M_writer(u'                    ')
                    __M_writer(unicode(tool.description))
                    __M_writer(u'\n')
                __M_writer(u'            </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 409, "29": 0, "36": 1, "37": 28, "38": 51, "39": 206, "40": 241, "41": 248, "42": 253, "43": 271, "44": 358, "45": 390, "46": 453, "52": 273, "69": 273, "70": 274, "75": 277, "76": 281, "77": 281, "78": 287, "83": 290, "84": 293, "85": 293, "86": 297, "87": 297, "88": 301, "89": 302, "90": 303, "91": 304, "92": 304, "93": 304, "94": 305, "95": 306, "96": 306, "98": 306, "99": 307, "100": 307, "101": 308, "102": 308, "103": 310, "104": 310, "105": 312, "106": 313, "107": 314, "108": 314, "109": 314, "110": 315, "111": 316, "112": 316, "113": 316, "114": 319, "115": 321, "116": 322, "117": 322, "118": 322, "119": 324, "120": 327, "121": 328, "122": 335, "123": 336, "124": 336, "125": 336, "126": 338, "127": 343, "128": 345, "129": 346, "130": 347, "131": 347, "132": 347, "133": 350, "134": 352, "140": 250, "148": 250, "149": 251, "151": 252, "157": 244, "163": 244, "164": 245, "165": 245, "166": 246, "167": 246, "173": 360, "181": 360, "182": 367, "183": 367, "184": 371, "185": 371, "186": 374, "187": 374, "188": 387, "189": 387, "195": 256, "201": 256, "202": 257, "203": 257, "204": 258, "205": 258, "206": 260, "207": 260, "208": 262, "209": 263, "210": 264, "211": 264, "212": 264, "213": 264, "214": 265, "215": 265, "216": 269, "222": 53, "230": 53, "231": 56, "232": 56, "233": 56, "234": 59, "235": 59, "236": 59, "237": 65, "238": 65, "239": 107, "240": 107, "241": 108, "242": 108, "243": 109, "244": 109, "245": 110, "246": 110, "247": 112, "248": 122, "249": 126, "255": 3, "267": 3, "268": 4, "293": 27, "299": 392, "310": 392, "311": 400, "312": 404, "313": 406, "314": 406, "315": 409, "316": 409, "317": 420, "318": 420, "319": 426, "320": 429, "321": 430, "322": 430, "323": 430, "324": 431, "325": 432, "326": 434, "327": 441, "328": 444, "334": 30, "343": 30, "344": 32, "345": 32, "346": 34, "354": 41, "355": 47, "356": 47, "362": 209, "368": 209, "369": 210, "370": 211, "371": 212, "372": 213, "373": 214, "374": 215, "375": 217, "376": 218, "377": 218, "378": 218, "379": 219, "380": 220, "381": 220, "382": 220, "383": 220, "384": 220, "385": 220, "386": 220, "387": 220, "388": 220, "389": 220, "390": 220, "391": 221, "392": 222, "393": 222, "394": 222, "395": 222, "396": 222, "397": 222, "398": 222, "399": 222, "400": 222, "401": 224, "402": 225, "403": 226, "404": 227, "405": 228, "406": 229, "407": 231, "408": 232, "409": 232, "410": 232, "411": 233, "412": 234, "413": 234, "414": 234, "415": 234, "416": 234, "417": 235, "418": 236, "419": 236, "420": 236, "421": 238, "427": 421}, "uri": "workflow/editor.mako", "filename": "templates/webapps/galaxy/workflow/editor.mako"}
__M_END_METADATA
"""
