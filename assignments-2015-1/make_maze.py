import sys
import random
import decimal



def main():
    argument=sys.argv #edw pairnoume ta argument pou exoume me tin klisi tou programmatos!!
    if(len(argument)<6) | (len(argument)>=7):  #edw elegxoume an i klisi tou programmatos periexei to swsto arithmo arguments pou orizei i ekfwnisi mas!
        print(TypeError('Requires 6 arguments!'))
        exit()
    else:
        x=argument[1] #pairnoume to argument pou einai sthn thesi 1
        input_seed=argument[4] #pairnoume to input_seed apo tin klisi touy programmatos pou tha xrisimopoiisoume pio katw sto random!
        #edw pairnoume ta start_x kai start_y pou einai o arxikos mas komvos pou vriskomaste se auto kai ksekiname!
        start_x=argument[2]
        start_y=argument[3]
        if(x.isdigit()&start_x.isdigit()&start_y.isdigit()&input_seed.isdigit()): #elegxo an auta ta arguments einai arithmoi kai oxi kapoia simvoloseira!!an einai einai kanw
            n=int(x) #metatrepw ton x se int kai ton ekxwrw sto n
           #elegxw an to n pou tha einai to megethos tou lavirithmou einai megalitero apo 30!an einai megalitero apo 30 pou den einai epitrepto termatizw to programma kai tipwnw ena error ston xristi!
            if(n>30): 
                print("Error n prepei na einai mexri 30")
                exit()
            #alliws metatrepw se int ta start_x kai start_y pou exw parei!
            start_x=int(start_x)
            start_y=int(start_y)
            #elegxw an o arxikos komvos pou mou edwse o xristis einai mesa sta oria 0 kai n pou dothike episis apo ton xristi!!alliws tipwnw error!!
            if((start_x<0 | start_x>n) |(start_y<0 | start_y>n)):
                print("Error ta arxika tha prepei na einai sto 0<=x i y <n")
                exit()
            input_seed=int(input_seed)
        else: 
            print("Error in the arguments!!")
            exit()
        random.seed(input_seed) #ektelw tin entoli pou mou dothike stin ekfwnisi tis ergasias!
        
       
       #anoigw ena try catch gia na boresw na anoiksw to arxeio!!
        try:
            outfile=open(argument[5],'w') #anoigw ena arxeio pou exei onomasia pou exw parei apo ta orismata tis klisis tou programmatos kai dilwnw pws einai gia grapsimo to arxeio kai mono!
        except:
            print('Could not make the file!') #an iparksei kapoio provlima tipwnw ena minima ston xristi!
        #NA VRW ALLO TROPO!!!
        allnodes=[] #xrisimopoiw to all nodes gia na prosthesw olous tous komvoyus pou tha exei o lavirinthos  pou tha xrisimopoiisw!
        for i in range(n):
            for j in range(n):
                allnodes+=[(i,j)]
        checked_nodes=[]   #dimiourgw to checked_nodes gia na topothetw ekei mesa tous komvous pou exw episkeftei otan kanw tin anazitisi kata vathos!!   
        dfs(start_x,start_y,allnodes,n,checked_nodes,0) #ektelw diadikasia dfs pou einai i anaziti kata vathos!
        
        
        
        
def dfs(start_x,start_y,allnodes1,n,checked_nodes,i):
   

    if(len(allnodes1)==0):return #an den iparxoun alloi komvoi gia na episkefteis tote epistrefei i diadikasia!!
    else:
       
        checked_nodes.insert(i,(start_x,start_y)) #prosthetw stin arxi tou checked_nodes ton arxiko komvo kai kathe komvo gia tin anadromiki klisi tou dfs
        
        i+=1
        #afairw ton komvo apo to allnodes pou einai eite o arxikos stin prwti klisi tis diadikasias eite auton pou exw orisei apo tin anadromiki klisi tis sinartisis!
        allnodes1.remove((start_x,start_y))
        #riskw olous tous geitonikous komvous pou exei o kmovos me sintentagmenes start_x kai start_y
        neighbouring_nodes=[]
        if((start_x-1>=0) & (start_x-1<n)):
            neighbouring_nodes+=[(start_x-1,start_y)]
        if((start_y-1>=0) & (start_y-1<n)):
            neighbouring_nodes+=[(start_x,start_y-1)]
        if((start_x+1>=0) & (start_x+1<n)):
            neighbouring_nodes+=[(start_x+1,start_y)]
        if((start_y+1>=0) & (start_y+1<n)):
            neighbouring_nodes+=[(start_x,start_y+1)]
        
        #kanw mia lista me tous geitones pou exei o komvos alla se tyxaia seira!!
        random_neighbours=random.sample(neighbouring_nodes,len(neighbouring_nodes))
        #afairw apo tin lista auti tous komvous pou exw episkeftei etsi wste na min ksanapaw ekei!!
        random_neighbours=set(random_neighbours) - set(checked_nodes)
        if(len(random_neighbours)==0):return #an i list einai adeia tote simainei pws den exei allous geitones na episkeftei kai etsi epistrefw me to return!
        else:
            #-------------------------test-----------------
            ##random_neighbours=set(random_neighbours) - set(checked_nodes)
            ##if(len(random_neighbours)==0):return
            #-----------------end test----------------------------
            selectnd=random_neighbours.pop() #edw afairw ton komvo apo tous tuxaious geitones pou exei!!
            
            temp_node=tuple(selectnd)
            start_x=selectnd[0] #pairnw tis sintentagmenes tou kai tis topothetw stis metaviltes start_x kai start_y
            start_y=selectnd[1]
            dfs(start_x,start_y,allnodes1,n,checked_nodes,i) # ksanaektelw tin dfs me ton neo komvo pou exw parei kai paw na ton episkeftw!!
        
        
        if(len(random_neighbours)==0):return
        else:
            print("edw xtipaei")
            
            selectnd=random_neighbours.pop()
            
            temp_node=tuple(selectnd)
            start_x=selectnd[0]
            start_y=selectnd[1]
            dfs(start_x,start_y,allnodes1,n,checked_nodes,i)
      
if __name__ == "__main__": main()
    