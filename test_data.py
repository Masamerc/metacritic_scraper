from data_wrangler import DataHelper
from email_data import send_email
import datetime 
dh = DataHelper

test_data = dh.load_and_clean()
complete_data = dh.get_complete_data(test_data)

o_best = dh.store_overall_best(complete_data)
u_best = dh.store_users_best(complete_data)
c_best = dh.store_critic_best(complete_data)
contr_good = dh.store_controverial_good(complete_data)
contr_bad = dh.store_controverial_bad(complete_data)


# send_email(subject=f"Metacritic Scraper {datetime.date.today()}", content=o_best + "\n" + u_best\
#     + "\n" + c_best + "\n" + contr_good + "\n" + contr_bad)

print(contr_bad)