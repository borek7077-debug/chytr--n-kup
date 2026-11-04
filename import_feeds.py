#!/usr/bin/env python3
"""Internal weekly audit of partner XML feeds, without public deployment."""
import csv, re, tempfile, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

FEEDS = {
"naradi":("Nářadí-Praha.cz","https://feeds.mergado.com/naradi-praha-cz-heureka-cz-92c0f0d84d921e653b3520c9875ee4be.xml"),
"simon":("Nářadí-Simon.cz","https://www.naradi-simon.cz/rss/heureka-zbozi-2342296.php"),
"cubenest":("Cubenest.cz","https://www.cubenest.cz/erp/impexp/heurekaexport/download"),
"portal":("Portál.cz","https://obchod.portal.cz/provisiondata/sc_portalovky.xml"),
"battex":("BATTEX.cz","https://feeds.mergado.com/battex-cz-heureka-cz-cz-e3d1fc78ef92bd6767b2cc085ae7b064.xml"),
"berserkr":("Berserkr.cz","https://www.berserkr.cz/heureka/export/products.xml?hash=i32UdmWkgBLWcpT1pLfBhdVD"),
"curele":("Curele-ceas.ro","https://www.curele-ceas.ro/google_nakupy_ro.php?key=5b147c22d84ed75541f8e112cb46b533"),
"venix":("Venixvape.cz","https://venixvape.cz/wp-content/uploads/xml/heureka_1.xml"),
"cigarety":("Cigaretycajk.cz","https://www.cigaretycajk.cz/fotky32085/xml/heureka_cz.xml"),
}
def name(tag): return tag.rsplit('}',1)[-1].lower()
def get(elem,*keys):
    for node in elem:
        if name(node.tag) in keys and node.text and node.text.strip(): return node.text.strip()
    return ""
def download(url,path):
    request=urllib.request.Request(url,headers={"User-Agent":"ChytryNakup-FeedAudit/1.0"})
    with urllib.request.urlopen(request,timeout=100) as response,open(path,"wb") as dst:
        if urlparse(response.url).scheme!="https": raise ValueError("Invalid redirect")
        total=0
        while True:
            chunk=response.read(1024*1024)
            if not chunk:break
            total+=len(chunk)
            if total>250000000:raise ValueError("XML too large")
            dst.write(chunk)
        if total<100:raise ValueError("Feed is empty")
def audit(path):
    total=valid=0
    for _,elem in ET.iterparse(path,events=("end",)):
        if name(elem.tag) not in ("shopitem","item"):continue
        total+=1
        url=get(elem,"url","link")
        raw=get(elem,"price_vat","price")
        title=get(elem,"productname","title","product")
        match=re.search(r"\d[\d\s.,]*",raw)
        if urlparse(url).scheme=="https" and title and match:
            try:
                if float(match.group().replace(" ","").replace(",","."))>0:valid+=1
            except ValueError:pass
        elem.clear()
    if not valid:raise ValueError("No valid products")
    return total,valid
def main():
    failures=[]; rows=[]
    with tempfile.TemporaryDirectory() as folder:
        for key,(label,url) in FEEDS.items():
            try:
                path=Path(folder)/(key+".xml")
                download(url,path)
                total,valid=audit(path)
                rows.append([label,total,valid,"OK"])
            except Exception as exc:
                failures.append(key)
                rows.append([label,0,0,"CHYBA "+str(exc)[:100]])
    with open("feed_report.csv","w",encoding="utf-8",newline="") as output:
        writer=csv.writer(output,delimiter=";")
        writer.writerow(["Obchod","Celkem","Platne","Stav"])
        writer.writerows(rows)
    for row in rows:print(*row,sep=" | ")
    if failures:raise SystemExit("Feed errors: "+", ".join(failures))
if __name__=="__main__":main()
