/*
 * Main Javascript file for my_flask_app.
 *
 * This file bundles all of your javascript together using webpack.
 */

// JavaScript modules
require('@fortawesome/fontawesome-free');
require('jquery');
require('popper.js');
require('bootstrap');
require('chart.js');

require.context(
  '../img', // context folder
  true, // include subdirectories
  /.*/, // RegExp
);

// Your own code
require('./plugins.js');
require('./script.js');
require('./sb-admin-2.js');
require('./demo/chart-pie-demo.js');
require('./demo/chart-area-demo.js');
