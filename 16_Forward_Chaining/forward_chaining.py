class ForwardChaining:
    def __init__(self):
        self.facts = set()  # Initialize a set to hold known facts
        self.rules = []     # Initialize a list to hold rules

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, condition, conclusion):
        self.rules.append((condition, conclusion))

    def infer(self):
        new_facts = True
        while new_facts:
            new_facts = False
            for condition, conclusion in self.rules:
                # Check if the condition is met
                if condition.issubset(self.facts) and conclusion not in self.facts:
                    print(f"Applying rule: if {condition} then {conclusion}")
                    self.facts.add(conclusion)
                    new_facts = True

    def get_facts(self):
        return self.facts


# Example usage
if __name__ == "__main__":
    # Create an instance of ForwardChaining
    fc = ForwardChaining()

    # Add initial facts (symptoms)
    fc.add_fact("fever")
    fc.add_fact("cough")

    # Define rules for diagnosis
    # Each rule is a tuple: (set of conditions, conclusion)
    fc.add_rule({"fever", "cough"}, "possible flu")
    fc.add_rule({"fever"}, "possible infection")
    fc.add_rule({"cough"}, "possible bronchitis")

    # Perform inference
    fc.infer()

    # Get the final set of facts (diagnoses)
    print("\nFinal Diagnoses:")
    for fact in fc.get_facts():
        print(fact)
