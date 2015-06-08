import sys
from sys import argv

from _collections import defaultdict




#Ksekiname apo tin main
def main():
    if((len(sys.argv) !=4) & (len(sys.argv)!=6) & (len(sys.argv)!=3) &(len(sys.argv)!=5)&(len(sys.argv)!=7)):#Edw elegxoume an i klisi tou programmatos exei to swsto arithmo orismatwn!an den ton exei tote:
        print(TypeError("Error arguments are 4 or 6!!")) #Tipwnoume error kai termatizoume to programma me to exit!
        exit()
    elif(len(sys.argv)==3): #Twra an i klisi tou programmatos mas exei sinolo 3 orismata kanoume:
        if(((sys.argv[1]).isdigit()) & (isinstance(sys.argv[2],str))): #Elegxoume an to to orismata stin thesi 1 ston argv einai arithmos (support) kai an to orismata stin thesi 2 einai simvoloseira(filename)
            #Pairnoume to orisma apo tin thesi 1 kai to metatrepoume apo str se int me tin entoli int(str)
            support=sys.argv[1] 
            support=int(support)

            #Edw dimourgoume mai list me oles tis sixnotites pou tha exoun oi lekseis kai ena dictionary me tin kathe leksi pou ta pairnoume apo tin epistrofi tis klisis A_priori me orismata to onoma arxeiou(sys.argv[2]) kai to support!
            freqall,allset=A_priori(sys.argv[2],support)
           #Kaloume tin sinartisi printResults gia na ektipwsoume ta apotelesmata!
            printResults(freqall,allset)
        else: #An ta orismata den eixan ton tipo pou theloume px to support itan simvoloseira kai oxi arithmos tote ektipwnei error!
            print(TypeError("Error in type of Arguments!!"))
    elif(len(sys.argv)==4): #An i klisi tou programatos exei sinolo 4 orismata kanoume ta ekseis stadia!
        if((isinstance(sys.argv[1],str)) & ((sys.argv[2]).isdigit()) & (isinstance(sys.argv[3],str))): #Elegxw opws panw an einai ta orismata exoun swstous tipous opws prepei na exoun!!an nai tote:
            #Pairnw to suuport kai to metatrepw se int!!
            support=sys.argv[2]
            support=int(support)
            #Twra an sto argv[1] exoume -n simainei oti einai akeraioi arithmoi tote ekteloume ta eksis:
            if(sys.argv[1]=="-n"):
                #ekteloume ton diadikasia me to filename kai to support kai epistrefw sto freqall kai allset kai ektelw to prinResults gia na tipwsw ta apotelesmata!
                freqall,allset=A_priori(sys.argv[3],support)
                printResults(freqall,allset)
            else:
                #Edw twra simainei oti sta orismata exoume to -p pou simainei oti tha pairnoume ws support mia timi kai meta tha prpeei na vroume to support apo to sinolo twn  kalathiwn!
                #Ekteloume tin diadikasia getDataFromFile me to filename orismata
                infile=getDataFromFile(sys.argv[3])
                support=returnSupport(infile,support) #Ekteloume tin returnSupport gia na paroume tin elaxisti timi ipostiriksis!!
                #Kai ksanaekteloume tin diadikasia pou exoume ektelesei kai panw prwta to A_Priori kai meta to printResults!
                freqall,allset=A_priori(sys.argv[3],support)
                
                printResults(freqall,allset)
        else: #An einai lathos oi tipoi twn orismatwn tipwnoume Error!!
            print(TypeError("Error in type of Arguments!!"))
      #Twra an ta orismata einai 5 exoume:  
    elif(len(sys.argv)==5):
        if((isinstance(sys.argv[1],str)) & (isinstance(sys.argv[2],str)) & ((sys.argv[3]).isdigit()) &(isinstance(sys.argv[4],str)) ): #Elegxw ksana ton tipo ton orismatwn pou exww!!!
            #Twra an exw 5 orismta tote exw tis eksis epiloges:
            if((sys.argv[1]=="-n") &((sys.argv[2])=="-p")):  #Oti ta orismata ston pinaka stin thesi 1 kai 2 exoun ta xaraktiristika -n kai -p opote oi times den einai string kai exw kai an vrw me pososto tin elaxisti timi ipostiriksis
                 #Ektelw tin diadikasia getDataFromFile gia times oxi string kai meta pairnw ton arithmo pou exw ws to pososto gia to support !
                 infile=getDataFromFile(sys.argv[4],"n")
                 support=sys.argv[3]
                 support=int(support) #To metatrepw arxika se int gia na borw na to leitourgisw opws thelw!
                 support=returnSupport(infile, support) #Epistrefoume apo tin returnSupport tin elaxisti timi ipostirksis!!
                 #Kai ekteloume tin idia diadikasia opws kai parapanw!!
                 freqall,allset=A_priori(sys.argv[4], support)
                 printResults(freqall, allset)
                #Alli epilogi otan exoume 5 orismata einai na exoume kai to -o pou simainei oti thelei na ektipwnoume ta apotelesmata se ena csv arxeio pou mas dinei apo ta orismata ektelesis! 
            elif((sys.argv[1])=="-o"):
                 support=sys.argv[3] #Pairnoume to support kai to metatrepoume se int!
                 support=int(support)
                 freqall,allset=A_priori(sys.argv[4], support) #Ekteloume ton algorithmo A_priori kai epistrefei to freqall kai allset 
                 printInFile(freqall, allset, sys.argv[2]) #Meta ws neo stoixeio pou den exoume dei einai i ektipwsi twn apotelesmatwn se arxeio pou ginetai me tin diadikasia printInFile!!
        else:
            print(TypeError("Error in type of Arguments!!")) #An den exoun ton swsto tipo ta orismata tipwnoume error!!
    #Twra gia 6 orismata exoume:
    elif(len(sys.argv)==6):
        if((isinstance(sys.argv[1],str)) & (isinstance(sys.argv[2],str)) &(isinstance(sys.argv[3],str)) & ((sys.argv[4]).isdigit()) &(isinstance(sys.argv[5],str)) ): #Elegxioume ton tipo twn orismatanw na doume an einai swstos!!
            #OI pithanes epiloges sta 6 orismata einai oti :
            if((sys.argv[1]=="-n") & (sys.argv[2]=="-o")): #Eite exoume tis epiloges -n kai -o!Diladi dedomena oxi string kai eggrafi se arxeio .csv pou mas dinetai!
                 #Pairnoume arxika to support kai to metatrepoume se int!Kai akolouthei i ektelesi tou algorithmou A_priori
                 support=sys.argv[4]
                 support=int(support)
                 freqall,allset=A_priori(sys.argv[5], support)
                 printInFile(freqall, allset, sys.argv[5]) #Kai edw ekteloume tin  diadikasia printInFile gia na grapsoume sto arxeio ta apotelesmata!!
            #Edw exoume ws epilogi na mas exoun dwthei sta orismata to -p kai -o pou simainei oti tha vroume to elaxisto arithmo ipostiriksis kai theloume kai eggrafi sto arxeio .csv ta apotelesmata!!
            elif((sys.argv[1]=="-p") &(sys.argv[2]=="-o")):
                 infile=getDataFromFile(sys.argv[5]) #ekteloume tin diadikasia getDataFromFile 
                 support=sys.argv[4] #Pairnoume to support apo ta orismata kai to metatrepoume se int!!
                 support=int(support)
                 support=returnSupport(infile, support) #Vriskoume to elaxisto arithmo ipostiriksis!!
                 freqall,allset=A_priori(sys.argv[5], support) #Ekteloume tin diadikasia A_priori gia na vroume ta apotelesmata pou theloume na paroume!!
            
                 printInFile(freqall, allset, sys.argv[3]) #Ekteloume tin diadikasia printInFile gia na grapsoume ta apotelesmata se ena arxeio!!
            else:
                print(TypeError("Problem in Arguments!!")) #An den exei dwsei swsti epilogi ektipwnei error!!
        else:
            print(TypeError("Error in type of Arguments!!")) #An den einai swsta oi tipoi twn orismatwn tote tipwnei error!!
    else: #Edw ennooume oti i ekteleis tou programmatos einai i eksisa a_priory.py -n -p -o exitfilename.csv  support infilename.csv
        if((isinstance(sys.argv[1],str)) & (isinstance(sys.argv[2],str)) & (isinstance(sys.argv[3],str)) & (isinstance(sys.argv[4],str)) & ((sys.argv[5]).isdigit()) &(isinstance(sys.argv[6],str)) ): #Elegxoume ton tipo ton orismatwn!!
            infile=getDataFromFile(sys.argv[6],"n") #Ekteloume tin diadikasia getDataFromFile gia dedomena mi string!!
            support=sys.argv[5] #Pairnoume to support meta to metatrepoume se int kai meta ekteloume to returnSupport gia na vroume to elaxisto arithmo ipostiriksis support diladi!!
            support=int(support)
            support=returnSupport(infile, support)
            freqall,allset=A_priori(sys.argv[6], support) #Ekteloume ton A_priori kai vriskoume ta apotelesmata tou!!
            
            printInFile(freqall, allset, sys.argv[4]) #Grafoume ta apotelesmata sto arxeio mesw tis diadikasia printInFile!!
        else:
            print(TypeError("Error in type of Arguments!!")) #An einai lathos oi tipoi twn orismatwn tipwnoume ena error!!
 #---------------------------------------------------||ALGORITHMOS A_PRIORI & VOITHITIKOI ALGORITHMOI!!!||-------------------------------------------------------------------------------------------------------------------     
