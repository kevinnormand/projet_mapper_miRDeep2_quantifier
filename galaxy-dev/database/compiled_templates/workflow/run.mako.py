# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467200919.151568
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/workflow/run.mako'
_template_uri = 'workflow/run.mako'
_source_encoding = 'ascii'
_exports = ['stylesheets', 'javascripts', 'do_inputs', 'row_for_param']


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
        isinstance = context.get('isinstance', UNDEFINED)
        errors = context.get('errors', UNDEFINED)
        workflow = context.get('workflow', UNDEFINED)
        int = context.get('int', UNDEFINED)
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        def do_inputs(inputs,values,errors,prefix,step,other_values=None,already_used=None):
            return render_do_inputs(context._locals(__M_locals),inputs,values,errors,prefix,step,other_values,already_used)
        value = context.get('value', UNDEFINED)
        self = context.get('self', UNDEFINED)
        util = context.get('util', UNDEFINED)
        step_version_changes = context.get('step_version_changes', UNDEFINED)
        steps = context.get('steps', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        has_upgrade_messages = context.get('has_upgrade_messages', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        history_id = context.get('history_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if util.string_as_bool(trans.app.config.get('run_workflow_toolform_upgrade',  False)):
            __M_writer(u'    ')
            __M_writer(unicode(h.js("libs/bibtex", "libs/jquery/jquery-ui")))
            __M_writer(u'\n    ')
            __M_writer(unicode(h.css('jquery-ui/smoothness/jquery-ui')))
            __M_writer(u'\n    ')

            from galaxy.tools.parameters import params_to_incoming
            from galaxy.jobs.actions.post import ActionBox
            step_models = []
            for i, step in enumerate( steps ):
                step_model = None
                if step.type in [ 'data_input', 'data_collection_input' ]:
                    type_filter = []
                    for oc in step.output_connections:
                        for ic in oc.input_step.module.get_data_inputs():
                            if 'extensions' in ic and ic[ 'name' ] == oc.input_name:
                                type_filter += ic[ 'extensions' ]
                    if not type_filter:
                        type_filter = [ 'data' ]
                    d = step.module.get_runtime_inputs( type_filter )
                    input = d[ 'input' ].to_dict( trans );
                    step_model = {
                        'name'   : input[ 'label' ],
                        'inputs' : [ input ]
                    }
                elif step.type == 'tool':
                    incoming = {}
                    tool = trans.app.toolbox.get_tool( step.tool_id )
                    params_to_incoming( incoming, tool.inputs, step.state.inputs, trans.app )
                    step_model = tool.to_json( trans, incoming, workflow_mode=True )
                    step_model[ 'post_job_actions' ] = [{
                        'short_str'         : ActionBox.get_short_str( pja ),
                        'action_type'       : pja.action_type,
                        'output_name'       : pja.output_name,
                        'action_arguments'  : pja.action_arguments
                    } for pja in step.post_job_actions ]
                step_model[ 'step_id' ] = step.id
                step_model[ 'step_type' ] = step.type
                step_model[ 'order_index' ] = step.order_index
                step_model[ 'output_connections' ] = [ {
                    'input_step_id'     : oc.input_step_id,
                    'output_step_id'    : oc.output_step_id,
                    'input_name'        : oc.input_name,
                    'output_name'       : oc.output_name
                } for oc in step.output_connections ]
                if step.annotations:
                    step_model[ 'annotation' ] = step.annotations[0].annotation
                step_models.append( step_model )
            self.form_config = {
                'id'                : app.security.encode_id( workflow.id ),
                'name'              : workflow.name,
                'history_id'        : history_id,
                'steps'             : step_models
            }
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['pja','ActionBox','d','type_filter','i','oc','tool','params_to_incoming','step_models','incoming','step','step_model','input','ic'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u"\n    <script>\n        require(['mvc/tool/tool-form-composite'], function( ToolForm ) {\n            $(function() {\n                var form = new ToolForm.View(")
            __M_writer(unicode( h.dumps( self.form_config ) ))
            __M_writer(u');\n            });\n        });\n    </script>\n')
        else:
            __M_writer(u'\n')
            __M_writer(u'\n\n')
            __M_writer(u'\n\n')

            from galaxy.tools.parameters.basic import DataCollectionToolParameter, DataToolParameter, RuntimeValue
            from galaxy.jobs.actions.post import ActionBox
            import re
            import colorsys
            import random
            from six import string_types
            
            def get_wf_parms(v, wf_parms):
                if isinstance(v, dict):
                    [ get_wf_parms(value, wf_parms) for value in v.values()  ]
                elif isinstance(v, string_types):
                    for rematch in re.findall('\$\{.+?\}', v):
                        if rematch[2:-1] not in wf_parms:
                            wf_parms[rematch[2:-1]] = ""
            
            used_accumulator = []
            wf_parms = {}
            
            for step in steps:
                for v in [ActionBox.get_short_str(pja) for pja in step.post_job_actions] + step.state.inputs.values():
                    get_wf_parms(v, wf_parms)
            
            if wf_parms:
                hue_offset = 1.0 / len(wf_parms)
                hue = 0.0
                for k in wf_parms.iterkeys():
                    wf_parms[k] = "#%X%X%X" % tuple([int(x * 255) for x in colorsys.hsv_to_rgb(hue, .1, .9)])
                    hue += hue_offset
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['hue','hue_offset','wf_parms','ActionBox','DataToolParameter','used_accumulator','pja','k','random','get_wf_parms','string_types','re','step','RuntimeValue','colorsys','v','DataCollectionToolParameter','x'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n\n')
            __M_writer(u'\n\n')
            __M_writer(u'\n\n<div id=\'ec_button_container\'>\n    <span class="action-button" id="show_all_tool_body">Expand All</span>\n    <span class="action-button" id="hide_all_tool_body">Collapse</span>\n</div>\n\n<h2>Running workflow "')
            __M_writer(filters.html_escape(unicode(h.to_unicode( workflow.name ) )))
            __M_writer(u'"</h2>\n\n')
            if has_upgrade_messages:
                __M_writer(u'<div class="warningmessage">\n    Warning: Some tools in this workflow have changed since it was last saved. The workflow may still run, but any new options will have default values.\n    Please review the messages below to make a decision about whether the changes will affect your analysis.\n</div>\n')
            __M_writer(u'\n')
            if step_version_changes:
                __M_writer(u'    <div class="infomessage">\n        The following tools are being executed with a different version from\n        what was available when this workflow was last saved because the\n        previous version is no longer available for use on this galaxy\n        instance.\n        To upgrade your workflow and dismiss this message simply edit the\n        workflow and re-save it to update the stored tool version.\n        <ul>\n')
                for vc in step_version_changes:
                    __M_writer(u'                <li>')
                    __M_writer(unicode(vc))
                    __M_writer(u'</li>\n')
                __M_writer(u'        </ul>\n    </div>\n')
            __M_writer(u'\n')
            if workflow.annotation:
                __M_writer(u'    <div class="workflow-annotation">')
                __M_writer(unicode(workflow.annotation))
                __M_writer(u'</div>\n    <hr/>\n')
            __M_writer(u'\n<form id="tool_form" name="tool_form" method="POST">\n')
            __M_writer(u'\n')
            if wf_parms:
                __M_writer(u'<div class="metadataForm">\n    <div class="metadataFormTitle">Workflow Parameters</div>\n    <div class="metadataFormBody">\n')
                for parm in wf_parms:
                    __M_writer(u"        <div class='form-row'><label>")
                    __M_writer(unicode(parm))
                    __M_writer(u'<br/><input size=40 style="border:2px solid ')
                    __M_writer(unicode(wf_parms[parm]))
                    __M_writer(u';border-left-width:8px;" type="text" class=\'wf_parm_input ptag_')
                    __M_writer(unicode(parm))
                    __M_writer(u'\' name="wf_parm|')
                    __M_writer(unicode(parm))
                    __M_writer(u'" value=""/></label></div>\n')
                __M_writer(u'    </div>\n</div>\n    <script type="text/javascript">\n    // Set the change hooks for workflow parameters.\n    $(document).ready(function () {\n        $(\'.wf_parm_input\').bind(\'change keypress keyup\', function(event){\n            // DBTODO This is probably not reliable.  Ensure we have the right class.\n            var new_text = $(this).val();\n            if (new_text === \'\'){\n                var tag_id = $(this).attr("class").split(\' \')[1].substring(5);\n                // Set text properly.\n                $(\'.wfpspan.wf_parm__\'+tag_id).text(tag_id);\n            }else{\n                var tag_id = $(this).attr("class").split(\' \')[1].substring(5);\n                // Set text properly.\n                $(\'.wfpspan.wf_parm__\'+tag_id).text(new_text);\n                // Now set the hidden input to the generated text.\n                $(\'.wfpspan.wf_parm__\'+tag_id).not(\'.pja_wfp\').each(function(){\n                    var new_text = $(this).parent().text();\n                    $(this).parent().siblings().children().val(new_text);\n                });\n            }\n        });\n    });\n    </script>\n')

            import base64
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['base64'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            for i, step in enumerate( steps ):
                __M_writer(u'    <!-- Only way module would be missing is if tool is missing, but\n         that would cause missing_tools.mako to render instead of this\n         template. -->\n    ')
                module = step.module 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['module'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n    <input type="hidden" name="')
                __M_writer(unicode(step.id))
                __M_writer(u'|tool_state" value="')
                __M_writer(unicode(base64.b64encode( module.get_state( step.state ))))
                __M_writer(u'">\n')
                if step.type == 'tool' or step.type is None:
                    __M_writer(u'      ')

                    tool = trans.app.toolbox.get_tool( step.tool_id )
                          
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tool'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n      <div class="toolForm">\n          <div class="toolFormTitle">\n              <span class=\'title_ul_text\'>Step ')
                    __M_writer(unicode(int(step.order_index)+1))
                    __M_writer(u': ')
                    __M_writer(unicode(tool.name))
                    __M_writer(u'</span>\n')
                    if tool.version:
                        __M_writer(u'                  (version ')
                        __M_writer(unicode(tool.version))
                        __M_writer(u')\n')
                    if step.annotations:
                        __M_writer(u'                <div class="step-annotation">')
                        __M_writer(unicode(h.to_unicode( step.annotations[0].annotation )))
                        __M_writer(u'</div>\n')
                    __M_writer(u'          </div>\n          <div class="toolFormBody">\n                ')
                    __M_writer(unicode(do_inputs( tool.inputs, step.state.inputs, errors.get( step.id, dict() ), "", step, None, used_accumulator )))
                    __M_writer(u'\n')
                    if step.post_job_actions:
                        __M_writer(u"                    <hr/>\n                    <div class='form-row'>\n")
                        if len(step.post_job_actions) > 1:
                            __M_writer(u'                        <label>Actions:</label>\n')
                        else:
                            __M_writer(u'                        <label>Action:</label>\n')
                        __M_writer(u'                    ')

                        pja_ss_all = []
                        for pja_ss in [ActionBox.get_short_str(pja) for pja in step.post_job_actions]:
                            for rematch in re.findall('\$\{.+?\}', pja_ss):
                                pja_ss = pja_ss.replace(rematch, '<span style="background-color:%s" class="wfpspan wf_parm__%s pja_wfp">%s</span>' % (wf_parms[rematch[2:-1]],
                                                                                                                                                      rematch[2:-1],
                                                                                                                                                      rematch[2:-1]))
                            pja_ss_all.append(pja_ss)
                        
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['rematch','pja_ss_all','pja','pja_ss'] if __M_key in __M_locals_builtin_stored]))
                        __M_writer(u'\n                    ')
                        __M_writer(unicode('<br/>'.join(pja_ss_all)))
                        __M_writer(u'\n                    </div>\n')
                    __M_writer(u'              </div>\n          </div>\n')
                else:
                    __M_writer(u'          <div class="toolForm">\n              <div class="toolFormTitle">\n                  <span class=\'title_ul_text\'>Step ')
                    __M_writer(unicode(int(step.order_index)+1))
                    __M_writer(u': ')
                    __M_writer(filters.html_escape(unicode(module.name )))
                    __M_writer(u'</span>\n')
                    if step.annotations:
                        __M_writer(u'                    <div class="step-annotation">')
                        __M_writer(unicode(step.annotations[0].annotation))
                        __M_writer(u'</div>\n')
                    __M_writer(u'          </div>\n          <div class="toolFormBody">\n              ')

              # Filter possible inputs to data types that are valid for subsequent steps
                    type_filter = []
                    for oc in step.output_connections:
                        for ic in oc.input_step.module.get_data_inputs():
                            if 'extensions' in ic and ic['name'] == oc.input_name:
                                type_filter += ic['extensions']
                    if not type_filter:
                        type_filter = ['data']
                    
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ic','oc','type_filter'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n              ')
                    __M_writer(unicode(do_inputs( module.get_runtime_inputs(filter_set=type_filter), step.state.inputs, errors.get( step.id, dict() ), "", step, None, used_accumulator )))
                    __M_writer(u'\n          </div>\n      </div>\n')
            if history_id is None:
                __M_writer(u'    <p id=\'new_history_p\'>\n        <input type="checkbox" name=\'new_history\' value="true" id=\'new_history_cbx\'/><label for=\'new_history_cbx\'>Send results to a new history </label>\n        <span id="new_history_input">named: <input type=\'text\' name=\'new_history_name\' value=\'')
                __M_writer(filters.html_escape(unicode( h.to_unicode( workflow.name ) )))
                __M_writer(u"'/></span>\n    </p>\n")
            __M_writer(u'<input type="submit" class="btn btn-primary" name="run_workflow" value="Run workflow" />\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.css( "autocomplete_tagging" )))
        __M_writer(u'\n    <style type="text/css">\n    #new_history_p{\n        line-height:2.5em;\n        margin:0em 0em .5em 0em;\n    }\n    #new_history_cbx{\n        margin-right:.5em;\n    }\n    #new_history_input{\n        display:none;\n        line-height:1em;\n    }\n    #ec_button_container{\n        float:right;\n    }\n    div.toolForm{\n        margin-top: 10px;\n        margin-bottom: 10px;\n    }\n    div.toolFormTitle{\n        cursor:pointer;\n    }\n    .title_ul_text{\n        text-decoration:underline;\n    }\n    .step-annotation {\n        margin-top: 0.25em;\n        font-weight: normal;\n        font-size: 97%;\n    }\n    .workflow-annotation {\n        margin-bottom: 1em;\n    }\n    .editable {\n        display: none;\n    }\n    .editable-param {\n        display: none;\n    }\n\n    .workflow-edit-button-editing {\n        color: black;\n    }\n\n    .workflow-edit-button-default {\n        color: Gray;\n    }\n\n    .workflow-edit-button:hover {\n        color: green; // TODO: Use a history panel green.\n    }\n\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        hide_fixed_params = context.get('hide_fixed_params', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n\n        // jQuery plugin to prevent double submission of forms\n        // Ref: http://stackoverflow.com/questions/2830542/prevent-double-submission-of-forms-in-jquery\n        jQuery.fn.preventDoubleSubmission = function() {\n            $(this).on(\'submit\',function(e){\n                var $form = $(this);\n\n                if ($form.data(\'submitted\') === true) {\n                    // Previously submitted - don\'t submit again\n                    e.preventDefault();\n                } else {\n                    // Mark it so that the next submit can be ignored\n                    $form.data(\'submitted\', true);\n                }\n            });\n            // Keep chainability\n            return this;\n        };\n\n        $.fn.outerHTML = function(s) {\n            return s ? this.before(s).remove() : jQuery("<p>").append(this.eq(0).clone()).html();\n        };\n        $( function() {\n            function show_tool_body(title){\n                title.parent().show().css(\'border-bottom-width\', \'1px\');\n                title.next().show(\'fast\');\n                if (\'')
        __M_writer(unicode(hide_fixed_params))
        __M_writer(u'\'.toLowerCase() == \'true\') {\n                    // show previously hidden parameters\n                    title.next().children(".form-row").show();\n                }\n            }\n            function hide_tool_body(title){\n                title.parent().css(\'border-bottom-width\', \'0px\');\n                title.next().hide(\'fast\');\n            }\n            function toggle_tool_body(title) {\n                if (title.next().is(\':visible\')){\n                    hide_tool_body(title);\n                }else{\n                    show_tool_body(title);\n                }\n            }\n            function toggle_multiinput(select) {\n                var placeholder;\n                if (select.attr(\'multiple\')) {\n                    $(\'.multiinput\').removeClass(\'disabled\');\n                    if (select.val()) {\n                        select.val(select.val()[0]);\n                    } else {\n                        select.val($(\'option:last\', select).val());\n                    }\n                    select.closest(\'.form-row\').children(\'label\').children(\'span.mode-icon\').hide();\n                    select.removeAttr(\'multiple\').removeAttr(\'size\');\n                    placeholder = \'type to filter\';\n                } else {\n                    $(\'.multiinput\', select.closest(\'.form-row\')).removeClass(\'disabled\');\n                    select.closest(\'.form-row\').children(\'label\').children(\'span.mode-icon\').show();\n                    select.attr(\'multiple\', \'multiple\').attr(\'size\', 8);\n                    placeholder = \'type to filter, [enter] to select all\';\n                }\n                $(\'input.multiinput-filter\', select.parent()).attr(\n                    \'placeholder\', placeholder);\n            }\n            $( "select[refresh_on_change=\'true\']").change( function() {\n                $( "#tool_form" ).submit();\n            });\n            $("div.toolFormTitle").click(function(){\n                toggle_tool_body($(this));\n            });\n            if (\'')
        __M_writer(unicode(hide_fixed_params))
        __M_writer(u'\'.toLowerCase() == \'true\') {\n                // hide parameters that are not runtime inputs\n                $("div.form-row:not(:has(select, textarea, input[type!=hidden], .wfpspan))").hide();\n                $("div.toolForm:not(:has(select, textarea, input[type!=hidden], .wfpspan))").hide();\n            }\n            else {\n                // Collapse non-interactive run-workflow panels by default.\n                $("div.toolFormBody:not(:has(.runtime-form-row))").hide().parent().css(\'border-bottom-width\', \'0px\');\n            }\n            $("#show_all_tool_body").click(function(){\n                $("div.toolFormTitle").each(function(){\n                    show_tool_body($(this));\n                });\n            });\n            $("#hide_all_tool_body").click(function(){\n                $("div.toolFormTitle").each(function(){\n                    hide_tool_body($(this));\n                });\n            });\n            $("#new_history_cbx").click(function(){\n                $("#new_history_input").toggle(this.checked);\n            });\n            $(\'span.multiinput_wrap select[name*="|input"]\').removeAttr(\'multiple\').each(function(i, s) {\n                var select = $(s);\n                // The destroy on the following line is temporary and prevents\n                // select2 use on Input Dataset Steps, but allows elsewhere.  We\n                // need a new widget to better handle pairwise matching.\n                select.select2("destroy");\n                var new_width = Math.max(200, select.width()) + 20;\n                // Find the label for this element.\n                select.closest(\'.form-row\').children(\'label\').append(\n                    $(\'<span class="icon-button multiinput"></span>\').click(function() {\n                        if ($(this).hasClass(\'disabled\')) return;\n                        toggle_multiinput(select);\n                        select.focus();\n                    }).attr(\'title\',\n                            \'Enable/disable selection of multiple input \' +\n                            \'files. Each selected file will have an \' +\n                            \'instance of the workflow.\').tooltip({placement: \'bottom\'})\n                );\n                var filter = $(\'<input type="text" class="multiinput-filter" \' +\n                               \'placeholder="type to filter">\');\n                var filter_timeout = false;\n                var original_rows = select.find(\'option\');\n                var previous_filter = \'\';\n                // Todo: might have to choose keypress, depending on browser\n                filter.keydown(function(e) {\n                    var filter_select = function() {\n                        var f = $.trim(filter.val());\n                        var filtered_rows = original_rows;\n                        if (f.length >= 1) {\n                            filtered_rows = original_rows.filter(function() {\n                                return new RegExp(f, \'ig\').test($(this).text());\n                            });\n                        }\n                        select.html(\'\');\n                        select.html(filtered_rows);\n                    };\n                    if (e.which == 13) { // 13 = enter key\n                        e.preventDefault();\n                        multi = select.attr(\'multiple\');\n                        if (typeof multi !== \'undefined\' && multi !== false) {\n                            if (!select.find(\'option:not(:selected)\').length) {\n                                select.find(\'option\').removeAttr(\'selected\');\n                            } else {\n                                select.find(\'option\').attr(\'selected\', \'selected\');\n                            }\n                        }\n                        return;\n                    }\n                    if (filter.val() != previous_filter) {\n                        if (filter_timeout) clearTimeout(filter_timeout);\n                        timeout = setTimeout(filter_select, 300);\n                        previous_filter = filter.val();\n                    }\n                }).width(new_width).css(\'display\', \'block\');\n                select.after(filter);\n                select.width(new_width);\n            });\n        // Editable Workflow\n\n        var readyParameter = function(icon) {\n            icon.attr("name", "edit");\n            icon.attr(\'title\', "Modify default value for this workflow parameter.");\n            icon.removeClass("workflow-edit-button-editing");\n            icon.addClass("workflow-edit-button-ready");\n            icon.addClass("fa-edit");\n            icon.removeClass("fa-undo");\n        };\n\n        var editingParameter = function(icon) {\n            icon.attr("name", "revert");\n            icon.attr(\'title\', "Restore workflow default value for this parameter.");\n            icon.addClass("workflow-edit-button-editing");\n            icon.removeClass("workflow-edit-button-ready");\n            icon.removeClass("fa-edit");\n            icon.addClass("fa-undo");\n        };\n\n         $(".workflow-edit-button").on("click",function(){\n                var state = $(this).attr("name");\n                var stepToolBox = $(this).parent().parent().find(\'.editable-param\').find(\'input:not([class]):not([type="hidden"]), select:not([class])\');\n                var labels = $(this).parent().parent().find(\'.editable-param\').find(\'label\');\n                var split_name = stepToolBox.attr("name").split("|");\n                var step_id = split_name[0];\n                var step_name = split_name.slice(2, split_name.length).join("|");\n                var hidden_html = "<input type=\'hidden\' name=\'"+step_id+"|__runtime__"+step_name+"\' value=\'true\' />";\n                var html = "";\n                if (state === "edit"){\n                    stepToolBoxClone = stepToolBox.clone();\n                    stepToolBoxClone.each(function(index){$(stepToolBoxClone[index]).attr({"name":step_id+"|"+step_name})});\n                    stepToolBoxClone.show();\n                    if (labels.length > 0){\n                        stepToolBoxClone.each(function(index){\n                        html += stepToolBoxClone[index].outerHTML + labels[index].outerHTML + "<br/>"});\n                    }\n                    else{\n                        html = stepToolBoxClone.outerHTML();\n                    }\n                    $(this).parent().find(".editable").show();\n                    $(this).parent().parent().find(".uneditable_field").hide();\n                    $(this).parent().find(".editable").html(html+hidden_html);\n                    editingParameter($(this));\n                }\n                else{\n                    $(this).parent().find(".editable").hide();\n                    $(this).parent().find(".editable").empty();\n                    $(this).parent().parent().find(".uneditable_field").show();\n                    $(this).attr("name", "edit");\n                    readyParameter($(this));\n                }\n            }).each(function(i, icon) {\n                var conditionalStart = $(this).closest(".form-row").prev().hasClass("conditional-start");\n                if(! conditionalStart ) {\n                    readyParameter($(icon));\n                }\n            });\n\n            // Augment hidden fields with icons.\n            // http://stackoverflow.com/a/2088430\n            $(function(){\n                $(".multi-mode").each(function(){\n                    if($(this).val() == "matched") {\n                        $(this).closest(\'.form-row\').children(\'label\').append($(\'<span class="icon-button link mode-icon" title="This input is linked and will be run in matched order with other input datasets (ex: use this for matching forward and reverse reads)."></span>\')\n                            .attr({id:$(this).attr("id")})\n                            .css("display", $(this).css("display"))\n                            .tooltip({placement: \'bottom\'}));\n                    } else {\n                        $(this).closest(\'.form-row\').children(\'label\').append($(\'<span class="icon-button link-broken mode-icon" title="This input is not linked and each selection will be run against *all* other inputs."></span>\')\n                            .attr({id:$(this).attr("id")})\n                            .css("display", $(this).css("display"))\n                            .tooltip({placement: \'bottom\'}));\n                    }\n                });\n                $("span.mode-icon").click(function(){\n                    i= $(this).closest(\'.form-row\').find("input[type=hidden]");\n                    if($(this).hasClass("link")) {\n                        $(this).removeClass("link").addClass("link-broken");\n                        $(i).val("product");\n                    } else {\n                        $(this).removeClass("link-broken").addClass("link");\n                        $(i).val("matched");\n                    }\n                });\n            });\n            $("#tool_form").preventDoubleSubmission().submit(function(e) {\n                var matchLength = -1;\n                $(\'span.multiinput_wrap select[name*="|input"]\').each(function() {\n                    var value = $(this).val();\n                    if(value instanceof Array) {\n                        // Multi-value\n                        if($(this).siblings("input[type=hidden]").val() == "matched") {\n                            var length = $(this).val().length;\n                            if(matchLength == -1) {\n                                matchLength = length;\n                            } else if(length != matchLength) {\n                                e.preventDefault();\n                                alert("Linked inputs must be submitted in equal number.");\n                                return false;\n                            }\n                        }\n                    }\n                });\n                return true;\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_do_inputs(context,inputs,values,errors,prefix,step,other_values=None,already_used=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        def row_for_param(param,value,other_values,error_dict,prefix,step,already_used):
            return render_row_for_param(context,param,value,other_values,error_dict,prefix,step,already_used)
        def do_inputs(inputs,values,errors,prefix,step,other_values=None,already_used=None):
            return render_do_inputs(context,inputs,values,errors,prefix,step,other_values,already_used)
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        str = context.get('str', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  ')

        from galaxy.util.expressions import ExpressionContext
        other_values = ExpressionContext( values, other_values )
        
        
        __M_writer(u'\n')
        for input_index, input in enumerate( inputs.itervalues() ):
            if input.type == "repeat":
                __M_writer(u'      <div class="repeat-group">\n          <div class="form-title-row"><b>')
                __M_writer(unicode(input.title_plural))
                __M_writer(u'</b></div>\n          ')
                repeat_values = values[input.name] 
                
                __M_writer(u'\n')
                for i in range( len( repeat_values ) ):
                    if input.name in errors:
                        __M_writer(u'                ')
                        rep_errors = errors[input.name][i] 
                        
                        __M_writer(u'\n')
                    else:
                        __M_writer(u'                ')
                        rep_errors = dict() 
                        
                        __M_writer(u'\n')
                    __M_writer(u'            <div class="repeat-group-item">\n            ')
                    index = repeat_values[i]['__index__'] 
                    
                    __M_writer(u'\n            <div class="form-title-row"><b>')
                    __M_writer(unicode(input.title))
                    __M_writer(u' ')
                    __M_writer(unicode(i + 1))
                    __M_writer(u'</b></div>\n            ')
                    __M_writer(unicode(do_inputs( input.inputs, repeat_values[ i ], rep_errors,  prefix + input.name + "_" + str(index) + "|", step, other_values, already_used )))
                    __M_writer(u'\n')
                    __M_writer(u'            </div>\n')
                __M_writer(u'      </div>\n')
            elif input.type == "conditional":
                if input.name == '__job_resource':
                    __M_writer(u'        ')
                    continue 
                    
                    __M_writer(u'\n')
                __M_writer(u'      ')
                group_values = values[input.name] 
                
                __M_writer(u'\n      ')
                current_case = group_values['__current_case__'] 
                
                __M_writer(u'\n      ')
                new_prefix = prefix + input.name + "|" 
                
                __M_writer(u'\n      ')
                group_errors = errors.get( input.name, {} ) 
                
                __M_writer(u'\n      <span class="conditional-start"></span>\n      ')
                __M_writer(unicode(row_for_param( input.test_param, group_values[ input.test_param.name ], other_values, group_errors, prefix, step, already_used )))
                __M_writer(u'\n      ')
                __M_writer(unicode(do_inputs( input.cases[ current_case ].inputs, group_values, group_errors, new_prefix, step, other_values, already_used )))
                __M_writer(u'\n')
            elif input.type == "section":
                __M_writer(u'      ')
                group_values = values[input.name] 
                
                __M_writer(u'\n      ')
                new_prefix = prefix + input.name + "|" 
                
                __M_writer(u'\n      ')
                group_errors = errors.get( input.name, {} ) 
                
                __M_writer(u'\n      <div class="form-title-row"><b>')
                __M_writer(unicode(input.title))
                __M_writer(u':</b></div>\n      <div class="repeat-group">\n        <div class="repeat-group-item">\n      ')
                __M_writer(unicode(do_inputs( input.inputs, group_values, group_errors, new_prefix, step, other_values, already_used )))
                __M_writer(u'\n        </div>\n      </div>\n')
            else:
                __M_writer(u'      ')
                __M_writer(unicode(row_for_param( input, values[ input.name ], other_values, errors, prefix, step, already_used )))
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_row_for_param(context,param,value,other_values,error_dict,prefix,step,already_used):
    __M_caller = context.caller_stack._push_frame()
    try:
        basestring = context.get('basestring', UNDEFINED)
        wf_parms = context.get('wf_parms', UNDEFINED)
        incoming = context.get('incoming', UNDEFINED)
        DataToolParameter = context.get('DataToolParameter', UNDEFINED)
        int = context.get('int', UNDEFINED)
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        list = context.get('list', UNDEFINED)
        enable_unique_defaults = context.get('enable_unique_defaults', UNDEFINED)
        re = context.get('re', UNDEFINED)
        RuntimeValue = context.get('RuntimeValue', UNDEFINED)
        t = context.get('t', UNDEFINED)
        str = context.get('str', UNDEFINED)
        DataCollectionToolParameter = context.get('DataCollectionToolParameter', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if error_dict.has_key( param.name ):
            __M_writer(u'        ')
            cls = "form-row form-row-error" 
            
            __M_writer(u'\n')
        else:
            __M_writer(u'        ')
            cls = "form-row" 
            
            __M_writer(u'\n')
        __M_writer(u'    <div class="')
        __M_writer(unicode(cls))
        __M_writer(u'">\n        <label>')
        __M_writer(filters.html_escape(unicode(param.get_label() )))
        __M_writer(u'</label>\n        <div>\n')
        if isinstance( param, DataToolParameter ) or isinstance( param, DataCollectionToolParameter ):
            if ( prefix + param.name ) in step.input_connections_by_name:
                __M_writer(u'                    ')

                conns = step.input_connections_by_name[ prefix + param.name ]
                if not isinstance(conns, list):
                    conns = [conns]
                vals = ["Output dataset '%s' from step %d" % (conn.output_name, int(conn.output_step.order_index)+1) for conn in conns]
                                    
                
                __M_writer(u'\n                    ')
                __M_writer(unicode(",".join(vals)))
                __M_writer(u'\n')
            else:
                __M_writer(u'                    ')

                if value is None:
                    value = other_values[ param.name ] = param.get_initial_value_from_history_prevent_repeats( t, other_values, already_used )
                    if not enable_unique_defaults:
                        del already_used[:]
                
                
                __M_writer(u'\n')
                if step.type in [ 'data_input', 'data_collection_input' ]:
                    __M_writer(u'                        <span class="runtime-form-row">\n                            <span class=\'multiinput_wrap\'>\n                            <input class="multi-mode" type="hidden" name="')
                    __M_writer(unicode(str(step.id)))
                    __M_writer(u'|multi_mode" id="')
                    __M_writer(unicode(str(step.id)))
                    __M_writer(u'|multi_mode" value="matched" />\n                            ')
                    __M_writer(unicode(param.get_html_field( t, value, other_values ).get_html( str(step.id) + "|" + prefix )))
                    __M_writer(u'\n                            </span>\n                        </span>\n')
                else:
                    __M_writer(u'                        <span class="runtime-form-row">\n                            ')
                    __M_writer(unicode(param.get_html_field( t, value, other_values ).get_html( str(step.id) + "|" + prefix )))
                    __M_writer(u'\n                        </span>\n')
                __M_writer(u'\n                    <input type="hidden" name="')
                __M_writer(unicode(step.id))
                __M_writer(u'|__force_update__')
                __M_writer(unicode(prefix))
                __M_writer(unicode(param.name))
                __M_writer(u'" value="true" />\n')
        elif isinstance( value, RuntimeValue ) or ( str(step.id) + '|__runtime__' + prefix + param.name ) in incoming:
            __M_writer(u'                ')

            value = other_values[ param.name ] = param.get_initial_value_from_history_prevent_repeats( t, other_values, already_used )
            if not enable_unique_defaults:
                del already_used[:]
                            
            
            __M_writer(u'\n                <span class="runtime-form-row">\n                    ')
            __M_writer(unicode(param.get_html_field( t, value, other_values ).get_html( str(step.id) + "|" + prefix )))
            __M_writer(u'\n                    <input type="hidden" name="')
            __M_writer(unicode(step.id))
            __M_writer(u'|__runtime__')
            __M_writer(unicode(prefix))
            __M_writer(unicode(param.name))
            __M_writer(u'" value="true" />\n                </span>\n')
        else:
            __M_writer(u'                ')

            p_text = param.value_to_display_text( value, app )
            replacements = []
            if isinstance(p_text, basestring):
                for rematch in re.findall('\$\{.+?\}', p_text):
                    if rematch[2:-1] in wf_parms:
                        replacements.append('wf_parm__%s' % rematch[2:-1])
                        p_text = p_text.replace(rematch, '<span style="background-color:%s" class="runtime-form-row wfpspan wf_parm__%s">%s</span>' % (wf_parms[rematch[2:-1]], rematch[2:-1], rematch[2:-1]))
            
            
            __M_writer(u'\n')
            if replacements:
                __M_writer(u'                    <span style="display:none" class="parm_wrap ')
                __M_writer(unicode(' '.join(replacements)))
                __M_writer(u'">\n                    ')
                __M_writer(unicode(param.get_html_field( t, value, other_values ).get_html( str(step.id) + "|" + prefix )))
                __M_writer(u'\n                    </span>\n                    <span class="p_text_wrapper">')
                __M_writer(unicode(p_text))
                __M_writer(u'</span>\n                    <input type="hidden" name="')
                __M_writer(unicode(step.id))
                __M_writer(u'|__runtime__')
                __M_writer(unicode(prefix))
                __M_writer(unicode(param.name))
                __M_writer(u'" value="true" />\n')
            else:
                __M_writer(u'                <span class="workflow_parameters">\n                    <span class="uneditable_field">\n                        ')
                __M_writer(filters.html_escape(unicode(param.value_to_display_text( value, app ) )))
                __M_writer(u'\n                    </span>\n                    <span class="editable_field">\n                        <span class="editable">\n                        </span>\n\n                        <i class="fa workflow-edit-button"></i>\n                    </span>\n                    <span class="editable-param">\n                        <!-- Pristine variant of param, this will be cloned\n                             and modified when the user opts to make this\n                             editable.\n                        -->\n                        ')
                __M_writer(unicode(param.get_html_field( t, value, other_values).get_html( str(step.id) + "|"+ "editable" + "|" + prefix )))
                __M_writer(u'\n                    </span>\n                </span>\n')
        __M_writer(u'        </div>\n')
        if step.upgrade_messages and param.name in step.upgrade_messages:
            __M_writer(u'        <div class="warningmark">')
            __M_writer(unicode(step.upgrade_messages[param.name]))
            __M_writer(u'</div>\n')
        if error_dict.has_key( param.name ):
            __M_writer(u'        <div style="color: red; font-weight: bold; padding-top: 1px; padding-bottom: 3px;">\n            <div style="width: 300px;"><img style="vertical-align: middle;" src="')
            __M_writer(unicode(h.url_for('/static/style/error_small.png')))
            __M_writer(u'">&nbsp;<span style="vertical-align: middle;">')
            __M_writer(unicode(error_dict[param.name]))
            __M_writer(u'</span></div>\n        </div>\n')
        __M_writer(u'        <div style="clear: both"></div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"512": 528, "513": 530, "514": 531, "515": 531, "525": 539, "526": 540, "527": 541, "528": 541, "529": 541, "530": 542, "531": 542, "532": 544, "533": 544, "534": 545, "535": 545, "536": 545, "537": 545, "538": 545, "27": 0, "540": 547, "541": 549, "542": 549, "543": 562, "544": 562, "545": 567, "546": 568, "547": 569, "548": 569, "549": 569, "550": 571, "551": 572, "552": 573, "553": 573, "554": 573, "555": 573, "556": 576, "562": 556, "52": 1, "53": 4, "54": 5, "55": 5, "56": 5, "57": 6, "58": 6, "59": 7, "112": 56, "113": 60, "114": 60, "115": 64, "116": 65, "117": 325, "118": 383, "119": 385, "152": 414, "153": 466, "154": 578, "155": 585, "156": 585, "157": 587, "158": 588, "159": 593, "160": 594, "161": 595, "162": 603, "163": 604, "164": 604, "165": 604, "166": 606, "167": 609, "168": 610, "169": 611, "170": 611, "171": 611, "172": 614, "173": 617, "174": 618, "175": 619, "176": 622, "177": 623, "178": 623, "179": 623, "180": 623, "181": 623, "182": 623, "183": 623, "184": 623, "185": 623, "186": 625, "187": 651, "193": 653, "194": 654, "195": 655, "196": 658, "200": 658, "201": 659, "202": 659, "203": 659, "204": 659, "205": 660, "206": 661, "207": 661, "213": 663, "214": 666, "215": 666, "216": 666, "217": 666, "218": 667, "219": 668, "220": 668, "221": 668, "222": 670, "223": 671, "224": 671, "225": 671, "226": 673, "227": 675, "228": 675, "229": 676, "230": 677, "231": 679, "232": 680, "233": 681, "234": 682, "235": 684, "236": 684, "248": 692, "249": 693, "250": 693, "251": 696, "252": 698, "253": 699, "254": 701, "255": 701, "256": 701, "257": 701, "258": 702, "259": 703, "260": 703, "261": 703, "262": 705, "263": 707, "276": 716, "277": 717, "278": 717, "279": 722, "280": 723, "281": 725, "282": 725, "283": 728, "289": 327, "295": 327, "296": 328, "297": 328, "298": 329, "299": 329, "305": 66, "311": 66, "312": 67, "313": 67, "314": 95, "315": 95, "316": 138, "317": 138, "539": 546, "323": 416, "336": 416, "337": 417, "342": 420, "343": 421, "344": 422, "345": 423, "346": 424, "347": 424, "348": 425, "350": 425, "351": 426, "352": 427, "353": 428, "354": 428, "356": 428, "357": 429, "358": 430, "359": 430, "361": 430, "362": 432, "363": 433, "365": 433, "366": 434, "367": 434, "368": 434, "369": 434, "370": 435, "371": 435, "372": 437, "373": 440, "374": 441, "375": 442, "376": 443, "377": 443, "379": 443, "380": 445, "381": 445, "383": 445, "384": 446, "386": 446, "387": 447, "389": 447, "390": 448, "392": 448, "393": 450, "394": 450, "395": 451, "396": 451, "397": 452, "398": 453, "399": 453, "401": 453, "402": 454, "404": 454, "405": 455, "407": 455, "408": 456, "409": 456, "410": 459, "411": 459, "412": 462, "413": 463, "414": 463, "415": 463, "421": 468, "440": 468, "441": 470, "442": 471, "443": 471, "445": 471, "446": 472, "447": 473, "448": 473, "450": 473, "451": 475, "452": 475, "453": 475, "454": 476, "455": 476, "456": 478, "457": 479, "458": 480, "459": 480, "466": 485, "467": 486, "468": 486, "469": 487, "470": 489, "471": 489, "478": 494, "479": 495, "480": 497, "481": 499, "482": 499, "483": 499, "484": 499, "485": 500, "486": 500, "487": 503, "488": 504, "489": 505, "490": 505, "491": 508, "492": 509, "493": 509, "494": 509, "495": 509, "496": 509, "497": 511, "498": 521, "499": 521, "505": 525, "506": 527, "507": 527, "508": 528, "509": 528, "510": 528, "511": 528}, "uri": "workflow/run.mako", "filename": "templates/webapps/galaxy/workflow/run.mako"}
__M_END_METADATA
"""
