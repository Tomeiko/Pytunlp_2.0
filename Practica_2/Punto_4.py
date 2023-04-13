from collections import Counter
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
lista = evaluar.split('resumen: ')
cnt = Counter()
for word in lista[0].split():
     if('título:' != word):
          cnt[word] += 1
aux = sum(cnt.values())
if (aux <= 10):
     print ('título: ok')
else:
     print ('titulo: no ok')
oraciones = {"fácil de leer": 0, "aceptable para leer": 0, "difícil de leer": 0, "muy difícil": 0}
for elem in lista[1].split('.'):
     cnt = Counter()
     if (elem != '\n'):
          for word in elem.split():
               cnt[word] += 1
          aux = sum (cnt.values())
          if (aux <= 12):
               oraciones['fácil de leer'] += 1
          elif (aux <= 17):
               oraciones['aceptable para leer'] += 1
          elif (aux <= 25):
               oraciones['difícil de leer'] += 1
          else:
               oraciones['muy difícil'] += 1
print('Cantida de oraciones', oraciones)          