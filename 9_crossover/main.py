import random
import math


def main():
    str1 = input("Enter the 1st genes: ")
    str2 = input("Enter the 2nd genes: ")
    gene1 = list(str1)
    gene2 = list(str2)
    n = len(gene1)
#     k = math.floor(random.random() * n)
    k = random.randint(0,len(str1))
    print(f"The crossover point is: {k}")
    final_genes1 = list()
    final_genes2 = list()
    index = 0
    while index < n:
        if index < k:
            final_genes1.append(gene1[index])
            final_genes2.append(gene2[index])          
        else:
            final_genes1.append(gene2[index])
            final_genes2.append(gene1[index])
        index += 1
    final_str1 = ""
    final_str2 = ""
    for bit in final_genes1:
        final_str1 += bit
    for bit in final_genes2:
        final_str2 += bit

    print(f"Chromosome 1 is: {str1}")
    print(f"Chromosome 2 is: {str2}")
    print(f"Offspring 1 is: {final_str1}")
    print(f"Offspring 2 is: {final_str2}")

main()