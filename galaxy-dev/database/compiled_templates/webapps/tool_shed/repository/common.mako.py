# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1466780419.015192
_enable_loop = True
_template_filename = u'templates/webapps/tool_shed/repository/common.mako'
_template_uri = u'/webapps/tool_shed/repository/common.mako'
_source_encoding = 'ascii'
_exports = ['render_tool_dependency_successful_installation', 'render_tool_dependency', 'render_not_tested', 'render_missing_test_component', 'render_folder', 'render_tool', 'render_clone_str', 'render_test_environment', 'container_javascripts', 'render_readme', 'render_tool_dependency_installation_error', 'render_tool_dependency_resolver', 'render_repository_dependency', 'render_repository_successful_installation', 'render_datatype', 'render_failed_test', 'common_javascripts', 'render_valid_data_manager', 'render_repository_installation_error', 'render_invalid_repository_dependency', 'render_invalid_tool', 'render_workflow', 'render_repository_type_select_field', 'render_passed_test', 'render_resolver_dependency_items', 'render_repository_items', 'render_invalid_data_manager', 'render_sharable_str', 'render_table_wrap_style', 'render_invalid_tool_dependency']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency_successful_installation(context,successful_installation,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( successful_installation.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rtdsi-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr bgcolor="#FFFFCC">\n                    <th>Type</th><th>Name</th><th>Version</th>\n                </tr>\n                <tr>\n                    <td>')
        __M_writer(filters.html_escape(unicode(successful_installation.name )))
        __M_writer(u'</td>\n                    <td>')
        __M_writer(filters.html_escape(unicode(successful_installation.type )))
        __M_writer(u'</td>\n                    <td>')
        __M_writer(filters.html_escape(unicode(successful_installation.version )))
        __M_writer(u'</td>\n                </tr>\n                <tr><th>Installation directory</th></tr>\n                <tr><td colspan="3">')
        __M_writer(filters.html_escape(unicode(successful_installation.installation_directory )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency(context,tool_dependency,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from galaxy.util import string_as_bool
        encoded_id = trans.security.encode_id( tool_dependency.id )
        is_missing = tool_dependency.installation_status not in [ 'Installed' ]
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rtd-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n')
        if row_is_header:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(tool_dependency.name )))
            __M_writer(u'\n')
        elif trans.webapp.name == 'galaxy' and tool_dependency.tool_dependency_id:
            if tool_dependency.repository_id and tool_dependency.installation_status in [ trans.install_model.ToolDependency.installation_status.INSTALLED ]:
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_tool_dependency', id=trans.security.encode_id( tool_dependency.tool_dependency_id ) )))
                __M_writer(u'">\n                        ')
                __M_writer(filters.html_escape(unicode(tool_dependency.name )))
                __M_writer(u'\n                    </a>\n')
            elif tool_dependency.installation_status not in [ trans.install_model.ToolDependency.installation_status.UNINSTALLED ]:
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository_tool_dependencies', tool_dependency_ids=trans.security.encode_id( tool_dependency.tool_dependency_id ) )))
                __M_writer(u'">\n                        ')
                __M_writer(unicode(tool_dependency.name))
                __M_writer(u'\n                    </a>\n')
            else:
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(tool_dependency.name )))
                __M_writer(u'\n')
        else:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(tool_dependency.name )))
            __M_writer(u'\n')
        __M_writer(u'        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n            ')

        if tool_dependency.version:
            version_str = tool_dependency.version
        else:
            version_str = ''
                    
        
        __M_writer(u'\n            ')
        __M_writer(filters.html_escape(unicode(version_str )))
        __M_writer(u'\n        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(tool_dependency.type )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n')
        if trans.webapp.name == 'galaxy':
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(tool_dependency.installation_status )))
            __M_writer(u'\n')
        __M_writer(u'        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_not_tested(context,not_tested,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( not_tested.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rnt-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr><td>')
        __M_writer(filters.html_escape(unicode(not_tested.reason )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_missing_test_component(context,missing_test_component,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( missing_test_component.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rmtc-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr><td bgcolor="#FFFFCC"><b>Tool id:</b> ')
        __M_writer(filters.html_escape(unicode(missing_test_component.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool version:</b> ')
        __M_writer(filters.html_escape(unicode(missing_test_component.tool_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool guid:</b> ')
        __M_writer(filters.html_escape(unicode(missing_test_component.tool_guid )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Missing components:</b> <br/>')
        __M_writer(filters.html_escape(unicode(missing_test_component.missing_components )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_folder(context,folder,folder_pad,parent=None,row_counter=None,is_root_folder=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_datatype(datatype,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_datatype(context,datatype,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        h = context.get('h', UNDEFINED)
        def render_tool_dependency(tool_dependency,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
            return render_render_tool_dependency(context,tool_dependency,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_invalid_repository_dependency(invalid_repository_dependency,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
            return render_render_invalid_repository_dependency(context,invalid_repository_dependency,pad,parent,row_counter,render_repository_actions_for)
        def render_invalid_tool_dependency(invalid_tool_dependency,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
            return render_render_invalid_tool_dependency(context,invalid_tool_dependency,pad,parent,row_counter,render_repository_actions_for)
        def render_readme(readme,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
            return render_render_readme(context,readme,pad,parent,row_counter,render_repository_actions_for)
        def render_valid_data_manager(data_manager,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_valid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_invalid_data_manager(data_manager,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_invalid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_invalid_tool(invalid_tool,pad,parent,row_counter,valid=True,render_repository_actions_for='tool_shed'):
            return render_render_invalid_tool(context,invalid_tool,pad,parent,row_counter,valid,render_repository_actions_for)
        str = context.get('str', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        def render_missing_test_component(missing_test_component,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_missing_test_component(context,missing_test_component,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_folder(folder,folder_pad,parent=None,row_counter=None,is_root_folder=False,render_repository_actions_for='tool_shed'):
            return render_render_folder(context,folder,folder_pad,parent,row_counter,is_root_folder,render_repository_actions_for)
        trans = context.get('trans', UNDEFINED)
        def render_repository_dependency(repository_dependency,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_repository_dependency(context,repository_dependency,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_tool(tool,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
            return render_render_tool(context,tool,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        def render_workflow(workflow,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
            return render_render_workflow(context,workflow,pad,parent,row_counter,row_is_header,render_repository_actions_for)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( folder.id )
        
        if is_root_folder:
            pad = folder_pad
            expander = h.url_for("/static/images/silk/resultset_bottom.png")
            folder_img = h.url_for("/static/images/silk/folder_page.png")
        else:
            pad = folder_pad + 20
            expander = h.url_for("/static/images/silk/resultset_next.png")
            folder_img = h.url_for("/static/images/silk/folder.png")
        my_row = None
            
        
        __M_writer(u'\n')
        if not is_root_folder:
            __M_writer(u'        ')

            if parent is None:
                bg_str = 'bgcolor="#D8D8D8"'
            else:
                bg_str = ''
                    
            
            __M_writer(u'\n        <tr id="folder-')
            __M_writer(unicode(encoded_id))
            __M_writer(u'" ')
            __M_writer(unicode(bg_str))
            __M_writer(u' class="folderRow libraryOrFolderRow"\n')
            if parent is not None:
                __M_writer(u'                parent="')
                __M_writer(unicode(parent))
                __M_writer(u'"\n                style="display: none;"\n')
            __M_writer(u'            >\n            ')

            col_span_str = ''
            folder_label = str( folder.label )
            if folder.datatypes:
                col_span_str = 'colspan="4"'
            elif folder.label == 'Missing tool dependencies':
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - repository tools require handling of these missing dependencies</i>" % folder_label
                col_span_str = 'colspan="5"'
            elif folder.label in [ 'Installed repository dependencies', 'Repository dependencies', 'Missing repository dependencies' ]:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                elif folder.label not in [ 'Installed repository dependencies' ] and folder.parent.label not in [ 'Installation errors' ]:
                    folder_label = "%s<i> - installation of these additional repositories is required</i>" % folder_label
                if trans.webapp.name == 'galaxy':
                    col_span_str = 'colspan="4"'
            elif folder.label == 'Invalid repository dependencies':
                folder_label = "%s<i> - click the repository dependency to see why it is invalid</i>" % folder_label
            elif folder.label == 'Invalid tool dependencies':
                folder_label = "%s<i> - click the tool dependency to see why it is invalid</i>" % folder_label
            elif folder.label == 'Valid tools':
                col_span_str = 'colspan="3"'
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - click the name to preview the tool and use the pop-up menu to inspect all metadata</i>" % folder_label
            elif folder.invalid_tools:
                if trans.webapp.name == 'tool_shed':
                    folder_label = "%s<i> - click the tool config file name to see why the tool is invalid</i>" % folder_label
            elif folder.tool_dependencies:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - repository tools require handling of these dependencies</i>" % folder_label
                col_span_str = 'colspan="4"'
            elif folder.workflows:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                else:
                    folder_label = "%s<i> - click the name to view an SVG image of the workflow</i>" % folder_label
                col_span_str = 'colspan="4"'
            elif folder.valid_data_managers:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                col_span_str = 'colspan="3"'
            elif folder.invalid_data_managers:
                if folder.description:
                    folder_label = "%s<i> - %s</i>" % ( folder_label, folder.description )
                col_span_str = 'colspan="2"'
                        
            
            __M_writer(u'\n            <td ')
            __M_writer(unicode(col_span_str))
            __M_writer(u' style="padding-left: ')
            __M_writer(unicode(folder_pad))
            __M_writer(u'px;">\n                <span class="expandLink folder-')
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click">\n                    <div style="float: left; margin-left: 2px;" class="expandLink folder-')
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click">\n                        <a class="folder-')
            __M_writer(unicode(encoded_id))
            __M_writer(u'-click" href="javascript:void(0);">\n                            ')
            __M_writer(unicode(folder_label))
            __M_writer(u'\n                        </a>\n                    </div>\n                </span>\n            </td>\n        </tr>\n        ')

            my_row = row_counter.count
            row_counter.increment()
                    
            
            __M_writer(u'\n')
        for sub_folder in folder.folders:
            __M_writer(u'        ')
            __M_writer(unicode(render_folder( sub_folder, pad, parent=my_row, row_counter=row_counter, is_root_folder=False, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        for readme in folder.readme_files:
            __M_writer(u'        ')
            __M_writer(unicode(render_readme( readme, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        for invalid_repository_dependency in folder.invalid_repository_dependencies:
            __M_writer(u'        ')
            __M_writer(unicode(render_invalid_repository_dependency( invalid_repository_dependency, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        for index, repository_dependency in enumerate( folder.repository_dependencies ):
            __M_writer(u'        ')
            row_is_header = index == 0 
            
            __M_writer(u'\n        ')
            __M_writer(unicode(render_repository_dependency( repository_dependency, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        for invalid_tool_dependency in folder.invalid_tool_dependencies:
            __M_writer(u'        ')
            __M_writer(unicode(render_invalid_tool_dependency( invalid_tool_dependency, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        for index, tool_dependency in enumerate( folder.tool_dependencies ):
            __M_writer(u'        ')
            row_is_header = index == 0 
            
            __M_writer(u'\n        ')
            __M_writer(unicode(render_tool_dependency( tool_dependency, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        if folder.valid_tools:
            for index, tool in enumerate( folder.valid_tools ):
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                __M_writer(unicode(render_tool( tool, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
        for invalid_tool in folder.invalid_tools:
            __M_writer(u'        ')
            __M_writer(unicode(render_invalid_tool( invalid_tool, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n')
        if folder.workflows:
            for index, workflow in enumerate( folder.workflows ):
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                __M_writer(unicode(render_workflow( workflow, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
        if folder.datatypes:
            for index, datatype in enumerate( folder.datatypes ):
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                __M_writer(unicode(render_datatype( datatype, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
        if folder.valid_data_managers:
            for index, data_manager in enumerate( folder.valid_data_managers ):
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                __M_writer(unicode(render_valid_data_manager( data_manager, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
        if folder.invalid_data_managers:
            for index, data_manager in enumerate( folder.invalid_data_managers ):
                __M_writer(u'            ')
                row_is_header = index == 0 
                
                __M_writer(u'\n            ')
                __M_writer(unicode(render_invalid_data_manager( data_manager, pad, my_row, row_counter, row_is_header, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
        if folder.missing_test_components:
            for missing_test_component in folder.missing_test_components:
                __M_writer(u'            ')
                __M_writer(unicode(render_missing_test_component( missing_test_component, pad, my_row, row_counter, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool(context,tool,pad,parent,row_counter,row_is_header,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( tool.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rt-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n')
        if row_is_header:
            __M_writer(u'            <th style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">')
            __M_writer(filters.html_escape(unicode(tool.name )))
            __M_writer(u'</th>\n')
        else:
            __M_writer(u'            <td style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n')
            if tool.repository_id:
                if trans.webapp.name == 'tool_shed':
                    __M_writer(u'                        <div style="float:left;" class="menubutton split popup" id="tool-')
                    __M_writer(unicode(encoded_id))
                    __M_writer(u'-popup">\n                            <a class="view-info" href="')
                    __M_writer(unicode(h.url_for( controller='repository', action='display_tool', repository_id=trans.security.encode_id( tool.repository_id ), tool_config=tool.tool_config, changeset_revision=tool.changeset_revision, render_repository_actions_for=render_repository_actions_for )))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(unicode(tool.name )))
                    __M_writer(u'</a>\n                        </div>\n                        <div popupmenu="tool-')
                    __M_writer(unicode(encoded_id))
                    __M_writer(u'-popup">\n                            <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='repository', action='view_tool_metadata', repository_id=trans.security.encode_id( tool.repository_id ), changeset_revision=tool.changeset_revision, tool_id=tool.tool_id, render_repository_actions_for=render_repository_actions_for )))
                    __M_writer(u'">View tool metadata</a>\n                        </div>\n')
                elif trans.webapp.name == 'galaxy':
                    if tool.repository_installation_status == trans.install_model.ToolShedRepository.installation_status.INSTALLED:
                        __M_writer(u'                            <a class="action-button" href="')
                        __M_writer(unicode(h.url_for( controller='admin_toolshed', action='view_tool_metadata', repository_id=trans.security.encode_id( tool.repository_id ), changeset_revision=tool.changeset_revision, tool_id=tool.tool_id )))
                        __M_writer(u'">')
                        __M_writer(filters.html_escape(unicode(tool.name )))
                        __M_writer(u'</a>\n')
                    else:
                        __M_writer(u'                            ')
                        __M_writer(filters.html_escape(unicode(tool.name )))
                        __M_writer(u'\n')
                else:
                    __M_writer(u'                        ')
                    __M_writer(filters.html_escape(unicode(tool.name )))
                    __M_writer(u'\n')
            else:
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(tool.name )))
                __M_writer(u'\n')
            __M_writer(u'            </td>\n')
        __M_writer(u'        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(tool.description )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(tool.version )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n')
        __M_writer(u'    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_clone_str(context,repository):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()

        from tool_shed.util.common_util import generate_clone_url_for_repository_in_tool_shed
        clone_str = generate_clone_url_for_repository_in_tool_shed( trans.user, repository )
            
        
        __M_writer(u'hg clone ')
        __M_writer(unicode( clone_str ))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_test_environment(context,test_environment,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        encoded_id = trans.security.encode_id( test_environment.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rte-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table class="grid" id="test_environment">\n                <tr><td><b>Time tested:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.time_tested )))
        __M_writer(u'</td></tr>\n                <tr><td><b>System:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.system )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Architecture:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.architecture )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Python version:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.python_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Galaxy revision:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.galaxy_revision )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Galaxy database version:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.galaxy_database_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool shed revision:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.tool_shed_revision )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool shed database version:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.tool_shed_database_version )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool shed mercurial version:</b> ')
        __M_writer(filters.html_escape(unicode(test_environment.tool_shed_mercurial_version )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        repository = context.get('repository', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <script type="text/javascript">\n        var init_dependencies = function() {\n            var storage_id = "library-expand-state-')
        __M_writer(unicode(trans.security.encode_id(10000)))
        __M_writer(u'";\n            var restore_folder_state = function() {\n                var state = $.jStorage.get(storage_id);\n                if (state) {\n                    for (var id in state) {\n                        if (state[id] === true) {\n                            var row = $("#" + id),\n                                index = row.parent().children().index(row);\n                            row.addClass("expanded").show();\n                            row.siblings().filter("tr[parent=\'" + index + "\']").show();\n                        }\n                    }\n                }\n            };\n            var save_folder_state = function() {\n                var state = {};\n                $("tr.folderRow").each( function() {\n                    var folder = $(this);\n                    state[folder.attr("id")] = folder.hasClass("expanded");\n                });\n                $.jStorage.set(storage_id, state);\n            };\n            $(".container-table").each(function() {\n                //var container_id = this.id.split( "-" )[0];\n                //alert( container_id );\n                var child_of_parent_cache = {};\n                // Recursively fill in children and descendants of each row\n                var process_row = function(q, parents) {\n                    // Find my index\n                    var parent = q.parent(),\n                        this_level = child_of_parent_cache[parent] || (child_of_parent_cache[parent] = parent.children());\n                    var index = this_level.index(q);\n                    // Find my immediate children\n                    var children = $(par_child_dict[index]);\n                    // Recursively handle them\n                    var descendants = children;\n                    children.each( function() {\n                        child_descendants = process_row( $(this), parents.add(q) );\n                        descendants = descendants.add(child_descendants);\n                    });\n                    // Set up expand / hide link\n                    var expand_fn = function() {\n                        if ( q.hasClass("expanded") ) {\n                            descendants.hide();\n                            descendants.removeClass("expanded");\n                            q.removeClass("expanded");\n                        } else {\n                            children.show();\n                            q.addClass("expanded");\n                        }\n                        save_folder_state();\n                    };\n                    $("." + q.attr("id") + "-click").click(expand_fn);\n                    // return descendants for use by parent\n                    return descendants;\n                }\n                // Initialize dict[parent_id] = rows_which_have_that_parent_id_as_parent_attr\n                var par_child_dict = {},\n                    no_parent = [];\n                $(this).find("tbody tr").each( function() {\n                    if ( $(this).attr("parent")) {\n                        var parent = $(this).attr("parent");\n                        if (par_child_dict[parent] !== undefined) {\n                            par_child_dict[parent].push(this);\n                        } else {\n                            par_child_dict[parent] = [this];\n                        }\n                    } else {\n                        no_parent.push(this);\n                    }\n                });\n                $(no_parent).each( function() {\n                    descendants = process_row( $(this), $([]) );\n                    descendants.hide();\n               });\n            });\n            restore_folder_state();\n        };\n\n        var init_clipboard = function() {\n')
        if hasattr( repository, 'clone_url' ):
            __M_writer(u'                    $(\'#clone_clipboard\').on(\'click\', function( event ) {\n                        event.preventDefault();\n                        window.prompt("Copy to clipboard: Ctrl+C, Enter", "hg clone ')
            __M_writer(unicode( repository.clone_url ))
            __M_writer(u'");\n                    });\n')
        if hasattr( repository, 'share_url' ):
            __M_writer(u'                    $(\'#share_clipboard\').on(\'click\', function( event ) {\n                        event.preventDefault();\n                        window.prompt("Copy to clipboard: Ctrl+C, Enter", "')
            __M_writer(unicode( repository.share_url ))
            __M_writer(u'");\n                    });\n')
        __M_writer(u'        };\n\n        $(function() {\n            init_dependencies();\n            init_clipboard();\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_readme(context,readme,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        encoded_id = trans.security.encode_id( readme.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rr-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="readme_files">\n                <tr><td>')
        __M_writer(unicode( readme.text ))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency_installation_error(context,installation_error,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from galaxy.util import unicodify
        encoded_id = trans.security.encode_id( installation_error.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rtdie-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr bgcolor="#FFFFCC">\n                    <th>Type</th><th>Name</th><th>Version</th>\n                </tr>\n                <tr>\n                    <td>')
        __M_writer(filters.html_escape(unicode(installation_error.name )))
        __M_writer(u'</td>\n                    <td>')
        __M_writer(filters.html_escape(unicode(installation_error.type )))
        __M_writer(u'</td>\n                    <td>')
        __M_writer(filters.html_escape(unicode(installation_error.version )))
        __M_writer(u'</td>\n                </tr>\n                <tr><th>Error</th></tr>\n                <tr><td colspan="3">')
        __M_writer(filters.html_escape(unicode(unicodify( installation_error.error_message ) )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_dependency_resolver(context,resolver_dependencies):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    <tr class="datasetRow">\n        <td style="padding-left: 20 px;">\n            <table class="grid" id="module_resolver_environment">\n')
        if resolver_dependencies['model_class'] == 'NullDependency':
            __M_writer(u'                   <tr>\n                        <td><b> Dependency was not resolved by any resolver module.</b></td>\n                   </tr>\n')
        else:
            __M_writer(u'                   <tr>\n                       <td><b>Dependency Resolver </b></td>\n                       <td> ')
            __M_writer(filters.html_escape(unicode(resolver_dependencies['model_class'] )))
            __M_writer(u'</td>\n                   </tr>\n                   <tr>\n                       <td><b>Exact </b></td>\n                       <td> ')
            __M_writer(filters.html_escape(unicode(resolver_dependencies['exact'] )))
            __M_writer(u'</td>\n                   </tr>\n                   <tr>\n                       <td><b>Dependency Type</b></td>\n                      <td> ')
            __M_writer(filters.html_escape(unicode(resolver_dependencies['dependency_type'] )))
            __M_writer(u'</td>\n                   </tr>\n')
        __M_writer(u'            </table>\n        </td>\n    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_dependency(context,repository_dependency,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from galaxy.util import asbool
        from tool_shed.util.shed_util_common import get_repository_by_name_and_owner
        encoded_id = trans.security.encode_id( repository_dependency.id )
        if trans.webapp.name == 'galaxy':
            if repository_dependency.tool_shed_repository_id:
                encoded_required_repository_id = trans.security.encode_id( repository_dependency.tool_shed_repository_id )
            else:
                encoded_required_repository_id = None
            if repository_dependency.installation_status:
                installation_status = str( repository_dependency.installation_status )
            else:
                installation_status = None
        repository_name = str( repository_dependency.repository_name )
        repository_owner = str( repository_dependency.repository_owner )
        changeset_revision = str( repository_dependency.changeset_revision )
        if asbool( str( repository_dependency.prior_installation_required ) ):
            prior_installation_required_str = " <i>(prior install required)</i>"
        else:
            prior_installation_required_str = ""
        if trans.webapp.name == 'galaxy':
            if row_is_header:
                cell_type = 'th'
            else:
                cell_type = 'td'
            rd = None
        else:
            # We're in the tool shed.
            cell_type = 'td'
            rd = get_repository_by_name_and_owner( trans.app, repository_name, repository_owner )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rrd-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n')
        if trans.webapp.name == 'galaxy':
            __M_writer(u'            <')
            __M_writer(unicode(cell_type))
            __M_writer(u' style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n')
            if row_is_header:
                __M_writer(u'                    ')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'\n')
            elif encoded_required_repository_id:
                __M_writer(u'                    <a class="action-button" href="')
                __M_writer(unicode(h.url_for( controller='admin_toolshed', action='manage_repository', id=encoded_required_repository_id )))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'</a>\n')
            else:
                __M_writer(u'                   ')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'\n')
            __M_writer(u'            </')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n            <')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n                ')
            __M_writer(filters.html_escape(unicode(changeset_revision )))
            __M_writer(u'\n            </')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n            <')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n                ')
            __M_writer(filters.html_escape(unicode(repository_owner )))
            __M_writer(u'\n            </')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n            <')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n                ')
            __M_writer(unicode(installation_status))
            __M_writer(u'\n            </')
            __M_writer(unicode(cell_type))
            __M_writer(u'>\n')
        else:
            __M_writer(u'            <td style="padding-left: ')
            __M_writer(unicode(pad+20))
            __M_writer(u'px;">\n')
            if render_repository_actions_for == 'tool_shed' and rd:
                __M_writer(u'                    <a class="view-info" href="')
                __M_writer(unicode(h.url_for( controller='repository', action='view_or_manage_repository', id=trans.security.encode_id( rd.id ), changeset_revision=changeset_revision )))
                __M_writer(u'">Repository <b>')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'</b> revision <b>')
                __M_writer(filters.html_escape(unicode(changeset_revision )))
                __M_writer(u'</b> owned by <b>')
                __M_writer(filters.html_escape(unicode(repository_owner )))
                __M_writer(u'</b></a>')
                __M_writer(unicode(prior_installation_required_str))
                __M_writer(u'\n')
            else:
                __M_writer(u'                    Repository <b>')
                __M_writer(filters.html_escape(unicode(repository_name )))
                __M_writer(u'</b> revision <b>')
                __M_writer(filters.html_escape(unicode(changeset_revision )))
                __M_writer(u'</b> owned by <b>')
                __M_writer(filters.html_escape(unicode(repository_owner )))
                __M_writer(u'</b>')
                __M_writer(unicode(prior_installation_required_str))
                __M_writer(u'\n')
            __M_writer(u'            </td>\n')
        __M_writer(u'    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_successful_installation(context,successful_installation,pad,parent,row_counter,row_is_header=False,is_current_repository=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( successful_installation.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rrsi-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n')
        if not is_current_repository:
            __M_writer(u'                    <tr bgcolor="#FFFFCC">\n                        <th>Tool shed</th><th>Name</th><th>Owner</th><th>Changeset revision</th>\n                    </tr>\n                    <tr>\n                        <td>')
            __M_writer(filters.html_escape(unicode(successful_installation.tool_shed )))
            __M_writer(u'</td>\n                        <td>')
            __M_writer(filters.html_escape(unicode(successful_installation.name )))
            __M_writer(u'</td>\n                        <td>')
            __M_writer(filters.html_escape(unicode(successful_installation.owner )))
            __M_writer(u'</td>\n                        <td>')
            __M_writer(filters.html_escape(unicode(successful_installation.changeset_revision )))
            __M_writer(u'</td>\n                    </tr>\n')
        __M_writer(u'            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_datatype(context,datatype,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( datatype.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rd-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">')
        __M_writer(filters.html_escape(unicode(datatype.extension )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(datatype.type )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(datatype.mimetype )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(datatype.subclass )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_failed_test(context,failed_test,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from tool_shed.util.basic_util import to_html_string
        encoded_id = trans.security.encode_id( failed_test.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rft-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr><td bgcolor="#FFFFCC"><b>Tool id:</b> ')
        __M_writer(filters.html_escape(unicode(failed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool version:</b> ')
        __M_writer(filters.html_escape(unicode(failed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Test:</b> ')
        __M_writer(filters.html_escape(unicode(failed_test.test_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Stderr:</b> <br/>')
        __M_writer(unicode( to_html_string( failed_test.stderr ) ))
        __M_writer(u'</td></tr>\n                <tr><td><b>Traceback:</b> <br/>')
        __M_writer(unicode( to_html_string( failed_test.traceback ) ))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_common_javascripts(context,repository):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <script type="text/javascript">\n        $(function(){\n\n            // --- Initialize sample trees\n            $("#tree").dynatree({\n                title: "')
        __M_writer(unicode(repository.name))
        __M_writer(u'",\n                minExpandLevel: 1,\n                persist: false,\n                checkbox: true,\n                selectMode: 3,\n                onPostInit: function(isReloading, isError) {\n                    // Re-fire onActivate, so the text is updated\n                    this.reactivate();\n                },\n                fx: { height: "toggle", duration: 200 },\n                // initAjax is hard to fake, so we pass the children as object array:\n                initAjax: {url: "')
        __M_writer(unicode(h.url_for( controller='repository', action='open_folder' )))
        __M_writer(u'",\n                           dataType: "json",\n                           data: { folder_path: "')
        __M_writer(unicode(repository.repo_path( trans.app )))
        __M_writer(u'", repository_id: "')
        __M_writer(unicode(trans.security.encode_id( repository.id )))
        __M_writer(u'"  },\n                },\n                onLazyRead: function(dtnode){\n                    dtnode.appendAjax({\n                        url: "')
        __M_writer(unicode(h.url_for( controller='repository', action='open_folder' )))
        __M_writer(u'",\n                        dataType: "json",\n                        data: { folder_path: dtnode.data.key, repository_id: "')
        __M_writer(unicode(trans.security.encode_id( repository.id )))
        __M_writer(u'"  },\n                    });\n                },\n                onSelect: function(select, dtnode) {\n                    // Display list of selected nodes\n                    var selNodes = dtnode.tree.getSelectedNodes();\n                    // convert to title/key array\n                    var selKeys = $.map(selNodes, function(node) {\n                        return node.data.key;\n                    });\n                    if (document.forms["select_files_to_delete"]) {\n                        // The following is used only ~/templates/webapps/tool_shed/repository/browse_repository.mako.\n                        document.select_files_to_delete.selected_files_to_delete.value = selKeys.join(",");\n                    }\n                    // The following is used only in ~/templates/webapps/tool_shed/repository/upload.mako.\n                    if (document.forms["upload_form"]) {\n                        document.upload_form.upload_point.value = selKeys.slice(-1);\n                    }\n                },\n                onActivate: function(dtnode) {\n                    var cell = $("#file_contents");\n                    var selected_value;\n                     if (dtnode.data.key == \'root\') {\n                        selected_value = "')
        __M_writer(unicode(repository.repo_path( trans.app )))
        __M_writer(u'/";\n                    } else {\n                        selected_value = dtnode.data.key;\n                    };\n                    if (selected_value.charAt(selected_value.length-1) != \'/\') {\n                        // Make ajax call\n                        $.ajax( {\n                            type: "POST",\n                            url: "')
        __M_writer(unicode(h.url_for( controller='repository', action='get_file_contents' )))
        __M_writer(u'",\n                            dataType: "json",\n                            data: { file_path: selected_value, repository_id: "')
        __M_writer(unicode(trans.security.encode_id( repository.id )))
        __M_writer(u'" },\n                            success : function ( data ) {\n                                cell.html( \'<label>\'+data+\'</label>\' )\n                            }\n                        });\n                    } else {\n                        cell.html( \'\' );\n                    };\n                },\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_valid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( data_manager.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rvdm-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">')
        __M_writer(filters.html_escape(unicode(data_manager.name )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(data_manager.version )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(data_manager.data_tables )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_installation_error(context,installation_error,pad,parent,row_counter,row_is_header=False,is_current_repository=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from galaxy.util import unicodify
        encoded_id = trans.security.encode_id( installation_error.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rrie-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n')
        if not is_current_repository:
            __M_writer(u'                    <tr bgcolor="#FFFFCC">\n                        <th>Tool shed</th><th>Name</th><th>Owner</th><th>Changeset revision</th>\n                    </tr>\n                    <tr>\n                        <td>')
            __M_writer(filters.html_escape(unicode(installation_error.tool_shed )))
            __M_writer(u'</td>\n                        <td>')
            __M_writer(filters.html_escape(unicode(installation_error.name )))
            __M_writer(u'</td>\n                        <td>')
            __M_writer(filters.html_escape(unicode(installation_error.owner )))
            __M_writer(u'</td>\n                        <td>')
            __M_writer(filters.html_escape(unicode(installation_error.changeset_revision )))
            __M_writer(u'</td>\n                    </tr>\n')
        __M_writer(u'                <tr><th>Error</th></tr>\n                <tr><td colspan="4">')
        __M_writer(filters.html_escape(unicode(unicodify( installation_error.error_message ) )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_repository_dependency(context,invalid_repository_dependency,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( invalid_repository_dependency.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rird-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            ')
        __M_writer(filters.html_escape(unicode( invalid_repository_dependency.error )))
        __M_writer(u'\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_tool(context,invalid_tool,pad,parent,row_counter,valid=True,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        encoded_id = trans.security.encode_id( invalid_tool.id ) 
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rit-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n')
        if trans.webapp.name == 'tool_shed' and invalid_tool.repository_id and invalid_tool.tool_config and invalid_tool.changeset_revision:
            __M_writer(u'                <a class="view-info" href="')
            __M_writer(unicode(h.url_for( controller='repository', action='load_invalid_tool', repository_id=trans.security.encode_id( invalid_tool.repository_id ), tool_config=invalid_tool.tool_config, changeset_revision=invalid_tool.changeset_revision, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'">\n                    ')
            __M_writer(filters.html_escape(unicode(invalid_tool.tool_config )))
            __M_writer(u'\n                </a>\n')
        else:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(invalid_tool.tool_config )))
            __M_writer(u'\n')
        __M_writer(u'        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_workflow(context,workflow,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from tool_shed.util.encoding_util import tool_shed_encode
        encoded_id = trans.security.encode_id( workflow.id )
        encoded_workflow_name = tool_shed_encode( workflow.workflow_name )
        if trans.webapp.name == 'tool_shed':
            encoded_repository_metadata_id = trans.security.encode_id( workflow.repository_metadata_id )
            encoded_repository_id = None
        else:
            encoded_repository_metadata_id = None
            encoded_repository_id = trans.security.encode_id( workflow.repository_id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rw-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n')
        if row_is_header:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'\n')
        elif trans.webapp.name == 'tool_shed' and encoded_repository_metadata_id:
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='repository', action='view_workflow', workflow_name=encoded_workflow_name, repository_metadata_id=encoded_repository_metadata_id, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'</a>\n')
        elif trans.webapp.name == 'galaxy' and encoded_repository_id:
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='view_workflow', workflow_name=encoded_workflow_name, repository_id=encoded_repository_id )))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'</a>\n')
        else:
            __M_writer(u'                ')
            __M_writer(filters.html_escape(unicode(workflow.workflow_name )))
            __M_writer(u'\n')
        __M_writer(u'        </')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(workflow.steps )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(workflow.format_version )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(workflow.annotation )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_type_select_field(context,repository_type_select_field,render_help=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="form-row">\n        <label>Repository type:</label>\n        ')

        from tool_shed.repository_types import util
        options = repository_type_select_field.options
        repository_types = []
        for option_tup in options:
            repository_types.append( option_tup[ 1 ] )
        render_as_text = len( options ) == 1
        if render_as_text:
            repository_type = options[ 0 ][ 0 ]
                
        
        __M_writer(u'\n')
        if render_as_text:
            __M_writer(u'            ')
            __M_writer(filters.html_escape(unicode(repository_type )))
            __M_writer(u'\n')
            if render_help:
                __M_writer(u'                <div class="toolParamHelp" style="clear: both;">\n                    This repository\'s type cannot be changed because its contents are valid only for its current type or it has been cloned.\n                </div>\n')
        else:
            __M_writer(u'            ')
            __M_writer(unicode(repository_type_select_field.get_html()))
            __M_writer(u'\n')
            if render_help:
                __M_writer(u'                <div class="toolParamHelp" style="clear: both;">\n                    Select the repository type based on the following criteria.\n                    <ul>\n')
                if util.UNRESTRICTED in repository_types:
                    __M_writer(u'                            <li><b>Unrestricted</b> - contents can be any set of valid Galaxy utilities or files\n')
                if util.REPOSITORY_SUITE_DEFINITION in repository_types:
                    __M_writer(u'                            <li><b>Repository suite definition</b> - contents will always be restricted to one file named repository_dependencies.xml\n')
                if util.TOOL_DEPENDENCY_DEFINITION in repository_types:
                    __M_writer(u'                            <li><b>Tool dependency definition</b> - contents will always be restricted to one file named tool_dependencies.xml\n')
                __M_writer(u'                    </ul>\n                </div>\n')
        __M_writer(u'        <div style="clear: both"></div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_passed_test(context,passed_test,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( passed_test.id )
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-rpt-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="test_environment">\n                <tr><td bgcolor="#FFFFCC"><b>Tool id:</b> ')
        __M_writer(filters.html_escape(unicode(passed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Tool version:</b> ')
        __M_writer(filters.html_escape(unicode(passed_test.tool_id )))
        __M_writer(u'</td></tr>\n                <tr><td><b>Test:</b> ')
        __M_writer(filters.html_escape(unicode(passed_test.test_id )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_resolver_dependency_items(context,resolver_dependencies):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_tool_dependency_resolver(resolver_dependencies):
            return render_render_tool_dependency_resolver(context,resolver_dependencies)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if resolver_dependencies:
            __M_writer(u'        <div class="toolForm">\n            <div class="toolFormTitle">Dependency Resolver Details</div>\n            <div class="toolFormBody">\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="module_resolvers">\n                    ')
            __M_writer(unicode(render_tool_dependency_resolver( resolver_dependencies)))
            __M_writer(u'\n                </table>\n            </div>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_repository_items(context,metadata,containers_dict,can_set_metadata=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_table_wrap_style(table_id):
            return render_render_table_wrap_style(context,table_id)
        def render_folder(folder,folder_pad,parent=None,row_counter=None,is_root_folder=False,render_repository_actions_for='tool_shed'):
            return render_render_folder(context,folder,folder_pad,parent,row_counter,is_root_folder,render_repository_actions_for)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from tool_shed.util.encoding_util import tool_shed_encode
        
        has_datatypes = metadata and 'datatypes' in metadata
        has_readme_files = metadata and 'readme_files' in metadata
        has_workflows = metadata and 'workflows' in metadata
        
        datatypes_root_folder = containers_dict.get( 'datatypes', None )
        invalid_data_managers_root_folder = containers_dict.get( 'invalid_data_managers', None )
        invalid_repository_dependencies_root_folder = containers_dict.get( 'invalid_repository_dependencies', None )
        invalid_tool_dependencies_root_folder = containers_dict.get( 'invalid_tool_dependencies', None )
        invalid_tools_root_folder = containers_dict.get( 'invalid_tools', None )
        missing_repository_dependencies_root_folder = containers_dict.get( 'missing_repository_dependencies', None )
        missing_tool_dependencies_root_folder = containers_dict.get( 'missing_tool_dependencies', None )
        readme_files_root_folder = containers_dict.get( 'readme_files', None )
        repository_dependencies_root_folder = containers_dict.get( 'repository_dependencies', None )
        test_environment_root_folder = containers_dict.get( 'test_environment', None )
        tool_dependencies_root_folder = containers_dict.get( 'tool_dependencies', None )
        tool_test_results_root_folder = containers_dict.get( 'tool_test_results', None )
        valid_data_managers_root_folder = containers_dict.get( 'valid_data_managers', None )
        valid_tools_root_folder = containers_dict.get( 'valid_tools', None )
        workflows_root_folder = containers_dict.get( 'workflows', None )
        
        has_contents = datatypes_root_folder or invalid_tools_root_folder or valid_tools_root_folder or workflows_root_folder
        has_dependencies = \
            invalid_repository_dependencies_root_folder or \
            invalid_tool_dependencies_root_folder or \
            missing_repository_dependencies_root_folder or \
            repository_dependencies_root_folder or \
            tool_dependencies_root_folder or \
            missing_tool_dependencies_root_folder
        
        class RowCounter( object ):
            def __init__( self ):
                self.count = 0
            def increment( self ):
                self.count += 1
            def __str__( self ):
                return str( self.count )
            
        
        __M_writer(u'\n')
        if readme_files_root_folder:
            __M_writer(u'        ')
            __M_writer(unicode(render_table_wrap_style( "readme_files" )))
            __M_writer(u'\n        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">Repository README files - may contain important installation or license information</div>\n            <div class="toolFormBody">\n                <p/>\n                ')
            row_counter = RowCounter() 
            
            __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="readme_files">\n                    ')
            __M_writer(unicode(render_folder( readme_files_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n                </table>\n            </div>\n        </div>\n')
        if has_dependencies:
            __M_writer(u'        <div class="toolForm">\n            <div class="toolFormTitle">Dependencies of this repository</div>\n            <div class="toolFormBody">\n')
            if invalid_repository_dependencies_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_repository_dependencies">\n                        ')
                __M_writer(unicode(render_folder( invalid_repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if missing_repository_dependencies_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="missing_repository_dependencies">\n                        ')
                __M_writer(unicode(render_folder( missing_repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if repository_dependencies_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="repository_dependencies">\n                        ')
                __M_writer(unicode(render_folder( repository_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if invalid_tool_dependencies_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_tool_dependencies">\n                        ')
                __M_writer(unicode(render_folder( invalid_tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if tool_dependencies_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="tool_dependencies">\n                        ')
                __M_writer(unicode(render_folder( tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if missing_tool_dependencies_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="missing_tool_dependencies">\n                        ')
                __M_writer(unicode(render_folder( missing_tool_dependencies_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            __M_writer(u'            </div>\n        </div>\n')
        if has_contents:
            __M_writer(u'        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">Contents of this repository</div>\n            <div class="toolFormBody">\n')
            if valid_tools_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="valid_tools">\n                        ')
                __M_writer(unicode(render_folder( valid_tools_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if invalid_tools_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_tools">\n                        ')
                __M_writer(unicode(render_folder( invalid_tools_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if valid_data_managers_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="valid_data_managers">\n                        ')
                __M_writer(unicode(render_folder( valid_data_managers_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if invalid_data_managers_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="invalid_data_managers">\n                        ')
                __M_writer(unicode(render_folder( invalid_data_managers_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if workflows_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="workflows">\n                        ')
                __M_writer(unicode(render_folder( workflows_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            if datatypes_root_folder:
                __M_writer(u'                    <p/>\n                    ')
                row_counter = RowCounter() 
                
                __M_writer(u'\n                    <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="datatypes">\n                        ')
                __M_writer(unicode(render_folder( datatypes_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
                __M_writer(u'\n                    </table>\n')
            __M_writer(u'            </div>\n        </div>\n')
        if tool_test_results_root_folder and trans.app.config.display_legacy_test_results:
            __M_writer(u'        ')
            __M_writer(unicode(render_table_wrap_style( "test_environment" )))
            __M_writer(u'\n        <p/>\n        <div class="toolForm">\n            <div class="toolFormTitle">Automated tool test results</div>\n            <div class="toolFormBody">\n                <p/>\n                ')
            row_counter = RowCounter() 
            
            __M_writer(u'\n                <table cellspacing="2" cellpadding="2" border="0" width="100%" class="tables container-table" id="test_environment">\n                    ')
            __M_writer(unicode(render_folder( tool_test_results_root_folder, 0, parent=None, row_counter=row_counter, is_root_folder=True, render_repository_actions_for=render_repository_actions_for )))
            __M_writer(u'\n                </table>\n            </div>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_data_manager(context,data_manager,pad,parent,row_counter,row_is_header=False,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( data_manager.id )
        if row_is_header:
            cell_type = 'th'
        else:
            cell_type = 'td'
            
        
        __M_writer(u'\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-ridm-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u' style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">')
        __M_writer(filters.html_escape(unicode(data_manager.index )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n        <')
        __M_writer(unicode(cell_type))
        __M_writer(u'>')
        __M_writer(filters.html_escape(unicode(data_manager.error )))
        __M_writer(u'</')
        __M_writer(unicode(cell_type))
        __M_writer(u'>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_sharable_str(context,repository,changeset_revision=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from tool_shed.util.shed_util_common import generate_sharable_link_for_repository_in_tool_shed
        sharable_link = generate_sharable_link_for_repository_in_tool_shed( repository, changeset_revision=changeset_revision )
            
        
        __M_writer(u'\n    <a href="')
        __M_writer(unicode( sharable_link ))
        __M_writer(u'" target="_blank">')
        __M_writer(unicode( sharable_link ))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_table_wrap_style(context,table_id):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    <style type="text/css">\n        table.')
        __M_writer(unicode(table_id))
        __M_writer(u'{ table-layout:fixed;\n                           width:100%;\n                           overflow-wrap:normal;\n                           overflow:hidden;\n                           border:0px;\n                           word-break:keep-all;\n                           word-wrap:break-word;\n                           line-break:strict; }\n        ul{ list-style-type: disc;\n            padding-left: 20px; }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_invalid_tool_dependency(context,invalid_tool_dependency,pad,parent,row_counter,render_repository_actions_for='tool_shed'):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        encoded_id = trans.security.encode_id( invalid_tool_dependency.id )
            
        
        __M_writer(u'\n    <style type="text/css">\n        #invalid_td_table{ table-layout:fixed;\n                           width:100%;\n                           overflow-wrap:normal;\n                           overflow:hidden;\n                           border:0px;\n                           word-break:keep-all;\n                           word-wrap:break-word;\n                           line-break:strict; }\n    </style>\n    <tr class="datasetRow"\n')
        if parent is not None:
            __M_writer(u'            parent="')
            __M_writer(unicode(parent))
            __M_writer(u'"\n')
        __M_writer(u'        id="libraryItem-ritd-')
        __M_writer(unicode(encoded_id))
        __M_writer(u'">\n        <td style="padding-left: ')
        __M_writer(unicode(pad+20))
        __M_writer(u'px;">\n            <table id="invalid_td_table">\n                <tr><td>')
        __M_writer(filters.html_escape(unicode( invalid_tool_dependency.error )))
        __M_writer(u'</td></tr>\n            </table>\n        </td>\n    </tr>\n    ')

        my_row = row_counter.count
        row_counter.increment()
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "21": 71, "22": 175, "23": 218, "24": 226, "25": 231, "26": 385, "27": 409, "28": 435, "29": 457, "30": 476, "31": 499, "32": 530, "33": 554, "34": 573, "35": 645, "36": 660, "37": 691, "38": 721, "39": 755, "40": 786, "41": 807, "42": 830, "43": 879, "44": 935, "45": 962, "46": 985, "47": 1027, "48": 1054, "49": 1067, "50": 1237, "56": 693, "61": 693, "62": 694, "66": 696, "67": 698, "68": 699, "69": 699, "70": 699, "71": 701, "72": 701, "73": 701, "74": 702, "75": 702, "76": 708, "77": 708, "78": 709, "79": 709, "80": 710, "81": 710, "82": 713, "83": 713, "84": 717, "89": 720, "95": 881, "101": 881, "102": 882, "112": 890, "113": 892, "114": 893, "115": 893, "116": 893, "117": 895, "118": 895, "119": 895, "120": 896, "121": 896, "122": 896, "123": 896, "124": 897, "125": 898, "126": 898, "127": 898, "128": 899, "129": 900, "130": 901, "131": 901, "132": 901, "133": 902, "134": 902, "135": 904, "136": 905, "137": 905, "138": 905, "139": 906, "140": 906, "141": 908, "142": 909, "143": 909, "144": 909, "145": 911, "146": 912, "147": 912, "148": 912, "149": 914, "150": 914, "151": 914, "152": 915, "153": 915, "154": 916, "161": 921, "162": 922, "163": 922, "164": 923, "165": 923, "166": 924, "167": 924, "168": 924, "169": 924, "170": 924, "171": 924, "172": 925, "173": 925, "174": 926, "175": 927, "176": 927, "177": 927, "178": 929, "179": 929, "180": 929, "181": 931, "186": 934, "192": 788, "197": 788, "198": 789, "202": 791, "203": 793, "204": 794, "205": 794, "206": 794, "207": 796, "208": 796, "209": 796, "210": 797, "211": 797, "212": 799, "213": 799, "214": 803, "219": 806, "225": 532, "230": 532, "231": 533, "235": 535, "236": 537, "237": 538, "238": 538, "239": 538, "240": 540, "241": 540, "242": 540, "243": 541, "244": 541, "245": 543, "246": 543, "247": 544, "248": 544, "249": 545, "250": 545, "251": 546, "252": 546, "253": 550, "258": 553, "264": 233, "298": 233, "299": 234, "313": 246, "314": 247, "315": 248, "316": 248, "323": 253, "324": 254, "325": 254, "326": 254, "327": 254, "328": 255, "329": 256, "330": 256, "331": 256, "332": 259, "333": 260, "386": 311, "387": 312, "388": 312, "389": 312, "390": 312, "391": 313, "392": 313, "393": 314, "394": 314, "395": 315, "396": 315, "397": 316, "398": 316, "399": 322, "404": 325, "405": 327, "406": 328, "407": 328, "408": 328, "409": 330, "410": 331, "411": 331, "412": 331, "413": 333, "414": 334, "415": 334, "416": 334, "417": 336, "418": 337, "419": 337, "421": 337, "422": 338, "423": 338, "424": 340, "425": 341, "426": 341, "427": 341, "428": 343, "429": 344, "430": 344, "432": 344, "433": 345, "434": 345, "435": 347, "436": 348, "437": 349, "438": 349, "440": 349, "441": 350, "442": 350, "443": 353, "444": 354, "445": 354, "446": 354, "447": 356, "448": 357, "449": 358, "450": 358, "452": 358, "453": 359, "454": 359, "455": 362, "456": 363, "457": 364, "458": 364, "460": 364, "461": 365, "462": 365, "463": 368, "464": 369, "465": 370, "466": 370, "468": 370, "469": 371, "470": 371, "471": 374, "472": 375, "473": 376, "474": 376, "476": 376, "477": 377, "478": 377, "479": 380, "480": 381, "481": 382, "482": 382, "483": 382, "489": 832, "495": 832, "496": 833, "504": 839, "505": 841, "506": 842, "507": 842, "508": 842, "509": 844, "510": 844, "511": 844, "512": 845, "513": 846, "514": 846, "515": 846, "516": 846, "517": 846, "518": 847, "519": 848, "520": 848, "521": 848, "522": 849, "523": 850, "524": 851, "525": 851, "526": 851, "527": 852, "528": 852, "529": 852, "530": 852, "531": 854, "532": 854, "533": 855, "534": 855, "535": 857, "536": 858, "537": 859, "538": 859, "539": 859, "540": 859, "541": 859, "542": 860, "543": 861, "544": 861, "545": 861, "546": 863, "547": 864, "548": 864, "549": 864, "550": 866, "551": 867, "552": 867, "553": 867, "554": 869, "555": 871, "556": 871, "557": 871, "558": 871, "559": 871, "560": 871, "561": 871, "562": 872, "563": 872, "564": 872, "565": 872, "566": 872, "567": 872, "568": 874, "569": 875, "574": 878, "580": 228, "585": 228, "590": 231, "591": 231, "597": 937, "602": 937, "603": 938, "605": 938, "606": 940, "607": 941, "608": 941, "609": 941, "610": 943, "611": 943, "612": 943, "613": 944, "614": 944, "615": 946, "616": 946, "617": 947, "618": 947, "619": 948, "620": 948, "621": 949, "622": 949, "623": 950, "624": 950, "625": 951, "626": 951, "627": 952, "628": 952, "629": 953, "630": 953, "631": 954, "632": 954, "633": 958, "638": 961, "644": 73, "651": 73, "652": 76, "653": 76, "654": 156, "655": 157, "656": 159, "657": 159, "658": 162, "659": 163, "660": 165, "661": 165, "662": 168, "668": 556, "673": 556, "674": 557, "676": 557, "677": 559, "678": 560, "679": 560, "680": 560, "681": 562, "682": 562, "683": 562, "684": 563, "685": 563, "686": 565, "687": 565, "688": 569, "693": 572, "699": 662, "704": 662, "705": 663, "710": 666, "711": 668, "712": 669, "713": 669, "714": 669, "715": 671, "716": 671, "717": 671, "718": 672, "719": 672, "720": 678, "721": 678, "722": 679, "723": 679, "724": 680, "725": 680, "726": 683, "727": 683, "728": 687, "733": 690, "739": 1029, "743": 1029, "744": 1033, "745": 1034, "746": 1037, "747": 1038, "748": 1040, "749": 1040, "750": 1044, "751": 1044, "752": 1048, "753": 1048, "754": 1051, "760": 575, "767": 575, "768": 576, "800": 606, "801": 608, "802": 609, "803": 609, "804": 609, "805": 611, "806": 611, "807": 611, "808": 612, "809": 613, "810": 613, "811": 613, "812": 613, "813": 613, "814": 614, "815": 615, "816": 615, "817": 615, "818": 616, "819": 617, "820": 617, "821": 617, "822": 617, "823": 617, "824": 618, "825": 619, "826": 619, "827": 619, "828": 621, "829": 621, "830": 621, "831": 622, "832": 622, "833": 623, "834": 623, "835": 624, "836": 624, "837": 625, "838": 625, "839": 626, "840": 626, "841": 627, "842": 627, "843": 628, "844": 628, "845": 629, "846": 629, "847": 630, "848": 630, "849": 631, "850": 632, "851": 632, "852": 632, "853": 633, "854": 634, "855": 634, "856": 634, "857": 634, "858": 634, "859": 634, "860": 634, "861": 634, "862": 634, "863": 634, "864": 634, "865": 635, "866": 636, "867": 636, "868": 636, "869": 636, "870": 636, "871": 636, "872": 636, "873": 636, "874": 636, "875": 638, "876": 640, "877": 641, "882": 644, "888": 757, "893": 757, "894": 758, "898": 760, "899": 762, "900": 763, "901": 763, "902": 763, "903": 765, "904": 765, "905": 765, "906": 766, "907": 766, "908": 768, "909": 769, "910": 773, "911": 773, "912": 774, "913": 774, "914": 775, "915": 775, "916": 776, "917": 776, "918": 779, "919": 782, "924": 785, "930": 387, "935": 387, "936": 388, "944": 394, "945": 396, "946": 397, "947": 397, "948": 397, "949": 399, "950": 399, "951": 399, "952": 400, "953": 400, "954": 400, "955": 400, "956": 400, "957": 400, "958": 400, "959": 400, "960": 401, "961": 401, "962": 401, "963": 401, "964": 401, "965": 401, "966": 402, "967": 402, "968": 402, "969": 402, "970": 402, "971": 402, "972": 403, "973": 403, "974": 403, "975": 403, "976": 403, "977": 403, "978": 405, "983": 408, "989": 411, "994": 411, "995": 412, "1000": 415, "1001": 417, "1002": 418, "1003": 418, "1004": 418, "1005": 420, "1006": 420, "1007": 420, "1008": 421, "1009": 421, "1010": 423, "1011": 423, "1012": 424, "1013": 424, "1014": 425, "1015": 425, "1016": 426, "1017": 426, "1018": 427, "1019": 427, "1020": 431, "1025": 434, "1031": 1, "1037": 1, "1038": 7, "1039": 7, "1040": 18, "1041": 18, "1042": 20, "1043": 20, "1044": 20, "1045": 20, "1046": 24, "1047": 24, "1048": 26, "1049": 26, "1050": 49, "1051": 49, "1052": 57, "1053": 57, "1054": 59, "1055": 59, "1061": 964, "1066": 964, "1067": 965, "1075": 971, "1076": 973, "1077": 974, "1078": 974, "1079": 974, "1080": 976, "1081": 976, "1082": 976, "1083": 977, "1084": 977, "1085": 977, "1086": 977, "1087": 977, "1088": 977, "1089": 977, "1090": 977, "1091": 978, "1092": 978, "1093": 978, "1094": 978, "1095": 978, "1096": 978, "1097": 979, "1098": 979, "1099": 979, "1100": 979, "1101": 979, "1102": 979, "1103": 981, "1108": 984, "1114": 723, "1119": 723, "1120": 724, "1125": 727, "1126": 729, "1127": 730, "1128": 730, "1129": 730, "1130": 732, "1131": 732, "1132": 732, "1133": 733, "1134": 733, "1135": 735, "1136": 736, "1137": 740, "1138": 740, "1139": 741, "1140": 741, "1141": 742, "1142": 742, "1143": 743, "1144": 743, "1145": 746, "1146": 747, "1147": 747, "1148": 751, "1153": 754, "1159": 459, "1164": 459, "1165": 460, "1169": 462, "1170": 464, "1171": 465, "1172": 465, "1173": 465, "1174": 467, "1175": 467, "1176": 467, "1177": 468, "1178": 468, "1179": 469, "1180": 469, "1181": 472, "1186": 475, "1192": 478, "1198": 478, "1199": 479, "1201": 479, "1202": 481, "1203": 482, "1204": 482, "1205": 482, "1206": 484, "1207": 484, "1208": 484, "1209": 485, "1210": 485, "1211": 486, "1212": 487, "1213": 487, "1214": 487, "1215": 488, "1216": 488, "1217": 490, "1218": 491, "1219": 491, "1220": 491, "1221": 493, "1222": 495, "1227": 498, "1233": 987, "1239": 987, "1240": 988, "1256": 1002, "1257": 1004, "1258": 1005, "1259": 1005, "1260": 1005, "1261": 1007, "1262": 1007, "1263": 1007, "1264": 1008, "1265": 1008, "1266": 1008, "1267": 1008, "1268": 1009, "1269": 1010, "1270": 1010, "1271": 1010, "1272": 1011, "1273": 1012, "1274": 1012, "1275": 1012, "1276": 1012, "1277": 1012, "1278": 1013, "1279": 1014, "1280": 1014, "1281": 1014, "1282": 1014, "1283": 1014, "1284": 1015, "1285": 1016, "1286": 1016, "1287": 1016, "1288": 1018, "1289": 1018, "1290": 1018, "1291": 1019, "1292": 1019, "1293": 1019, "1294": 1019, "1295": 1019, "1296": 1019, "1297": 1020, "1298": 1020, "1299": 1020, "1300": 1020, "1301": 1020, "1302": 1020, "1303": 1021, "1304": 1021, "1305": 1021, "1306": 1021, "1307": 1021, "1308": 1021, "1309": 1023, "1314": 1026, "1320": 177, "1325": 177, "1326": 180, "1337": 189, "1338": 190, "1339": 191, "1340": 191, "1341": 191, "1342": 192, "1343": 193, "1344": 197, "1345": 198, "1346": 198, "1347": 198, "1348": 199, "1349": 200, "1350": 203, "1351": 204, "1352": 206, "1353": 207, "1354": 209, "1355": 210, "1356": 212, "1357": 216, "1363": 809, "1368": 809, "1369": 810, "1373": 812, "1374": 814, "1375": 815, "1376": 815, "1377": 815, "1378": 817, "1379": 817, "1380": 817, "1381": 818, "1382": 818, "1383": 820, "1384": 820, "1385": 821, "1386": 821, "1387": 822, "1388": 822, "1389": 826, "1394": 829, "1400": 1056, "1406": 1056, "1407": 1057, "1408": 1058, "1409": 1062, "1410": 1062, "1416": 1069, "1425": 1069, "1426": 1070, "1467": 1109, "1468": 1110, "1469": 1111, "1470": 1111, "1471": 1111, "1472": 1117, "1474": 1117, "1475": 1119, "1476": 1119, "1477": 1124, "1478": 1125, "1479": 1128, "1480": 1129, "1481": 1130, "1483": 1130, "1484": 1132, "1485": 1132, "1486": 1135, "1487": 1136, "1488": 1137, "1490": 1137, "1491": 1139, "1492": 1139, "1493": 1142, "1494": 1143, "1495": 1144, "1497": 1144, "1498": 1146, "1499": 1146, "1500": 1149, "1501": 1150, "1502": 1151, "1504": 1151, "1505": 1153, "1506": 1153, "1507": 1156, "1508": 1157, "1509": 1158, "1511": 1158, "1512": 1160, "1513": 1160, "1514": 1163, "1515": 1164, "1516": 1165, "1518": 1165, "1519": 1167, "1520": 1167, "1521": 1170, "1522": 1173, "1523": 1174, "1524": 1178, "1525": 1179, "1526": 1180, "1528": 1180, "1529": 1182, "1530": 1182, "1531": 1185, "1532": 1186, "1533": 1187, "1535": 1187, "1536": 1189, "1537": 1189, "1538": 1192, "1539": 1193, "1540": 1194, "1542": 1194, "1543": 1196, "1544": 1196, "1545": 1199, "1546": 1200, "1547": 1201, "1549": 1201, "1550": 1203, "1551": 1203, "1552": 1206, "1553": 1207, "1554": 1208, "1556": 1208, "1557": 1210, "1558": 1210, "1559": 1213, "1560": 1214, "1561": 1215, "1563": 1215, "1564": 1217, "1565": 1217, "1566": 1220, "1567": 1223, "1568": 1224, "1569": 1224, "1570": 1224, "1571": 1230, "1573": 1230, "1574": 1232, "1575": 1232, "1581": 437, "1586": 437, "1587": 438, "1595": 444, "1596": 446, "1597": 447, "1598": 447, "1599": 447, "1600": 449, "1601": 449, "1602": 449, "1603": 450, "1604": 450, "1605": 450, "1606": 450, "1607": 450, "1608": 450, "1609": 450, "1610": 450, "1611": 451, "1612": 451, "1613": 451, "1614": 451, "1615": 451, "1616": 451, "1617": 453, "1622": 456, "1628": 220, "1632": 220, "1633": 221, "1638": 224, "1639": 225, "1640": 225, "1641": 225, "1642": 225, "1648": 647, "1652": 647, "1653": 649, "1654": 649, "1660": 501, "1665": 501, "1666": 502, "1670": 504, "1671": 516, "1672": 517, "1673": 517, "1674": 517, "1675": 519, "1676": 519, "1677": 519, "1678": 520, "1679": 520, "1680": 522, "1681": 522, "1682": 526, "1687": 529, "1693": 1687}, "uri": "/webapps/tool_shed/repository/common.mako", "filename": "templates/webapps/tool_shed/repository/common.mako"}
__M_END_METADATA
"""
