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

from CIM14.IEC61970.Dynamics.MetaBlockConnectable import MetaBlockConnectable

class MetaBlockParameter(MetaBlockConnectable):
    """An identified parameter of a block.   This is meta dynamics model and does not contain specific parameter values. When using a block one would need to supply specific parameter values. These are typically time constants, but are not restricted to this.  Sometimes, for standard blocks, the block paramter may come directly from the attributes of an associated PowerSystemResource object, but such parameters may be specified to enable user defined models to alter the behavior of a standard block.
    """

    def __init__(self, BlockParameter=None, MemberOf_MetaBlock=None, *args, **kw_args):
        """Initialises a new 'MetaBlockParameter' instance.

        @param BlockParameter:
        @param MemberOf_MetaBlock: Paramters belong to a block.
        """
        self._BlockParameter = []
        self.BlockParameter = [] if BlockParameter is None else BlockParameter

        self._MemberOf_MetaBlock = None
        self.MemberOf_MetaBlock = MemberOf_MetaBlock

        super(MetaBlockParameter, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["BlockParameter", "MemberOf_MetaBlock"]
    _many_refs = ["BlockParameter"]

    def getBlockParameter(self):
        
        return self._BlockParameter

    def setBlockParameter(self, value):
        for x in self._BlockParameter:
            x.MetaBlockParameter = None
        for y in value:
            y._MetaBlockParameter = self
        self._BlockParameter = value

    BlockParameter = property(getBlockParameter, setBlockParameter)

    def addBlockParameter(self, *BlockParameter):
        for obj in BlockParameter:
            obj.MetaBlockParameter = self

    def removeBlockParameter(self, *BlockParameter):
        for obj in BlockParameter:
            obj.MetaBlockParameter = None

    def getMemberOf_MetaBlock(self):
        """Paramters belong to a block.
        """
        return self._MemberOf_MetaBlock

    def setMemberOf_MetaBlock(self, value):
        if self._MemberOf_MetaBlock is not None:
            filtered = [x for x in self.MemberOf_MetaBlock.MetaBlockParameter if x != self]
            self._MemberOf_MetaBlock._MetaBlockParameter = filtered

        self._MemberOf_MetaBlock = value
        if self._MemberOf_MetaBlock is not None:
            if self not in self._MemberOf_MetaBlock._MetaBlockParameter:
                self._MemberOf_MetaBlock._MetaBlockParameter.append(self)

    MemberOf_MetaBlock = property(getMemberOf_MetaBlock, setMemberOf_MetaBlock)

