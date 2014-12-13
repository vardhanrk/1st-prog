#writing the program using functions 

def newfun( var1):
    print (var1)
    return 

var1="Renuk"
newfun( var1 );

def newfun2( var22, var32 ):
    print( var22, var32) 
    if ( var22 >= var32 ):
     print ("print var 2 ")
    else : 
     print ("print var 3")
    return var22,var32

var5=3
var6=4
ff = newfun2( var5, var6 ); 	
  
print("function out put",ff)