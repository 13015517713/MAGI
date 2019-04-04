#from cgroupspy import trees
import subprocess
import resourceMonitor as rM

def createCgroup(subsystem,name):
    '''
    sS = trees.Tree().get_node_by_path('/'+str(subsystem)+'/')
    if sS.create_cgroup(name) is None:
        print('Err: Wrong Path:',str(subsystem)+str(name)+'/')
        '''
    if subprocess.getstatusoutput("cgcreate -g " + subsystem + ":" + "name") == 1:
        print("Err: create cgroup")

def addProcs(subsystem,path_to_cgroup,pid):
    '''
    if subprocess.getstatusoutput('echo '+str(proId)+' > /sys/fs/cgroup/'+str(path)+'/cgroup.procs') == 1:
        print('Err: Add Process Fail')
'''
    if subprocess.getstatusoutput("cgclassify -g " + subsystem + ":" + path_to_cgroup + str(pid)) == 1:
        print("Err: Add Process Fail")

def startProcs(subsystems,path_to_cgroup,cmd):
    if subprocess.getstatusoutput("cgexec -g " + subsystems + ":/" + path_to_cgroup + " " + cmd) == 1:
        print("Err: Start Process in cgroup Fail")


def cpu_quotaSet(group,quota):
    if subprocess.getstatusoutput("cgset -r cpu.cfs_quota_us=" + str(quota) + " " + group) == 1:
        print("Err: quotaSet Fail")
        return -1
    return 0

def cfs_periodSet(group,period):
    if subprocess.getstatusoutput("cgset -r cpu.cfs_period_us=" + str(period) + " " + group) == 1:
        print("Err: cpu_periodSet Fail")
        return -1
    return 0
    
def cpusSet(value,path_to_cgroup):
    if subprocess.getstatusoutput("cgset -r cpuset.cpus=" + str(value) + path_to_cgroup) == 1:
        print("Err:set cpus Fail")
        return -1
    return 0

def cfs_quotaCut(group,percent):
    if cfs_periodSet(group,int(float(rM.get_cfs_quota(group)) * float(percent))) == -1:
        return -1
    return 0

if __name__ == '__main__':
    #addProcs(input("pid:"),input("path"))
    #createCgroup(input('subsystem:'),input('name:'))
    #quotaSet(input("appName:"),input(" quota value:"))
    addProcs(input("subsystem:"),input("path_to_group:"),input("pid:"))
    cpusSet(input("cpus:"),input("path_to_group:"))
