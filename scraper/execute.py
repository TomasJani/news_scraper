import time
from datetime import datetime

import schedule

from scraper import update_time
from scraper.dennik_n import DennikN
from scraper.hlavne_spravy import HlavneSpravy
from scraper.mail_notifier import send_logs
from scraper.plus_7_dni import Plus7Dni
from scraper.sme import SME
from scraper.zem_a_vek import ZemAVek


def set_and_scrape():  # get sections from config
    update_time()
    print(f'Started at: {datetime.now()}')
    DennikN.main()
    HlavneSpravy.main()
    Plus7Dni.main()
    SME.main()
    ZemAVek.main()
    send_logs()


schedule.every().day.at('05:00').do(set_and_scrape)


def start():
    while True:
        schedule.run_pending()
        time.sleep(1)