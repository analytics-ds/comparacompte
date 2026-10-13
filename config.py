# -*- coding: utf-8 -*-
"""Identité du média et textes transverses. UN SEUL endroit à remplir pour tout ce qui
n'est pas du contenu éditorial (nom, baseline, CTA, méthode, critères du comparateur).

Rempli par Claude à l'étape 4 de la skill pbn-ao-geo. Tout ce qui est marqué OBLIGATOIRE
doit être adapté au secteur : la QA (check_site.py) refuse les valeurs d'exemple.
"""

# ------------------------------------------------------------------ identité
NOM = "Comparacompte"
SLUG = "comparacompte"                      # OBLIGATOIRE nom du dossier et du repo GitHub (ascii, minuscules, tirets)
OWNER = "analytics-ds"                    # compte GitHub qui héberge le repo (rempli par scripts/prereqs.sh)
SITE = f"https://{OWNER}.github.io/{SLUG}"  # racine publique, sans slash final (canonical, JSON-LD, sitemap)
LANG = "fr"
ACCENT = "#0E9F6E"                        # couleur d'accent, réécrite par scripts/recolor.py (theme-color)
CSS_V = "7"                               # cache-buster des assets

# ------------------------------------------------------------------ vocabulaire
UNIT = "comptes"
UNIT_ONE = "compte"
CTA = "Comparer 2 comptes"
CTA_LONG = "Comparer deux comptes"
BASELINE = "Le média des comptes bancaires du quotidien, perso, pro et ado. Nous relevons les tarifs, nous comparons, nous classons."
TAGLINE_FOOTER = "Le média de la finance du quotidien."
AUTHOR = "La rédaction Comparacompte"
AUTHOR_INITIAL = "C"

# Liste « Marques » du pied de page : (libellé, href). Mettre le client en premier.
FOOTER_BRANDS = [("Nickel", "compte-perso/"), ("Qonto", "compte-pro/"), ("BoursoBank", "compte-perso/"), ("Revolut", "compte-ado/")]

# ------------------------------------------------------------------ textes transverses
NEWSLETTER_P = "Un email par semaine, le classement du mois, les nouveaux comparatifs et les hausses de tarifs bancaires repérées dans les plaquettes."
NEWSLETTER_NOTE = "Pas de publicité, désinscription en un clic."
ASIDE_NEWS_P = "Le classement du mois et les nouveaux comparatifs de comptes, un email par semaine."

# Encart « Notre méthode » en bas de chaque article. OBLIGATOIRE : 5 puces propres au secteur.
METHOD_INTRO = "Ce comparatif repose sur des données publiques, vérifiables une par une, et sur des critères affichés avant le classement."
METHOD_ITEMS = [
 "Les tarifs sont relevés dans les plaquettes tarifaires et les pages officielles des établissements, frais de tenue de compte et de carte compris",
 "Les conditions d'ouverture (revenus, âge, justificatifs, délai) sont vérifiées sur le parcours d'ouverture de chaque offre",
 "Les plafonds réglementaires (frais d'incident, offre clientèle fragile, droit au compte) sont ceux publiés par la Banque de France et service-public.fr",
 "Les avis clients sont lus sur les stores d'applications et Trustpilot, en retenant les motifs récurrents plutôt que la note seule",
 "Chaque critère est noté sur 10 et la grille de notation est identique d'un comparatif à l'autre",
]

# Critères du comparateur 2 entités de l'accueil : 5 critères, le dernier est la note globale.
CRITERIA = [
 ("Accessibilité", "conditions de revenus, d'âge et de situation bancaire"),
 ("Prix", "coût annuel du compte et de la carte"),
 ("Ouverture", "délai, justificatifs, en ligne ou en point de vente"),
 ("Services", "espèces, virements, application, assistance"),
 ("Note globale", "moyenne pondérée"),
]

# Liens internes supplémentaires pour linkify : (fragment de titre présent dans le libellé du lien, chemin).
# Les titres complets des articles publiés sont branchés automatiquement.
EXTRA_LINKS = [
 ("Nickel ou N26", "compte-perso/nickel-ou-n26/"),
 ("Nickel ou Revolut", "compte-ado/nickel-ou-revolut-ado/"),
]

# Google Fonts : réécrit par scripts/recolor.py --display/--text
FONTS_HREF = "https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@600;700;800&family=Inter:wght@300;400;500;600&display=swap"
COMPARED = "comparés"                    # accord du participe dans l en-tête d article (comparées pour marques, comparés pour comptes)
