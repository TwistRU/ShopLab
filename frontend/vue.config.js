module.exports = {
    css: {
        loaderOptions: {
            sass: {
                prependData: `@import "@/assets/styles/styles.scss";`
            }
        }
    },
    publicPath: "./",
    outputDir: "D:\\Programs\\ShopLab\\frontend\\dist"
};