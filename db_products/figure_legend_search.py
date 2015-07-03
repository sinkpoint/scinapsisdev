"""
This is a method on the ScinPubMeta model class
"""

from search.models import PubTechProdResult, PubProductInfo, ScinPubFigure,PubProductName,ScinPubMeta,PubTechniqueList


import re
for pup in ScinPubMeta.objects.all()[:]:
    imunoindex ={}
    # get figures specific for a publication using the django select_related method
    for fig in pup.scinpubfigure_set.all(): 
        # order by technique group to make help handle cases of repeated alternative names in same figure legend
        for tech in PubTechniqueList.objects.order_by('technique_group').iterator():
            # Search alternative name in figure legend
            if  bool(re.compile("\W"+tech.alternative+"\W").search(fig.content.lower())):
               # check if technique has already been found on a legend and skip to next technique if true
               if getattr(fig,'previous',None) ==tech.technique_group:
                    continue
               else:
                  # attach technique to figure legend to help handle repeated alternative names in legend. 
                  setattr(fig,'previous',tech.technique_group)
               if tech.technique_group in imunoindex:
                   imunoindex[tech.technique_group]=imunoindex[tech.technique_group]+1
               else:
                   imunoindex[tech.technique_group]=1                       
    print   imunoindex  
