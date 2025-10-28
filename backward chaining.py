from collections import defaultdict
import re

# Parse atoms like: predicate(arg) where arg is a constant "duck" or variable A
atom_re = re.compile(r"\s*([a-zA-Z_][a-zA-Z0-9_]*)\(([^()]*)\)\s*")

def parse_atom(s):
    m = atom_re.fullmatch(s.strip())
    if not m:
        raise ValueError(f"Bad atom: {s}")
    pred = m.group(1)
    arg = m.group(2).strip()
    return (pred, arg)

def is_var(x):
    # Convention: variables start with uppercase letter
    return len(x) > 0 and x[0].isupper()

# Knowledge base: rules as (head, body_list) and facts as ground atoms
class KB:
    def __init__(self):
        self.facts = set()          # set of ground atoms ("pred","const")
        self.rules = defaultdict(list)  # head predicate -> list of (head_atom, body_atoms)

    def add_fact(self, atom):
        self.facts.add(atom)

    def add_rule(self, head, body):
        self.rules[head[0]].append((head, body))

def substitute(atom, theta):
    pred, arg = atom
    if is_var(arg) and arg in theta:
        return (pred, theta[arg])
    return atom

def unify(a, b, theta):
    # a, b are atoms (pred,arg). Only single-argument predicates here.
    (pa, xa), (pb, xb) = a, b
    if pa != pb:
        return None
    theta = dict(theta)  # copy
    if is_var(xa) and is_var(xb):
        # prefer binding left variable to right if possible
        if xa in theta and xb in theta:
            return theta if theta[xa] == theta[xb] else None
        if xa in theta:
            return theta if (not xb in theta and not is_var(theta[xa])) else None
        if xb in theta:
            theta[xa] = theta[xb]
            return theta
        # both unbound variables: no concrete info needed
        return theta
    if is_var(xa) and not is_var(xb):
        if xa in theta and theta[xa] != xb:
            return None
        theta[xa] = xb
        return theta
    if not is_var(xa) and is_var(xb):
        if xb in theta and theta[xb] != xa:
            return None
        theta[xb] = xa
        return theta
    # both constants
    return theta if xa == xb else None

def prove(goal, kb, theta=None, visited=None):
    # goal is an atom (pred,arg); returns generator of theta extensions that satisfy goal
    theta = {} if theta is None else dict(theta)
    visited = set() if visited is None else set(visited)
    goal = substitute(goal, theta)
    key = (goal, tuple(sorted(theta.items())))
    if key in visited:
        return
    visited.add(key)

    # 1) Try to match against a fact
    if not is_var(goal[1]) and goal in kb.facts:
        yield theta
        return
    # If fact is variable form, check facts that unify
    for f in kb.facts:
        ut = unify(goal, f, theta)
        if ut is not None:
            yield ut

    # 2) Try rules whose head predicate matches
    for head, body in kb.rules.get(goal[0], []):
        # Standardize apart: rename variables uniquely
        rename = {}
        def std_atom(a):
            p, x = a
            if is_var(x):
                if x not in rename:
                    rename[x] = f"{x}_{id(a)}"
                return (p, rename[x])
            return a
        head_std = std_atom(head)
        body_std = [std_atom(b) for b in body]

        ut = unify(goal, head_std, theta)
        if ut is None:
            continue
        # Prove all premises in body (conjunction)
        def prove_all(goals, theta_curr):
            if not goals:
                yield theta_curr
                return
            first, rest = goals[0], goals[1:]
            for t1 in prove(substitute(first, theta_curr), kb, theta_curr, visited):
                yield from prove_all(rest, t1)

        for t in prove_all(body_std, ut):
            yield t

def explain_proof(query, kb):
    # Construct one proof path if exists
    for theta in prove(query, kb):
        const = query[1]
        bound = theta.get(const, const)
        return True, bound, theta
    return False, None, {}

if __name__ == "__main__":
    # Build the KB from the prompt
    kb = KB()
    # Rules:
    # mammal(A) ==> vertebrate(A).
    kb.add_rule(parse_atom("vertebrate(A)"), [parse_atom("mammal(A)")])
    # vertebrate(A) ==> animal(A).
    kb.add_rule(parse_atom("animal(A)"), [parse_atom("vertebrate(A)")])
    # vertebrate(A), flying(A) ==> bird(A).
    kb.add_rule(parse_atom("bird(A)"), [parse_atom("vertebrate(A)"),
                                        parse_atom("flying(A)")])
    # Facts:
    for s in ['vertebrate("duck")', 'flying("duck")', 'mammal("cat")']:
        kb.add_fact(parse_atom(s))

    # Example queries
    tests = [
        parse_atom('bird("duck")'),
        parse_atom('animal("duck")'),
        parse_atom('vertebrate("cat")'),
        parse_atom('bird("cat")'),
    ]
    for q in tests:
        ok, const, theta = explain_proof(q, kb)
        print(f"Query {q}: {'PROVED' if ok else 'FAILED'}; bindings={theta}")




output
Query ('bird', '"duck"'): PROVED; bindings={'A_1654081914368': '"duck"'}
Query ('animal', '"duck"'): PROVED; bindings={'A_1654081916608': '"duck"'}
Query ('vertebrate', '"cat"'): PROVED; bindings={'A_1654078118656': '"cat"'}
Query ('bird', '"cat"'): FAILED; bindings={}

                
