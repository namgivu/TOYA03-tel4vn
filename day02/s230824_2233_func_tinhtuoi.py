# tinhtuoi(1982)  # 2023 -> age=41
import datetime


def tinhtuoi(namsinh):
    """tinh tuoi tu nam sinh"""
    return datetime.datetime.now().year - namsinh

print( tinhtuoi(1982) )
print( tinhtuoi(1983) )
print( tinhtuoi(1986) )
