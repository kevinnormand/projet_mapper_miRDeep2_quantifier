# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467014030.032065
_enable_loop = True
_template_filename = 'templates/show_params.mako'
_template_uri = 'show_params.mako'
_source_encoding = 'ascii'
_exports = ['inputs_recursive_indent', 'inputs_recursive']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7ffb500db850', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7ffb500db850')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ffb500db850')._populate(_import_ns, [u'render_msg'])
        upgrade_messages = _import_ns.get('upgrade_messages', context.get('upgrade_messages', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        tool = _import_ns.get('tool', context.get('tool', UNDEFINED))
        def inputs_recursive(input_params,param_values,depth=1,upgrade_messages=None):
            return render_inputs_recursive(context._locals(__M_locals),input_params,param_values,depth,upgrade_messages)
        job = _import_ns.get('job', context.get('job', UNDEFINED))
        hda = _import_ns.get('hda', context.get('hda', UNDEFINED))
        inherit_chain = _import_ns.get('inherit_chain', context.get('inherit_chain', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        params_objects = _import_ns.get('params_objects', context.get('params_objects', UNDEFINED))
        has_parameter_errors = _import_ns.get('has_parameter_errors', context.get('has_parameter_errors', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        from galaxy.util import listify 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['listify'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from galaxy.util import nice_size 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['nice_size'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n<style>\n    .inherit {\n        border: 1px solid #bbb;\n        padding: 15px;\n        text-align: center;\n        background-color: #eee;\n    }\n</style>\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<table class="tabletip">\n    <thead>\n        <tr><th colspan="2" style="font-size: 120%;">\n')
        if tool:
            __M_writer(u'                Tool: ')
            __M_writer(filters.html_escape(unicode(tool.name )))
            __M_writer(u'\n')
        else:
            __M_writer(u'                Unknown Tool\n')
        __M_writer(u'        </th></tr>\n    </thead>\n    <tbody>\n        ')

        encoded_hda_id = trans.security.encode_id( hda.id )
        encoded_history_id = trans.security.encode_id( hda.history_id )
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['encoded_hda_id','encoded_history_id'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n        <tr><td>Name:</td><td>')
        __M_writer(filters.html_escape(unicode(hda.name )))
        __M_writer(u'</td></tr>\n        <tr><td>Created:</td><td>')
        __M_writer(unicode(hda.create_time.strftime(trans.app.config.pretty_datetime_format)))
        __M_writer(u'</td></tr>\n')
        __M_writer(u'        <tr><td>Filesize:</td><td>')
        __M_writer(unicode(nice_size(hda.dataset.file_size)))
        __M_writer(u'</td></tr>\n        <tr><td>Dbkey:</td><td>')
        __M_writer(filters.html_escape(unicode(hda.dbkey )))
        __M_writer(u'</td></tr>\n        <tr><td>Format:</td><td>')
        __M_writer(filters.html_escape(unicode(hda.ext )))
        __M_writer(u'</td></tr>\n')
        if job:
            __M_writer(u'            <tr><td>Galaxy Tool ID:</td><td>')
            __M_writer(filters.html_escape(unicode( job.tool_id )))
            __M_writer(u'</td></tr>\n            <tr><td>Galaxy Tool Version:</td><td>')
            __M_writer(filters.html_escape(unicode( job.tool_version )))
            __M_writer(u'</td></tr>\n')
        __M_writer(u'        <tr><td>Tool Version:</td><td>')
        __M_writer(filters.html_escape(unicode(hda.tool_version )))
        __M_writer(u'</td></tr>\n        <tr><td>Tool Standard Output:</td><td><a href="')
        __M_writer(unicode(h.url_for( controller='dataset', action='stdout', dataset_id=encoded_hda_id )))
        __M_writer(u'">stdout</a></td></tr>\n        <tr><td>Tool Standard Error:</td><td><a href="')
        __M_writer(unicode(h.url_for( controller='dataset', action='stderr', dataset_id=encoded_hda_id )))
        __M_writer(u'">stderr</a></td></tr>\n')
        if job:
            __M_writer(u'            <tr><td>Tool Exit Code:</td><td>')
            __M_writer(filters.html_escape(unicode( job.exit_code )))
            __M_writer(u'</td></tr>\n')
        __M_writer(u'        <tr><td>History Content API ID:</td><td>')
        __M_writer(unicode(encoded_hda_id))
        __M_writer(u'</td></tr>\n')
        if job:
            __M_writer(u'            <tr><td>Job API ID:</td><td>')
            __M_writer(unicode(trans.security.encode_id( job.id )))
            __M_writer(u'</td></tr>\n')
        __M_writer(u'        <tr><td>History API ID:</td><td>')
        __M_writer(unicode(encoded_history_id))
        __M_writer(u'</td></tr>\n')
        if hda.dataset.uuid:
            __M_writer(u'        <tr><td>UUID:</td><td>')
            __M_writer(unicode(hda.dataset.uuid))
            __M_writer(u'</td></tr>\n')
        if trans.user_is_admin() or trans.app.config.expose_dataset_path:
            __M_writer(u'            <tr><td>Full Path:</td><td>')
            __M_writer(filters.html_escape(unicode(hda.file_name )))
            __M_writer(u'</td></tr>\n')
        if job and job.command_line and trans.user_is_admin():
            __M_writer(u'            <tr><td>Job Command-Line:</td><td>')
            __M_writer(filters.html_escape(unicode( job.command_line )))
            __M_writer(u'</td></tr>\n')
        if job and trans.user_is_admin():
            __M_writer(u'            ')
            job_metrics = trans.app.job_metrics 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['job_metrics'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            for metric in job.metrics:
                __M_writer(u'                ')
                metric_title, metric_value = job_metrics.format( metric.plugin, metric.metric_name, metric.metric_value ) 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['metric_title','metric_value'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                <tr><td>')
                __M_writer(filters.html_escape(unicode( metric_title )))
                __M_writer(u'</td><td>')
                __M_writer(filters.html_escape(unicode( metric_value )))
                __M_writer(u'</td></tr>\n')
        __M_writer(u'</table>\n<br />\n\n<table class="tabletip">\n    <thead>\n        <tr>\n            <th>Input Parameter</th>\n            <th>Value</th>\n            <th>Note for rerun</th>\n        </tr>\n    </thead>\n    <tbody>\n')
        if params_objects and tool:
            __M_writer(u'            ')
            __M_writer(unicode( inputs_recursive( tool.inputs, params_objects, depth=1, upgrade_messages=upgrade_messages ) ))
            __M_writer(u'\n')
        elif params_objects is None:
            __M_writer(u'            <tr><td colspan="3">Unable to load parameters.</td></tr>\n')
        else:
            __M_writer(u'            <tr><td colspan="3">No parameters.</td></tr>\n')
        __M_writer(u'    </tbody>\n</table>\n')
        if has_parameter_errors:
            __M_writer(u'    <br />\n    ')
            __M_writer(unicode( render_msg( 'One or more of your original parameters may no longer be valid or displayed properly.', status='warning' ) ))
            __M_writer(u'\n')
        __M_writer(u'\n<script type="text/javascript">\n$(function(){\n    $( \'.input-dataset-show-params\' ).on( \'click\', function( ev ){\n')
        __M_writer(u'        if( window.parent.Galaxy && window.parent.Galaxy.currHistoryPanel ){\n            window.parent.Galaxy.currHistoryPanel.scrollToId( \'dataset-\' + $( this ).data( \'hda-id\' ) );\n        }\n    })\n});\n</script>\n\n    <h3>Inheritance Chain</h3>\n    <div class="inherit" style="background-color: #fff; font-weight:bold;">')
        __M_writer(filters.html_escape(unicode(hda.name )))
        __M_writer(u'</div>\n\n')
        for dep in inherit_chain:
            __M_writer(u'        <div style="font-size: 36px; text-align: center; position: relative; top: 3px">&uarr;</div>\n        <div class="inherit">\n            \'')
            __M_writer(filters.html_escape(unicode(dep[0].name )))
            __M_writer(u"' in ")
            __M_writer(unicode(dep[1]))
            __M_writer(u'<br/>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_inputs_recursive_indent(context,text,depth):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ffb500db850')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        __M_writer(u'\n    <td style="padding-left: ')
        __M_writer(unicode( ( depth - 1 ) * 10 ))
        __M_writer(u'px">\n        ')
        __M_writer(filters.html_escape(unicode(text )))
        __M_writer(u'\n    </td>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_inputs_recursive(context,input_params,param_values,depth=1,upgrade_messages=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7ffb500db850')._populate(_import_ns, [u'render_msg'])
        listify = _import_ns.get('listify', context.get('listify', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def inputs_recursive_indent(text,depth):
            return render_inputs_recursive_indent(context,text,depth)
        range = _import_ns.get('range', context.get('range', UNDEFINED))
        def inputs_recursive(input_params,param_values,depth=1,upgrade_messages=None):
            return render_inputs_recursive(context,input_params,param_values,depth,upgrade_messages)
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        if upgrade_messages is None:
            upgrade_messages = {}
            
        
        __M_writer(u'\n')
        for input_index, input in enumerate( input_params.itervalues() ):
            if input.name in param_values:
                if input.type == "repeat":
                    for i in range( len(param_values[input.name]) ):
                        __M_writer(u'                    ')
                        __M_writer(unicode( inputs_recursive(input.inputs, param_values[input.name][i], depth=depth+1) ))
                        __M_writer(u'\n')
                elif input.type == "section":
                    __M_writer(u'                <tr>\n')
                    __M_writer(u'                    ')
                    __M_writer(unicode(inputs_recursive_indent( text=input.name, depth=depth )))
                    __M_writer(u'\n                    <td></td>\n                </tr>\n                ')
                    __M_writer(unicode( inputs_recursive( input.inputs, param_values[input.name], depth=depth+1, upgrade_messages=upgrade_messages.get( input.name ) ) ))
                    __M_writer(u'\n')
                elif input.type == "conditional":
                    __M_writer(u'                ')

                    try:
                        current_case = param_values[input.name]['__current_case__']
                        is_valid = True
                    except:
                        current_case = None
                        is_valid = False
                    
                    
                    __M_writer(u'\n')
                    if is_valid:
                        __M_writer(u'                    <tr>\n                        ')
                        __M_writer(unicode( inputs_recursive_indent( text=input.test_param.label, depth=depth )))
                        __M_writer(u'\n')
                        __M_writer(u'                        <td>')
                        __M_writer(filters.html_escape(unicode(input.cases[current_case].value )))
                        __M_writer(u'</td>\n                        <td></td>\n                    </tr>\n                    ')
                        __M_writer(unicode( inputs_recursive( input.cases[current_case].inputs, param_values[input.name], depth=depth+1, upgrade_messages=upgrade_messages.get( input.name ) ) ))
                        __M_writer(u'\n')
                    else:
                        __M_writer(u'                    <tr>\n                        ')
                        __M_writer(unicode( inputs_recursive_indent( text=input.name, depth=depth )))
                        __M_writer(u'\n                        <td><em>The previously used value is no longer valid</em></td>\n                        <td></td>\n                    </tr>\n')
                elif input.type == "upload_dataset":
                    __M_writer(u'                    <tr>\n                        ')
                    __M_writer(unicode(inputs_recursive_indent( text=input.group_title( param_values ), depth=depth )))
                    __M_writer(u'\n                        <td>')
                    __M_writer(unicode( len( param_values[input.name] ) ))
                    __M_writer(u' uploaded datasets</td>\n                        <td></td>\n                    </tr>\n')
                elif input.type == "data":
                    __M_writer(u'                    <tr>\n                        ')
                    __M_writer(unicode(inputs_recursive_indent( text=input.label, depth=depth )))
                    __M_writer(u'\n                        <td>\n')
                    for i, element in enumerate(listify(param_values[input.name])):
                        if i > 0:
                            __M_writer(u'                        ,\n')
                        if element.history_content_type == "dataset":
                            __M_writer(u'                        ')

                            hda = element
                            encoded_id = trans.security.encode_id( hda.id )
                            show_params_url = h.url_for( controller='dataset', action='show_params', dataset_id=encoded_id )
                                                    
                            
                            __M_writer(u'\n                        <a class="input-dataset-show-params" data-hda-id="')
                            __M_writer(unicode(encoded_id))
                            __M_writer(u'"\n                               href="')
                            __M_writer(unicode(show_params_url))
                            __M_writer(u'">')
                            __M_writer(filters.html_escape(unicode(hda.name )))
                            __M_writer(u'</a>\n')
                        else:
                            __M_writer(u'                        ')
                            __M_writer(unicode(element.hid))
                            __M_writer(u': ')
                            __M_writer(filters.html_escape(unicode(element.name )))
                            __M_writer(u'\n')
                    __M_writer(u'                        </td>\n                        <td></td>\n                    </tr>\n')
                elif input.visible:
                    __M_writer(u'                ')

                    if  hasattr( input, "label" ) and input.label:
                        label = input.label
                    else:
                        #value for label not required, fallback to input name (same as tool panel)
                        label = input.name
                    
                    
                    __M_writer(u'\n                <tr>\n                    ')
                    __M_writer(unicode(inputs_recursive_indent( text=label, depth=depth )))
                    __M_writer(u'\n                    <td>')
                    __M_writer(filters.html_escape(unicode(input.value_to_display_text( param_values[input.name], trans.app ) )))
                    __M_writer(u'</td>\n                    <td>')
                    __M_writer(filters.html_escape(unicode( upgrade_messages.get( input.name, '' ) )))
                    __M_writer(u'</td>\n                </tr>\n')
            else:
                __M_writer(u'            <tr>\n                ')

                    # Get parameter label.
                if input.type == "conditional":
                    label = input.test_param.label
                elif input.type == "repeat":
                    label = input.label()
                else:
                    label = input.label or input.name
                                
                
                __M_writer(u'\n                ')
                __M_writer(unicode(inputs_recursive_indent( text=label, depth=depth )))
                __M_writer(u'\n                <td><em>not used (parameter was added after this job was run)</em></td>\n                <td></td>\n            </tr>\n')
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 2, "29": 0, "48": 1, "49": 2, "50": 3, "54": 3, "55": 4, "59": 4, "60": 120, "61": 127, "62": 132, "63": 133, "64": 133, "65": 133, "66": 134, "67": 135, "68": 137, "69": 140, "76": 143, "77": 144, "78": 144, "79": 145, "80": 145, "81": 147, "82": 147, "83": 147, "84": 148, "85": 148, "86": 149, "87": 149, "88": 150, "89": 151, "90": 151, "91": 151, "92": 152, "93": 152, "94": 154, "95": 154, "96": 154, "97": 155, "98": 155, "99": 156, "100": 156, "101": 157, "102": 158, "103": 158, "104": 158, "105": 160, "106": 160, "107": 160, "108": 161, "109": 162, "110": 162, "111": 162, "112": 164, "113": 164, "114": 164, "115": 165, "116": 166, "117": 166, "118": 166, "119": 168, "120": 169, "121": 169, "122": 169, "123": 171, "124": 172, "125": 172, "126": 172, "127": 174, "128": 175, "129": 175, "133": 175, "134": 176, "135": 177, "136": 177, "140": 177, "141": 178, "142": 178, "143": 178, "144": 178, "145": 181, "146": 193, "147": 194, "148": 194, "149": 194, "150": 195, "151": 196, "152": 197, "153": 198, "154": 200, "155": 202, "156": 203, "157": 204, "158": 204, "159": 206, "160": 211, "161": 219, "162": 219, "163": 221, "164": 222, "165": 224, "166": 224, "167": 224, "168": 224, "174": 123, "180": 123, "181": 124, "182": 124, "183": 125, "184": 125, "190": 15, "207": 15, "208": 16, "213": 19, "214": 20, "215": 21, "216": 22, "217": 23, "218": 24, "219": 24, "220": 24, "221": 26, "222": 27, "223": 29, "224": 29, "225": 29, "226": 32, "227": 32, "228": 33, "229": 34, "230": 34, "239": 41, "240": 42, "241": 43, "242": 44, "243": 44, "244": 46, "245": 46, "246": 46, "247": 49, "248": 49, "249": 50, "250": 51, "251": 52, "252": 52, "253": 57, "254": 58, "255": 59, "256": 59, "257": 60, "258": 60, "259": 64, "260": 65, "261": 66, "262": 66, "263": 68, "264": 69, "265": 70, "266": 72, "267": 73, "268": 73, "274": 77, "275": 78, "276": 78, "277": 79, "278": 79, "279": 79, "280": 79, "281": 80, "282": 81, "283": 81, "284": 81, "285": 81, "286": 81, "287": 84, "288": 87, "289": 88, "290": 88, "298": 94, "299": 96, "300": 96, "301": 97, "302": 97, "303": 98, "304": 98, "305": 101, "306": 103, "307": 104, "317": 112, "318": 113, "319": 113, "320": 118, "326": 320}, "uri": "show_params.mako", "filename": "templates/show_params.mako"}
__M_END_METADATA
"""
