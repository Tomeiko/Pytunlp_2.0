evaluar = """ título: Experiences in Developing a Distributed Agent-based 
Modeling Toolkit with Python 
resumen: Distributed agent-based modeling (ABM) on high-performance 
computing resources provides the promise of capturing unprecedented details 
of large-scale complex systems. However, the specialized knowledge required 
for developing such ABMs creates barriers to wider adoption and utilization. 
Here we present our experiences in developing an initial implementation of 
Repast4Py, a Python-based distributed ABM toolkit. We build on our 
experiences in developing ABM toolkits, including Repast for High 
Performance Computing (Repast HPC), to identify the key elements of a useful 
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages 
and the Python C-API to create a scalable modeling system that can exploit 
the largest HPC resources and emerging computing architectures.
"""
listaresumen = evaluar.split('resumen: ')[1].split(".")
listatitulo = evaluar.split (":")[1].split("resumen")[0]
if (len(listatitulo.split()) <= 10):
     print ('título: ok')
else:
     print ('titulo: no ok')
facil = 0
acept = 0
dificl = 0
muy = 0
for elem in listaresumen:
     if (elem != "\n"):
          aux = len(elem.split())
          if (aux <= 12):
               facil += 1
          elif (aux <= 17):
               acept += 1
          elif (aux <= 25):
               dificl += 1
          else:
               muy += 1
print('Cantidad de oraciones fáciles de leer:', facil, ', aceptables para leer:', acept, ', dificil de leer:', dificl, ', muy difícil de leer:', muy)    