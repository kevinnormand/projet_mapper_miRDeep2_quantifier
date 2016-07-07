# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467200739.353964
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/workflow/editor_tool_form.mako'
_template_uri = 'workflow/editor_tool_form.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        tool = context.get('tool', UNDEFINED)
        module = context.get('module', UNDEFINED)
        job = context.get('job', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()

    ## TEMPORARY: create tool dictionary in mako while both tool forms are in use.
    ## This avoids making two separate requests since the classic form requires the mako anyway.
        from galaxy.tools.parameters import params_to_incoming
        incoming = {}
        params_to_incoming( incoming, tool.inputs, module.state.inputs, trans.app )
        self.form_config = tool.to_json(trans, incoming, workflow_mode=True)
        self.form_config.update({
            'id'                : tool.id,
            'job_id'            : trans.security.encode_id( job.id ) if job else None,
            'history_id'        : trans.security.encode_id( trans.history.id ),
            'container'         : '#right-content'
        })
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['params_to_incoming','incoming'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(unicode( h.dumps(self.form_config) ))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "51": 45, "27": 1, "44": 14, "45": 15}, "uri": "workflow/editor_tool_form.mako", "filename": "templates/webapps/galaxy/workflow/editor_tool_form.mako"}
__M_END_METADATA
"""
