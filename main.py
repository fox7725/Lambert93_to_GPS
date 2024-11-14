import math

# Constantes pour la projection Lambert 93
n = 0.7256077650532670
c = 11754255.426096
lambda0 = 3 * math.pi / 180  # Conversion de 3° en radians
Xs = 700000
Ys = 12655612.049876
e = 0.081819191042816


# Fonction pour convertir les coordonnées Lambert 93 vers WGS84
def lambert93_to_wgs84(x, y):
    # Calcul de la distance au pôle en projection (r)
    r = math.sqrt((x - Xs) ** 2 + (y - Ys) ** 2)

    # Calcul de l'angle par rapport au méridien central (γ)
    gamma = math.atan((x - Xs) / -(y - Ys))

    # Calcul de la latitude isométrique (L)
    L = -math.log(r / c) / n

    # Estimation initiale de la latitude (φ)
    phi = 2 * math.atan(math.exp(L)) - math.pi / 2

    # Itération pour affiner la latitude
    phi_prev = None
    while phi_prev is None or abs(phi - phi_prev) > 1e-12:
        phi_prev = phi
        phi = 2 * math.atan(
            math.exp(L + (e / 2) * math.log((1 + e * math.sin(phi)) / (1 - e * math.sin(phi))))) - math.pi / 2

    # Calcul de la longitude (λ)
    lambda_ = gamma / n + lambda0

    # Conversion en degrés
    latitude = phi * 180 / math.pi
    longitude = lambda_ * 180 / math.pi

    return latitude, longitude


demande = "prout"
while demande.lower() != "stop":
    x_lambert = None
    y_lambert = None

    # Boucle pour obtenir des valeurs de type float
    while True:
        try:
            x_lambert = float(input("Entre la coordonnée X en Lambert 93 : "))
            y_lambert = float(input("Entre la coordonnée Y en Lambert 93 : "))
            break  # Sort de la boucle si les deux valeurs sont correctement converties en float
        except ValueError:
            print("Mais non Owen ! Il faut entrer des valeurs numériques valides pour X et Y.")

    latitude, longitude = lambert93_to_wgs84(x_lambert, y_lambert)

    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print("")

    demande = input('Tape "stop" pour arrêter ou autre chose pour continuer : ')
    if demande.lower() == "stop":
        print("bye bye")
        break
