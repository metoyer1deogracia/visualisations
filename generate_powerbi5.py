#!/usr/bin/env python3

def generate_final_content():
    final_content = '''
            <div class="page-container" id="terms_and_conditions">
                <div class="analytics-card">
                    <h2>Conditions Générales de Vente</h2>
                    <p>Intégrant les aspects fiscaux conformément aux dispositions légales en vigueur.</p>
                    <div class="section">
                        <h3>Prestations et Plateforme</h3>
                        <p>
                            Nos services et notre plateforme offrent des avantages stratégiques pour votre entreprise. 
                            Les dépenses liées à nos prestations peuvent être considérées comme des investissements.
                        </p>
                        <h3>Traitement Fiscal</h3>
                        <ul>
                            <li>
                                <strong>Charges Déductibles :</strong> Conformément à l'article 39, alinéa 1 du Code Général des Impôts (CGI), les dépenses engagées dans l'intérêt de l'exploitation sont déductibles du résultat imposable.
                            </li>
                            <li>
                                <strong>Actifs Immobilisés :</strong> La plateforme et les logiciels fournis peuvent être inscrits à l'actif du bilan en tant qu'immobilisations incorporelles, selon l'article 38 quinquies de l'annexe III et l'article 52 de l'annexe II du CGI.
                            </li>
                            <li>
                                <strong>Amortissement :</strong> Ces actifs peuvent faire l'objet d'un amortissement sur plusieurs années, réduisant ainsi l'assiette de l'impôt futur tout en enrichissant le patrimoine de l'entreprise.
                            </li>
                        </ul>
                        <h3>Protection Intellectuelle</h3>
                        <p>
                            Les logiciels et plateformes SaaS fournis sont protégés par l'article L112-2 du Code de la Propriété Intellectuelle en tant qu'œuvres de l'esprit.
                        </p>
                        <h3>Conditions d'Utilisation</h3>
                        <p>
                            La licence d'accès à la plateforme est incluse dans nos prestations, avec une tarification modulable en fonction des besoins spécifiques.
                        </p>
                        <h3>Sources des Données</h3>
                        <p>
                            Les informations présentées dans ce document sont basées sur des données provenant de sources fiables :
                        </p>
                        <ul>
                            <li>
                                <a href="https://www.gartner.com/en/research" target="_blank">Rapports Gartner</a>
                            </li>
                            <li>
                                <a href="https://www.insee.fr/fr/statistiques" target="_blank">Statistiques INSEE</a>
                            </li>
                            <li>
                                <a href="https://www.data.gouv.fr" target="_blank">Data.gouv.fr</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <script>
            function showPage(pageId, btn) {
                document.querySelectorAll('.page-container').forEach(page => {
                    page.classList.remove('active');
                });
                
                document.querySelectorAll('.nav-button').forEach(button => {
                    button.classList.remove('active');
                });
                
                document.getElementById(pageId).classList.add('active');
                btn.classList.add('active');

                trackPageView(btn.textContent);
            }
            
            document.addEventListener('DOMContentLoaded', function() {
                const firstButton = document.querySelector('.nav-button');
                const firstPage = document.querySelector('.page-container');
                if (firstButton && firstPage) {
                    firstButton.classList.add('active');
                    firstPage.classList.add('active');
                }
            });
            
            function trackPageView(pageName) {
                console.log(`Page viewed: ${pageName}`);
                // Add real analytics tracking here
            }
        </script>
    </body>
</html>'''

    # Ajout du contenu final au fichier existant
    with open('PowerBI.html', 'a', encoding='utf-8') as f:
        f.write(final_content)

    print("Contenu final ajouté avec succès! Le fichier PowerBI.html est maintenant complet.")

if __name__ == "__main__":
    generate_final_content()
