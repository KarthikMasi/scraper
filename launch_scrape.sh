#!/bin/bash
source /home/ramadak/environments/scraper/bin/activate

python /home/ramadak/git_repo/scraper/scraper_test.py >> /home/ramadak/git_repo/scraper/Elections_scrape.txt
