from logging import getLogger
from zope import component

from z3c.saconfig.interfaces import IEngineFactory

from headnet.formexamples import model

log = getLogger('headnet.formexamples:setup')

def setupVarious(context):
    if context.readDataFile('headnet.formexamples_various.txt') is None:
        return

    portal = context.getSite()
    setupDb(portal)

def setupDb(site):
    """ """
    from ipdb import set_trace; set_trace()
    factory = component.getUtility(IEngineFactory, name="headnet.formexamples")
    engine = factory()
    model.Base.metadata.create_all(engine)
    log.info("Setup db tables")
