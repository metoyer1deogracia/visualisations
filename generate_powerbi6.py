#!/usr/bin/env python3

class PowerBIPathCorrector:
    def __init__(self):
        self.viz_paths = {
            'service_hierarchy': 'html_viz/service_hierarchy.html',
            'cost_hierarchy': 'html_viz/cost_hierarchy.html',
            'flux_financiers': 'html_viz/flux_financiers_enhanced.html',
            'subsidies_main': 'html_viz/subsidies_heatmap_Code APE_Source Principale.html',
            'subsidies_alt1': 'html_viz/subsidies_heatmap_Délai_Alternative 1.html',
            'subsidies_alt2': 'html_viz/subsidies_heatmap_Délai_Alternative 2.html',
            'roadmap': 'html_viz/roadmap.html',
            'funding_treemap': 'html_viz/funding_treemap.html'
        }

    def update_powerbi_file(self):
        try:
            with open('PowerBI.html', 'r', encoding='utf-8') as f:
                content = f.read()

            # Correction des chemins
            for old_path, new_path in [
                ('src="service_hierarchy.html"', f'src="{self.viz_paths["service_hierarchy"]}"'),
                ('src="cost_hierarchy.html"', f'src="{self.viz_paths["cost_hierarchy"]}"'),
                ('src="flux_financiers_enhanced.html"', f'src="{self.viz_paths["flux_financiers"]}"'),
                ('src="subsidies_heatmap_Code APE_Source Principale.html"', f'src="{self.viz_paths["subsidies_main"]}"'),
                ('src="subsidies_heatmap_Délai_Alternative 1.html"', f'src="{self.viz_paths["subsidies_alt1"]}"'),
                ('src="subsidies_heatmap_Délai_Alternative 2.html"', f'src="{self.viz_paths["subsidies_alt2"]}"'),
                ('src="roadmap.html"', f'src="{self.viz_paths["roadmap"]}"'),
                ('src="funding_treemap.html"', f'src="{self.viz_paths["funding_treemap"]}"')
            ]:
                content = content.replace(old_path, new_path)

            # Sauvegarde du fichier mis à jour
            with open('PowerBI.html', 'w', encoding='utf-8') as f:
                f.write(content)

            print("Les chemins ont été corrigés avec succès dans PowerBI.html!")
            print("\nChemins mis à jour :")
            for viz_type, path in self.viz_paths.items():
                print(f"- {viz_type}: {path}")

        except FileNotFoundError:
            print("Erreur: PowerBI.html n'a pas été trouvé.")
        except Exception as e:
            print(f"Une erreur est survenue: {str(e)}")

if __name__ == "__main__":
    corrector = PowerBIPathCorrector()
    corrector.update_powerbi_file()
