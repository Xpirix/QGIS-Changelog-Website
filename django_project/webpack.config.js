const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require('webpack');

const mode = process.argv.includes("production") ? "production" : "development";
console.log(`Webpack mode: ${mode}`);

// Common plugins
const plugins = [
  new BundleTracker({ path: __dirname, filename: 'webpack-stats.json' }),
  new MiniCssExtractPlugin({
    filename: 'css/[name].[contenthash].css',
  }),
  new webpack.ProvidePlugin({
    $: 'jquery',
    jQuery: 'jquery',
    'window.jQuery': 'jquery',
    'window.$': 'jquery',
  }),
];

// Development-only plugins
if (mode === 'development') {
  const LiveReloadPlugin = require('webpack-livereload-plugin');
  plugins.push(new LiveReloadPlugin({ appendScriptTag: true }));
}

// List of libraries to expose globally
const exposeLibraries = [
  { name: 'jquery', exposes: ['$', 'jQuery'] },
  { name: 'datatables.net', exposes: ['DataTable'] },
  { name: 'moment', exposes: ['moment'] },
  { name: 'leaflet', exposes: ['Leaflet'] },
  { name: 'air-datepicker', exposes: ['AirDatepicker'] },
  { name: 'air-datepicker/locale/en', exposes: ['localeEn'] },
  { 
    name: 'jquery-ui/ui/widgets/sortable', 
    exposes: [{
      globalName: 'jQuery.fn.sortable',
      override: true
    }]
  },
];

module.exports = {
  entry: './base/static/js/index',
  output: {
    path: path.resolve('./base/static/bundles'),
    filename: "[name].[contenthash].js",
    publicPath: '/static/bundles/',
  },
  plugins,
  module: {
    rules: [
      // Auto-generate expose-loader rules
      ...exposeLibraries.map(lib => ({
        test: require.resolve(lib.name),
        loader: 'expose-loader',
        options: {
          exposes: lib.exposes,
        },
      })),
      // CSS and SCSS rules
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader"],
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          {
            loader: 'sass-loader',
            options: {
              sourceMap: true,
            },
          },
        ],
      },
      // For jQuery UI images
      {
        test: /\.(png|jpe?g|gif|svg)$/,
        type: 'asset/resource',
        generator: {
          filename: 'images/[name].[hash][ext]',
        },
      },
    ],
  },
  stats: {
    assets: false,
    chunks: false,
    modules: false,
    entrypoints: false,
    performance: false,
    errors: true,
    errorDetails: true,
    warnings: true,
    builtAt: true,
    colors: true,
  },
};