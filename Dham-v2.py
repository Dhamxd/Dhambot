import requests, os, random

komen = random.choice(["nyoba graph", "komen 2"])
class Dump:

    def __init__(self):
        self.ses=requests.Session()
        self.tok="EAAAAUaZA8jlABAKBdneLKcIQyVr6JqASfzTiwKY9tPSdgZBrU2EE40S8DOT5lfe3HOsK5Vp2YtjSR7Pu3VsBRmZCQaNGNFDblvH3WQLgiUC0apNrHnMziBWQuAIMl7Gdcuspz7e10RrmTZASJ29peuQ7LMJtetENPABd0Uh2FhVYH6ZBxU9ghYV2KlVIdlisZD"
        self.cok={"cookie":"datr=TK1SYxelA1gNrHVS9ByFvDmI;sb=TK1SY9u0QLTuGkV-F2LLm3jz;locale=id_ID;c_user=100087281280151;xs=35%3AsbRc1ck-p60tiw%3A2%3A1666363370%3A-1%3A-1;m_page_voice=100087281280151;wd=412x758;fr=0WFTn8RN6Eg5bxKW9.AWVwbTAq0HMS3qBicn3oDCkNF6I.BjUq1M.6p.AAA.0.0.BjUq_7.AWXyhmo2Ks4;"}
        self.komen()

    def komen(self):
        try:
            xxx = self.ses.post(f"https://graph.facebook.com/637031754466680/comments/?message={komen}&access_token={self.tok}", cookies=self.cok).json()
            exit(xxx)
        except Exception as e:
            exit(e)

os.system("cls")

Dump()