# OpenShift Cartridge for Vert.x
A downloadable cartridge which can be used to run Vert.x on OpenShift

## Getting started

To create a vertx application on OpenShift (we'll call it demo) run the following command using the rhc client tools:

    rhc app create demo https://raw.github.com/vert-x/openshift-cartridge/master/metadata/manifest.yml

To create a scaled vertx application run the following command:

    rhc app create demo https://raw.github.com/vert-x/openshift-cartridge/master/metadata/manifest.yml -s

This will create a directory named `demo` which will house the Vert.x application. Inside this folder is
a `server.js` file which is the default cartridge application which just serves static files under the `web-root` directory.

## Running a raw verticle

The default application is configured to run the raw `server.js`. This is controlled by the `configuration/vertx.env` file entry:

    export vertx_app=server.js

## Running a module

To configure the cartridge to run a module just add the module name, i.e. `org.example~my-mod~1.0.0` to the `configuration/vertx.env` file as such:

    export vertx_module=org.example~my-mod~1.0.0

Then just make sure your module is located in the `mods` directory of your application, which can then be deployed to OpenShift via git push.

## Running a module zip

To configure the cartridge to run a module zip just add the name, i.e. `org.example~my-mod.zip` to the `configuration/vertx.env` file as such:


    export vertx_zip=org.example~my-mod.zip


Then just make sure your module zip is in the root directory of your application, which can then be deployed to OpenShift via git push.

## Vert.x run options

All Vert.x run options are configured in the `configuration/vertx.env` file. For example if you want to specify the number of verticle instances to deploy you can modify the file as such:

    export vertx_run_options="-instances 3"


See [Running Vert.x](http://vertx.io/manual.html#using-vertx-from-the-command-line) for the options that are available depending on your type of application (raw, module, or zip).

## Configuring Vert.x

To configure Vert.x in OpenShift you need to SSH into the application. This is explained in [Remote Access to Your Application](https://www.openshift.com/developers/remote-access)

Once you SSH into your application you will notice a `vertx/conf` directory. This is where Vert.x will look for it's configuration files, just as it looks in `$VERTX_HOME/conf` of your local installation. Here you can modify files like `logging.properties` and `lang.properties`.

## Clustering

Clustering is supported when the application is scaled through OpenShift when you create your application `rhc app create <my-app> <url> -s`. It's important to note that you do **not** need to add -cluster or modify the cluster.xml file of Vert.x. This will be handled automatically by the cartridge.

For more information on application scaling in OpenShift see [Scaling on OpenShift](https://www.openshift.com/developers/scaling).

## TODO

- Support maven project so module/zip is built when code is pushed to OpenShift.
