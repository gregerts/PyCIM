# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.ENTSOE.Equipment.Wires.EnergyConsumer import EnergyConsumer

class ConformLoad(EnergyConsumer):
    """ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.-  [R8.2] is satisfied by navigation to ConnectivityNode and Substation -  The definition of the real and reactive power injections for an EnergyConsumer can be done using different sets of attributes.  In the simplest case, the injections can be defined directly using only the attributes “pfixed” and “qfixed”. -  The injections for a ConformLoad can be defined as a percentage of the ConformLoadGroup with the attributes “pfixedPct” and “qfixedPct”.  In this case, the associated ConformLoadGroup would have to have an associated ConformLoadSchedule. -  See EnergyConsumer for specific notes about inherited attributes. 
    """

    def __init__(self, LoadGroup=None, *args, **kw_args):
        """Initialises a new 'ConformLoad' instance.

        @param LoadGroup: Group of this ConformLoad.
        """
        self._LoadGroup = None
        self.LoadGroup = LoadGroup

        super(ConformLoad, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["LoadGroup"]
    _many_refs = []

    def getLoadGroup(self):
        """Group of this ConformLoad.
        """
        return self._LoadGroup

    def setLoadGroup(self, value):
        if self._LoadGroup is not None:
            filtered = [x for x in self.LoadGroup.EnergyConsumers if x != self]
            self._LoadGroup._EnergyConsumers = filtered

        self._LoadGroup = value
        if self._LoadGroup is not None:
            if self not in self._LoadGroup._EnergyConsumers:
                self._LoadGroup._EnergyConsumers.append(self)

    LoadGroup = property(getLoadGroup, setLoadGroup)

