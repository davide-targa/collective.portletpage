# -*- coding: utf-8 -*-

from zope.component import getMultiAdapter
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.memoize.instance import memoize

class Base(BrowserView):
    """Base class for index page views
    """

    @memoize
    def plone_view(self):
        return getMultiAdapter((self.context, self.request), name=u"plone")

class FourColumns(Base):
    """A four-column layout.

       |ColumnFirst|ColumnSecond|ColumnThird|ColumnFourth|
       ---------------------------------------------------
       |                  ColumnTop                      |
       ---------------------------------------------------
       |    ColumnMiddleFirst   |   ColumnMiddleSecond   |
       ---------------------------------------------------
       |                  ColumnBottom                   |
    """

    __call__ = ViewPageTemplateFile('four-columns.pt')

    def hasColumnFirst(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.firstcolumn', view=self)

    def hasColumnSecond(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.secondcolumn', view=self)

    def hasColumnThird(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.thirdcolumn', view=self)

    def hasColumnFourth(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.fourthcolumn', view=self)

    def fourColumnCount(self):
        """Returns the number of columns for the four columns section
        """
        i = 0
        if self.hasColumnFirst():
            i = i + 1
        if self.hasColumnSecond():
            i = i + 1
        if self.hasColumnThird():
            i = i + 1
        if self.hasColumnFourth():
            i = i + 1
        return i

    def columnCountInWords(self, number):
        """Returns a number (in words).
           Accepts a number as parameter.
        """
        numbers = {1:'one', 2:'two', 3:'three', 4:'four'}
        return numbers[number]

    def hasColumnTop(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.toprow', view=self)

    def hasColumnMiddleFirst(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.middlefirst', view=self)

    def hasColumnMiddleSecond(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.middlesecond', view=self)

    def middleColumnCount(self):
        i = 0
        if self.hasColumnMiddleFirst():
            i += 1
        if self.hasColumnMiddleSecond():
            i += 1
        return i

    def hasColumnBottom(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.bottomrow', view=self)
