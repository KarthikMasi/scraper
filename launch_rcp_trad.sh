#!/bin/bash
source /home/ramadak/environments/scraper/bin/activate

python /home/ramadak/git_repo/scraper/real_clear_politics_scrap_trad.py >> /home/ramadak/git_repo/scraper/rcp_scrap_trad.txt
