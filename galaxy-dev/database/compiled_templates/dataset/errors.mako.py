# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467641918.571329
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/dataset/errors.mako'
_template_uri = 'dataset/errors.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        util = context.get('util', UNDEFINED)
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        hda = context.get('hda', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n    <head>\n        <title>Dataset generation errors</title>\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n        <link href="/static/style/base.css" rel="stylesheet" type="text/css" />\n        <style>\n            pre\n            {\n                background: white;\n                color: black;\n                border: dotted black 1px;\n                overflow: auto;\n                padding: 10px;\n            }\n        </style>\n\n        <script type="text/javascript">\n            function sendReport( button, form, target, doConfirm )\n            {\n                var doIt = true;\n                if ( doConfirm==true )\n                {\n                    doIt = confirm( \'You are about to submit to a public forum, do you want to continue?\' );\n                }\n                if ( doIt==true )\n                {\n                    form.setAttribute( \'target\', target );\n                    for( i=0; i<form.elements.length; i++ )\n                    {\n                        if ( form.elements[i].type == \'submit\' )\n                        {\n                            form.elements[i].disabled = true;\n                        }\n\n                    }\n                    var hiddenInput = document.createElement(\'input\');\n                    hiddenInput.type = \'hidden\';\n                    hiddenInput.name = button.name;\n                    hiddenInput.value = button.value;\n                    form.appendChild( hiddenInput );\n                    form.submit();\n                    return false;\n                }\n                return false;\n            }\n        </script>\n    </head>\n\n    <body>\n        <h2>Dataset generation errors</h2>\n        <p><b>Dataset ')
        __M_writer(unicode(hda.hid))
        __M_writer(u': ')
        __M_writer(filters.html_escape(unicode(hda.display_name() )))
        __M_writer(u'</b></p>\n        ')
        job = hda.creating_job 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['job'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if job:
            __M_writer(u'\n')
            if job.traceback:
                __M_writer(u'                The Galaxy framework encountered the following error while attempting to run the tool:\n                <pre>')
                __M_writer(filters.html_escape(unicode( util.unicodify( job.traceback ) )))
                __M_writer(u'</pre>\n')
            if job.stderr or job.info:
                __M_writer(u'                Tool execution generated the following error message:\n')
                if job.stderr:
                    __M_writer(u'                    <pre>')
                    __M_writer(filters.html_escape(unicode( util.unicodify( job.stderr ) )))
                    __M_writer(u'</pre>\n')
                elif job.info:
                    __M_writer(u'                    <pre>')
                    __M_writer(filters.html_escape(unicode( util.unicodify( job.info ) )))
                    __M_writer(u'</pre>\n')
            else:
                __M_writer(u'                Tool execution did not generate any error messages.\n')
            if job.stdout:
                __M_writer(u'                The tool produced the following additional output:\n                <pre>')
                __M_writer(filters.html_escape(unicode( util.unicodify( job.stdout ) )))
                __M_writer(u'</pre>\n')
        else:
            __M_writer(u'            The tool did not create any additional job / error info.\n')
        __M_writer(u'        ')

        if trans.user:
            user_email = trans.user.email
        else:
            user_email = ''
                
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['user_email'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n        <h2>Report this error to the local Galaxy administrators</h2>\n        <p>\n            Usually the local Galaxy administrators regularly review errors that occur on the server.\n            However, if you would like to provide additional information (such as\n            what you were trying to do when the error occurred) and a contact e-mail\n            address, we will be better able to investigate your problem and get back\n            to you.\n        </p>\n        <div class="toolForm">\n            <div class="toolFormTitle">Error Report</div>\n            <div class="toolFormBody">\n                <form name="report_error" action="')
        __M_writer(unicode(h.url_for(controller='dataset', action='report_error')))
        __M_writer(u'" method="post" >\n                    <input type="hidden" name="id" value="')
        __M_writer(unicode(trans.security.encode_id( hda.id)))
        __M_writer(u'" />\n                    <div class="form-row">\n                        <label>Your email</label>\n                        <input type="text" name="email" size="40" value="')
        __M_writer(filters.html_escape(unicode(user_email)))
        __M_writer(u'" />\n                    </div>\n                    <div class="form-row">\n                        <label>Message</label>\n                        <textarea name="message" rows="10" cols="60"></textarea>\n                    </div>\n                    <div class="form-row">\n                        <input type="submit" name="submit_error_report" value="Report" onclick="return sendReport( this, this.form, \'_self\' );"/>\n')
        if trans.app.config.biostar_url and trans.app.config.biostar_enable_bug_reports:
            __M_writer(u'                            <input type="submit" name="submit_error_report" value="Post on Biostar" onclick="return sendReport( this, this.form, \'_blank\', true );"/>\n')
        __M_writer(u'                    </div>\n                </form>\n            </div>\n      </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "25": 1, "26": 52, "27": 52, "28": 52, "29": 52, "30": 53, "34": 53, "35": 54, "36": 55, "37": 56, "38": 57, "39": 58, "40": 58, "41": 60, "42": 61, "43": 62, "44": 63, "45": 63, "46": 63, "47": 64, "48": 65, "49": 65, "50": 65, "51": 67, "52": 68, "53": 70, "54": 71, "55": 72, "56": 72, "57": 74, "58": 75, "59": 77, "60": 77, "69": 82, "70": 94, "71": 94, "72": 95, "73": 95, "74": 98, "75": 98, "76": 106, "77": 107, "78": 109, "84": 78}, "uri": "dataset/errors.mako", "filename": "templates/webapps/galaxy/dataset/errors.mako"}
__M_END_METADATA
"""
