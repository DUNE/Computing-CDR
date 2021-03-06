#NumberUtils.py

# Utility function: object = cummulate(object,lifetime)
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# sum backwards over lifetime of record
def cumulate(a,lifetime=100):
  if lifetime < 1:
    return a*lifetime
  b = np.zeros(len(a))
  for i in range(0,len(a)):
    begin = max(0,i-lifetime+1)
    for j in range(begin,i+1):
      b[i] += a[j]
  return b
  


# Utility function: string = dump(datatype,det,object)

# make a dump of a record

def dump(det,datatype,a,Units):
  s = ""
  s  += "%5s, %10s (%s)"%(det,datatype,Units[datatype])
  for j in range(0,len(a)):
    s += ", "
    s += "%8.1f"%a[j]
  s += "\n"
  return s


# Utility function: DrawDet(Value,Years,Data,Types,Units,detcolors,detlines)

# for detector values
def DrawDet(Value,Years,Data,Types,Units,detcolors,detlines):
    
    maxyears = Years[-1]

    fig=plt.figure()
    ax = fig.add_axes([0.2,0.2,0.7,0.7])
    ax.set_xlim(Years[0],maxyears)
    
    ax.spines['bottom'].set_position('zero')
    toplot = Data[Value]
    for type in Types:
      ax.plot(Years,toplot[type],color=detcolors[type],linestyle=detlines[type],label=type)
    ax.legend(frameon=False)
    ax.set_title(Value)
    ax.set_xlabel("Year")
    ax.set_ylabel(Value + ", " + Units[Value])
    plt.grid()
    plt.savefig(Value.replace(" ","-")+".png",transparent=True)
    #plt.savefig(Value+"_w.jpg",transparent=False)
   
    plt.show()


# Utility function: DrawType(Value,Years,Data,Types,Units,typecolors,typelines)

# draw by data type (transpose of the detectors)

def DrawType(Value,Years,Data,Types,Units,typecolors,typelines):
    fig=plt.figure()
    ax = fig.add_axes([0.2,0.2,0.7,0.7])
    maxyears = Years[-1]
    ax.set_xlim(Years[0],maxyears)
   
    ax.spines['bottom'].set_position('zero')
    for type in Types:
      ax.plot(Years,Data[type][Value],color=typecolors[type],linestyle=typelines[type],label=type)
    
    ax.legend(frameon=False)
    ax.set_xlabel("Year")
    ax.set_ylabel(Value + ", " + Units[Value])
    ax.set_title(Value)
    plt.grid()
    plt.savefig(Value.replace(" ","-")+".png",transparent=True)
    #plt.savefig(Value+"_w.jpg",transparent=False)
    
    plt.show()

