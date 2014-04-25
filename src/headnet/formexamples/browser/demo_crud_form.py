# -*- coding: utf-8 -*-
from zExceptions import NotFound
from ZODB.POSException import ConflictError
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.app.pagetemplate import viewpagetemplatefile as zopetemplate
from zope.component import getUtility
import zope.event

from zope import schema
from zope.interface import Invalid
import z3c.form.widget
from z3c.form import field, form, button, validator
from z3c.form.interfaces import DISPLAY_MODE, HIDDEN_MODE
from plone.z3cform.layout import FormWrapper, wrap_form
from plone.z3cform.crud import crud
from plone.app.z3cform.wysiwyg.widget import WysiwygFieldWidget

from z3c.saconfig import named_scoped_session

from headnet.formexamples.model.demo import IDemo, Demo

from plone.z3cform import MessageFactory as _

Session = named_scoped_session("headnet.formexamples")

class BaseCrudForm(crud.CrudForm):
    def __init__(self, context, request):
        super(BaseCrudForm, self).__init__(context, request)
        self._db_session = None

    @property
    def db_session(self):
        if not self._db_session:
            self._db_session = Session()
        return self._db_session

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()


class DemoCrudForm(BaseCrudForm):
    update_schema = IDemo

    # cache this? Probably not, since we add and getitems might need to reflect that.
    def get_items(self):
        session = self.db_session
        return [(i.row_id, i) for i in session.query(Demo).all()]

    def add(self, data):
        session = self.db_session
        item = Demo(**data)
        session.add(item)
        return item

    def remove(self, (id, item)):
        session = self.db_session
        session.delete(item)


DemoCrudFormView = wrap_form(DemoCrudForm)
# class GoalCrudFormView(FormWrapper):
#     index = ViewPageTemplateFile('templates/form-wrapper.pt')
#     form = GoalCrudForm

