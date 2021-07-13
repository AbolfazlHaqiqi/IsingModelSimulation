
# Russell Kajouri & Abolfazl Haqiqifar
#Imail : afzhqq@gmail.com


from spin import Spin
import numpy as np



class Lattice():
#Lattice is a number of Spins together.
    ###########################################################################################

    def __init__(self, n, d , mode, dirr, J)-> None:

        """
        n is Number of spins 
        d is Number of dimension
        J is called the exchange energy The size of J tells you how strongly neighboring spins are
             coupled to each other – how much they want to (anti-)align
             The sign of J tells you whether neighbors prefer to align or to anti-align.
              """

        self.Jfactor = J
        self.number = n
        self.L = []

        if mode == "ordered":
		        self.ordered_localization1D(dirr)
        else:
		        self.stochastic_localization1D()
    
		#self.display()
        pass
    #1##########################################################################################
    """
    Spins can have one of the following initial conditions:
        1- Radomly and in a random direction(stochastic) --> Paramagnetism
        2- Regularly and in a specific direction(ordered) --> Ferromagnetism
    The end result has nothing to do whit the initial condition
    """
    def stochastic_localization1D(self):
        for l in range(self.number):
            self.L.append(Spin(np.random.randint(0,2)*2-1))   
                # Here we need discrete random addiction (0 or 1)  
            pass
        pass
    #2##########################################################################################

    def ordered_localization1D(self, dirr):
        for l in range(self.number):
            self.L.append(Spin(dirr))
            pass
        pass
    ###########################################################################################

    def display(self):

        # Depending on the dimension the system show different behaviors

        for l in range(self.number):
                print(self.L[l].direction, end= "")
        print()
        pass
    ###########################################################################################

    def energy(self):

        """
        Suppose the system is periodic & ferromagnetism ->  'J = 1 '
         Consider the system from base 2^n 
              so that we can easily get mood from it
              H = -J sum_i=0^N-1 (L_i)*(L_i+1)
              """
        ene = 0
        for l in range(self.number):
            # ene += self.L[l].direction * self.L[self.period(l+1)].direction
            # ene += self.L[l].direction * self.L[self.period(l-1)].direction
            #or
            ene += self.energyOf(l)#instead of the abov calculations, use the energyof function
        return ene * 0.5 #TODO
        pass
    ###########################################################################################

    def period(self, n):

        """
        If the number it receives is out of range ,
          it returns it to the first ---> If the particles are N ==> L_N = L_0 
            """

        if n == self.number:
            return n % self.number
        elif n == -1:
            return self.number - 1
        else:
            return n
    ###########################################################################################

    def polarization(self):

        """
         This function finds the regularity of lattice 
        The initial value of the function is zero 
        Polarization should be close to zero
            """

        polariz = 0.0
        for l in range(self.number):
            polariz += self.L[l].direction
            pass
        return float(polariz / self.number)
    ###########################################################################################

    def energyOf(self, l):

        # Calculation of single Spin energy

        return -1 * self.Jfactor * ((self.L[l].direction * self.L[self.period(l-1)].direction) +\
            (self.L[l].direction * self.L[self.period(l+1)].direction))
    ###########################################################################################

    def flipSpin(self, l):
        # Changes the direction of the spin
        self.L[l].direction *= -1
    ###########################################################################################

    def chooseSpin(self):
         # Selects a spin at random
            return np.random.randint(0, self.number)
    ###########################################################################################
    
    def MetropoliceStep(self, temp, deltaE):
        """
         if temp = 0 --> false 
         if the temperature is bigger than zero , we get a random number between zero and one
               if bigger than exp(-deltaE/ temp) return True else return false
               """

        if temp == 0:
            return False
        else :
            return True if np.random.random() < np.exp(-deltaE / temp) else False
    ###########################################################################################
    def GetsBackSpin(self, i):
        return self.L[i].direction