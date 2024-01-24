from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)

miFrame.pack()

operacion=""

resultado=0

coma=False

digitoDisplay=StringVar()

display=Entry(miFrame, textvariable=digitoDisplay, font="Arial 15")

display.grid(row=1, column=1, columnspan=4, pady=10) # columnspan=4 es para ampliar a 4 casillas

display.config(background="black", fg="#00db00", justify="right", width=30)

digitoDisplay.set("0")

#-------------------- funcion alternativa para coma ----------------

def pulsacion_coma():
    
    contador=0
    
    for i in digitoDisplay.get():
        
        if i==",":
            
            contador+=1
            
    if contador==0:
        
        digitoDisplay.set(digitoDisplay.get()+",")

#-------------------- pulsaciones numeros --------------------------

def pulsacionesTeclas(numPulsado):
    
    global operacion 
    
    global coma
    
    if operacion!=" ":
        
        digitoDisplay.set(numPulsado)
        
        operacion=" "
        
    else:
        
        if numPulsado=="0" and digitoDisplay.get()=="0":
            
            digitoDisplay.set("0")
            
        elif numPulsado=="," and digitoDisplay.get()=="0":
            
            digitoDisplay.set(digitoDisplay.get() + numPulsado)
            
            coma=True
        
        elif numPulsado!="0" and digitoDisplay.get()=="0":
            
            digitoDisplay.set(numPulsado)
            
      
            
        elif numPulsado=="," and coma==False:
            
            digitoDisplay.set(digitoDisplay.get() + numPulsado)
                
            coma=True
                
        elif numPulsado!="," and coma==True:
            
            digitoDisplay.set(digitoDisplay.get() + numPulsado)
            
        elif numPulsado!="," and coma==False:
            
            digitoDisplay.set(digitoDisplay.get() + numPulsado)
    
#-------------------- función suma ---------------------------------------

def suma(num):
    
    global operacion # palabra reservada global, sino pyhton pensaría que es la misma operacion que la de arriba
    
    global resultado
    
    resultado+=float(num)
    
    if resultado.is_integer():
        digitoDisplay.set(int(resultado))
   
    operacion="suma"
    
    digitoDisplay.set(resultado)
    
#--------------------funcion total-----------------------------------

def total():
    
    global resultado
    
    if(resultado+float(digitoDisplay.get())).is_integer():
        digitoDisplay.set(int(resultado+int(digitoDisplay.get())))
        
        resultado=0
    
    else:
            
        digitoDisplay.set(resultado+int(digitoDisplay.get()))
    
        resultado=0


#--------------------primera fila ----------------------------------

boton7=Button(miFrame, text="7", width=5, command=lambda:pulsacionesTeclas("7"))
boton7.grid(row=2, column=1)

boton8=Button(miFrame, text="8", width=5, command=lambda:pulsacionesTeclas("8"))
boton8.grid(row=2, column=2)

boton9=Button(miFrame, text="9", width=5, command=lambda:pulsacionesTeclas("9"))
boton9.grid(row=2, column=3)

botondiv=Button(miFrame, text="/", width=5)
botondiv.grid(row=2, column=4)

#--------------------segunda fila ----------------------------------

boton4=Button(miFrame, text="4", width=5, command=lambda:pulsacionesTeclas("4"))
boton4.grid(row=3, column=1)

boton5=Button(miFrame, text="5", width=5, command=lambda:pulsacionesTeclas("5"))
boton5.grid(row=3, column=2)

boton6=Button(miFrame, text="6", width=5, command=lambda:pulsacionesTeclas("6"))
boton6.grid(row=3, column=3)

botonmult=Button(miFrame, text="x", width=5)
botonmult.grid(row=3, column=4)

#--------------------tercera fila ----------------------------------

boton1=Button(miFrame, text="1", width=5, command=lambda:pulsacionesTeclas("1"))
boton1.grid(row=4, column=1)

boton2=Button(miFrame, text="2", width=5, command=lambda:pulsacionesTeclas("2"))
boton2.grid(row=4, column=2)

boton3=Button(miFrame, text="3", width=5, command=lambda:pulsacionesTeclas("3"))
boton3.grid(row=4, column=3)

botonrest=Button(miFrame, text="-", width=5)
botonrest.grid(row=4, column=4)

#--------------------cuarta fila ----------------------------------

boton0=Button(miFrame, text="0", width=5, command=lambda:pulsacionesTeclas("0"))
boton0.grid(row=5, column=1)

botoncoma=Button(miFrame, text=",", width=5, command=lambda:pulsacion_coma())
botoncoma.grid(row=5, column=2)

botonigual=Button(miFrame, text="=", width=5, command=lambda:total())
botonigual.grid(row=5, column=3)

botonsum=Button(miFrame, text="+", width=5, command=lambda:suma(digitoDisplay.get()))
botonsum.grid(row=5, column=4)

raiz.mainloop()