
'''
MAP Client Plugin Step
'''
import json

from PySide import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.chooserstep.configuredialog import ConfigureDialog


class ChooserStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    def __init__(self, location):
        super(ChooserStep, self).__init__('Chooser', location)
        self._configured = False # A step cannot be executed until it has been configured.
        self._category = 'Source'
        # Add any other initialisation code here:
        self._icon =  QtGui.QImage(':/chooserstep/images/data-source.png')
        # Ports:
#         self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
#                       'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
#                       'http://physiomeproject.org/workflow/1.0/rdf-schema#file'))
#         self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
#                       'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
#                       'http://physiomeproject.org/workflow/1.0/rdf-schema#directory'))
        # Port data:
        self._portFileAnnotation = ('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                                    'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                                    'http://physiomeproject.org/workflow/1.0/rdf-schema#file')
        self._portDirectoryAnnotation = ('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                                         'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                                         'http://physiomeproject.org/workflow/1.0/rdf-schema#directory')
        self._portData = []
        # Config:
        self._config = {}
        self._config['identifier'] = ''
        self._config['file_chooser_count'] = 0
        self._config['directory_chooser_count'] = 1


    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        self._doneExecution()

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        return self._portData[index]

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog()
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()
            self._configurePorts()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self):
        '''
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)


    def deserialize(self, string):
        '''
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.
        '''
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configurePorts()
        self._configured = d.validate()
        
    def _configurePorts(self):
        self._ports = []
        file_choosers = self._config['file_chooser_count']
        for _ in range(file_choosers):
            self.addPort(self._portFileAnnotation)
        directory_choosers = self._config['directory_chooser_count']
        for _ in range(directory_choosers):
            self.addPort(self._portDirectoryAnnotation)


