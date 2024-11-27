#!/usr/bin/env python3

class SubsidiesAnalysis:
    def get_subsidies_analysis_insights(self) -> str:
        """Generate comprehensive subsidies analysis formatted to match document structure."""
        return """
        ::::::::::::::::::::: {#subsidies_analysis.html .page-container}
        :::::::::::::::: analytics-card
        ## Subsidies Analysis

        Analysis of Available Subsidies and Grants

        ::::::::::::::: metric-container
        :::::: metric-card
        ::: metric-header
        ### Subsidy Potential
        :::
        ::: metric-value
        €1M+
        :::
        ::: metric-trend
        [ ↑ +10% ]{.trend-indicator style="color: green"}
        :::
        ::::::

        :::::: metric-card
        ::: metric-header
        ### Application Success Rate
        :::
        ::: metric-value
        75%
        :::
        ::: metric-trend
        [ ↑ +5% ]{.trend-indicator style="color: green"}
        :::
        ::::::

        :::::: metric-card
        ::: metric-header
        ### Funding Timeline
        :::
        ::: metric-value
        3-12 months
        :::
        ::: metric-trend
        [ ↓ -1 month ]{.trend-indicator style="color: red"}
        :::
        ::::::
        :::::::::::::::
        ::::::::::::::::

        :::::: analytics-card
        ::::: section
        # Analyse des Subventions et Aides Disponibles

        ## 1. Dispositifs Majeurs Immédiats
        ::: highlight
        ### Statut JEI (Jeune Entreprise Innovante)
        - Exonération sociale : [181 388€]{.amount}
        - Exonération fiscale : [53 419€]{.amount}
        - Exonération CFE/CVAE : [12 000€]{.amount}
        - Difficulté : Moyenne | Délai : 3 mois
        :::

        ::: visual-content
        #### Subventions Principales
        <iframe src="html_viz/subsidies_heatmap_Code APE_Source Principale.html" style="width:100%; height:800px; border:none;"></iframe>
        :::

        ## 2. Crédits d'Impôt Stratégiques
        - CIR (Crédit Impôt Recherche) : [79 500€]{.amount}
        - CII (Crédit Impôt Innovation) : [82 072€]{.amount}
        - [Attention : Délai long (12 mois) mais montants significatifs]{.hard}

        ## 3. Répartition par Secteur
        ::: visual-content
        #### Analyse des Délais de Financement
        <iframe src="html_viz/subsidies_heatmap_Délai_Alternative 1.html" style="width:100%; height:800px; border:none;"></iframe>
        <iframe src="html_viz/subsidies_heatmap_Délai_Alternative 2.html" style="width:100%; height:800px; border:none;"></iframe>
        :::

        ### Multimédia et Tech (62.01Z)
        - Transformation Numérique Équipements : [50 000€]{.amount} [Facile]{.easy}
        - Aide au Développement d'Applications : [100 000€]{.amount}
        - Subvention i-Lab : [600 000€]{.amount} [Très Difficile]{.hard}

        ### Production et Divertissement (59.11B)
        - Aide à la Création de Jeux Vidéo : [200 000€]{.amount}
        - Fonds de Soutien Innovation : [50 000€]{.amount}
        - Aide Création Contenus Numériques : [90 000€]{.amount}

        ## 4. Opportunités "Quick Wins"
        ::: highlight
        **Subventions faciles à obtenir :**
        - Pass PI INPI : [5 000€]{.amount} (1 mois)
        - OPCO Formation : [15 000€]{.amount} (1 mois)
        - Aide Unique Apprentissage : [30 000€]{.amount} (1 mois)
        :::

        ::: visual-content
        #### Répartition des Financements
        <iframe src="html_viz/funding_treemap.html" style="width:100%; height:800px; border:none;"></iframe>
        :::

        ## 5. Stratégie de Financement Recommandée
        ### Court terme (0-3 mois)
        - Activer JEI immédiatement : [246 807€]{.amount} potentiels
        - Démarrer OPCO et Pass PI : [20 000€]{.amount} rapides

        ### Moyen terme (3-6 mois)
        - Monter dossiers BPI : [40 000€ à 100 000€]{.amount}
        - Préparer CIR/CII : [161 572€]{.amount} combinés

        ### Long terme (6-12 mois)
        - Programmes européens : [60 000€ à 80 000€]{.amount}
        - Fonds sectoriels CNC : [200 000€]{.amount} potentiels

        ## 6. Points d'Attention
        - [Cumul possible de la plupart des aides]{.medium}
        - [Plafonnements à respecter (notamment JEI)]{.medium}
        - [Anticiper les délais longs pour les gros montants]{.hard}
        - [Privilégier d'abord les aides "faciles"]{.easy}

        ## 7. Conclusion
        Le potentiel total de subventions accessibles dépasse [1 million d'euros]{.amount}. Une approche structurée, commençant par les dispositifs les plus simples tout en préparant les dossiers plus complexes, permettra d'optimiser les chances d'obtention et de maximiser les montants perçus.
        :::::
        ::::::
        :::::::::::::::::::::
        """

    def find_section_markers(self, content: str) -> tuple:
        """Find the appropriate section markers in the content."""
        markers = [
            ('::::::::::::::::::::: {#subsidies_analysis.html .page-container}', ':::::::::::::::::::::'),
            ('## Subsidies Analysis', '::::::::::::::::::::::::::'),
            ('Subsidies Analysis', '::::::::::::::::::::')
        ]
        
        for start_marker, end_marker in markers:
            start_index = content.find(start_marker)
            if start_index != -1:
                # Find the section start
                section_start = content.rfind(':::::::::::::::::::::', 0, start_index)
                # Find the section end
                section_end = content.find(end_marker, start_index)
                
                if section_start != -1 and section_end != -1:
                    return section_start, section_end + len(end_marker)
        
        return -1, -1

    def find_insertion_point(self, content: str) -> int:
        """Find appropriate insertion point for new content."""
        # Look for the last major section before the document end
        insertion_markers = [
            ':::::::::::::::::::::::::::::::::::::::::::::::',
            '::::::::::::::::::::::::::::::::::::::::::::::',
            '::::::::::::::::::::::::::::::::::::::::::::::'
        ]
        
        for marker in insertion_markers:
            pos = content.rfind(marker)
            if pos != -1:
                return pos

        return -1

    def update_powerbi_file(self):
        """Update the PowerBI.html file with the subsidies analysis content."""
        try:
            # Read current content
            with open('PowerBI.html', 'r', encoding='utf-8') as f:
                content = f.read()

            # Find section boundaries
            start_index, end_index = self.find_section_markers(content)

            if start_index != -1 and end_index != -1:
                # Replace existing section
                new_content = (
                    content[:start_index] + 
                    self.get_subsidies_analysis_insights() + 
                    content[end_index:]
                )
                print("Mise à jour de la section d'analyse des subventions existante...")
            else:
                # Insert new section
                insert_pos = self.find_insertion_point(content)
                if insert_pos != -1:
                    new_content = (
                        content[:insert_pos] + 
                        self.get_subsidies_analysis_insights() + 
                        content[insert_pos:]
                    )
                    print("Ajout d'une nouvelle section d'analyse des subventions...")
                else:
                    raise ValueError("Impossible de trouver un point d'insertion approprié dans le fichier")

            # Write updated content
            with open('PowerBI.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Opération terminée avec succès!")

        except Exception as e:
            print(f"Une erreur est survenue: {str(e)}")
            print("Veuillez vérifier la structure du fichier PowerBI.html")

if __name__ == "__main__":
    analysis = SubsidiesAnalysis()
    analysis.update_powerbi_file()
