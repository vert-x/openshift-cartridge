# OpenShift Cartridge for Vert.x
A downloadable cartridge which can be used to run Vert.x on OpenShift

## Getting started

To create a vertx application on OpenShift run the following command using the rhc client tools:

    rhc app create <app-name> https://raw.github.com/vert-x/openshift-cartridge/master/metadata/manifest.yml

To create a scaled vertx application run the following command:

    rhc app create <app-name> https://raw.github.com/vert-x/openshift-cartridge/master/metadata/manifest.yml -s

## Running a raw verticle

The default application is configured to run the raw `server.js`. This is controlled by the `configuration/vertx.env` file entry:

  export vertx_app=server.js

## Running a module

To configure the cartridge to run a module just add the module name, i.e. `org.example~my-mod~1.0.0` to the `configuration/vertx.env` file as such:

```
  export vertx_module=org.example~my-mod~1.0.0
```

Then just make sure your module is located in the `mods` directory of your application, which can then be deployed to OpenShift via git push.

## Running a module zip

To configure the cartridge to run a module zip just add the name, i.e. `org.example~my-mod.zip` to the `configuration/vertx.env` file as such:

```
  export vertx_zip=org.example~my-mod.zip
```

Then just make sure your module zip is in the root directory of your application, which can then be deployed to OpenShift via git push.

## TODO

Support maven project so module/zip is built when code is pushed to OpenShift.
