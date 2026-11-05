const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
const root=require('node:path').resolve(__dirname,'..');
const html=fs.readFileSync(root+'/app/templates/index.html','utf8');
const ids=[...html.matchAll(/id="([^"]+)"/g)].map(m=>m[1]);
class Element{constructor(){this.children=[];this.value='';this.textContent='';this.files=[];}append(...c){this.children.push(...c);}replaceChildren(...c){this.children=c;}setAttribute(k,v){this[k]=v;}scrollIntoView(){}select(){}click(){}}
const elements=Object.fromEntries(ids.map(id=>[id,new Element()]));
const dataset={sales:[],social:[]};
const analysis=JSON.parse(fs.readFileSync(root+'/docs/demo_analysis.json','utf8'));
const context={document:{getElementById(id){assert.ok(elements[id],`Unknown element ${id}`);return elements[id];},createElement:()=>new Element(),createElementNS:()=>new Element()},fetch:async path=>({ok:true,json:async()=>path==='/api/demo'?dataset:analysis}),Intl,console,setTimeout,Blob,URL};
vm.createContext(context);vm.runInContext(fs.readFileSync(root+'/app/static/app.js','utf8'),context);
setTimeout(()=>{assert.equal(elements.metrics.children.length,4);assert.equal(elements.groups.children.length,6);assert.equal(elements.price.value,2200);assert.equal(elements.adSpend.value,0);assert.ok(elements.chart.children.length>0);const parsed=vm.runInContext('parseCSV(\'name,value\\r\\n"a,b",2\\r\\n"a""b",3\')',context);assert.equal(parsed[0].name,'a,b');assert.equal(parsed[1].name,'a"b');assert.throws(()=>vm.runInContext('parseCSV(\'a,a\\n1,2\')',context));assert.throws(()=>vm.runInContext('parseCSV(\'a,b\\n1\')',context));console.log('Frontend render smoke check and CSV edge cases passed in a simulated DOM. This is not browser QA.');},30);
