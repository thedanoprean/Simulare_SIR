import networkx as nx
import matplotlib.pyplot as plt
import csv

#Echipa care a lucrat la codul de generare de graph-uri: Deva Dan, Hirceaga Andreea, Pascu Lorena, Racz Christine

# Verificari
def check(v, m):
    muchii_max = v * (v - 1) // 2

    if v > 100:
        print("Numarul maxim de varfuri este 100.")
        return False

    if m > 5000:
        print("Numarul maxim de muchii este 5000.")
        return False

    if m > muchii_max:
        print("Prea multe muchii pentru un graf neorientat.")
        return False

    if m < v - 1:
        print("Graful nu poate fi conex (m < v - 1).")
        return False

    return True

def probability(v,m):           #calcul probabilitate
    muchii_max = m*(m-1)/2
    return m/muchii_max

def main():
    # introducere numar varfuri si muchii
    v = int(input("Varfuri: "))
    m = int(input("Muchii: "))

    p = probability(v, m)
    print(f"probability: {p:.5f}")

    if check(v, m):
        # generare graf
        G = nx.gnm_random_graph(v, m)

        # salvare muchii in CSV
        with open("graph.csv", "w", newline="") as f:
            writer = csv.writer(f)
            for u, w in G.edges():
                writer.writerow([u, w])

        print("Graful a fost salvat in graph.csv")

        # desen graf
        nx.draw(G, with_labels=True)
        plt.show()


if __name__ == "__main__":
    main()