#!/usr/bin/env python3

def update_roadmap_section():
    # Contenu de la nouvelle section roadmap
    roadmap_content = '''
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
                        <h3>ROI Expectations</h3>
                    </div>
                    <div class="metric-value">60%</div>
                    <div class="metric-trend">
                        <span class="trend-indicator" style="color: green">
                            ↑ +10%
                        </span>
                    </div>
                </div>
            </div>

            <div class="roadmap-section">
                <h1>Geographic Distribution Strategy 2024-2026</h1>
                
                <div class="phase flagship">
                    <h2>Phase 1: Flagship Locations (2024)</h2>
                    <div class="grid-container">
                        <div class="grid-item">
                            <h3>Paris</h3>
                            <p class="highlight">Hub Principal</p>
                            <ul>
                                <li>Studio Production Principale</li>
                                <li>Centre R&D</li>
                                <li>Équipe Tech Core</li>
                                <p class="metric">Potentiel marché: 500M€</p>
                            </ul>
                        </div>
                        <div class="grid-item">
                            <h3>La Rochelle</h3>
                            <p class="highlight">Innovation Hub</p>
                            <ul>
                                <li>Studio Créatif</li>
                                <li>Centre Formation</li>
                                <li>Lab Digital</li>
                                <p class="metric">Potentiel marché: 150M€</p>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="phase innovation-hub">
                    <h2>Phase 2: Market Expansion (2025)</h2>
                    <div class="grid-container">
                        <div class="grid-item">
                            <h3>Lyon</h3>
                            <p class="highlight">Hub Régional Sud-Est</p>
                            <ul>
                                <li>Studio Production Secondaire</li>
                                <li>Centre Events</li>
                                <li>Base Tech</li>
                                <p class="metric">Potentiel marché: 250M€</p>
                            </ul>
                        </div>
                        <div class="grid-item">
                            <h3>Bordeaux</h3>
                            <p class="highlight">Hub Digital</p>
                            <ul>
                                <li>Studio Gaming</li>
                                <li>Centre AR/VR</li>
                                <li>Lab Innovation</li>
                                <p class="metric">Potentiel marché: 200M€</p>
                            </ul>
                        </div>
                        <div class="grid-item">
                            <h3>Nantes</h3>
                            <p class="highlight">Tech Hub</p>
                            <ul>
                                <li>Centre Dev</li>
                                <li>Studio Design</li>
                                <li>Base Formation</li>
                                <p class="metric">Potentiel marché: 180M€</p>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="phase">
                    <h2>Phase 3: International Expansion (2026)</h2>
                    <div class="grid-container">
                        <div class="grid-item">
                            <h3>Londres</h3>
                            <p class="highlight">Hub International</p>
                            <ul>
                                <li>Studio Production UK</li>
                                <li>Centre Business</li>
                                <li>Base Tech Europe</li>
                                <p class="metric">Potentiel marché: 800M€</p>
                            </ul>
                        </div>
                        <div class="grid-item">
                            <h3>Berlin</h3>
                            <p class="highlight">Tech Hub Europe</p>
                            <ul>
                                <li>Centre R&D Europe</li>
                                <li>Studio Innovation</li>
                                <li>Base Formation EU</li>
                                <p class="metric">Potentiel marché: 600M€</p>
                            </ul>
                        </div>
                        <div class="grid-item">
                            <h3>Amsterdam</h3>
                            <p class="highlight">Creative Hub</p>
                            <ul>
                                <li>Studio Digital</li>
                                <li>Centre Gaming</li>
                                <li>Lab Métavers</li>
                                <p class="metric">Potentiel marché: 400M€</p>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>'''

    try:
        # Lire le contenu actuel du fichier
        with open('PowerBI.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # Trouver et remplacer la section roadmap
        start_marker = '<div class="page-container" id="roadmap.html">'
        end_marker = '</div>\n</div>'
        start_index = content.find(start_marker)
        if start_index != -1:
            # Trouver la fin de la section
            end_index = content.find(end_marker, start_index) + len(end_marker)
            # Remplacer l'ancienne section par la nouvelle
            new_content = content[:start_index] + roadmap_content + content[end_index:]
            
            # Écrire le contenu mis à jour
            with open('PowerBI.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print("La section Geographic Roadmap a été mise à jour avec succès!")
        else:
            print("Section roadmap non trouvée dans le fichier.")
    except Exception as e:
        print(f"Une erreur est survenue: {str(e)}")

if __name__ == "__main__":
    update_roadmap_section()
