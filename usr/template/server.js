/**
 * JBoss, Home of Professional Open Source
 * Copyright Red Hat, Inc., and individual contributors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

var env = Java.type("java.lang.System").env;

var ip = env['OPENSHIFT_VERTX_IP'] || '127.0.0.1';
var port = parseInt(env['OPENSHIFT_VERTX_PORT'] || 8080);

vertx.createHttpServer({port: port, host: ip}).requestHandler(function(req) {
  var file = req.path() === '/' ? 'index.html' : req.path();
  req.response().sendFile('webroot/' + file);
}).listen(function(server, err) {
    if (!err) {
      console.log('Successfully listening on ' + ip + ':' + port);
    } else {
      console.log('Could not bind to ' + ip + ':' + port + '. Error: ' + err);
    }
});
