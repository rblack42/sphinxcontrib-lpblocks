import sys
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
sys.path.append('ext')
extensions = ['ext.lpblock']
exclude_patterns = ['_build', 'tests', '_venv', '.DS_Store']
master_doc = 'index'
nitpicky = True
