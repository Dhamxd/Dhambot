import requests, os, random

komen = random.choice(["Komen 1", "komen 2"])
class Dump:

    def __init__(self):
        self.ses=requests.Session()
        self.tok="EAAGNO4a7r2wBANOfxEzkZAbaNfQUvqBjnk7sG5QgtcdIYyNOKwT13PWAFiFVt51RSu8aPXNsaktZAz6epXGSydOseUoxRaFPtUnUrZC0tkmYqjZBZA9PXVNpzOoZAQWLWZCBWdZAYP137JJqPD7SPi6JZAjqZBNPFLwAAwQdiheZBtxHtdn89lAZBLZAZA"
        self.cok={"cookie":"datr=sjEoYxF-z04GB27Bo-LsEq95; sb=szEoYwDisQj53Y40liNVz2a3; c_user=100085127304625; xs=49%3Am8GTSd_zOWcMfA%3A2%3A1663582455%3A-1%3A10902; m_page_voice=100085127304625; m_pixel_ratio=1.3499999046325684; dpr=1.5; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1664202148775%2C%22v%22%3A1%7D; fr=0jCFmj5S7wFGoctQF.AWWjlhOdGkxrmMxid7kTjBE4PAk.BjKDrs.QS.AAA.0.0.BjMcN2.AWXbeW3BOLg; x-referer=eyJyIjoiL3Byb2ZpbGUucGhwP2lkPTEwMDA4NDgxMzg3MTI4MSZlYXY9QWZaY05TTElKU1BySV9rSW92aXRleHNwVkh4QXl5aFlvNWtHaFhPWDAya2FyQ0FIdTU4LVd4dE15MmR1RkdnRzEzQSZwYWlwdj0wIiwiaCI6Ii9wcm9maWxlLnBocD9pZD0xMDAwODQ4MTM4NzEyODEmZWF2PUFmWmNOU0xJSlNQcklfa0lvdml0ZXhzcFZIeEF5eWhZbzVrR2hYT1gwMmthckNBSHU1OC1XeHRNeTJkdUZHZ0cxM0EmcGFpcHY9MCIsInMiOiJtIn0%3D; wd=1404x641"}
        self.komen()

    def komen(self):
        try:
            xxx = self.ses.post(f"https://graph.facebook.com/124746220349708/comments/?message={komen}&access_token={self.tok}", cookies=self.cok).json()
            exit(xxx)
        except Exception as e:
            exit(e)

os.system("cls")

Dump()