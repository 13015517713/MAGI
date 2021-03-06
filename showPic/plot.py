import matplotlib.pyplot as plt
import numpy as np
import json
import csv
import pandas as pd
def normalize(X, up):
    x = np.array(X)
    mi = x.min()
    ma = x.max()
    if mi == ma:
        return (x/ma)*up
    return ((x - mi)/(ma - mi))*up

def drawXY(X, Y):
    x = np.array(X)
    y = np.array(Y)
    plt.plot(x,y)
    plt.show()


def drawTimeY(Y):
    x = np.linspace(0,len(Y[0]),len(Y[0]))
    for y in Y:
        plt.plot(x, np.array(y))
    plt.show()

if __name__ == '__main__':
    apps = ["sphinx","mcf"]
    fileName = "../stored_data/"
    appResources = []
    #Fi = {}
    for a in apps:
        fileName = fileName + a +'_'
        appResources.append(a+"_ipc")
        appResources.append(a + "_llc")
        appResources.append(a + "_cpu")
        appResources.append(a + "_sla")
        #Fi[a] = {}
    fileName = fileName[:-1]
    fileName += "/data_for_plot.csv"
    df = pd.read_csv(fileName)

    df = df[appResources]
    # Fi = json.loads(dataF.read())

    '''
    Fi["memcached"]["ipc"] = df["memcached_ipc"]
    Fi["mcf"]["ipc"] = df["mcf_ipc"]
    Fi["lbm"]["ipc"] = df["lbm_ipc"]
    Fi["memcached"]["llc"] = df["memcached_llc"]
    Fi["mcf"]["llc"] = df["mcf_llc"]
    Fi["lbm"]["llc"] = df["lbm_llc"]
    Fi["memcached"]["cpu"]= df["memcached_cpu"]
    Fi["mcf"]["cpu"] = df["mcf_cpu"]
    Fi["lbm"]["cpu"] = df["lbm_cpu"]
    Fi["memcached"]["sla"] = df["memcached_sla"]
    Fi["mcf"]["sla"] = df["mcf_sla"]
    Fi["lbm"]["sla"] = df["lbm_sla"]
    '''
    ll = len(df[apps[0]+"_ipc"])
    x = np.linspace(0, ll, ll)
    #sla_memcached = []
    #for i in range(ll):
    #   sla_memcached.append(0.14)

    plt.figure(1)
    plt.subplot(311)
    plt.grid(linestyle=':')
    for a in apps:
        plt.plot(x, df[a+"_ipc"], ">-", label=a)
    #plt.plot(x, Fi["memcached"]["sla"], "r-", label='SLA')
    plt.title("Performance of Apps")
    plt.xlabel("time")
    plt.ylabel("ipc")
    plt.legend(loc='best')

    plt.subplot(312)
    plt.grid(linestyle=':')
    for a in apps:
        plt.plot(x, df[a + "_llc"], ">-", label=a)
    #plt.plot(x, Fi["lbm"]["llc"], ">-", label="lbm")
    plt.title("LLC of Apps")
    plt.xlabel("time")
    plt.ylabel("llc num")
    plt.legend(loc='best')

    plt.subplot(313)
    plt.grid(linestyle=':')
    for a in apps:
        plt.plot(x, df[a + "_cpu"], ">-", label=a)
    #plt.plot(x, Fi["lbm"]["cpu"], ">-", label="lbm")
    plt.title("Cpu of Apps")
    plt.xlabel("time")
    plt.ylabel("cpu quota")
    plt.legend(loc='best')
    '''
    plt.figure(1)
    plt.grid(linestyle=':')
    plt.plot(x,Fi["memcached"]["ipc"],">-",label="memcached")
    plt.plot(x,Fi["mcf"]["ipc"],">-",label="mcf")
    plt.plot(x,sla_memcached,"r-",label='SLA')
    plt.title("Performance of Apps")
    plt.xlabel("time")
    plt.ylabel("ipc")
    plt.legend(loc='best')

    plt.figure(2)
    plt.grid(linestyle=':')
    plt.plot(x, Fi["memcached"]["llc"], ">-",label="memcached")
    plt.plot(x, Fi["mcf"]["llc"], ">-",label="mcf")
    plt.title("LLC of Apps")
    plt.xlabel("time")
    plt.ylabel("llc num")
    plt.legend(loc='best')

    plt.figure(3)
    plt.grid(linestyle=':')
    plt.plot(x, Fi["memcached"]["ipc"], ">-",label="ipc")
    plt.plot(x, sla_memcached, label='SLA')
    plt.plot(x, normalize(Fi["memcached"]["llc"],0.4),">-", label="llc")
    plt.plot(x, normalize(Fi["memcached"]["cpu"],0.4), ">-",label="cpu")
    plt.title("memcached")
    plt.xlabel("time")
    plt.ylabel("normalized data")
    plt.legend(loc='best')

    plt.figure(4)
    plt.grid(linestyle=':')
    plt.plot(x, Fi["mcf"]["ipc"], ">-",label="ipc")
    plt.plot(x, normalize(Fi["mcf"]["llc"],0.4), ">-",label="llc")
    plt.plot(x, normalize(Fi["mcf"]["cpu"],0.4), ">-",label="cpu")
    plt.title("Mcf")
    plt.xlabel("time")
    plt.ylabel("normalized data")
    plt.legend(loc='best')

    plt.figure(5)
    plt.grid(linestyle=':')
    plt.plot(x, Fi["memcached"]["ipc"], ">-",label="Fi["memcached"]["ipc"]")
    plt.plot(x, normalize(Fi["mcf"]["llc"],0.4), ">-",label="Fi["mcf"]["llc"]")
    plt.plot(x, sla_memcached, label='SLA')
    plt.plot(x, normalize(Fi["mcf"]["cpu"],0.4),">-", label='Fi["mcf"]["cpu"]')
    plt.title("memcached\'s SLA with mcf resource")
    plt.xlabel("time")
    plt.ylabel("normalized data")
    plt.legend(loc='best')
'''
    plt.subplots_adjust(hspace=0.4)
    plt.show()
