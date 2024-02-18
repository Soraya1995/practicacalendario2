class fecha:
 def __init__(self,dia=1,mes=1,año=1970):
    self.dia=dia
    self.mes=mes
    self.año=año
    self.dia_semana=self.semana_validar()
    
   
    
    
    
 def info(self):
    return f" del {self.dia},del mes {self.mes},del año {self.año}"

    

 def validar_dia_mes(self):  
   if self.mes<1 or self.mes>12:
       return False
   if self.mes in (1,3,5,7,8,10,12):
      return 1<=self.dia <=31
  
   elif self.mes in(4,6,9,11):
      return 1<= self.dia <=30
   elif self.mes==2:
       if self.validar_año():
           return 1<= self.dia <=29
       else:
           return 1<= self.dia <=28
   else:
        return False 
  
    

 def error_fecha(self):  
  if not self.validar_dia_mes() and self.validar_año():
      raise ValueError("fecha erronea")
  return True ,"fecha correcta"
     
 
            
      
      
 def validar_año(self):
     #para verificar si es bisiesto o no el año.
      if (self.año%4==0 and self.año%100!=0) or (self.año%400==0):
             return True,"el año es bisiesto"
      else:
             return False,"el año no es bisiesto"
    
     
         

                 
                 
          
    
     

 def semana_validar(self):
    if self.mes in(1,2):
        self.mes1=self.mes+12
        self.año1=self.año-1
        
    else:
        self.mes1=self.mes
        self.año1=self.año
        
    A=self.año1%100
    B=self.año1//100
    C=2-B+B//4
    D=A//4
    E=13*(self.mes1+1)//5
    if self.año <2000:
      F=A+C+D+E+self.dia
    else:
      F=A+C+D+E+self.dia-1
    
    dia_semana=int(F%7)
    dia=["SABADO","DOMINGO","LUNES","MARTES","MIERCOLES:","JUEVES:","VIERNES"]
    return dia [dia_semana]
    
         
     



dia= fecha(29,10,1995)
print(dia.info( )) 
print(dia.validar_año())
#print(dia.validar_dia_mes())
print(dia.error_fecha())
print(dia.semana_validar())