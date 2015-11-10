object euler112 {
    
    def bouncy(n:Long):Boolean = {
        var oldc=' '
        var increasing=false
        var decreasing=false
        for(c <- n.toString){
            if(oldc!=' '){
                if(! decreasing)decreasing=(c<oldc)
                if(! increasing)increasing=(c>oldc)
                if(increasing && decreasing)
                    return true
                oldc=c
            }else{
                oldc=c
            }
        }
        //return increasing && decreasing
        return false
    }

    def main(args: Array[String]) {
 
       
        var i:Long=0
        var nbBouncy:Double=0
        var n:Long=99
        while(nbBouncy/n.toDouble < 99.0/100.0){
            n+=1
            if(bouncy(n))nbBouncy+=1
        }
        println(n)
        
    }
}
