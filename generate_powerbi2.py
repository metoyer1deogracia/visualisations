#!/usr/bin/env python3

def generate_service_architecture_content():
    # Cette fonction va ajouter le contenu à PowerBI.html
    service_content = '''
    <div class="content">
        <div class="page-container" id="service_hierarchy.html">
            <div class="analytics-card">
                <h2>Service Architecture</h2>
                <p>Service Hierarchy and Dependencies</p>
                <div class="metric-container">
                    <div class="metric-card">
                        <div class="metric-header">
                            <i class="fas fa-layer-group"></i>
                            <h3>Pricing Tiers</h3>
                        </div>
                        <div class="metric-value">3 Tiers</div>
                        <div class="metric-trend">
                            <span class="trend-indicator" style="color: green">
                                ↑ +5%
                            </span>
                        </div>
                        <div class="metric-source">Source : <a href="https://www.marketingprofs.com" target="_blank">MarketingProfs</a></div>
                    </div>

                    <div class="metric-card">
                        <div class="metric-header">
                            <i class="fas fa-calendar-alt"></i>
                            <h3>Seasonal Variation</h3>
                        </div>
                        <div class="metric-value">+45%</div>
                        <div class="metric-trend">
                            <span class="trend-indicator" style="color: green">
                                ↑ +12%
                            </span>
                        </div>
                        <div class="metric-source">Source : <a href="https://www.statista.com" target="_blank">Statista</a></div>
                    </div>

                    <div class="metric-card">
                        <div class="metric-header">
                            <i class="fas fa-users"></i>
                            <h3>Customer Segments</h3>
                        </div>
                        <div class="metric-value">5 Segments</div>
                        <div class="metric-trend">
                            <span class="trend-indicator" style="color: green">
                                ↑ +8%
                            </span>
                        </div>
                        <div class="metric-source">Source : <a href="https://www.nielsen.com" target="_blank">Nielsen</a></div>
                    </div>
                </div>
            </div>
            
            <div class="analytics-card">
                <h3>Analyse Architecturale des Services</h3>
                
                <p>Analyse multi-niveaux des services avec impact tarifaire saisonnier</p>
                
                <div class="section">
                    <h4>Structure Actuelle</h4>
                    <ul>
                        <li>Services Core: <span class="data-highlight">8 services</span></li>
                        <li>Services Premium: <span class="data-highlight">12 services</span></li>
                        <li>Services Enterprise: <span class="data-highlight">5 services</span></li>
                    </ul>
                </div>

                <div class="tech-stack">
                    <strong>Métriques Clés:</strong>
                    <ul>
                        <li>Élasticité des prix par niveau</li>
                        <li>Modèles de demande saisonnière</li>
                        <li>Dépendances inter-services</li>
                    </ul>
                </div>

                <div class="visual-content">
                    <h4>Hiérarchie des Services</h4>
                    <iframe src="service_hierarchy.html" 
                            style="width:100%; height:1200px; border:none;">
                    </iframe>
                </div>

                <div class="section">
                    <h4>Performances</h4>
                    <ul>
                        <li>Taux d'adoption: <span class="data-highlight">78%</span></li>
                        <li>Satisfaction client: <span class="data-highlight">92%</span></li>
                        <li>Taux de rétention: <span class="data-highlight">85%</span></li>
                    </ul>
                </div>
            </div>

            <div class="visual-content">
                <iframe src="service_hierarchy.html" style="width:100%; height:600px; border:none; border-radius:8px;"></iframe>
            </div>
        </div>
'''

    # On ajoute le contenu au fichier existant
    with open('PowerBI.html', 'a', encoding='utf-8') as f:
        f.write(service_content)

    print("Section Service Architecture ajoutée avec succès!")

if __name__ == "__main__":
    generate_service_architecture_content()