#ALGORITHMOS A_PRIORI!!!
#Pairnoume to onoma tou arxeiou kai to support diladi to elaxisto arithmo ipostiriksis!!
def A_priori(infile,support):
    infile=getDataFromFile(infile) #Ekteloume tin diadikasia getDataFromFile 
    lineList= list() #Dimiourgoume tin lista lineList
    Items=set() #Dimiourgoume to set me onoma Items etsi wste na proshtesoume ola ta stoixeia pou periexontai sta arxeia ws dedomena!!Me to set tha apaloifthoun kai oi diplotipes eggrafes diladi den tha exoume 2 fores to idio item!! 
    for line in infile:
        #To frozenset dilwnei oti den borei na allaksei to periexomeno tou!!
        lineList.append(frozenset(line)) #Prosthetw sto telos kathe fora tin kathe grammi pou periexei to arxeio pou exoume anoiksei apo ti diadikasia getDataFromFile!!    
        for item in line:
                Items.add(frozenset([item])) #Prosthetw to Items tis lekseis pou exei kathe grammi!!
    
    
    All_freqSet=defaultdict(int) #Epistrefei ena leksiko san antikeimeno pou einai mia ipokatigoria tou dict!Edw tha bainoun ola ta stoixeia stis lekseis kai me ton arithmo emfanisi tous sta kalathia pou einai oi grammes!
    freqk=defaultdict(int) #Tha xrisimopoietai gia na periexe tis sixnotites ton stoixeiwsinolwn gia to kathe kalathi se ola ta kalathia!!
    allset=dict()
    k=2
    #Edw kanoume to prwto perasama apo ton algorithmo A_Priori!!
    fristpass,allset_temp=FindItemsFirstTime(lineList,Items,support,freqk) #sto firstpass,kai sto allset_temp pername ta apotelesmata tis sinartisis findItemsFirstTime!!
    freqk=fristpass #Edw topothetoume to firstpass se to dict freqk!!
    #Twra oso to  dict freqk einai gemato kane to eksis:
    while (bool(freqk)):
        All_freqSet.update(freqk) #Vale tis sixnotites twn stoixeiosinolwn pou vrikame sto kathe perasama sto all_freqSet
        allset[k-1]=allset_temp #Sto all set vazoume to allset_temp pou exoume parei ws apoteelsma apo to FindItemsFirstTime pou tha periexei kathe fora ta stoxeia pou pernane ton elegxo me ton elaxisto arithmo ipostiriksis!!
        anotherpass,allset_temp=AprioriPass(lineList,freqk,support,k) #Ekteloume ton algorithmo AprioriPass pou einai ta epomena vimata tou algorithmou A_Priori kai epistrefei ta apotelesmata kai ta vazei sto anotherpass kai sto allset_temp
        freqk=anotherpass #To freqk ginetai iso me to neo sinolo sixnotitwn pou einai apo to anotherpass!!
        k+=1 #auksisi tou megethos twn newn stoixeiwn!!
    #Edw Dimiorgoume mia lista me tin onomasia final_fREQ pou tha periexei ta stoixeia pou exoume parei apo ton A_Priori mazi me tis sixnotites tous!!
    final_freq=[]
   
    for key,value in All_freqSet.items():
        final_freq.extend(([tuple(key),All_freqSet[key]])) #sto final_Freq tha periexei prwta to stoixeiosinolo kai meta tin sixnolotita emfanisi tou sto basket!!
    
    return final_freq,allset #Epistrefoume to final_freq me tis sixnotites twn stoixeiosinolown kai to to allset pou periexei ola ta stoixeiosinola kai ta nea stoixeiosinola pou pernoume apo tin ektelesi tou A_Priori!
 #EDW EINAI I DIADIKASIA AprioriPass pou o algorithmos a_priori gia k+1!
 #Me eisodous tin lista me tis grammes tou arxeiou kai freqk pou periexe tis sixnotites twn stoixeiosinolwn ,to support ton elaxisto airthmo ipostiriksis kai to k pou einai to megathos twn stoixeiosinolwn!!    
