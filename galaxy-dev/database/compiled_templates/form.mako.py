# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467200725.193815
_enable_loop = True
_template_filename = 'templates/form.mako'
_template_uri = 'form.mako'
_source_encoding = 'ascii'
_exports = ['body', 'title', 'center_panel', 'stylesheets', 'init', 'javascripts', 'render_form']



def inherit(context):
    if context.get('use_panels'):
        if context.get('webapp'):
            app_name = context.get('webapp')
        elif context.get('app'):
            app_name = context.get('app').name
        else:
            app_name = 'galaxy'
        return '/webapps/%s/base_panels.mako' % app_name
    else:
        return '/base.mako'


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
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        n_ = context.get('n_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_form():
            return render_render_form(context)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(render_form( )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(unicode(form.title )))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_form():
            return render_render_form(context)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(render_form( )))
        __M_writer(u'\n')
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
        __M_writer(unicode(h.css("autocomplete_tagging")))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        active_view = context.get('active_view', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view=active_view
        self.message_box_visible=False
        
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.js("libs/jquery/jquery.autocomplete")))
        __M_writer(u'\n    <script type="text/javascript">\n        $(function(){\n            $("input:text:first").focus();\n        })\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_form(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        util = context.get('util', UNDEFINED)
        header = context.get('header', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if header:
            __M_writer(u'        ')
            __M_writer(unicode(header))
            __M_writer(u'\n')
        __M_writer(u'    \n    <div class="form" style="margin: 1em">\n        <div class="form-title">')
        __M_writer(filters.html_escape(unicode(util.unicodify( form.title ) )))
        __M_writer(u'</div>\n        <div class="form-body">\n        ')

        has_file_input = False
        for input in form.inputs:
            if input.type == 'file':
                has_file_input = True
                break
                
        
        __M_writer(u'\n        <form name="')
        __M_writer(filters.html_escape(unicode(form.name )))
        __M_writer(u'" action="')
        __M_writer(unicode(form.action))
        __M_writer(u'" method="post" \n')
        if has_file_input:
            __M_writer(u'             enctype="multipart/form-data"\n')
        __M_writer(u'        >\n')
        for input in form.inputs:
            __M_writer(u'                ')

            cls = "form-row"
            if input.error:
                cls += " form-row-error"
            
            
            __M_writer(u'\n                <div class="')
            __M_writer(unicode(cls))
            __M_writer(u'">\n')
            if input.use_label:
                __M_writer(u'                  <label>\n                      ')
                __M_writer(filters.html_escape(unicode(_(input.label) )))
                __M_writer(u':\n                  </label>\n')
            __M_writer(u'                <div class="form-row-input">\n')
            if input.type == 'textarea':
                __M_writer(u'                        <textarea name="')
                __M_writer(filters.html_escape(unicode(input.name )))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(input.value )))
                __M_writer(u'</textarea>\n')
            elif input.type == 'select':
                __M_writer(u'                        <select name="')
                __M_writer(filters.html_escape(unicode(input.name )))
                __M_writer(u'">\n')
                for (name, value) in input.options:
                    __M_writer(u'                                <option value="')
                    __M_writer(filters.html_escape(unicode(value )))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(unicode(name )))
                    __M_writer(u'</option>\n')
                __M_writer(u'                        </select>\n')
            else:
                __M_writer(u'                        <input type="')
                __M_writer(unicode(input.type))
                __M_writer(u'" name="')
                __M_writer(filters.html_escape(unicode(input.name )))
                __M_writer(u'" value="')
                __M_writer(filters.html_escape(unicode(input.value )))
                __M_writer(u'">\n')
            __M_writer(u'                </div>\n')
            if input.error:
                __M_writer(u'                    <div class="form-row-error-message">')
                __M_writer(filters.html_escape(unicode(input.error )))
                __M_writer(u'</div>\n')
            if input.help:
                __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        ')
                __M_writer(filters.html_escape(unicode(input.help )))
                __M_writer(u'\n                    </div>\n')
            __M_writer(u'                <div style="clear: both"></div>\n        </div>\n')
        __M_writer(u'        <div class="form-row"><input type="submit" value="')
        __M_writer(unicode(form.submit_text))
        __M_writer(u'"></div>\n        </form>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 1, "41": 0, "47": 13, "48": 14, "49": 15, "53": 15, "54": 24, "55": 27, "56": 37, "57": 42, "58": 46, "59": 50, "60": 112, "66": 48, "72": 48, "73": 49, "74": 49, "80": 27, "85": 27, "91": 44, "97": 44, "98": 45, "99": 45, "105": 39, "111": 39, "112": 40, "113": 40, "114": 41, "115": 41, "121": 17, "127": 17, "128": 18, "135": 23, "141": 29, "147": 29, "148": 30, "149": 30, "150": 31, "151": 31, "157": 52, "165": 52, "166": 53, "167": 54, "168": 54, "169": 54, "170": 56, "171": 58, "172": 58, "173": 60, "181": 66, "182": 67, "183": 67, "184": 67, "185": 67, "186": 68, "187": 69, "188": 71, "189": 72, "190": 73, "191": 73, "197": 77, "198": 78, "199": 78, "200": 79, "201": 80, "202": 81, "203": 81, "204": 84, "205": 85, "206": 86, "207": 86, "208": 86, "209": 86, "210": 86, "211": 87, "212": 88, "213": 88, "214": 88, "215": 89, "216": 90, "217": 90, "218": 90, "219": 90, "220": 90, "221": 92, "222": 93, "223": 94, "224": 94, "225": 94, "226": 94, "227": 94, "228": 94, "229": 94, "230": 96, "231": 97, "232": 98, "233": 98, "234": 98, "235": 100, "236": 101, "237": 102, "238": 102, "239": 105, "240": 108, "241": 108, "242": 108, "248": 242}, "uri": "form.mako", "filename": "templates/form.mako"}
__M_END_METADATA
"""
