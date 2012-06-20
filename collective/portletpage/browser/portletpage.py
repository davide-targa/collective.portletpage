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
       |                  ColumnTop                      |
       |    ColumnMiddleFirst   |   ColumnMiddleSecond   |
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

    def hasColumnTop(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.toprow', view=self)

    def hasColumnMiddleFirst(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.middlefirst', view=self)

    def hasColumnMiddleSecond(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.middlesecond', view=self)

    def hasColumnBottom(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.bottomrow', view=self)
