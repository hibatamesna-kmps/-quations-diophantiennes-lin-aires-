def pgcd_with_steps(a, b):
    """
    Calcul du PGCD en affichant les étapes de l'algorithme d'Euclide.
    Retourne le PGCD positif.
    """
    a0, b0 = a, b
    a, b = abs(a), abs(b)
    print("\n--- Étapes de l'algorithme d'Euclide ---")
    while b != 0:
        q = a // b
        r = a % b
        print(f"{a} = {b} * ({q}) + {r}")
        a, b = b, r
    print(f"PGCD({a0}, {b0}) = {a}")
    return a


def euclide_etendu(a, b):
    """
    Algorithme d'Euclide étendu (retourne (d, x0, y0) tels que a*x0 + b*y0 = d).
    Ici on garde les signes originaux de a et b (fonction marche pour entiers).
    """
    if b == 0:
        return abs(a), 1 if a >= 0 else -1, 0  # d = |a|
    else:
        d, x1, y1 = euclide_etendu(b, a % b)
        x0 = y1
        y0 = x1 - (a // b) * y1
        return d, x0, y0


def solve_diophantine(a, b, c):
    """
    Résout a*x + b*y = c (si possible).
    Affiche PGCD, test 'premiers entre eux', solution particulière et forme générale.
    """
    print("\n=== Résolution de a*x + b*y = c ===")
    # 1) PGCD avec étapes
    d = pgcd_with_steps(a, b)

    # 2) Test 'premiers entre eux'
    if d == 1:
        print(f"\nDéfinition : {a} et {b} sont premiers entre eux (PGCD = 1).")
    else:
        print(f"\nDéfinition : {a} et {b} ne sont pas premiers entre eux (PGCD = {d}).")

    # 3) Vérifier existence de solution
    if c % d != 0:
        print("\n❌ Il n'existe aucune solution entière car d ne divise pas c.")
        return None  # pas de solution
    else:
        print("\n✅ d divise c → il existe des solutions entières.")

    # 4) Euclide étendu pour obtenir x0, y0 tel que a*x0 + b*y0 = d
    d2, x0, y0 = euclide_etendu(a, b)
    # euclide_etendu retourne d2 = |d| ; s'assurer que d2 positive et correspond
    if d2 != abs(d):
        # Ajustement si nécessaire (rare, mais pour cohérence)
        d = d2

    print(f"\nEuclide étendu donne : {a}*({x0}) + {b}*({y0}) = {d2}")

    # 5) solution particulière pour c
    mult = c // d2
    x_part = x0 * mult
    y_part = y0 * mult
    print(f"\nSolution particulière (x_p, y_p) = ({x_part}, {y_part})")

    # 6) forme générale : (x, y) = (x_p + (b/d) * k, y_p - (a/d) * k)
    alpha = b // d2
    beta = - (a // d2)  # on utilisera + beta*k dans l'affichage, beta = -a/d
    print("\nForme générale des solutions :")
    print(f"(x, y) = ({x_part} + ({alpha})·k, {y_part} + ({beta})·k),  k ∈ ℤ")

    # 7) vérification rapide (optionnelle) : plug k=0 should satisfy
    check = a * x_part + b * y_part
    print(f"\nVérification (k=0) : a*x_p + b*y_p = {check}  (doit = c = {c})")

    return {
        "d": d2,
        "x_part": x_part,
        "y_part": y_part,
        "alpha": alpha,
        "beta": beta
    }


if __name__ == "__main__":
    print("TP : PGCD + 'premiers entre eux' + solutions de a*x + b*y = c")
    try:
        a = int(input("\nEntrer la valeur de a : ").strip())
        b = int(input("Entrer la valeur de b : ").strip())
        c = int(input("Entrer la valeur de c : ").strip())
    except ValueError:
        print("Erreur : entrez des entiers valides.")
        exit(1)

    result = solve_diophantine(a, b, c)

    if result is not None:
        # Impression résumée finale (pour la capture d'écran / rapport)
        print("\n--- Résumé final ---")
        print(f"d = {result['d']}")
        print(f"Solution particulière : (x_p, y_p) = ({result['x_part']}, {result['y_part']})")
        print(f"Forme générale : (x, y) = ({result['x_part']} + {result['alpha']}·k, {result['y_part']} + {result['beta']}·k)")
    print("\nFin du programme.")
