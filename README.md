# github-actions-demo
This repo is a demo for scraping on a schedule with GitHub Actions. It's a work in progress.

## What's happening?

We're using [GitHub Actions](https://github.com/features/actions) to scrape calls for service from Oakland, CA. It's the same information you can find [here](https://www.arcgis.com/home/webmap/viewer.html?url=http%3A%2F%2Fgismaps.oaklandca.gov%2Foaklandgis%2Frest%2Fservices%2Fcallforservice_2015_FC%2FFeatureServer%2F0&source=sd), but in CSV form. If you'd like more information, [here's all we know about the Data Source](https://airtable.com/shrUAtA8qYasEaepI/tblx8XaKnFTphWNQM/viw9mmOR0fw8HFOje/rec993D5V56tjO2UB).

### Note:
*The city of Oakland [reported a ransomware attack](https://www.oaklandca.gov/news/2023/city-of-oakland-targeted-by-ransomware-attack-core-services-not-affected) that they confirm affected this data. February 9 is the last day the city posted new data. For February 10, the data is identical to the day before. There was no data at all posted for February 11 and 12. And since February 13, the data again repeats, identically, what the city had available February 9. We've been in touch the city of Oakland and will note here when there is a fix.*

## Why GitHub Actions?
It gives us, in this case, cron capability and free storage ([to a point](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions)) for any scraper we tell it how to run.

It will also monitor the jobs for us and commit and push back to the repo any new data it finds at our endpoint. All without us having to do anything beyond setting it up in `.github/workflows/update.yml`.
