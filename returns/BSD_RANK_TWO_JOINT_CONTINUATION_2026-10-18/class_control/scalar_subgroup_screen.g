Gm:=GL(2,7);;
iso:=IsomorphismPermGroup(Gm);;
G:=Image(iso);;
Zc:=Centre(G);;
Print("GROUP ",Size(G)," CENTER ",Size(Zc),"\n");
C:=ConjugacyClassesSubgroups(G);;
Print("SUBGROUP_CLASSES ",Length(C),"\n");
for c in C do
 H:=Representative(c);
 z:=Size(Intersection(H,Zc));
 Print("SUBGROUP ",Size(H)," ",Index(G,H)," ",z,"\n");
 if z=1 then Print("CENTER_FREE ",Size(H)," ",Index(G,H)," ",StructureDescription(H),"\n"); fi;
od;
Print("COMPLETED\n");
QUIT;
