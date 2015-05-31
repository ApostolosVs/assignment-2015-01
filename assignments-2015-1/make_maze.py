import sys
import random
import decimal



def main():
    argument=sys.argv #edw pairnoume ta argument pou exoume me tin klisi tou programmatos!!
    if(len(argument)<6) | (len(argument)>=7): 
        print(TypeError('Requires 6 arguments!'))
        exit()
    else:
        x=argument[1]
        input_seed=argument[4]
        start_x=argument[2]
        start_y=argument[3]
        if(x.isdigit()&start_x.isdigit()&start_y.isdigit()&input_seed.isdigit()):
            n=int(x)
           
            if(n>30):
                print("Error n prepei na einai mexri 30")
                exit()
            start_x=int(start_x)
            start_y=int(start_y)
           
            if((start_x<0 | start_x>n) |(start_y<0 | start_y>n)):
                print("Error ta arxika tha prepei na einai sto 0<=x i y <n")
                exit()
            input_seed=int(input_seed)
        else: 
            print("Error in the arguments!!")
            exit()
        random.seed(input_seed)
        
       
       
        try:
            outfile=open(argument[5],'w')
        except:
            print('Could not make the file!')
        #NA VRW ALLO TROPO!!!
        allnodes=[]
        for i in range(n):
            for j in range(n):
                allnodes+=[(i,j)]
        checked_nodes=[]     
        dfs(start_x,start_y,allnodes,n,checked_nodes,0)
        
        
        
        
def dfs(start_x,start_y,allnodes1,n,checked_nodes,i):
   
    print(start_x,start_y)
    print(allnodes1)
    if(len(allnodes1)==0):return
    else:
       
        checked_nodes.insert(i,(start_x,start_y))
        
        i+=1
        print("exw elegksei {}".format(checked_nodes))
        allnodes1.remove((start_x,start_y))
        print("oloi oi komvoi einai {}".format(allnodes1))
        neighbouring_nodes=[]
        if((start_x-1>=0) & (start_x-1<n)):
            neighbouring_nodes+=[(start_x-1,start_y)]
        if((start_y-1>=0) & (start_y-1<n)):
            neighbouring_nodes+=[(start_x,start_y-1)]
        if((start_x+1>=0) & (start_x+1<n)):
            neighbouring_nodes+=[(start_x+1,start_y)]
        if((start_y+1>=0) & (start_y+1<n)):
            neighbouring_nodes+=[(start_x,start_y+1)]
        print("oi geitones einai {}".format(neighbouring_nodes))
        
        random_neighbours=random.sample(neighbouring_nodes,len(neighbouring_nodes))
        random_neighbours=set(random_neighbours) - set(checked_nodes)
        if(len(random_neighbours)==0):return
        else:
            ##random_neighbours=set(random_neighbours) - set(checked_nodes)
            ##if(len(random_neighbours)==0):return
            selectnd=random_neighbours.pop()
            print("epilogi mou einai {}".format(selectnd))
            temp_node=tuple(selectnd)
            start_x=selectnd[0]
            start_y=selectnd[1]
            dfs(start_x,start_y,allnodes1,n,checked_nodes,i)
        
        
        if(len(random_neighbours)==0):return
        else:
            print("edw xtipaei")
            print("oi random einai {}:".format(random_neighbours))
            selectnd=random_neighbours.pop()
            print("epilogi mou einai {}".format(selectnd))
            temp_node=tuple(selectnd)
            start_x=selectnd[0]
            start_y=selectnd[1]
            dfs(start_x,start_y,allnodes1,n,checked_nodes,i)
      
if __name__ == "__main__": main()
    