const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
	publicPath: process.env.NODE_ENV === "production"
		? "/"
		: "http://localhost:8080/",
	outputDir: 'dist',
	assetsDir: 'static',

	chainWebpack: config => {

		config.optimization
			.splitChunks(false)

		config
			.plugin('BundleTracker')
			.use(BundleTracker, [{filename: './webpack-stats.json'}])

		config.resolve.alias
			.set('__STATIC__', 'static')

		config.devServer
			.public('http://localhost:8080')
			.host('localhost')
			.port(8080)
			.hotOnly(true)
			.watchOptions({poll: 1000})
			.https(false)
			.headers({"Access-Control-Allow-Origin": ["\*"]})
	}
};