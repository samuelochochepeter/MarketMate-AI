"""Regenerate fictional demo records. Overwrites only the two demo CSV files."""
import csv
import datetime
from pathlib import Path
import random

def main():
    root=Path(__file__).resolve().parent
    rng=random.Random(42)
    start=datetime.date(2026,7,1)
    with (root/'sales_demo.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['date','units','unit_price','promo','ad_spend'])
        for i in range(120):
            day=start+datetime.timedelta(days=i)
            price=rng.choice([2200,2400,2500,2700])
            promo=int(rng.random()<.3)
            spend=rng.choice([0,500,1000,1500,2000])
            units=max(0,round(35+12*(day.weekday()>=5)+9*promo+.005*spend-.012*(price-2400)+rng.gauss(0,3)))
            w.writerow([day,units,price,promo,spend])
    with (root/'social_demo.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['date','platform','format','reach','likes','comments','shares','saves','clicks','leads','spend'])
        for i in range(36):
            platform=['Facebook','Instagram'][i%2]
            fmt=['Reel','Carousel','Image'][(i//2)%3]
            reach=rng.randint(300,1800)
            rate={'Reel':.055,'Carousel':.041,'Image':.018}[fmt]
            interactions=round(reach*rate)
            likes=round(interactions*.6);comments=round(interactions*.12);shares=round(interactions*.13)
            saves=interactions-likes-comments-shares
            clicks=rng.randint(5,35);leads=rng.randint(1,min(clicks,10));spend=rng.choice([0,500,1000])
            w.writerow([start+datetime.timedelta(days=i*3),platform,fmt,reach,likes,comments,shares,saves,clicks,leads,spend])

if __name__=='__main__':main()
