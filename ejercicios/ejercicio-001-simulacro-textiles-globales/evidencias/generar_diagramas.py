"""Crea seis fuentes nativas DRAW.IO. No usa otros lenguajes de diagramación."""
from pathlib import Path
import xml.etree.ElementTree as E
import json
import textwrap

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "diagramas" / "fuentes"
OUT.mkdir(parents=True, exist_ok=True)
BLUE = "#dae8fc"
GREEN = "#d5e8d4"
GRAY = "#f5f5f5"
ACTORS = ["Jefe de Planta", "Operario de Corte", "Operario de Confección", "Inspector de Calidad"]
FLOWS = [
    ("F01",0,"in","Orden de Trabajo y datos de tela asignada"),
    ("F02",0,"out","OT habilitada y resumen de producción"),
    ("F03",1,"in","Registro de corte y merma"),
    ("F04",1,"out","Datos de corte y estado del registro"),
    ("F05",2,"in","Registro de avance y tiempo por lote"),
    ("F06",2,"out","Datos de paquete habilitado y estado de confección"),
    ("F07",3,"in","Resultado de inspección y defectos"),
    ("F08",3,"out","Resumen de calidad y código de lote"),
]
MESSAGES = [
    (1,0,4,"OT y metraje asignado"),
    (2,4,5,"Guardar OT y habilitación"),
    (3,5,4,"OT persistida"),
    (4,4,0,"OT habilitada"),
    (5,1,4,"Conteo de piezas y merma"),
    (6,4,5,"Guardar corte y paquete"),
    (7,5,4,"Corte persistido"),
    (8,4,1,"Confirmación de corte"),
    (9,2,4,"Avance por paquete y tiempo de lote"),
    (10,4,5,"Guardar avance y tiempo"),
    (11,5,4,"Confección persistida"),
    (12,4,2,"Confirmación de confección"),
    (13,3,4,"Resultado individual de inspección"),
    (14,4,5,"[aprobada] Guardar prenda aprobada"),
    (15,4,5,"[rechazada] Guardar rechazo y causa"),
    (16,5,4,"Inspección persistida"),
    (17,4,3,"Resumen de aprobadas y rechazadas"),
    (18,3,4,"Liberación de aprobadas para empaque"),
    (19,4,5,"[hay aprobadas] Generar y guardar código de lote"),
    (20,4,3,"Código de lote y confirmación de liberación"),
]

class Diagram:
    def __init__(self, title, width, height):
        self.title, self.width, self.height = title, width, height
        self.xml = E.Element("mxfile",host="app.diagrams.net",version="32.3.0")
        d=E.SubElement(self.xml,"diagram",id=title.split()[0],name=title)
        m=E.SubElement(d,"mxGraphModel",dx=str(width),dy=str(height),grid="1",gridSize="10",page="1",pageWidth=str(width),pageHeight=str(height),math="0",shadow="0")
        self.root=E.SubElement(m,"root")
        E.SubElement(self.root,"mxCell",id="0")
        E.SubElement(self.root,"mxCell",id="1",parent="0")
        self.coords={}
        self.n=0
        self.box("title",title+"\nTextiles Globales S.A.",30,15,width-60,65,"text;html=0;align=left;fontSize=24;fontStyle=1;strokeColor=none;fillColor=none;")
    def box(self,id,text,x,y,w,h,style=None,kind="node"):
        c=E.SubElement(self.root,"mxCell",id=id,value=text,vertex="1",parent="1",style=style or f"rounded=1;whiteSpace=wrap;html=0;fontSize=17;spacing=9;fillColor={BLUE};strokeColor=#6c8ebf;")
        c.set("kind",kind)
        E.SubElement(c,"mxGeometry",x=str(x),y=str(y),width=str(w),height=str(h),attrib={"as":"geometry"})
        self.coords[id]=(x,y,w,h)
        return id
    def edge(self,s,t,label="",style="",points=None,meta=None):
        self.n+=1
        label = "\n".join(textwrap.fill(line, width=48 if (meta or {}).get("message_id") or (meta or {}).get("link_messages") else 24) for line in label.split("\n"))
        styles="edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;fontSize=15;labelBackgroundColor=#ffffff;endArrow=block;endFill=1;strokeWidth=1.5;"+style
        merged=dict(item.split("=",1) for item in styles.split(";") if "=" in item)
        c=E.SubElement(self.root,"mxCell",id=f"e{self.n}",value=label,edge="1",parent="1",source=s,target=t,style=";".join(f"{k}={v}" for k,v in merged.items())+";")
        for k,v in (meta or {}).items(): c.set(k,str(v))
        g=E.SubElement(c,"mxGeometry",relative="1",attrib={"as":"geometry"})
        if points:
            arr=E.SubElement(g,"Array",attrib={"as":"points"})
            for x,y in points:E.SubElement(arr,"mxPoint",x=str(x),y=str(y))
        return c
    def save(self,name):
        E.indent(self.xml)
        E.ElementTree(self.xml).write(OUT/(name+".drawio"),encoding="utf-8",xml_declaration=True)

