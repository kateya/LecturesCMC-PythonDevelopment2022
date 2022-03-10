import cmd
import shlex
import pynames

class commandline(cmd.Cmd):
    intro = 'Welcome to command line name generator'

    lang = 'native'

    def do_language(self, args):
        """Set language"""
        params = shlex.split(args)
        self.lang = 'native'
        if params:
            if params[0].lower() in pynames.relations.LANGUAGE.ALL:
                self.lang = params[0].lower()

    def do_exit(self, args):
        return True

if __name__ == '__main__':
    commandline().cmdloop()