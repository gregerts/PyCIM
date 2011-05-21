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

"""An extension to the Core and Wires packages that models information for protection equipment such as relays. These entities are used within training simulators and distribution network fault location applications.
"""

from CIM14.IEC61970.Protection.RecloseSequence import RecloseSequence
from CIM14.IEC61970.Protection.ProtectionEquipment import ProtectionEquipment
from CIM14.IEC61970.Protection.CurrentRelay import CurrentRelay
from CIM14.IEC61970.Protection.SurgeProtector import SurgeProtector
from CIM14.IEC61970.Protection.FaultIndicator import FaultIndicator
from CIM14.IEC61970.Protection.SynchrocheckRelay import SynchrocheckRelay

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Protection"
nsPrefix = "cimProtection"