# Stack por zonas; HTTPS es un enlace, no un equipo ni un despliegue.
d=Diagram("01 Stack de tecnologías",2000,1080)
zone_style="rounded=0;html=0;verticalAlign=top;align=left;fontSize=24;fontStyle=1;spacing=18;fillColor=#f5f5f5;strokeColor=#999999;"
for id,label,x,w in [('planta','PLANTA',30,440),('perimetro','PERÍMETRO',520,390),('nube','NUBE',960,1000)]:
    d.box(id,label,x,115,w,790,zone_style,kind='zone')
components=[
('usuarios','Usuarios de planta\n4 roles',65,205,370,100,'planta'),
('dispositivos','Dispositivos\nTableta o terminal\nLector de código\nImpresora de etiquetas\ncuando corresponda',65,390,370,180,'planta'),
('red','Red local\nCat 6\nWi-Fi industrial / AP',65,685,370,125,'planta'),
('router','Router / firewall',560,680,310,130,'perimetro'),
('internet','Internet',560,390,310,130,'perimetro'),
('servicio','Servicio administrado\nUna aplicación: frontend y backend',1000,195,920,85,'nube'),
('frontend','Frontend\nHTML / CSS\nJavaScript mínimo',1010,385,390,150,'nube'),
('backend','Backend / API\nDjango\nMonolito modular',1510,385,390,150,'nube'),
('postgres','Base de datos\nPostgreSQL\nAcceso privado',1510,695,390,135,'nube'),
('respaldo','Respaldo y monitoreo\nCopia separada\nAlertas',1010,695,390,135,'nube')]
for id,label,x,y,w,h,zone in components:
    d.box(id,label,x,y,w,h,kind='component'); d.root.find(f"./mxCell[@id='{id}']").set('zone',zone)
for s,t in [('usuarios','dispositivos'),('dispositivos','red'),('red','router'),('router','internet')]:d.edge(s,t)
d.edge('internet','frontend','HTTPS','exitX=1;exitY=0.5;entryX=0;entryY=0.5;',meta={'protocol':'HTTPS'})
d.edge('frontend','backend','API','exitX=1;exitY=0.5;entryX=0;entryY=0.5;')
d.edge('backend','postgres','Acceso privado','exitX=0.5;exitY=1;entryX=0.5;entryY=0;')
d.edge('backend','respaldo','Aplicación: monitoreo','exitX=0.1;exitY=1;entryX=0.5;entryY=0;',points=[(1549,610),(1205,610)])
d.edge('postgres','respaldo','Copia de datos','exitX=0;exitY=0.5;entryX=1;entryY=0.5;')
d.box('note','Nube recomendada condicionada a Internet y energía confiables; contingencia manual.\nFrontend y backend: responsabilidades del mismo servicio, no dos despliegues.\nObjetivos propuestos: RPO 24 h y RTO 8 h, sujetos a prueba; no garantías.',40,935,1920,115,'text;html=0;fontSize=20;align=left;strokeColor=none;fillColor=none;')
d.save("01-stack-tecnologias")

# Contexto: cuatro actores reales, ocho flujos nominales.
d=Diagram("02 DFD de contexto",1800,1200)
d.box("p0","0\nSistema de Gestión de Manufactura\nde Textiles Globales S.A.",650,470,500,240,kind="process")
positions=[(60,140),(1420,140),(60,940),(1420,940)]
for i,(x,y) in enumerate(positions):
    d.box(f"a{i}",ACTORS[i],x,y,280,100,f"rounded=0;html=0;whiteSpace=wrap;fontSize=19;spacing=8;fillColor={GRAY};strokeColor=#666666;",kind="entity")
