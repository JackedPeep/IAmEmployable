


def molecularCloningInstructions(verbs,adjectives,nouns,rule):
    import random
    verbs = ("Insert","Wash","Sterilize","Incubate","Ligate","Anneal","Recalibrate","Collect","Autoclave","Heat-shock")
    adjectives = ("dirty","bacterial","contaminated","prepped","sticky","malfunctioning","annealed","biohazard","blunt","ideal")
    nouns = ("E. coli","pipet","Dish","auger","plasmid","vector","DNA","centrifuge","clone","fridge")
    rule = 1
    print("\n\n")
    print("Molecular Cloning Instruction Generator\n")
    for rule in range(10):
        print(str(rule+1),"-", random.choice(verbs), "the", random.choice(adjectives), random.choice(nouns) + ".")
        rule += 1

    print("\n\n")
molecularCloningInstructions(verbs = (),adjectives = (),nouns = (),rule = 1)