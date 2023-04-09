from pybleno import Characteristic
import array
import struct
import sys
import traceback

class P_Characteristic(Characteristic):
    
    def __init__(self, uuid):
        Characteristic.__init__(self, {
            'uuid': uuid,
            'properties': ['read', 'write'],
            'value': None
          })
          
        self._value = array.array('B', [0] * 0)
        self._updateValueCallback = None
          
    def onReadRequest(self, offset, callback):
        print('P_Characteristic - %s - onReadRequest: value = %s' % (self['uuid'], [hex(c) for c in self._value]))
        callback(Characteristic.RESULT_SUCCESS, self._value[offset:])

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        self._value = data

        print('P_Characteristic - %s - onWriteRequest: value = %s' % (self['uuid'], [hex(c) for c in self._value]))

        if self._updateValueCallback:
            print('P_Characteristic - onWriteRequest: notifying');
            
            self._updateValueCallback(self._value)
        
        callback(Characteristic.RESULT_SUCCESS)