for fid,i,direction,label in FLOWS:
    s,t=(f"a{i}","p0") if direction=="in" else ("p0",f"a{i}")
    # Two distinct corridors per actor keep the request and return readable.
    left=i in (0,2); upper=i<2
    outgoing=direction=="out"
    ax=.65 if outgoing else .35
    px=(.4 if outgoing else .2) if left else (.8 if outgoing else .6)
    lane_y=(330 if outgoing else 400) if upper else (890 if outgoing else 820)
    if not left:
        lane_y=(400 if outgoing else 330) if upper else (820 if outgoing else 890)
    actor_x=positions[i][0]+280*ax
    process_x=650+500*px
    points=[(actor_x,lane_y),(process_x,lane_y)]
    actor_y=1 if upper else 0; process_y=0 if upper else 1
    style=f"exitX={ax};exitY={actor_y};entryX={px};entryY={process_y};"
    if outgoing:
        points.reverse()
        style=f"exitX={px};exitY={process_y};entryX={ax};entryY={actor_y};"
    d.edge(s,t,fid+"\n"+label,style,points=points,meta={"flow_id":fid,"actor":i,"direction":direction})
d.box("note","Entidades externas al software: roles humanos de la planta. Los materiales físicos no son flujos DFD.\nF01-F08 se conservan exactamente en el nivel 0.",40,1110,1700,70,"text;html=0;fontSize=18;align=left;strokeColor=none;fillColor=none;")
d.save("02-dfd-contexto")

# Nivel cero: columnas de responsabilidad con almacenes abiertos abajo.
d=Diagram("03 DFD nivel cero",2300,1120)
processes=["1.0 Gestionar Orden\nde Producción","2.0 Gestionar Corte","3.0 Gestionar Confección","4.0 Gestionar Calidad\ny Empaque"]
stores=["D1 Órdenes de producción\ny tela","D2 Registros de corte","D3 Avances de confección","D4 Inspecciones y\nlotes liberados"]
for i in range(4):
    x=240+i*510
    d.box(f"a{i}",ACTORS[i],x+20,110,400,80,f"rounded=0;whiteSpace=wrap;html=0;fontSize=20;fillColor={GRAY};strokeColor=#666666;",kind="entity")
    d.box(f"p{i}",processes[i],x+20,440,400,110,kind="process")
    d.box(f"db{i}",stores[i],x+20,840,400,80,"shape=partialRectangle;left=0;right=0;top=1;bottom=1;html=0;whiteSpace=wrap;fontSize=19;fillColor=#fff2cc;strokeColor=#d6b656;",kind="store")
    fs=[f for f in FLOWS if f[1]==i]
    for fid,_,direction,label in fs:
        s,t=(f"a{i}",f"p{i}") if direction=="in" else (f"p{i}",f"a{i}")
        ex=.25 if direction=="in" else .75
        d.edge(s,t,fid+"\n"+label,f"exitX={ex};exitY={1 if direction=='in' else 0};entryX={ex};entryY={0 if direction=='in' else 1};",meta={"flow_id":fid,"actor":i,"direction":direction})
    d.edge(f"p{i}",f"db{i}",["OT, tela y metraje","Conteo y merma","Avance y duración","Inspección, defectos\ny código de lote"][i],"exitX=0.25;exitY=1;entryX=0.25;entryY=0;")
    d.edge(f"db{i}",f"p{i}",["OT y estándar registrados","Corte y paquetes registrados","Avances registrados","Calidad y lotes registrados"][i],"exitX=0.75;exitY=0;entryX=0.75;entryY=1;")
for i,label in enumerate(["OT habilitada y datos de tela","Paquete cortado y trazabilidad","Lote confeccionado y tiempos"]):
    e=d.edge(f"p{i}",f"p{i+1}",label,"exitX=1;exitY=0.5;entryX=0;entryY=0.5;")
    E.SubElement(e.find("mxGeometry"),"mxPoint",x="0",y="-95",attrib={"as":"offset"})
