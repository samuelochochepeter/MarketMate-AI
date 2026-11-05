import base64
import io
import json
import sys
import threading
import unittest
from pathlib import Path
from http.server import ThreadingHTTPServer
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from unittest.mock import patch
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'app'))
from server import Handler

class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start()
        cls.base=f'http://127.0.0.1:{cls.server.server_port}'
    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join()
    def call(self,path,data,origin=None):
        headers={'Content-Type':'application/json'}
        if origin:headers['Origin']=origin
        request=Request(self.base+path,data=json.dumps(data).encode(),headers=headers)
        try:
            with urlopen(request) as response:return response.status,json.load(response)
        except HTTPError as e:return e.code,json.load(e)
    def test_demo_page_and_analysis(self):
        with urlopen(self.base) as r:self.assertIn(b'MarketMate AI',r.read())
        with urlopen(self.base+'/api/demo') as r:data=json.load(r)
        code,result=self.call('/api/analyse',data)
        self.assertEqual(code,200);self.assertEqual(result['summary']['units'],5519)
    def test_bad_origin_and_bad_payload(self):
        code,_=self.call('/api/analyse',{},'https://untrusted.example')
        self.assertEqual(code,403)
        code,_=self.call('/api/analyse',{})
        self.assertEqual(code,400)
        code,_=self.call('/api/analyse',[])
        self.assertEqual(code,400)
    def test_prompt_and_model_failure(self):
        with urlopen(self.base+'/api/demo') as r:data=json.load(r)
        data.update(brand='Demo',audience='Adults',product='Bread')
        code,result=self.call('/api/prompt',data)
        self.assertEqual(code,200);self.assertIn('ROLE:',result['prompt'])
        data['generate']=True
        with patch('server.llama',side_effect=URLError('offline')):
            code,result=self.call('/api/prompt',data)
        self.assertEqual(code,503);self.assertIn('unavailable',result['error'])
    def test_vision_routing_with_mock_and_bad_image(self):
        b=io.BytesIO();Image.new('RGB',(20,20),'white').save(b,format='PNG')
        image=base64.b64encode(b.getvalue()).decode()
        # Mock proves image plumbing only. It is not an inference evaluation.
        with patch('server.llama',return_value={'text':'MOCK ONLY','model':'llama3.2-vision'}) as mocked:
            code,result=self.call('/api/vision',{'image':image})
            self.assertEqual(code,200);self.assertEqual(result['text'],'MOCK ONLY')
            self.assertTrue(mocked.call_args.args[1])
        code,_=self.call('/api/vision',{'image':'not-valid-base64'})
        self.assertEqual(code,400)

if __name__=='__main__':unittest.main()
