# config.py

# Configuration des fichiers de téléchargement
FILES_CONFIG = [
    {
        "name": "Compta_journaliere.csv",
        "path": "/cleaned_final/Compta_journaliere.csv",
        "type": "Comptabilité",
        "message": "📊 La compta quotidienne, claire comme de l'eau de roche !"
    },
    {
        "name": "Subsides.csv",
        "path": "/cleaned_final/Subsides.csv",
        "type": "Subsides",
        "message": "💰 Tous les subsides, bien ordonnés"
    },
    {
        "name": "agency_payroll_cleaned_final.csv",
        "path": "/cleaned_final/agency_payroll_cleaned_final.csv",
        "type": "Paie",
        "message": "💼 Paie agence - Tout est carré !"
    },
    {
        "name": "costs_cleaned_final.csv",
        "path": "/cleaned_final/costs_cleaned_final.csv",
        "type": "Coûts",
        "message": "📉 Analyse des coûts optimisée"
    },
    {
        "name": "franchise_payroll_cleaned_final.csv",
        "path": "/cleaned_final/franchise_payroll_cleaned_final.csv",
        "type": "Franchise",
        "message": "🤝 Paie franchise - Nickel chrome !"
    },
    {
        "name": "material_pricing_cleaned_final.csv",
        "path": "/cleaned_final/material_pricing_cleaned_final.csv",
        "type": "Prix",
        "message": "🏷️ Prix matériaux actualisés"
    },
    {
        "name": "services_cleaned_final.csv",
        "path": "/cleaned_final/services_cleaned_final.csv",
        "type": "Services",
        "message": "🛠️ Services alignés et vérifiés"
    },
    {
        "name": "tax_credit_with_APE.csv",
        "path": "/cleaned_final/tax_credit_with_APE.csv",
        "type": "Fiscal",
        "message": "✨ Crédits d'impôt avec codes APE"
    }
]

# Configuration des messages et sections spéciales
SPECIAL_SECTIONS = {
    "disclaimer_title": "LEX | LIBERTAS | CIVIS",
    "disclaimer_text": "Notre engagement envers la transparence et l'intérêt public guide chacune de nos actions. Bien que notre plateforme traite des données variables en constante évolution, notre mission demeure immuable : servir la communauté avec intégrité et précision.",
    "disclaimer_text_2": "Ce projet, porté par des valeurs communautaires fortes et un engagement envers l'intérêt public, représente plus qu'une simple analyse de données. Il incarne notre vision d'une société où la technologie sert le bien commun.",
    "disclaimer_motto": "En perpétuel mouvement, mais ancrés dans nos valeurs.",
    "mai_expert_message": "Données nettoyées et structurées selon vos besoins. Les codes APE sont vérifiés et les calculs automatisés sont prêts pour l'analyse fiscale !",
    "doug_message": "La compta est plus propre qu'un sou neuf ! Tous les fichiers sont harmonisés et les subsides sont tracés jusqu'au centime. Le rapport de subvention est disponible en PDF. Bonne analyse !"
}

# Configuration des liens externes
EXTERNAL_LINKS = {
    "pdf_report": "https://acrobat.adobe.com/id/urn:aaid:sc:eu:0f7beab6-c206-42c3-a9b5-b2488c7a2067",
    "pdf_title": "Rapport de Subvention 2024",
    "pdf_desc": "📑 Document officiel des subventions accordées"
}
