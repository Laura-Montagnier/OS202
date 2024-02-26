from mpi4py import MPI

# On initialise le MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# On initialise le jeton
jeton = None

# On code pour le procédé zéro, qui doit en quelque sorte "initialiser"
if rank == 0:
    jeton = 1
    
    dest_rank = (rank + 1) % size #On travaille modulo le nombre de procédés.
    comm.send(jeton, dest=dest_rank)
    
    jeton = comm.recv(source=size - 1)
    
    print(f"Le jeton est égal à {jeton}")
    

# Il faut coder l'action symétrique à l'envoi, c'est-à-dire la réception, 
# pour tous les procédés non égaux à zéro.

else:
    # On reçoit le jeton du procédé précédent
    source_rank = (rank - 1) % size
    jeton = comm.recv(source=source_rank)
    

    
    
    
    jeton += 1
    
    
    dest_rank = (rank + 1) % size
    comm.send(jeton, dest=dest_rank)

# On "ferme" MPI
MPI.Finalize()

