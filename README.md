# OpenShift Cartridge for Vert.x
A downloadable cartridge which can be used to run Vert.x on OpenShift. 

## Getting started

If you don't have an account, or aren't familiar with OpenShift you can go to 
[Getting Started with OpenShift](https://www.openshift.com/get-started/) to help guide you through setting up your environment.

Once our environment is setup we can create our first application (we'll call it demo) using the rhc client tools.

    rhc app create demo https://raw.github.com/vert-x/openshift-cartridge/master/metadata/manifest.yml

To create a scaled vertx application:

    rhc app create demo https://raw.github.com/vert-x/openshift-cartridge/master/metadata/manifest.yml -s

This will create a directory named `demo` which will include the `server.js` application that this cartridge uses as the
default application. You should be able to access your application and see a OpenShift Vertx welcome page. From here you
now have the ability to run your favorite Vert.x application in the cloud. Enjoy !

## Running a raw verticle

The cartridge by default is configured to run the `server.js` as a raw verticle. To modify this value change the variable in the `configuration/vertx.env` file:

    export vertx_app=server.js

## Running a module

To configure the cartridge to run a module just add the module name, i.e. `org.example~my-mod~1.0.0` to the `configuration/vertx.env` file:

    export vertx_module=org.example~my-mod~1.0.0

This tells Vert.x to look for the module `org.example~my-mod~1.0.0` under the `mods` directory of your application. To deploy the module just add the module (under the `mods` directory) to the git repository and push.

## Running a module zip

To configure the cartridge to run a module zip just add the name, i.e. `org.example~my-mod.zip` to the `configuration/vertx.env` file:


    export vertx_zip=org.example~my-mod.zip


This tells Vert.x to look for the `org.example~my-mod.zip` file in the root of your application. To deploy the module zip just add the zip module to the git repository and push.

## Vert.x run options

All Vert.x run options are configured with the `vertx_run_options` variable in the `configuration/vertx.env` file. For example if you want to specify the number of instances to deploy:

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
