import pandas as pd
import numpy as np
import json
from datetime import datetime
import datetime as dt


class DataHelper:
    @staticmethod
    def load_and_clean():
        with open("data.json", "r") as f:
            raw_json= json.load(f)
            data = pd.DataFrame(raw_json)
            data.replace("tbd", np.nan, inplace=True)
            data.release_date = data.release_date.apply(lambda x: datetime.strptime(x, "%b %d"))
            data["user_score"] = data["user_score"].astype(float)
            data["critic_score"] = data["critic_score"].astype(float)
            return data
    

    @staticmethod
    def get_complete_data(data, save_csv=False):
        data_complete = data.dropna(subset=["critic_score", "user_score"]).copy()
        data_complete["combined_score"] = data_complete["user_score"] + data_complete["critic_score"]
        data_complete["score_gap"] = (data_complete["user_score"] * 10) - data_complete["critic_score"]
        if save_csv==True:
            data_complete.to_csv("./out_csv_files/output_"+ str(dt.date.today()) +".csv", index=False)
        return data_complete


    @staticmethod
    def store_overall_best(data_complete):
        best_10 = data_complete.sort_values("combined_score", ascending=False)[:10]
        overal_bests = f"""
            This time around, the No.1 overall best game is...

            '{best_10.iloc[0].title}'
            with user_score = {best_10.iloc[0].user_score}
            and critic_score = {best_10.iloc[0].critic_score}
            Overall score = {best_10.iloc[0].combined_score}

            Followed by:

            No.2 '{best_10.iloc[1].title}',
                user_score = {best_10.iloc[1].user_score}
                citic_score = {best_10.iloc[1].critic_score}
                Overall score = {best_10.iloc[0].combined_score}

            No.3 '{best_10.iloc[2].title}',
                user_score = {best_10.iloc[2].user_score}
                citic_score = {best_10.iloc[2].critic_score}
                Overall score = {best_10.iloc[0].combined_score}

            No.4 '{best_10.iloc[3].title}',
                user_score = {best_10.iloc[3].user_score}
                citic_score = {best_10.iloc[3].critic_score}
                Overall score = {best_10.iloc[0].combined_score}

            No.5 '{best_10.iloc[4].title}',
                user_score = {best_10.iloc[4].user_score}
                citic_score = {best_10.iloc[4].critic_score} 
                Overall score = {best_10.iloc[0].combined_score}
            """ + '-'*65
        return overal_bests


    @staticmethod
    def store_critic_best(data_complete):
        critic_10 = data_complete.sort_values("critic_score", ascending=False)[:10]
        critic_bests = f"""
            This time around, the No.1 critcs' favorite game is...

            '{critic_10.iloc[0].title}'
            with user_score = {critic_10.iloc[0].user_score}
            and critic_score = {critic_10.iloc[0].critic_score}
  
            Followed by:

            No.2 '{critic_10.iloc[1].title}',
                user_score = {critic_10.iloc[1].user_score}
                citic_score = {critic_10.iloc[1].critic_score}
     
            No.3 '{critic_10.iloc[2].title}',
                user_score = {critic_10.iloc[2].user_score}
                citic_score = {critic_10.iloc[2].critic_score}
        
            No.4 '{critic_10.iloc[3].title}',
                user_score = {critic_10.iloc[3].user_score}
                citic_score = {critic_10.iloc[3].critic_score}
  
            No.5 '{critic_10.iloc[4].title}',
                user_score = {critic_10.iloc[4].user_score}
                citic_score = {critic_10.iloc[4].critic_score} 
            """ + '-'*65
        return critic_bests


    @staticmethod
    def store_users_best(data_complete):
        users_10 = data_complete.sort_values("user_score", ascending=False)[:10]
        users_bests = f"""
            This time around, the No.1 users' favorite game is...

            '{users_10.iloc[0].title}'
            with user_score = {users_10.iloc[0].user_score}
            and critic_score = {users_10.iloc[0].critic_score}
  
            Followed by:

            No.2 '{users_10.iloc[1].title}',
                user_score = {users_10.iloc[1].user_score}
                citic_score = {users_10.iloc[1].critic_score}
     
            No.3 '{users_10.iloc[2].title}',
                user_score = {users_10.iloc[2].user_score}
                citic_score = {users_10.iloc[2].critic_score}
        
            No.4 '{users_10.iloc[3].title}',
                user_score = {users_10.iloc[3].user_score}
                citic_score = {users_10.iloc[3].critic_score}
  
            No.5 '{users_10.iloc[4].title}',
                user_score = {users_10.iloc[4].user_score}
                citic_score = {users_10.iloc[4].critic_score} 
            """ + '-'*65
        return users_bests


    @staticmethod
    def store_controverial_good(data_complete):
        turnout_good = data_complete.sort_values("score_gap", ascending=False)[:10]
        controversial_good = f"""
            This time around, the No.1 controversial but actually good game is
            '{turnout_good.iloc[0].title}'
            with adjusted user_score = {turnout_good.iloc[0].user_score*10}
            and critic_score = {turnout_good.iloc[0].critic_score}
            Score gap is {turnout_good.iloc[0].score_gap}
            
            Followed by:
            No.2 '{turnout_good.iloc[1].title}',
                adjusted user_score = {turnout_good.iloc[1].user_score*10}
                citic_score = {turnout_good.iloc[1].critic_score}
                Score gap is {turnout_good.iloc[1].score_gap}
            
            No.3 '{turnout_good.iloc[2].title}',
                adjusted user_score = {turnout_good.iloc[2].user_score*10}
                citic_score = {turnout_good.iloc[2].critic_score}
                Score gap is {turnout_good.iloc[2].score_gap}
                
            No.4 '{turnout_good.iloc[3].title}',
                adjusted user_score = {turnout_good.iloc[3].user_score*10}
                citic_score = {turnout_good.iloc[3].critic_score}
                Score gap is {turnout_good.iloc[3].score_gap}
                
            No.5 '{turnout_good.iloc[4].title}',
                adjusted user_score = {turnout_good.iloc[0].user_score*10}
                citic_score = {turnout_good.iloc[4].critic_score}
                Score gap is {turnout_good.iloc[4].score_gap}
            """+ '-'*65
        return controversial_good


    @staticmethod
    def store_controverial_bad(data_complete):
        turnout_bad = data_complete.sort_values("score_gap", ascending=True)[:10]
        controversial_bad = f"""
            This time around, the No.1 controversial but actually bad game is
            '{turnout_bad.iloc[0].title}'
            with adjusted user_score = {turnout_bad.iloc[0].user_score*10}
            and critic_score = {turnout_bad.iloc[0].critic_score}
            Score gap is {turnout_bad.iloc[0].score_gap}

            Followed by:
            No.2 '{turnout_bad.iloc[1].title}',
                adjusted user_score = {turnout_bad.iloc[1].user_score*10}
                citic_score = {turnout_bad.iloc[1].critic_score}
                Score gap is {turnout_bad.iloc[1].score_gap}

            No.3 '{turnout_bad.iloc[2].title}',
                adjusted user_score = {turnout_bad.iloc[2].user_score*10}
                citic_score = {turnout_bad.iloc[2].critic_score}
                Score gap is {turnout_bad.iloc[2].score_gap}

            No.4 '{turnout_bad.iloc[3].title}',
                adjusted user_score = {turnout_bad.iloc[3].user_score*10}
                citic_score = {turnout_bad.iloc[3].critic_score}
                Score gap is {turnout_bad.iloc[3].score_gap}

            No.5 '{turnout_bad.iloc[4].title}',
                adjusted user_score = {turnout_bad.iloc[4].user_score*10}
                citic_score = {turnout_bad.iloc[4].critic_score}
                Score gap is {turnout_bad.iloc[4].score_gap}
            """ + '-'*65
        return controversial_bad

    

    