def AprioriPass(lineList,freqk,Support,k):
    items_pairs=GetPairs(freqk,k) #ekteloume tin diadikasia getPairs pou pairnoume ta dinata zeugaria apo ta stoixeiosinola pou exoume ws orisma apo tin sinartisi AprioriPass
    freqk=defaultdict(int) #to freqk gia na vroume tin sixnotita twn newn stoixeiosinolwn!
    item_temp=set() #Ta antikeimena pou tha exoun kseperasei ton elegxo tis sixnotitas tous me to support!
    local_temp=defaultdict(int)
    for items in items_pairs: #gia kathe item pou exoume parei apo to GetPairs tote exoume:
            for line in lineList: #gia kathe grammi tou arxeiou exoume
                    if items.issubset(line): #An to item periexete stin grammi tote
                       local_temp[items]+=1 # #Auksise to local_temp tou item kata 1!
    for item1,count in local_temp.items(): #Twra gia antikeimeno tou local_temp pairnoume to item1(key) kai to count(value) tote:
        if(count >= Support): #An to count einai megalitero tou support tote
            freqk[item1]=count   #vale sto freqk tou item1 to count(tin sixnotita)
            item_temp.add(item1) #kai vale to antikeimeno sto item_temp
    return freqk,item_temp #Epistrefoume to freqk(ta stoixeiosinla me tin sixnotita tous) kai to item_temp(ta stoixeiosinola tou k+1 a_priori)
                            
