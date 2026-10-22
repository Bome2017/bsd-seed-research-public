Gm:=GL(2,5);;
iso:=IsomorphismPermGroup(Gm);;
G:=Image(iso);; Zc:=Centre(G);;
C:=ConjugacyClassesSubgroups(G);;
Print("GROUP ",Size(G)," CENTER ",Size(Zc)," SUBGROUP_CLASSES ",Length(C),"\n");
for c in C do
 J:=Representative(c);;
 Print("SUBGROUP ",Size(J)," ",Index(G,J)," ",Size(Intersection(J,Zc)),"\n");
od;
Print("SUBGROUP_SCREEN_COMPLETE\n");
QUIT;
