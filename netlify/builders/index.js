const { builder } = require('@netlify/functions')
const chromium = require('chrome-aws-lambda')
const puppeteer = require('puppeteer-core')

async function handler (event, context) {
  
  const browser = await puppeteer.launch({
    executablePath: '/opt/google/chrome/google-chrome'
      || await chromium.executablePath,
    args: chromium.args,
    headless: chromium.headless
  })

  const page = await browser.newPage()

  await page.goto('https://en.loader.to/4/')
  
  const title = await page.title()

  await browser.close()

  return {
    statusCode: 200,
    body: title
  }
}

exports.handler = builder(handler)