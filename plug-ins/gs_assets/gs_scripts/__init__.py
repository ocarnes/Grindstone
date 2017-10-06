# this file just marks the gs_scripts directory as a safe import source

# bundle all scripts in this folder into a single module
'''from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]'''