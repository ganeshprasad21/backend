/** @type {CodeceptJS.MainConfig} */
exports.config = {
  tests: './*_test.js',
  output: './output',
  helpers: {
    WebDriver: {
      url: 'https://google.com',
      browser: 'chrome',
      host: 'localhost',
      port: 4444,
      restart: false,
      windowSize: '1920x1680',
      desiredCapabilities: {
        chromeOptions: {
          args: [ /*"--headless",*/ "--disable-gpu", "--no-sandbox" ]
        }
      }
    },
  },
  include: {
    I: './steps_file.js'
  },
  name: 'codecept'
}