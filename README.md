openshift-cartridge
===================

Vert.x cartridge for OpenShift

To create a vertx application on OpenShift run the following command using the rhc client tools:

    rhc app create <app-name> https://raw.github.com/vert-x/openshift-cartridge/master/metadata/manifest.yml

To create a scaled vertx application run the following command:

    rhc app create <app-name> https://raw.github.com/vert-x/openshift-cartridge/master/metadata/manifest.yml -s