d.box('d4alias','D4 Inspecciones y lotes liberados\n(representación repetida del mismo D4)',260,965,400,65,'shape=partialRectangle;left=0;right=0;top=1;bottom=1;html=0;whiteSpace=wrap;fontSize=16;fillColor=#fff2cc;strokeColor=#d6b656;',kind='store_alias')
d.root.find("./mxCell[@id='d4alias']").set('logical_store','db3')
e=d.edge('d4alias','p0','Resumen de calidad y lote liberado','exitX=0;exitY=0.5;entryX=0;entryY=0.8;',points=[(80,998),(80,528)],meta={'logical_source':'db3'})
E.SubElement(e.find('mxGeometry'),'mxPoint',x='100',y='0',attrib={'as':'offset'})
d.box("note","D1-D4: cuatro almacenes lógicos; D4 se representa dos veces para abreviar su lectura por P1.\nP4 actualiza D4; P1 consulta D4 para F02. Balance F01-F08; sin conexión entidad-almacén.",710,970,1540,100,"text;html=0;fontSize=17;align=left;strokeColor=none;fillColor=none;")
d.save("03-dfd-nivel-0")

# Casos de uso: dos columnas permiten relaciones obligatorias y extensión condicional.
d=Diagram("04 Casos de uso",1700,1230)
d.box("boundary","Sistema de Gestión de Manufactura",390,95,1240,1050,"rounded=0;html=0;verticalAlign=top;align=left;fontSize=23;spacing=12;fillColor=none;strokeColor=#333333;",kind="boundary")
ucstyle="ellipse;whiteSpace=wrap;html=0;fontSize=19;spacing=10;fillColor=#dae8fc;strokeColor=#6c8ebf;"
rows=[150,345,540,735,970]
main=["Crear OT y habilitar tela","Registrar corte","Registrar confección","Registrar inspección","Liberar aprobadas para empaque"]
included=["Verificar metraje","Registrar conteo y merma","Registrar avance y tiempo","Clasificar y contar prendas","Generar código de lote"]
for i,y in enumerate(rows):
    d.box(f"uc{i}",main[i],480,y,380,100,ucstyle,kind="usecase")
    d.box(f"inc{i}",included[i],1160,y,380,100,ucstyle,kind="usecase")
    d.edge(f"uc{i}",f"inc{i}","«include»","dashed=1;endArrow=open;endFill=0;",meta={"relation":"include"})
for i,y in enumerate(rows[:4]):
    d.box(f"a{i}",ACTORS[i],60,y,220,115,"shape=umlActor;html=0;whiteSpace=wrap;fontSize=18;verticalLabelPosition=bottom;verticalAlign=top;",kind="entity")
    d.edge(f"a{i}",f"uc{i}","","endArrow=none;")
d.edge("a3","uc4","","endArrow=none;",points=[(300,805),(300,1020)])
d.box("reject","Registrar causa de rechazo",900,870,340,90,ucstyle,kind="usecase")
d.edge("reject","uc3","«extend»\n[prenda rechazada]","dashed=1;endArrow=open;endFill=0;",meta={"relation":"extend"})
d.box("note","Precondición de liberación: existen prendas aprobadas. No atribuye empaque físico al Inspector.",400,1160,1230,55,"text;html=0;fontSize=18;align=left;strokeColor=none;fillColor=none;")
d.save("04-casos-uso")

# Secuencia: líneas de vida nativas y mensajes reutilizados por colaboración.
d=Diagram("05 Diagrama de secuencia",2000,1710)
participants=ACTORS+["Sistema de Gestión\nde Manufactura","Persistencia\nPostgreSQL"]
xs=[150,460,770,1080,1430,1820]
for i,(name,x) in enumerate(zip(participants,xs)):
    d.box(f"h{i}",name,x-130,105,260,90,kind="participant")
    d.box(f"line{i}","",x,210,1,1410,"fillColor=none;strokeColor=#777777;dashed=1;",kind="lifeline")
    if i>=4:d.box(f"act{i}","",x-6,255,12,1320,"fillColor=#dae8fc;strokeColor=#6c8ebf;",kind="activation")
# Frames drawn before messages; no opaque fill.
d.box("loop","loop [por cada prenda]",1000,1040,960,365,"fillColor=none;strokeColor=#888888;html=0;verticalAlign=top;align=left;fontSize=16;spacing=5;",kind="frame")
d.box("alt","alt",1350,1120,580,155,"fillColor=none;strokeColor=#888888;html=0;verticalAlign=top;align=left;fontSize=16;spacing=3;",kind="frame")
d.box("alt-divider","",1350,1192,580,1,"fillColor=none;strokeColor=#888888;dashed=1;",kind="separator")
for n,s,t,label in MESSAGES:
    y=235+n*66
    for idx in (s,t):d.box(f"anchor{n}_{idx}","",xs[idx],y,1,1,"fillColor=none;strokeColor=none;",kind="anchor")
    return_style="dashed=1;endArrow=open;endFill=0;" if s==5 or n in (4,8,12,17,20) else "endArrow=block;"
    d.edge(f"anchor{n}_{s}",f"anchor{n}_{t}",f"{n}. {label}","edgeStyle=none;"+return_style,meta={"message_id":n,"sender":s,"receiver":t,"message":label})
