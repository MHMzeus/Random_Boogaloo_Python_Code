import random
print("Mutation tables")

table_version = int(input("Table number 1.\nTable number 2.\nTable number 3.\nWhich table number?\nNumber: "))

def rollable_table(t_v: int) -> int and str:
    #-
    def rolled_number() -> int:
        return random.randint(0,66)
    #-
    def mutation(r_n: int, mutagen: int) -> int:
        if mutagen > 66:
            raise Exception("Error, something is WRONG!")
        if r_n <= mutagen:
            return mutagen
        if r_n > mutagen:
            return mutation(r_n, mutagen + 6)   
    #-
    dictionary: dict[int, str] = {
        1: "Subtle chaos table",
        2: "Minor chaos table",
        3: "Extreme chaos table"
        }
    keys, values = zip(*dictionary.items())
    for number in keys:
        if t_v == number:
            return mutation(rolled_number(), 6), values[number-1]
    return rollable_table(int(input("Try again.\nNumber:")))


mutagen_number, assigned_table = rollable_table(table_version)
print(mutagen_number, assigned_table)

def rolled_mutation_description(mutagen: int, table: str) -> str:
    mutation_dictionary = {
        6: {
            "Subtle chaos table": ".",
            "Minor chaos table": ".",
            "Extreme chaos table": "."
            },
            
        12: {
            "Subtle chaos table": ".",
            "Minor chaos table": ".",
            "Extreme chaos table": "."
            },
        18: {
            "Subtle chaos table": ".",
            "Minor chaos table": ".",
            "Extreme chaos table": "."
            },
        24: {
            "Subtle chaos table": ".",
            "Minor chaos table": ".",
            "Extreme chaos table": "."
            },
        30: {
            "Subtle chaos table": ".",
            "Minor chaos table": ".",
            "Extreme chaos table": "."
            },
        36: {
            "Subtle chaos table": ".",
            "Minor chaos table": ".",
            "Extreme chaos table": "."
            },
        42: {
            "Subtle chaos table": ".",
            "Minor chaos table": ".",
            "Extreme chaos table": "."
            },
        48: {
            "Subtle chaos table": ".",
            "Minor chaos table": ".",
            "Extreme chaos table": "."
            },
        54: {
            "Subtle chaos table": ".",
            "Minor chaos table": ".",
            "Extreme chaos table": "."
            },
        60: {
            "Subtle chaos table": ".",
            "Minor chaos table": ".",
            "Extreme chaos table": "."
            },
        66: {
            "Subtle chaos table": ".",
            "Minor chaos table": ".",
            "Extreme chaos table": "."
            }
        }
