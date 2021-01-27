# Network clusters. Tools to add nodes, find duplicate clusters, delete duplicate clusters, split cluster.
# Copyright Ilpo Kantonen 2021.

class nclusters:
    def __init__(self, id_p, gd_p):
        self.id = id_p
        self.names = gd_p                    # This cluster has all kits of mcluster
        self.links = []
        self.ind = 0
        self.nclusters = []

    def __init__(self):
        self.nclusters = []
        self.ind = 0

    def add(self, cluster_p=[]):
        # First we create a tuple whwre is node name and then list of persons (oldest mother line mother)
        self.nclusters.append(cluster_p)
        self.ind += 1

    def show(self):
        print('NETCLUSTERS ===================================================')
        for a in self.nclusters:
            print(a)
            print('----------')
        print('NETCLUSTERS ===================================================')

    def show_cluster_mdkas(self, cluster_p):
        i = 0
        for clu in self.nclusters:
            if i == cluster_p:
                for match in clu:
                    if match[6] == '':
                        print('Unknown MDKA')
                    else:
                        print('MDKA', match[6])
            i = i+1

    def show_all_mdkas(self):
        for clu in self.nclusters:
            for match in clu:
                if match[6] == '':
                    print('Unknown MDKA')
                else:
                    print('MDKA', match[6])

    def find_duplicates(self,cluster_p):
        # https: // stackoverflow.com / questions / 1388818 / how - can - i - compare - two - lists - in -python - and -
        # return -matches
        # Sort cluster_p, sort clusters in nclusters if you are not using above method

        # If you find same mdka in other cluster, it is duplicate.
        # In same cluster there can be several same mdka's
        # Don't remove duplicates before splitting is done.
        found = False
        ind = 0
        for clu in nclusters:
            for clu2 in nclusters[clu[0]+1]                 # Compare first iterable with next to end of list
            if cluster_p == clu and ind > clu[0]:           # First cluster is not a duplicate
                found = True
                this.nclusters.pop(ind)

        if found:
            return found

    def remove(self, toremove_p):
        if toremove_p < len(this.nclusters):
            self.nclusters.pop(toremove_p)
            return True
        else:
            return False

    def to_be_splitted(self):
        # TODO: Koodaa nclusters etsi splittitarpeita
        return False

    def split(self, node_p):
        # TODO: Koodaa klusterin splittaus
        return False

    def clusteramount(self):
        i = 0
        for a in self.nclusters:
            i += 1
        return i

    def addlink(self,another):
        self.links.add(another)

    def split_cluster(self):
        print("Coming soon!")
        return

    def __len__(self):
        return len(self.nclusters)
        # TODO: Testaa __len__

#    def add_match_to_network(self, match):

