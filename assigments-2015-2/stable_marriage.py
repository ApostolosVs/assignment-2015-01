#Simfwna me tin ekfwnisi mas zitithike na lisoume to prolvima twn Statherwn Gamwn eite ksekinontas apo tin meria twn antrwn eite twn gynaikwn!!
#Apo opoiadipote meria na ksekinisoume gia na vroume tin veltisti lisi tha stirixtoume ston geniko algorithmo pou exoume:
#function stableMatching {
#   Initialize all m ∈ M and w ∈ W to free
#    while ∃ free man m who still has a woman w to propose to {
#       w = highest ranked woman to whom m has not yet proposed
#       if w is free
#         (m, w) become engaged
#       else some pair (m', w) already exists
#         if w prefers m to m'
#           (m, w) become engaged
#           m' becomes free
#         else
#           (m', w) remain engaged
#    }
#}



import json
import sys
import pprint

#I main mas einai:
def main():
    #Edw pairnw ta orismata pou dinontai kata tin ektelesi tou programmatos!Kai elegxw an einai swsta se arithmo alliws na tipwnei ena error kai na stamataei to programma!
    argument=sys.argv
  
    if((len(argument)!=3) & (len(argument)!= 5) ):
       print(TypeError('Required 3 or 5 arguments!'))
       exit()
    
    #An einai swsta ta orismata tote pigenoume se auton ton klado tou if!
    else:
        katigoria=argument[1]   #pairnoume tin katigoria(-m or -w) pou tha ektelesoume diladi tha vroume tin veltisti lisi gia antres i gia gynaikes!!
        filename=argument[2]    #pairnoume to onoma tou arxeiou json pou periexei tis protimiseis kai gia tous antres kai gia tis gynaikes!
        #Edw anoigoume to arxeio json kai vazoume ta stoixeia stin metavliti data!
        with open(filename,'r') as data_file:
            data=json.load(data_file)
        
        mens=data.get('men_rankings')   #pairnoume tous antres kai tis protimiseis tous!!
      
        girls=data.get('women_rankings')  #episis pairnoume tis gyanikes kai tis protimisous tous kai tis topothetoume stin metavliti girls!
        
      
        #An mas zitithike na vroume tin veltisti lisi gia antres (diladi dothike -m) tha akolouthisoume to klado tou if afou i sinthiki tha einai alithis!
        if(katigoria=='-m'):
            
            desm=stablemarriage(mens,girls,"man") #ekteloume tin sinartisi forMens pou tha mas epistrepsei ta zeugaria pou exoun epilexthei me ton algorithmo stablemarriage!
            inv_desm = {v: k for k, v in desm.items()} # Edw kanoume ena reverse ta key me ta values sto dictionary desm etsi wste na pane san keys ta onomata twn antrwn kai ws values ta onomata twn gynaikwn!!
            pprint.pprint(inv_desm) #Edw xrisimopoioume tin pprint gia na boresoume na ektipwthoun se alfavitiki seira ta onoma twn antrwn!!
            
            if(len(argument)==5 ):
                outfile=open(argument[4],'w')
                outfile.write(json.dumps(inv_desm))
        #An mas zitithei na vroume tin veltisti lisi gia gynaikes (-w) tote akolouthoume ton klado else:   
        else:
            desm=stablemarriage(mens,girls,category="women") #ekteloume tin stablemarriage gia na vroume tin veltisti lisi twn gynaikwn!
            inv_desm = {v: k for k, v in desm.items()} #kanoume reverse opws kai panw gia na rthoun ta onomata twn gynaikwn ws keys kai twn antrwn ws values!
            pprint.pprint(inv_desm) # ektipwnoume ta zeugaria me kritirio tin alfavitiki seira sta onomata twn gynaikwn!
            if(len(argument)==5 ):
                outfile=open(argument[4],'w')
                outfile.write(json.dumps(inv_desm))
    

