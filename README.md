<!-- -------------- -->
main.py                     : main code file, run this on default
mst.py                      : code containing the algorithms. This file is called by main.py
dataset/                    : directory with various datasets in .graphml format
        /tokyo.graphml      : huge dataset with 898,430 nodes
        /los_angeles.graphml: large dataset with 297,333 nodes
        /newyork.graphml    : medium dataset with 54,128 nodes
        /manhatten.graphml  : small dataset with 4,426 nodes 
        /maldives.graphml   : tiny dataset with 639 nodes
docs/                       : directory with outputs, results and report
        /code_algorithms/   : screenshots of implementation of prims and kruskals algorithm from mst.py
        /graphs/            : generated graphs including original data, mst generated after running mst.py
        /results/           : snapshots of program output on different datasets where algorithm = 'both'
        /PROJECT_REPORT.pdf : report
references.txt              : references for this project
README.md                   : information to run the program

<!-- -------------- -->
The code uses Networkx library to handle the data and graphs. Install the networkx library running the following line in terminal:
pip install networkx 
<!-- -------------- -->

main.py
    init() method contains variables to be changed to run the code accordingly
        graphsize : 'tiny', 'small', 'medium', 'large', 'huge' 
        algorithm : 'none', 'kruskal', 'prim', 'both'
            'none' Generate the graph passed in the dataset.
            'kruskal' Implements Kruskal's algorithm to generate and show minimum spanning tree and print running time in console
            'prim' Implements Prim's algorithm to generate and show minimum spanning tree and print running time in console
            'both' Will NOT generate graphs:  only runtime-comparative values printed in console
            Recommended: Use only 'both' for 'large' and 'huge' graphsize values, the program uses a lot of resources and time for these datasets
    do_algo() (referenced by implement_algo()) method does not give good results for 'tiny' 'small' 'medium' datasets
    do_algo1() (referenced by implement_algo()) method is modified do_algo() to work with those datasets
    Allother methods run as default, information for each can be found in the comments

mst.py
    kruskal_mst_edges() implementation of Kruskal's algorithm on the graph of interest
    prim_mst_edges() implementation of Prium's algorithm on the graph of interest
    minimum_spanning_edges() method deals with calling the other functions
<!-- -------------- -->