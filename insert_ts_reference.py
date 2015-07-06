import sublime, sublime_plugin, os.path

class InsertTsReferenceCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    comment_template = '/// <reference path="$PATH$" />'
    view = self.view
    references_file_name = sublime.load_settings('InsertTsReference').get('references_file_name', 'references.ts');
    if view is not None:
     local_references_name = view.settings().get('InsertTsReference', {}).get('references_file_name')
     if local_references_name is not None: references_file_name = local_references_name

     max_attempts = 50
     
     file_folder = os.path.realpath(view.file_name() + '/..')
     root_folders = view.window().folders()

     attemps = 0
     current_folder = file_folder
     while attemps < max_attempts:
      # print('Trying ', current_folder)
      if os.path.isfile(current_folder + '/' + references_file_name):
        # print('Found', file_folder, i)
        file_folder =  os.path.relpath(current_folder, file_folder) + '/' if current_folder != file_folder else '';
        view.insert(edit, 0, comment_template.replace('$PATH$', file_folder + references_file_name) + '\n\n');
        break;
      else:
        current_folder =  current_folder + '/..'

        if os.path.realpath(current_folder) in root_folders:
          sublime.error_message('unable to find references file named "' + references_file_name + '" while traversing this files directory tree!')
          break;
          attemps = attemps + 1

          if attemps == max_attempts:
           sublime.error_message('unable to find references file named "' + references_file_name + '" while traversing this files directory tree!')



    #allcontent = sublime.Region(0, self.view.size())
    #self.view.replace(edit, allcontent, self.view.file_name() + self.view.scope_name(0))
