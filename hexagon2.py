def print_honeycomb(rows, colse):
    cols=colse-2
    for row in range(rows): 
        if row == 0:
                print(" ___    " * cols)
                print("/   \\___" * cols)
        else:
            if row == 1:
                print("\___/   "*cols)
            print("/   \\___"*cols)
            print("\___/   " * cols)



print_honeycomb(3,7)