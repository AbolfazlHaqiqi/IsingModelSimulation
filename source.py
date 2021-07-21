# We define the main function in which the code is executed


from numpy import fabs
from medium import Medium

def main():
    out = open("data.ising", "w")

    dt = 0.010
    for t in range(200,401):
        print("temp: {:6.4f}".format(t*dt))
        medium = Medium(num = 8,
				dim = 2,
				initial_config = "ordered",
				inputFilename="lattice.data",
				outputfilename='trajectory.xyz',
				dump_step=0,
				initial_direction = 1,
        J= 1,
        h = 0,
				steps = 50,
				temp = t*dt,
				display=True )

        aveE, varE, aveP, varP = medium.Evolution(display=False)
        print("%-5.3f\t%-5.3f\t%-5.3f\t%-5.3f\t%-5.3f" %(t*dt,aveE,varE,aveP,varP), file=out)

        medium.WriteTheLattice()
        print("#", "-"*70)
        pass
    
if "__main__"==__name__:
        main()  