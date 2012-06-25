.. contents:: **Table of contents**

Overview
========

After installing this product, you will be able to add a "Portlet Page".

This is like a standard Plone Page, but it also has a "*Manage portlets*" tab, from
which you may assign portlets into eight slots. The portlets will be shown on the main
view of the content.

.. image:: http://s17.postimage.org/ynu6d1xot/edit.png
   :alt: Managing content's portlets

Use of other content data like title, description and body text can be avoided, making the Portlet
Page simply a portlet container.

This product is great for providing to your Plone sites a tool for building the site *homepage*,
or the home for a site subsection.

.. image:: http://s17.postimage.org/gatl2hn7x/result.png
   :alt: Example of the user view

Similar product
---------------

Other Plone users like creating homepage using `Collage`__.

__ http://plone.org/products/collage

Installation
============

1) Clone the repository : ``git://github.com/davide-targa/collective.portletpage.git`` in your $PLONE/src folder

2) 
Add the ``collective.portletpage`` eggs in your buildout.cfg configuration file
(see also the `Plone buildout documentation`__)::

    [instance]
    ...
    eggs=
       ...
       collective.portletpage

    develop= 
    	...
    	src/collective.portletpage


__ http://plone.org/documentation/manual/developer-manual/managing-projects-with-buildout/packages-products-and-eggs

Support
=======

For reporting issues or ask for new features, please refer to the `issue tracker`__

__ https://github.com/davide-targa/collective.portletpage/issues

Authors
=======

This product was forked from `collective portletpage`__, extended by `Davide Targa`__ and `Damiano Braga`__.

__ https://github.com/collective/collective.portletpage
__ https://github.com/davide-targa
__ https://github.com/dbraga