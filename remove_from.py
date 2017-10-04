import sys

def remove_from():
    if len(sys.argv) != 3:
        print("where are your files?")
        return
    file_test = sys.argv[1]
    file_train = sys.argv[2]
    print(file_test)
    print(file_train)
    
    tris_in_test = [l.strip().split("\t") for l in open(file_test, "r").readlines()]
    h, t, r = zip(*tris_in_test)
    ents_in_test = set(h + t)
    print(len(ents_in_test))

    u_train = []
    tris_in_train = [l.strip().split("\t") for l in open(file_train, "r").readlines()]
    
    for tri in tris_in_train:
        if tri[0] not in ents_in_test and tri[1] not in ents_in_test:
            u_train.append(tri)
        else:
            pass
    
    self_rel = "SELF"
    for ent in ents_in_test:
        #u_train.append((ent, ent, self_rel))
        pass

    print(len(u_train))
    print(len(set(zip(*u_train)[2])))
    open("train.txt", "w").write("\n".join(["\t".join(tri) for tri in u_train])+"\n")

    print("=" * 36 + "Finish" + "=" * 36)

if __name__ == "__main__":
    remove_from()
