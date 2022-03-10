import cmd
import shlex
import pynames

FNAMEGEN = 'FullnameGenerator'
NAMEGEN = 'NamesGenerator'
LANG_PREFIX = 'language=pynames.LANGUAGE.'
GENDER_PREFIX = 'gender=pynames.GENDER.'

class commandline(cmd.Cmd):
    intro = 'Welcome to command line name generator'

    lang = 'NATIVE'
    iron_kingdoms_subclasses = [k[:-17] for k in pynames.generators.iron_kingdoms.__dict__ if k.endswith(FNAMEGEN)]
    elven_subclasses = [k[:-14] for k in pynames.generators.elven.__dict__ if k.endswith(NAMEGEN)]

    def do_language(self, args):
        """Set language"""
        params = shlex.split(args)
        self.lang = 'NATIVE'
        if params:
            if params[0].lower() in pynames.LANGUAGE.ALL:
                self.lang = params[0].upper()

    def do_generate(self, args):
        """Generate a name"""
        params = shlex.split(args)
        if params:
            if params[0] in pynames.generators.__all__:
                gen_class_name = 'pynames.generators.' + params[0] + '.'
                if params[0] == 'iron_kingdoms':
                    if len(params) > 1 and params[1] in self.iron_kingdoms_subclasses:
                        gen_class_name += params[1]
                    else:
                        gen_class_name += self.iron_kingdoms_subclasses[0]
                    gen_class_name += FNAMEGEN
                elif params[0] == 'elven':
                    if len(params) > 1 and params[1] in self.elven_subclasses:
                        gen_class_name += params[1]
                    else:
                        gen_class_name += self.elven_subclasses[0]
                    gen_class_name += NAMEGEN
                else:
                    gen_class_name += [k for k in eval(gen_class_name + '__dict__') if k.endswith(NAMEGEN)][0]

                gender = ''
                if len(params) > 1 and params[-1].upper() in pynames.GENDER.__dict__:
                    gender = GENDER_PREFIX + params[-1].upper()

                gen_params = (gender + ', ') if gender else ''
                gen_params += (LANG_PREFIX + self.lang) if eval(LANG_PREFIX[9:] + self.lang) in eval(gen_class_name + '().languages') else ''

                result = eval(gen_class_name + '().get_name_simple(' + gen_params + ')')

                print(result)

    def do_info(self, args):
        """Show info"""
        params = shlex.split(args)
        if params:
            if params[0] in pynames.generators.__all__:
                gen_class_name = 'pynames.generators.' + params[0] + '.'
                if params[0] == 'iron_kingdoms':
                    if len(params) > 1 and params[1] in self.iron_kingdoms_subclasses:
                        gen_class_name += params[1]
                    else:
                        gen_class_name += self.iron_kingdoms_subclasses[0]
                    gen_class_name += FNAMEGEN
                elif params[0] == 'elven':
                    if len(params) > 1 and params[1] in self.elven_subclasses:
                        gen_class_name += params[1]
                    else:
                        gen_class_name += self.elven_subclasses[0]
                    gen_class_name += NAMEGEN
                else:
                    gen_class_name += [k for k in eval(gen_class_name + '__dict__') if k.endswith(NAMEGEN)][0]

                if len(params) > 1 and params[-1] == 'language':
                    print(*eval(gen_class_name + '().languages'))
                    return

                gender = ''
                if len(params) > 1 and params[-1].upper() in pynames.GENDER.__dict__:
                    gender = GENDER_PREFIX[7:] + params[-1].upper()

                result = eval(gen_class_name + '().get_names_number(' + gender + ')')

                print(result)

    def complete_generate(self, prefix, allcmd, beg, end):
        params = shlex.split(allcmd[:beg])
        if len(params) == 1:
            return [var for var in pynames.generators.__all__ if var.startswith(prefix)]
        result = ['male', 'female']
        if len(params) == 2:
            if params[1] == 'iron_kingdoms':
                result += self.iron_kingdoms_subclasses
            elif params[1] == 'elven':
                result += self.elven_subclasses
            return [var for var in result if var.startswith(prefix)]
        if len(params) == 3:
            return [var for var in result if var.startswith(prefix)]

    def complete_info(self, *args):
        return self.complete_generate(*args)

    def complete_language(self, prefix, allcmd, beg, end):
        result = pynames.LANGUAGE.ALL
        return [var for var in result if var.startswith(prefix)]

    def do_exit(self, args):
        return True

if __name__ == '__main__':
    commandline().cmdloop()