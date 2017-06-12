var webpack = require('webpack')

module.exports = {
  context: __dirname,

  entry: {
     app: './main.jsx',
  },

  output: {
      path: '../SherwoodBET/Static/static/Apps/',
      filename: "[name].js",
  },

  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        }
      },
      {
        test: /\.css$/,
        loader: "style-loader!css-loader"
      }
    ],
  },

  resolve: {
    modulesDirectories: ['node_modules', 'assets/css', 'assets/js'],
    extensions: ['', '.js', '.jsx', '.css']
  },
}
