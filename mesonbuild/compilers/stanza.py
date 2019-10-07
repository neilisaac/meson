
import subprocess, os.path

from ..mesonlib import EnvironmentException, MachineChoice

from .compilers import Compiler

class StanzaCompiler(Compiler):
    id = 'stanza'
    language = 'stanza'
    file_suffixes = ['stanza']
    is_cross = False

    def __init__(self, exelist, version, for_machine: MachineChoice, **kwargs):
        self.version = version
        super().__init__(exelist, version, for_machine, **kwargs)

    def name_string(self):
        return ' '.join(self.exelist)

    def sanity_check(self, work_dir, environment):
        pass

    def needs_static_linker(self):
        return False

    def get_compile_only_args(self):
        return ['-pkg']

    def get_output_args(self, target):
        return ['-o', target]

    def get_werror_args(self):
        return []

    def get_warn_args(self, level):
        return []

    def get_buildtype_args(self, buildtype):
        return []

    def get_optimization_args(self, level):
        if level in {'1', '2', '3', 's'}:
            return ['-optimize']
        return []

    def get_debug_args(self, is_debug):
        return []

    def get_include_args(self, dirname, is_system=False):
        return ['-ccflags', '-l' + dirname]

    def compute_parameters_with_absolute_paths(self, parameter_list, build_dir):
        return parameter_list

    def get_dependency_gen_args(self, outtarget, outfile):
        return []

    def depfile_for_object(self, objfile):
        return os.path.splitext(objfile)[0] + '.d'
