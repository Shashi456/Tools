import tarfile
fname="c:\\users\\venkateshd\\corpus\\news20.tar.gz"#enter the path of the file you want to extract here, with drives included
if (fname.endswith("tar.gz")):
    tar = tarfile.open(fname, "r:")
    tar.extractall("c://users//venkateshd//corpus")#enter the file where you want the output at 
    tar.close()
elif (fname.endswith("tar")):
    tar = tarfile.open(fname, "r:")
    tar.extractall("<string2>")#enter the file where you want the output at 
    tar.close()
    
