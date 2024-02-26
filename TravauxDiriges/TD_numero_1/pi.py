from mpi4py import MPI
import time
import numpy as np

def compute_pi(samples):
    # on génère des points aléatoires
    x = 2 * np.random.random(samples) - 1
    y = 2 * np.random.random(samples) - 1
    
    # on vérifie que les points se trouvent bien dans le cercle unité
    filtre = x**2 + y**2 < 1
    
    # on compte combien il y a de points
    return np.sum(filtre)

def main():
    # on initialise MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    
    nb_samples = 40_000_000
    
    
    samples_per_task = nb_samples // size
    
    #Le timer va nous donner le temps de calcul.
    beg = time.time()

    
    count = compute_pi(samples_per_task)
    
    
    total_count = comm.reduce(count, op=MPI.SUM, root=0)

    # Le procédé zéro calcule une approximation de pi
    if rank == 0:
        
        approx_pi = 4 * total_count / nb_samples
        
        # on n'oublie pas d'arrêter le temps !
        end = time.time()
        
        # Print results
        print(f"Temps mis pour calculer Pi: {end - beg} seconds")
        print(f"La valeur de Pi est approximativement: {approx_pi}")

if __name__ == '__main__':
    main()
