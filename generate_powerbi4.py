#!/usr/bin/env python3

def generate_subsidies_and_roadmap_content():
    subsidies_roadmap_content = '''
        <div class="page-container" id="subsidies_analysis.html">
            <div class="analytics-card">
                <h2>Subsidies Analysis</h2>
                <p>Analysis of Available Subsidies and Grants</p>
                <div class="metric-container">
                    <div class="metric-card">
                        <div class="metric-header">
                            <i class="fas fa-hand-holding-usd"></i>
                            <h3>Subsidy Potential</h3>
                        </div>
                        <div class="metric-value">€1M+</div>
                        <div class="metric-trend">
                            <span class="trend-indicator" style="color: green">
                                ↑ +10%
                            </span>
                        </div>
                    </div>

                    <div class="metric-card">
                        <div class="metric-header">
                            <i class="fas fa-thumbs-up"></i>
                            <h3>Application Success Rate</h3>
                        </div>
                        <div class="metric-value">75%</div>
                        <div class="metric-trend">
                            <span class="trend-indicator" style="color: green">
                                ↑ +5%
                            </span>
                        </div>
                    </div>

                    <div class="metric-card">
                        <div class="metric-header">
                            <i class="fas fa-clock"></i>
                            <h3>Funding Timeline</h3>
                        </div>
                        <div class="metric-value">3-12 months</div>
                        <div class="metric-trend">
                            <span class="trend-indicator" style="color: red">
                                ↓ -1 month
                            </span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="analytics-card">
                <div class="section">
                    <h1>Analyse des Subventions et Aides Disponibles</h1>

                    <h2>1. Dispositifs Majeurs Immédiats</h2>
                    <div class="highlight">
                        <h3>Statut JEI (Jeune Entreprise Innovante)</h3>
                        <ul>
                            <li>Exonération sociale : <span class="amount">181 388€</span></li>
                            <li>Exonération fiscale : <span class="amount">53 419€</span></li>
                            <li>Exonération CFE/CVAE : <span class="amount">12 000€</span></li>
                            <li class="easy">Difficulté : Moyenne | Délai : 3 mois</li>
                        </ul>
                    </div>

                    <div class="visual-content">
                        <h4>Subventions Principales</h4>
                        <iframe src="subsidies_heatmap_Code APE_Source Principale.html" style="width:100%; height:800px; border:none;"></iframe>
                    </div>
                </div>
            </div>
        </div>

        <div class="page-container" id="roadmap.html">
            <div class="analytics-card">
                <h2>Geographic Roadmap</h2>
                <p>Development Roadmap and Expansion Plans</p>
                <div class="metric-container">
                    <div class="metric-card">
                        <div class="metric-header">
                            <i class="fas fa-project-diagram"></i>
                            <h3>Expansion Phases</h3>
                        </div>
                        <div class="metric-value">3 Phases</div>
                        <div class="metric-trend">
                            <span class="trend-indicator" style="color: green">
                                ↑ On Track
                            </span>
                        </div>
                    </div>

                    <div class="metric-card">
                        <div class="metric-header">
                            <i class="fas fa-chart-pie"></i>
                            <h3>Market Potential</h3>
                        </div>
                        <div class="metric-value">€3B</div>
                        <div class="metric-trend">
                            <span class="trend-indicator" style="color: green">
                                ↑ +15%
                            </span>
                        </div>
                    </div>

                    <div class="metric-card">
                        <div class="metric-header">
                            <i class="fas fa-chart-line"></i>
                            <h3>Roi Expectations</h3>
                        </div>
                        <div class="metric-value">60%</div>
                        <div class="metric-trend">
                            <span class="trend-indicator" style="color: green">
                                ↑ +10%
                            </span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="analytics-card">
                <div class="visual-content">
                    <h4>Geographic Distribution Strategy 2024-2026</h4>
                    <iframe src="roadmap.html" style="width:100%; height:800px; border:none;"></iframe>
                </div>
            </div>
        </div>
'''

    # Ajout du contenu au fichier existant
    with open('PowerBI.html', 'a', encoding='utf-8') as f:
        f.write(subsidies_roadmap_content)

    print("Sections Subsidies Analysis et Geographic Roadmap ajoutées avec succès!")

if __name__ == "__main__":
    generate_subsidies_and_roadmap_content()
