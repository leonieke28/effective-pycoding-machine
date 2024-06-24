INDENTS = 4


def print_hanging_indents(poem):
    stanzas = poem.split("\n\n")

    for stanza in stanzas:
        lines = stanza.strip().split("\n")
        print(lines[0])
        for line in lines[1:]:
            print(" " * INDENTS + line.strip())
