#!/usr/bin/env python3

def generate_cost_and_subsidies_content():
    cost_subsidies_content = '''
        <div class="page-container" id="cost_analysis.html">
            <div class="analytics-card">
                <h2>Cost Analysis</h2>
                <p>Financial Flux and Cost Hierarchy Analysis</p>
                <div class="metric-container">
                    <div class="metric-card">
                        <div class="metric-header">
                            <i class="fas fa-money-bill-wave"></i>
                            <h3>Cost Efficiency</h3>
                        </div>
                        <div class="metric-value">88%</div>
                        <div class="metric-trend">
                            <span class="trend-indicator" style="color: green">
                                ↑ +3%
                            </span>
                        </div>
                    </div>

                    <div class="metric-card">
                        <div class="metric-header">
                            <i class="fas fa-chart-area"></i>
                            <h3>Expense Trends</h3>
                        </div>
                        <div class="metric-value">+5%</div>
                        <div class="metric-trend">
                            <span class="trend-indicator" style="color: red">
                                ↓ -1%
                            </span>
                        </div>
                    </div>

                    <div class="metric-card">
                        <div class="metric-header">
                            <i class="fas fa-piggy-bank"></i>
                            <h3>Investment Returns</h3>
                        </div>
                        <div class="metric-value">12%</div>
                        <div class="metric-trend">
                            <span class="trend-indicator" style="color: green">
                                ↑ +2%
                            </span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="analytics-card">
                <h3>Prévision de la Structure Financière</h3>
                
                <div class="section">
                    <h4>Structure Prévisionnelle des Coûts</h4>
                    <ul>
                        <li>Coûts Fixes: <span class="data-highlight">45%</span></li>
                        <li>Coûts Variables: <span class="data-highlight">35%</span></li>
                        <li>Investissements R&D: <span class="data-highlight">20%</span></li>
                    </ul>
                </div>

                <div class="visual-content">
                    <h4>Projection des Flux Financiers</h4>
                    <iframe src="flux_financiers_enhanced.html" style="width:100%; height:800px; border:none;"></iframe>
                </div>

                <div class="analysis-section">
                    <h1>Prévisions et Points Forts - Novembre 2024</h1>

                    <h2>🌟 Points Positifs Anticipés</h2>
                    
                    <h3>1. Nos Avantages Fiscaux Projetés</h3>
                    <ul>
                        <li class="positive-point">Le statut JEI nous apportera 20 000€ d'économies sur les charges sociales</li>
                        <li class="positive-point">Nous bénéficierons d'allègements sociaux générant environ 4 700€ d'économies</li>
                        <li class="positive-point">Les exonérations apprentissage nous feront gagner 3 333€</li>
                    </ul>

                    <h3>2. Nos Investissements Planifiés</h3>
                    <ul>
                        <li class="positive-point">Notre équipement professionnel inclura le DJI Ronin 4D-8K</li>
                        <li class="positive-point">L'infrastructure tech sera basée sur Apple Silicon</li>
                        <li class="positive-point">Le matériel sera éligible aux amortissements accélérés</li>
                    </ul>

                    <h3>3. Notre Gestion Financière Prévisionnelle</h3>
                    <ul>
                        <li class="positive-point">Nous récupérerons la TVA sur la majorité des investissements</li>
                        <li class="positive-point">Les modes de paiement seront diversifiés</li>
                        <li class="positive-point">Le suivi par centres de coûts sera précis</li>
                    </ul>
                </div>

                <div class="visual-content">
                    <h4>Projection de la Répartition des Coûts</h4>
                    <iframe src="cost_hierarchy.html" style="width:100%; height:800px; border:none;"></iframe>
                </div>

                <div class="highlight">
                    <h4>Axes d'Optimisation Prévus</h4>
                    <ul>
                        <li>Automatisation: nous réduirons de <span class="amount">15% les coûts opérationnels</span></li>
                        <li>Économies d'échelle: nous atteindrons <span class="amount">+25% d'efficacité</span></li>
                    </ul>
                </div>

                <!-- Suite du contenu de l'analyse des coûts -->
            </div>
        </div>
'''

    # Ajout du contenu au fichier existant
    with open('PowerBI.html', 'a', encoding='utf-8') as f:
        f.write(cost_subsidies_content)

    print("Sections Cost Analysis ajoutée avec succès!")

if __name__ == "__main__":
    generate_cost_and_subsidies_content()
