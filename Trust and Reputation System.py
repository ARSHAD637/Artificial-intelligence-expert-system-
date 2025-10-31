class ServiceProvider:
    def __init__(self, name):
        self.name = name
        self.feedback = []

    def receive_feedback(self, score): # score: 0 to 1
        self.feedback.append(score)

    def trust_score(self):
        if not self.feedback:
            return 0.0
        return sum(self.feedback)/len(self.feedback)

def client_leave_feedback(providers, interactions):
    for client_id, (provider, score) in enumerate(interactions):
        print(f"Client {client_id+1} gives feedback {score} to {provider.name}")
        provider.receive_feedback(score)

# Example setup
providers = [ServiceProvider("Provider A"), ServiceProvider("Provider B"), ServiceProvider("Provider C")]

# Simulate feedback: (Provider, Score)
interactions = [
    (providers[0], 0.7), (providers[0], 0.5), (providers[1], 0.9),
    (providers[1], 0.8), (providers[2], 0.5), (providers[2], 0.6)
]
client_leave_feedback(providers, interactions)

# Compute reputation (average trust score)
print("\nProvider Trust and Reputation Scores:")
for p in providers:
    print(f"{p.name} trust score: {[round(f,2) for f in p.feedback]}")
    print(f"{p.name} reputation: {p.trust_score():.2f}")

# Select the provider with highest reputation
best_provider = max(providers, key=lambda p: p.trust_score())

print(f"\nBest provider (highest reputation): {best_provider.name}")

# Optionally, show all reputation values in a sorted list:
print("\nAll provider reputation values:")
for p in sorted(providers, key=lambda x: x.trust_score(), reverse=True):
    print(f"{p.name}: {p.trust_score():.2f}")


output:
Client 1 gives feedback 0.7 to Provider A
Client 2 gives feedback 0.5 to Provider A
Client 3 gives feedback 0.9 to Provider B
Client 4 gives feedback 0.8 to Provider B
Client 5 gives feedback 0.5 to Provider C
Client 6 gives feedback 0.6 to Provider C

Provider Trust and Reputation Scores:
Provider A trust score: [0.7, 0.5]
Provider A reputation: 0.60
Provider B trust score: [0.9, 0.8]
Provider B reputation: 0.85
Provider C trust score: [0.5, 0.6]
Provider C reputation: 0.55

Best provider (highest reputation): Provider B

All provider reputation values:
Provider B: 0.85
Provider A: 0.60
Provider C: 0.55

