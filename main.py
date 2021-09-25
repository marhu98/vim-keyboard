#!/usr/bin/python

import sys

def main():
    result_file = "layout_file"

    if len(sys.argv)<2:
        print("You need to specify the file name")
        return
    if len(sys.argv)==3:
        result_file = sys.argv[2]
        
    
    qw = ""
    with open("qwerty","r") as f:
        qw=f.read()
    
    nw = ""
    with open(sys.argv[1],"r") as f:
        nw=f.read()
    
    #print(qw,nw,end="")

    ins = ""

    for z in zip(qw,nw):
        if z[0]=="\n":
            continue
        ins+="inoremap {} {}\n".format(z[0],z[1])

    result = """function! {scheme_name}()
        {insert}        
    endunction
    call {scheme_name}()
    """.format(scheme_name=sys.argv[1],insert=ins)
    #print(result)
    #return

    with open(result_file,"w") as f:
        f.write(result)

if __name__=="__main__":
    main()