#I diadikasia GetPairs pou vriskoume ta dinata stoixeiosinolwn meta tin enwsi tous!!
#Ws eisodo pairnoume to freqk pou eipame parapanw ti einai kai k to dinato megethos tou stoixeiosinolou!!      
def GetPairs(freqk,k):
        pairs=set() #Edw exoume ena set pou tha periexe ta stoixeiosinola pou exoume parei!!
        for i in freqk: #Gia kathe stoixeio tou freqk me onomasia i
            for j in freqk: #Gia kathe allo stoixeio tou freqk me onomasia j exoume:
                if(len(i.union(j))==k): #An i ennwsi tous exei megethos iso me to k tote kanoume:
                    pairs.add(i.union(j)) #prosthetoume sto pairs to dinato auto zeugari enwsis twn stoixeiosinolwn!!
        return pairs #Epestrepse auto to set!!

#I Diadikasia gia na ekteleoume to prwto perasma tou algorithmou A_Priori!!
#Pairnei ws orismata to lineList pou periexei tis grammes tou arxeiou!!
#To items pou periexei ta stoixeia pou pirame apo to arxeio
#To support pou einai o elaxistos arithmos ipostiriksis!! kai to freqset me tis sixnotita tou kathe stoixeiosnilou!!
def FindItemsFirstTime(lineList,Items,support,freqSet):
    item_temp=set() #Exoume ena set me onomasia item_temp pou tha valoume ta pou pairnane ton elegxo me to support!!
    local_temp=defaultdict(int) #gia na borw na vriskw to plitos kathes leksis pou exw sto local_temp!
    for item in Items: #Gia kathe item sto item exoume:
        for line in lineList: #Gia kathe grammi sto LineList exoume:
                if item.issubset(line): #An periexete to item sto line tote 
                        local_temp[item]+=1 #Auksise to value sto local_temp tou item kata 1 
    for item1,count in local_temp.items(): #Twra gia kathe antikeimeno sto local_temp
            if(count >= support): #An to count (i sixnotita tou ) einai megaliteri i isi tou support tote 
                freqSet[item1]=count #vale sto freqk tou item1 to count(tin sixnotita)
                item_temp.add((item1)) #Prosthese to sto itemp_temp to antikeimeno!!
    
    return freqSet,item_temp #Epestrepse to freqset kai to item_temp

