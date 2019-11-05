from data_wrangler import DataHelper

dh = DataHelper

test_data = dh.load_and_clean()
complete_data = dh.get_complete_data(test_data)

o_best = dh.store_overall_best(complete_data)
u_best = dh.store_users_best(complete_data)
c_best = dh.store_critic_best(complete_data)
contr_good = dh.store_controverial_good(complete_data)
contr_bad = dh.store_controverial_bad(complete_data)

print(contr_bad)