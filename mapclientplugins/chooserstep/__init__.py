
'''
MAP Client Plugin
'''

__version__ = '0.1.0'
__author__ = 'Hugh Sorby'
__stepname__ = 'Chooser'
__location__ = 'https://github.com/mapclient-plugins/chooser/archive/master.zip'

# import class that derives itself from the step mountpoint.
from mapclientplugins.chooserstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
import resources_rc