class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        
        sTime,fTime,sMin,fMin = int(startTime[0:2]),int(finishTime[0:2]),int(startTime[3:]),int(finishTime[3:])
    
        
        if(sTime==fTime):
            if(sTime==0):
                sTime=24
            if(fTime==0):
                fTime=24
            if(sMin>fMin):
                return (fTime+24 - sTime)*4 -(sMin+14)//15 +int(fMin/15)
            else:
                if((fTime - sTime)*4 -(sMin+14)//15 +int(fMin/15))<0:
                    return 0
                else:
                    return (fTime - sTime)*4 -(sMin+14)//15 +int(fMin/15)
        elif(sTime<fTime):
            if((fTime - sTime)*4 -(sMin+14)//15 +int(fMin/15))<0:
                return 0
            else:
                return(fTime - sTime)*4 -(sMin+14)//15 +int(fMin/15)
        else:
            return (fTime+24 - sTime)*4 -(sMin+14)//15 +int(fMin/15)
        
      
            
            
            
            
         
        
        
