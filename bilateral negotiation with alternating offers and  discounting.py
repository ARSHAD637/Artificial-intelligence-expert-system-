# Alternating-Offers and Discounting Negotiation Simulation

units = 100
discount_A = 0.9  # Agent A's discount factor
discount_B = 0.9  # Agent B's discount factor
max_rounds = 10

def utility(share, discount, round_num):
    return share * (discount ** round_num)

def negotiate():
    round_num = 0
    agreement = None
    history = []

    while round_num < max_rounds:
        if round_num % 2 == 0:  # Agent A proposes
            offer_A = units // 2 + 10 if round_num == 0 else units // 2
            offer_B = units - offer_A
            # Agent B decides
            util_B = utility(offer_B, discount_B, round_num)
            util_B_next = utility(offer_A, discount_B, round_num+1)
            if util_B >= util_B_next:
                agreement = (offer_A, offer_B)
                history.append((round_num, "A offers", offer_A, offer_B, "B accepts"))
                break
            else:
                history.append((round_num, "A offers", offer_A, offer_B, "B rejects"))
        else:  # Agent B proposes
            offer_B = units // 2 + 10 if round_num == 1 else units // 2
            offer_A = units - offer_B
            # Agent A decides
            util_A = utility(offer_A, discount_A, round_num)
            util_A_next = utility(offer_B, discount_A, round_num+1)
            if util_A >= util_A_next:
                agreement = (offer_A, offer_B)
                history.append((round_num, "B offers", offer_A, offer_B, "A accepts"))
                break
            else:
                history.append((round_num, "B offers", offer_A, offer_B, "A rejects"))
        round_num += 1

    print("Negotiation History:")
    for h in history:
        print(f"Round {h[0]}: {h[1]}, Offer: (A:{h[2]}, B:{h[3]}) - {h[4]}")
    if agreement:
        util_A = utility(agreement[0], discount_A, round_num)
        util_B = utility(agreement[1], discount_B, round_num)
        print(f"\nAgreement reached: Agent A gets {agreement[0]}, Agent B gets {agreement[1]}")
        print(f"Utility Agent A: {util_A:.2f}, Utility Agent B: {util_B:.2f}")
        if abs(util_A - util_B) < 5:
            print("Result resembles Nash-like fair outcome")
        else:
            print("Result does NOT resemble Nash-like fair outcome")
    else:
        print("\nNo agreement reached.")

negotiate()