#I diadikasia gia na ektipwnoume ta apotelesmata
#Me orismata exoume to items pou periexe ta antikeimena kai tis sixnotites tous kai me to alllist exoume ola ta antikeimena!!
def printResults(Items,Alllist):
  
    for keys,values in Alllist.items(): #Gia kathe antikeimeno tou Alllist
      
        for itas in values: #Gia kathe timi tou values exoume
           
            temp=str(itas) #Metetrepse to temp se string
            
            temp=temp.strip("frozenset({") #Afairese apo to str to frozenset({ kai to }) kai na meinei mono to periexomen tou
            temp=temp.strip("})")
            if(len(itas)==1): #An exei mikos mono 1 tha prepei na exei tin morfi (test,) ara prostheto to ( to , kai to )
                temp="("+temp+"," +")"
            else:# alliws tha prepei na einai (test1,test2,.)
                temp="("+temp +")"
            
            
            for i in range(0,len(Items)-1): #Twra pernw ta antikeimena tou Items kai tipwnw!!
                if(temp == str(Items[i])):
                        print(("{}:{};".format(temp,Items[i+1])),end="") 
                   
                
        print()
        
#I diadikasia printInFile xrisimopoietai gia na borw na grafw se arxeia!!
#Pairnei orismata  to Items pou periexei ta stoixeia kai tis sixnotites tous!
#Pairnei ola ta stoixeia pou exoun dimiourgithei!!
#Pairnei to onoma tou arxeiou!!
def printInFile(Items,Alllist,filename):
    
     target = open(filename, 'w')  #Anoigw ena erxeio me onomasia  apo to orisma pou dinei o xristis kai me idiotita w(write)
     for keys,values in Alllist.items(): #Pairnoume ola ta item tou Alllist
        strToWrite="" #mia metavliti pou tha tin xrisomopoiisoume gia na dwsoume ti tha grapsoume sto arxeio!!!
        for itas in values:
           #Idia diadikasia opws to printResults
            temp=str(itas)
            
            temp=temp.strip("frozenset({")
            temp=temp.strip("})")
            if(len(itas)==1):
                temp="("+temp+"," +")"
            else:
                temp="("+temp +")"
            
                
            for i in range(0,len(Items)-1):
                    
                if(temp == str(Items[i])):
                    strToWrite=strToWrite+ temp +":" +str(Items[i+1])+";" #Aplws edw prosthetoume auta pou ektipwname sto strToWrite
                    strToWrite.strip()
            
        
        target.write(strToWrite)#Sto telos grafoume sto arxeio to strToWrite
        target.write('\n')  #Kai allazoume grammi gia na grapsoume stin apo katw grammi sto arxeio!!
        
#i diadikasia returnSupport einai i diadikasia gia na epistrefei to support otan dinetai sta orismata -p!!
#Pairnei ws orisma to infile kai to support!             
def returnSupport(infile,support):
    lineList= list() #Dimiorugoume mia list gia na exoume tis grammes tou arxeiou!!
     
    for line in infile:
        lineList.append(line) #Prosthetoume tin grammi tou arxeiou sto lineList
    temp=support/100 #Diairoume to support dia ekato gia na vroume to pososto tis % se dekadiki morfi!  
    return (temp*len(lineList)) #Epistrefoume to support simfwna me tin ekfwnisi mas !!
#I diadikasia getDataFromfile xrisimopoiietai gia na boroume na paroume ta dedomena pou exoume apo to arxeio me tin onomasia pou mas dothike apo ta orismata tis klisis tou programmatos!!
#Pairnei ws eisodo to onoma tou arxieou (filename) kai to tipo twn dedomenwn eite s gia string eite n gia integer!!
def  getDataFromFile(filename,type="s"):
    infile=open(filename,'r') #Anoigoume to arxeio me onomasia pou exei i metavliti filename pou einai gia read!!
    for line in infile: #gia kathe grammi sto infile exoume
        line=line.lower() #Kanoume tin grammi xamila giati den iparxei diaxwrismos eite mikra eite kefalaia grammata!!
        line=line.split(',') #Afairoume ton komma!!
        list=[] #I lista pou xrisimopoietai gia na prosthetw tis grammes!!
    
        for temp in line:
            if(type=="s"): #An exoume type == s einai tote ta dedomena string
                temp=temp.strip()
                list.append(temp) #Prostheto stin lista to temp!!
            else:#Alliws einai dedomena int tote exoume metatropi tou temp se int!!
                temp=int(temp)
                
                list.append(temp)#prosthetw sto list to temp!!
                
        wordinfile=frozenset(list) #vazw sto wordinfile to frozenset list pou einai ena set pou den borei na allaksei!!
       
        yield  wordinfile
    
if __name__ == '__main__':main()
    