from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class HeadnetformexamplesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import headnet.formexamples
        xmlconfig.file(
            'configure.zcml',
            headnet.formexamples,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'headnet.formexamples:default')

HEADNET_FORMEXAMPLES_FIXTURE = HeadnetformexamplesLayer()
HEADNET_FORMEXAMPLES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(HEADNET_FORMEXAMPLES_FIXTURE,),
    name="HeadnetformexamplesLayer:Integration"
)
HEADNET_FORMEXAMPLES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(HEADNET_FORMEXAMPLES_FIXTURE, z2.ZSERVER_FIXTURE),
    name="HeadnetformexamplesLayer:Functional"
)
