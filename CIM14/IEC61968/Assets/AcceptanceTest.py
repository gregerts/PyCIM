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

from CIM14.Element import Element

class AcceptanceTest(Element):
    """Acceptance test for assets.
    """

    def __init__(self, success=False, type='', dateTime='', *args, **kw_args):
        """Initialises a new 'AcceptanceTest' instance.

        @param success: True if asset has passed acceptance test and may be placed in or is in service. It is set to false if asset is removed from service and is required to be tested again before being placed back in service, possibly in a new location. Since asset may go through multiple tests during its life cycle, the date of each acceptance test may be recorded in Asset.ActivityRecord.status.dateTime. 
        @param type: Type of test or group of tests that was conducted on 'dateTime'. 
        @param dateTime: Date and time the asset was last tested using the 'type' of test and yielding the current status in 'success' attribute. 
        """
        #: True if asset has passed acceptance test and may be placed in or is in service. It is set to false if asset is removed from service and is required to be tested again before being placed back in service, possibly in a new location. Since asset may go through multiple tests during its life cycle, the date of each acceptance test may be recorded in Asset.ActivityRecord.status.dateTime.
        self.success = success

        #: Type of test or group of tests that was conducted on 'dateTime'.
        self.type = type

        #: Date and time the asset was last tested using the 'type' of test and yielding the current status in 'success' attribute.
        self.dateTime = dateTime

        super(AcceptanceTest, self).__init__(*args, **kw_args)

    _attrs = ["success", "type", "dateTime"]
    _attr_types = {"success": bool, "type": str, "dateTime": str}
    _defaults = {"success": False, "type": '', "dateTime": ''}
    _enums = {}
    _refs = []
    _many_refs = []

