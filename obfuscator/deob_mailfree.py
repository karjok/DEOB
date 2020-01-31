import base64,zlib,re,sys


def dekod(sc=""):
    """This function get from mailfree module it self"""
    if sc == "":
       return
    sc = sc.split("%")
    sc = sc[::-1]
    if "" in sc:
        sc.remove("")
    sc1=[""] * len(sc)
    for b in sc:
        c = b.split("$",1)
        sc1[int(c[0])]=c[1]

    for n,i in enumerate(sc1):
        if i != None:
                sc1[n] = i[::-1]
                sc1[n] = base64.b64decode(sc1[n])
                sc1[n] = sc1[n][::-1]
                sc1[n] = zlib.decompress(sc1[n])
                sc1[n] = sc1[n][::-1]
                sc1[n] = base64.b64decode(sc1[n])
                sc1[n] = sc1[n][::-1]
    if "" in sc:
       sc.remove("")
    sc2=[""]*len(sc1)
    for b in sc1:
        b = b.split("$",1)
        sc2[int(b[0])]=b[1]

    sc2 = sc2[::-1]
    sc2 = "\n".join(sc2)
    return sc2
def get_sc(file):
	f = open(file,"r").read().replace("\n","%")
	sc = re.search(r"([\"\']{3}(.*?)[\"\']{3})",f)
	z=dekod(bytes(sc.group(1).replace('"""','').replace("'''","")))
	print(z)
if __name__=='__main__':
	get_sc(sys.argv[1])
