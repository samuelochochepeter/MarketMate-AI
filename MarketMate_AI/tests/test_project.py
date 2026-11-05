"""Run from the project root: python -m unittest discover -s tests -v"""
import sys
import unittest
from pathlib import Path
import numpy as np
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'app'))
from core import analyse, clean, fit_model, content_prompt, scenario

class ProjectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sales=pd.read_csv(ROOT/'data/sales_demo.csv').to_dict('records')
        cls.social=pd.read_csv(ROOT/'data/social_demo.csv').to_dict('records')

    def test_revenue_and_weighted_engagement(self):
        result=analyse(self.sales,self.social)
        expected=sum(r['units']*r['unit_price'] for r in self.sales)
        self.assertEqual(result['summary']['revenue_ngn'],expected)
        rate=sum(sum(r[k] for k in ['likes','comments','shares','saves']) for r in self.social)/sum(r['reach'] for r in self.social)*100
        self.assertEqual(result['summary']['engagement_rate_pct'],round(rate,2))

    def test_zero_denominators(self):
        social=[dict(self.social[0],reach=0,likes=0,comments=0,shares=0,saves=0,clicks=0,leads=0)]
        s=analyse(self.sales,social)['summary']
        self.assertEqual(s['engagement_rate_pct'],0)
        self.assertEqual(s['click_to_lead_pct'],0)
        self.assertIsNone(s['cost_per_lead_ngn'])

    def test_invalid_values(self):
        for changes in [{'units':-1},{'units':'bad'},{'units':float('inf')},{'date':'2026-99-01'},{'promo':2},{'unit_price':0},{'units':1.5}]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                clean([dict(self.sales[0],**changes)],'sales')

    def test_duplicate_and_missing_columns(self):
        df,notes=clean(self.sales+[self.sales[0]],'sales')
        self.assertEqual(len(df),120)
        with self.assertRaises(ValueError): clean([{'date':'2026-01-01'}],'sales')
        with self.assertRaises(ValueError): clean(self.sales+[dict(self.sales[0],units=200)],'sales')

    def test_chronological_split_no_test_label_leakage(self):
        df,_=clean(self.sales,'sales')
        _,before=fit_model(df)
        changed=df.copy();changed.loc[96:,'units']=changed.loc[96:,'units']+500
        _,after=fit_model(changed)
        self.assertEqual(before['train_rows'],96)
        self.assertEqual(before['test_rows'],24)
        self.assertLess(before['train_end'],before['test_start'])
        self.assertEqual([r['predicted'] for r in before['holdout']],[r['predicted'] for r in after['holdout']])
        self.assertNotEqual(before['mae_units'],after['mae_units'])

    def test_scenario_and_small_dataset(self):
        df,_=clean(self.sales,'sales')
        result=scenario(df,{'unit_price':9000,'ad_spend':0,'promo':0})
        self.assertTrue(result['warnings'])
        self.assertGreaterEqual(result['estimated_units'],0)
        self.assertIsNone(analyse(self.sales[:10],self.social)['forecast'])
        with self.assertRaises(ValueError):scenario(df,{'unit_price':float('nan')})

    def test_prompt_disclosure_and_evidence(self):
        a=analyse(self.sales,self.social)
        p=content_prompt('Demo','Adults','Bread',a['summary'],a['groups'])
        for x in ['ROLE:','CONTEXT:','TASK:','CONSTRAINTS:','FORMAT:','untrusted','Do not invent','disclosure']:
            self.assertIn(x,p)
        self.assertIn(str(a['summary']['revenue_ngn']),p)

if __name__=='__main__': unittest.main()
