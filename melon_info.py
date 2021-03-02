"""Print out all the melons in our inventory."""


from melons import melons


def print_melons(melons):
    """Print each melon with corresponding attribute information."""
    
    for name, attributes in melons.items():
        print(name.upper())

        for attributes, value in attributes.items():
            print(f"     {attributes}: {value}")

print_melons(melons)