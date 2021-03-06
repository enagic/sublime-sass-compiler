import os, sublime, sublime_plugin, subprocess, functools, time
from threading  import Thread
import sys

if (sys.version_info > (3, 0)):
    from queue import Queue
else:
    import Queue

bin_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin')
ruby = os.path.join(bin_folder, 'Ruby193', 'ruby.jar')

ON_POSIX = 'posix' in sys.builtin_module_names
bufsize = -1

class SassCompileCommand(sublime_plugin.WindowCommand):
    def run(self, paths=[]):
        self.paths = paths

        if (sys.version_info > (3, 0)):
            q = Queue()
        else:
            q = Queue.Queue()

        for path in self.paths:
            proc = subprocess.Popen(
                self.build_cmd(path),
                bufsize=bufsize,
                cwd=os.path.dirname(path),
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                close_fds=ON_POSIX)

            thread = Thread(
                target=self.output,
                args=(proc.stdout, proc.stderr, q))
            thread.daemon = True
            thread.start()

        self.thread = thread
        self.message = 'Compiling'
        self.addend = 1
        self.size = 8
        sublime.set_timeout(lambda: self.show_progress(0), 100)

    def show_progress(self, i):
        if not self.thread.is_alive():
            return

        before = i % self.size
        after = (self.size - 1) - before

        sublime.status_message('%s [%s=%s]' % \
            (self.message, ' ' * before, ' ' * after))

        if not after:
            self.addend = -1
        if not before:
            self.addend = 1
        i += self.addend

        sublime.set_timeout(lambda: self.show_progress(i), 100)

    def show_status(self, status):
        sublime.status_message(status)

    def output(self, stdout, stderr, q):
        errs = []

        for line in iter(stdout.readline, b''):
            if len(errs) == 0 and ('error' not in line.lower().decode('utf-8')):
                q.put(line)
                print(line.decode('utf-8'))
            else:
                errs.append(line)

            # print(str(line))

        for line in iter(stderr.readline, b''):
            errs.append(line)

        if len(errs) != 0:
            message = ''
            sublime.set_timeout(lambda: self.show_status('Error'), 0)
            for line in errs:
                message += line.decode('utf-8')

            sublime.error_message(message)
        else:
            sublime.set_timeout(lambda: self.show_status('Success'), 0)

        stderr.close()
        stdout.close()

    def build_cmd(self, path):
        java = os.path.join(self.get_java_home(), 'java')
        settings = sublime.load_settings('SassCompiler.sublime-settings')
        style = settings.get('style') or 'nested'
        include_line_numbers = settings.get('include_line_numbers')
        include_line_comments = settings.get('include_line_comments')
        cache = settings.get('cache')
        cache_location = settings.get('cache_location')
        filename, file_extension = os.path.splitext(path)
        gem = 'scss'

        if (file_extension == '.sass'):
            gem = 'sass'

        cmd = [
            java,
            '-jar',
            ruby,
            '-S',
            gem,
            '--update', # Compile files or directories to CSS.
            '--style', style
        ]

        if (cache):
            cmd.append('--cache-location');
            cmd.append(cache_location);
        else:
            cmd.append('--no-cache')

        # if (include_line_numbers):
        cmd.append('--line-numbers')

        # if (include_line_comments):
        cmd.append('--line-comments')

        cmd.append(path)

        print(cmd)

        return cmd

    def get_java_home(self):
        java_home = None
        settings = sublime.load_settings('SassCompiler.sublime-settings')

        if (java_home == None):
            java_home = settings.get('java_home')

        if (java_home == None):
            print("WARNING: JAVA_HOME could not be found")
            java_home = ''

        return java_home

    def is_visible(self, paths=[]):
        is_visible = True

        for path in paths:
            filename, file_extension = os.path.splitext(path)
            if is_visible:
                is_visible = file_extension == '.scss' or file_extension == '.sass'

        return is_visible
