#!/usr/bin/python

import sys
import click

@click.command()
@click.argument("input_file")
@click.option("--template","-t",default=False)
@click.option("--output","-o",type=str,default="layout_vim")
def main(input_file,template,output):
    #output = "layout_file"
    print(output)

    if len(sys.argv)<2:
        print("You need to specify the file name")
    
    qw = ""
    with open(input_file,"r") as f:
        qw=f.read()
    
    nw = ""
    with open(input_file,"r") as f:
        nw=f.read()
    
    #print(qw,nw,end="")

    ins = ""

    for z in zip(qw,nw):
        if z[0]=="\n":
            continue
        ins+="\tinoremap {} {}\n".format(z[0],z[1])

    result = """function! {scheme_name}()
    {insert}        
    endunction
    call {scheme_name}()
    """.format(scheme_name=input_file,insert=ins)
    #print(result)
    #return

    with open(output,"w") as f:
        f.write(result)

if __name__=="__main__":
    main()
