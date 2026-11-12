from typing import List, Dict, Union


class FOPLResolution:
    def __init__(self):
        self.clauses = []  # List to store clauses in CNF form

    def add_clause(self, clause: List[str]):
        """Add a clause to the knowledge base."""
        self.clauses.append(clause)

    def unify(self, x: str, y: str, subst: Dict[str, str]) -> Union[Dict[str, str], None]:
        """Unifies two literals, if possible, and returns the substitution map."""
        if x == y:
            return subst
        elif isinstance(x, str) and x.islower():
            return self.unify_var(x, y, subst)
        elif isinstance(y, str) and y.islower():
            return self.unify_var(y, x, subst)
        else:
            return None

    def unify_var(self, var: str, x: str, subst: Dict[str, str]) -> Union[Dict[str, str], None]:
        """Unifies a variable with another literal or variable."""
        if var in subst:
            return self.unify(subst[var], x, subst)
        elif x in subst:
            return self.unify(var, subst[x], subst)
        else:
            subst[var] = x
            return subst

    def apply_substitution(self, clause: List[str], subst: Dict[str, str]) -> List[str]:
        """Applies substitution to a clause."""
        result = []

        for literal in clause:
            for var, value in subst.items():
                literal = literal.replace(f"({var})", f"({value})")
            result.append(literal)

        return result

    def resolve(self, clause1: List[str], clause2: List[str]) -> Union[List[str], None]:
        """Resolves two clauses and returns the resolvent if resolution is possible."""
        for literal1 in clause1:
            for literal2 in clause2:
                if literal1.startswith("~") != literal2.startswith("~"):
                    atom1 = literal1.lstrip("~")
                    atom2 = literal2.lstrip("~")

                    subst = self.unify(atom1, atom2, {})

                    if subst is not None:
                        new_clause1 = self.apply_substitution(clause1, subst)
                        new_clause2 = self.apply_substitution(clause2, subst)

                        new_clause1.remove(literal1 if not subst else self.apply_substitution([literal1], subst)[0])
                        new_clause2.remove(literal2 if not subst else self.apply_substitution([literal2], subst)[0])

                        resolvent = list(set(new_clause1 + new_clause2))
                        return resolvent

        return None

    def resolution(self, query: List[str]) -> bool:
        """Perform resolution on the knowledge base to check if the query can be inferred."""
        self.add_clause([f"~{q}" for q in query])

        while True:
            new = set()

            pairs = [
                (self.clauses[i], self.clauses[j])
                for i in range(len(self.clauses))
                for j in range(i + 1, len(self.clauses))
            ]

            for clause1, clause2 in pairs:
                resolvent = self.resolve(clause1, clause2)

                if resolvent == []:
                    return True

                if resolvent is not None:
                    new.add(tuple(resolvent))

            existing = set(map(tuple, self.clauses))

            if new.issubset(existing):
                return False

            for clause in new:
                if clause not in existing:
                    self.clauses.append(list(clause))


# Example usage
if __name__ == "__main__":
    # Initialize the FOPLResolution class
    resolution = FOPLResolution()

    # Add clauses in CNF form to the knowledge base
    resolution.add_clause(["P(x)", "~Q(x)"])
    resolution.add_clause(["Q(a)"])
    resolution.add_clause(["~P(a)"])

    # Query to check for resolution
    query = ["Q(a)"]

    # Perform resolution
    result = resolution.resolution(query)

    if result:
        print("Query can be inferred from the knowledge base (Contradiction found).")
    else:
        print("Query cannot be inferred from the knowledge base (No contradiction).")