d.box("note","Alternativas 14 y 15 son excluyentes por prenda. 18-20: Liberar aprobadas para empaque, si existen.\n20 confirma liberación registrada, no empaque físico. ID interno previo al código de empaque.",40,1625,1920,70,"text;html=0;fontSize=18;align=left;strokeColor=none;fillColor=none;")
d.save("05-secuencia")

# Comunicación: red de participantes, números de mensaje en enlaces y texto completo en tabla.
d=Diagram("06 Diagrama de colaboración",1900,1470)
for i in range(4):
    d.box(f"a{i}",ACTORS[i],40,125+i*220,280,80,kind="participant")
d.box("system","Sistema de Gestión\nde Manufactura",730,125,340,740,kind="participant")
d.box("db","Persistencia\nPostgreSQL",1480,410,300,120,kind="participant")
calls={1:'registrarOT()',2:'guardarOT()',3:'confirmarPersistencia()',4:'confirmarOT()',5:'registrarCorte()',6:'guardarCorte()',7:'confirmarPersistencia()',8:'confirmarCorte()',9:'registrarConfeccion()',10:'guardarAvance()',11:'confirmarPersistencia()',12:'confirmarConfeccion()',13:'registrarInspeccion()',14:'[aprobada] guardarAprobada()',15:'[rechazada] guardarRechazo()',16:'confirmarInspeccion()',17:'mostrarResumen()',18:'liberarAprobadas()',19:'[hay aprobadas] guardarCodigoLote()',20:'confirmarLiberacion()'}
def communication(s,t,numbers,style,offset=None):
    e=d.edge(s,t,'\n'.join(f'{n}: {calls[n]}' for n in numbers),style,meta={'link_messages':','.join(map(str,numbers))})
    if offset:E.SubElement(e.find('mxGeometry'),'mxPoint',x=str(offset[0]),y=str(offset[1]),attrib={'as':'offset'})
for i in range(4):
    req=[n for n,s,t,l in MESSAGES if s==i and t==4]
    res=[n for n,s,t,l in MESSAGES if s==4 and t==i]
    communication(f'a{i}','system',req,"edgeStyle=none;exitX=1;exitY=0.25;entryX=0;entryY="+str((20+220*i)/740)+";",(0,-24))
    communication('system',f'a{i}',res,"edgeStyle=none;exitX=0;exitY="+str((60+220*i)/740)+";entryX=1;entryY=0.75;",(0,24))
communication('system','db',[2,6,10,14,15,19],'exitX=1;exitY='+str((440-125)/740)+';entryX=0;entryY=0.25;',(0,-140))
communication('db','system',[3,7,11,16],'exitX=0;exitY=0.75;entryX=1;entryY='+str((500-125)/740)+';',(0,65))
d.box("guard","14 [aprobada] / 15 [rechazada]:\nalternativas excluyentes. 13-17: repetir por prenda.\n18-20: Liberar aprobadas para empaque, si existen.\n20: liberación registrada, no empaque físico.",1120,670,700,160,"text;html=0;align=left;fontSize=18;strokeColor=none;fillColor=none;")
for n,s,t,label in MESSAGES:
    col=0 if n<=10 else 1
    row=(n-1)%10
    d.box(f"msg{n}",f"{n}. {label}",40+col*930,920+row*49,890,46,"rounded=0;html=0;whiteSpace=wrap;align=left;spacing=7;fontSize=18;fillColor=#f5f5f5;strokeColor=#dddddd;",kind="message")
    c=d.root.find(f"./mxCell[@id='msg{n}']")
    for k,v in {"message_id":n,"sender":s,"receiver":t,"message":label}.items():c.set(k,str(v))
d.save("06-colaboracion")
(BASE/"evidencias"/"modelo.json").write_text(json.dumps({"actors":ACTORS,"flows":FLOWS,"messages":MESSAGES},ensure_ascii=False,indent=2),encoding="utf-8")
print("Seis fuentes DRAW.IO nativas creadas.")