#I sinartisi pou tha ektelouyme gia na vroume tin veltisti lisi eite gia antres eite gia gynaikes!!!!
def stablemarriage(mens,girls,category="man"): #Pairnei ws orismata tous antres kai tis gynaikes me tis protimiseis tous !!
    mensfree=sorted(mens.keys()) # Pairnoume tous antres pou einai eleutheroi kai tous topothetoume se mia lista me alfavitiki seira afou to mensfree einai list!!
    
    desmeuseis={}  #me ton dictionary desmeuseis tha topothetoume ta zeugaria pou tha antistoixoun!!
    
    mensprefer=mens.copy() # Ston mensprefer topothetoume ena antigrafo apo tis protimiseis twn antrws stis gynaikes!
  
    womanprefer=girls.copy() #Antistoixa ston womanprefer topothetoume ena antigrafo apo tis protimiseis twn gynaikwn stous antres!
    #Twra an einai i katigoria antrwn exoume to eksis:
    if(category=="man"):
    #Oso tha uparxoun antres eleutheroi!!Ekteloume gia na vroume tin veltisti lisi gia tous antres!
        while mensfree:
            man=mensfree.pop(0) #Afairoume apo tin lista mensfree to prwton antra kai ton topothetoume stin metavliti man!
            
            manlist=mensprefer[man] #Stin list manlist topotethoume tis gynaikes pou exei protimisei o man me tin seira pou tis pirame apo to arxeio!!
           
            girlwho=manlist.pop(0) #Afairoume tin prwti gynaika (apo tin manlist) pou protimaei o antras man pou exoume parei kathe fora 
           
            couple=desmeuseis.get(girlwho) #Twra elegxoume apo to dict desmeuseis ama i gynaika einai desmeumeni me kapoion allon antra!!
           
            #An den einai desmeumeni me allon antra tote:
            if not couple:
                desmeuseis[girlwho]=man #Desmeuontai i gynaika ws key kai o antras ws value!!Dioti  apo tin parapanw entoli pou psaxnoume ton antra tis gynaikas ama einai desmeumeni tha prepei i gynaika na einai sto key gia na boroume na tin entopisoume!!
                
                #Alliws:       
            else:
                girllist=womanprefer[girlwho] # pairnoume tous antres pou protimaei i gynaika pou exoume dialeksei apo panw kai tous topothetoume stin lista girllist!
                
                #Twra alegxoume an i gynaika pou einai desmeumeni prwtimaei ton antra pou tin exei epileksei apo to idi antra pou einai desmeumeni!!
                if(girllist.index(couple)>girllist.index(man)): #An o antras pou tin epelekse einai se pio mikri thesi stin lista tis apo to zeugari tis tote protimaei ton allon antra etsi:
                    
                    desmeuseis[girlwho]=man #Tote exoume tin desmeusi tou antra me tin gynaika pou eixe epileksei an kai desmeumeni!!
                   
                    if mensprefer[couple]: #An o antras vrisketai stin lista manlist tote:
                        mensfree.append(couple) #O antras pou ton xwrise ton i gynaika ginetai eleutheros kai benei stin lista mensfree!!
                        
                else: #Edw an i gyanika protimaei perissotero ton antra pou idi exei tote exoume:
                      
                    mensfree.append(man) #Tote o antras pou eixame epileksei apo tous mensfree ksanatopotheteitai sto telos tis listas mensfree!!
                   
    #Enw an theloume na vroume tin veltisti lisi gia tis gynaikes exoume:
    else:
        womensfree=sorted((girls.keys()))      
        while womensfree: 
           girl=womensfree.pop(0) #Pairnoume tin prwti gynaika apo tin lista!
           womanlist=womanprefer[girl] #Vriskoume tis protimiseis pou exei i gynaika stous antres!
           manwho=womanlist.pop(0) #Pairnoume ton prwto se seira protimisi pou exei i gynaika!
           couple=desmeuseis.get(manwho) #Koitame ean o antras pou epileksame apo panw einai desmeumenos me alli gynaika!         
           if not couple: #An den einai desmeumenos tote :
                desmeuseis[manwho]=girl #Exoume desmeusi twn 2 pou eixame  apo panw!
           else:
                manlist=mensprefer[manwho]  #pairnoume tin lista protimiseis tou antra gia tis gynaikes!
                if(manlist.index(couple)>manlist.index(girl)): #An i gynaika ton pou ton epelekse einai se mikroteri thesi stin lista apo tin gynaika pou exei idi tote:
                    desmeuseis[manwho]=girl #allazoume  ton antra me tin nea gynaika kai epomenos i gynaika pou eixe ginetai eleutheri kai topotheteite stin lista womensfree!
                    if womanprefer[couple]:
                        womensfree.append(couple)
                else:
                    womensfree.append(girl)
            
                            
    
    
    return desmeuseis
 
if __name__ == "__main__":main()