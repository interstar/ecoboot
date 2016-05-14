from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


import os

def get(d,k) :
    try : 
        return d[k]
    except Exception, e:
        return ""
        
def hasTag(ent,tag):
    ts = get(ent,"tags")
    if ts == "" : return False
    return tag in ts
    
def makeSection(ents,title,includeIt) :    
    row = []
    rows = []
    count = 0
    for e in [e for e in ents if includeIt(e)] :
        if (count == 0) or count % 3 != 0 :
            row.append(e)     
        else :
            rows.append(row)
            row = [e]
        count = count + 1
    rows.append(row)        
                        
    return {
        "title" : title,
        "entities" : rows }


def makePage(pageName,sections) :
    return {"pageName":pageName, "sections" : sections}

def W(cls,s) : return """
[.%s
%s
.]""" % (cls,s)

def j(xs): return "\n".join(xs)

def G(ents,cell) :
    return "\n".join(
       ( W(".row", j([cell(c) for c in row]) ) for row in ents)
    )
    
def getLinks(ent) :
    xs = get(ent,"links")
    if xs == "" : return []
    return ["""<a href="%s">%s</a>""" % ((x.split(" ")[0],x.split(" ")[1])) for x in xs]
        
def cell(ent) :
    
    return """
[.col-md-4 
#### %s
%s

%s

%s 
.] """ %  (ent["name"],get(ent,"desc"),"\n".join(getLinks(ent)),",".join(ent["tags"]))

def ppSection(section) :     
    return """
[.container
### %s    

%s
.]""" % (section["title"], G(section["entities"],cell))

def ppPage(pageName,sections) :
    s = "////%s.html\n" % pageName
    return s + "\n".join([ppSection(s).encode("utf-8") for s in sections])
     
def process(ents) :
    for x in ents : 
        print x['name'], get(x,'desc')
    

def isMappable(ent) : 
    if get(ent,"map") == "" : return False
    
    return True

def ppMap(pageName,ents) :

    mappable = [e for e in ents if isMappable(e)]
    s  = ""
    for m in mappable :
        print m
        x,y = m["map"].split(" ")
        lnk = get(m,"links")
        if lnk != "" : lnk = lnk[0].split(" ")[0]
        s = s + """
makeMarker(%s,%s,'%s',"%s","%s");
""" % (x,y,m["name"],get(m,"desc"),lnk)


    return """
////%s.html

[.container
[.row [.col-md-12
## Makers, Hackers e Artistas em Brasilia
.] .]
[.row [.col-md-12

<div id="map"></div>

.] .] .]

<script>

    var map = L.map('map').setView([-15.7758,-47.8608], 12);

    L.tileLayer('http://b.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>'
    }).addTo(map);

    var h4 = function(s) { return '<h4>' + s + '</h4>'; }
    var link = function(url,s) { return '<a href=\"' + url + '\">' + s + '</a>'; }
    var p = function(s) { return '<p>' + s + '</p>'; }

    var makeMarker = function(x,y,name,desc,url) {
        var m = L.marker([x,y]);
        m.bindPopup(h4(name) + p(desc) + p(link(url,'Site'))) .openPopup();
        m.addTo(map);
        return m;
    }
    
    %s
</script>"
""" % (pageName,s.encode("utf-8"))


DIR = "./data/"

if __name__ == '__main__' :
    with open("data/eco.tpl") as ftpl :
        tpl = ftpl.read()
        print tpl
     
        data = []   
        for fileName in [f for f in os.walk(DIR).next()[2] if f[-5:]=='.yaml'] :
            with open("%s/%s" % (DIR,fileName)) as f :
                data = data + load(f, Loader=Loader)

        print ppMap("index",data)
        print ppPage("lugares",[makeSection(data,"Lugares",lambda x : (hasTag(x,"lugar") ) ) ] )
        print ppPage("makers",[makeSection(data,"Makers",lambda x : (hasTag(x,"maker") or hasTag(x,"hacker"))) ] )
                    
        print ppPage("empresas",[makeSection(data,"Empresas",lambda x : (hasTag(x,"empresa") ) ) ])
        print ppPage("arte",[makeSection(data,"Galerias",lambda x : (hasTag(x,"galeria") ) ) ])        

