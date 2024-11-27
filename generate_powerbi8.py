def get_subsidies_analysis_insights(self) -> str:
    """Generate comprehensive subsidies analysis with enhanced metrics and visualizations."""
    return """
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
                    <span class="trend-indicator" style="color: green">↑ +10%</span>
                </div>
            </div>

            <div class="metric-card">
                <div class="metric-header">
                    <i class="fas fa-thumbs-up"></i>
                    <h3>Application Success Rate</h3>
                </div>
                <div class="metric-value">75%</div>
                <div class="metric-trend">
                    <span class="trend-indicator" style="color: green">↑ +5%</span>
                </div>
            </div>

            <div class="metric-card">
                <div class="metric-header">
                    <i class="fas fa-clock"></i>
                    <h3>Funding Timeline</h3>
                </div>
                <div class="metric-value">3-12 months</div>
                <div class="metric-trend">
                    <span class="trend-indicator" style="color: red">↓ -1 month</span>
                </div>
            </div>
        </div>

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
                <iframe src="html_viz/subsidies_heatmap_Code APE_Source Principale.html" style="width:100%; height:800px; border:none;"></iframe>
            </div>

            <h2>2. Crédits d'Impôt Stratégiques</h2>
            <ul>
                <li>CIR (Crédit Impôt Recherche) : <span class="amount">79 500€</span></li>
                <li>CII (Crédit Impôt Innovation) : <span class="amount">82 072€</span></li>
                <li class="hard">Attention : Délai long (12 mois) mais montants significatifs</li>
            </ul>

            <h2>3. Répartition par Secteur</h2>
            <div class="visual-content">
                <h4>Alternatives de Subventions</h4>
                <iframe src="html_viz/subsidies_heatmap_Délai_Alternative 1.html" style="width:100%; height:800px; border:none;"></iframe>
                <iframe src="html_viz/subsidies_heatmap_Délai_Alternative 2.html" style="width:100%; height:800px; border:none;"></iframe>
            </div>

            <h3>Multimédia et Tech (62.01Z)</h3>
            <ul>
                <li>Transformation Numérique Équipements : <span class="amount">50 000€</span> <span class="easy">(Facile)</span></li>
                <li>Aide au Développement d'Applications : <span class="amount">100 000€</span></li>
                <li>Subvention i-Lab : <span class="amount">600 000€</span> <span class="hard">(Très Difficile)</span></li>
            </ul>

            <h3>Production et Divertissement (59.11B)</h3>
            <ul>
                <li>Aide à la Création de Jeux Vidéo : <span class="amount">200 000€</span></li>
                <li>Fonds de Soutien Innovation : <span class="amount">50 000€</span></li>
                <li>Aide Création Contenus Numériques : <span class="amount">90 000€</span></li>
            </ul>

            <h2>4. Opportunités "Quick Wins"</h2>
            <div class="highlight">
                <p class="opportunity">Subventions faciles à obtenir :</p>
                <ul>
                    <li>Pass PI INPI : <span class="amount">5 000€</span> (1 mois)</li>
                    <li>OPCO Formation : <span class="amount">15 000€</span> (1 mois)</li>
                    <li>Aide Unique Apprentissage : <span class="amount">30 000€</span> (1 mois)</li>
                </ul>
            </div>

            <div class="visual-content">
                <h4>Répartition des Financements</h4>
                <iframe src="html_viz/funding_treemap.html" style="width:100%; height:800px; border:none;"></iframe>
            </div>

            <h2>5. Stratégie de Financement Recommandée</h2>
            <ol>
                <li><strong>Court terme (0-3 mois)</strong>
                    <ul>
                        <li>Activer JEI immédiatement : <span class="amount">246 807€</span> potentiels</li>
                        <li>Démarrer OPCO et Pass PI : <span class="amount">20 000€</span> rapides</li>
                    </ul>
                </li>
                <li><strong>Moyen terme (3-6 mois)</strong>
                    <ul>
                        <li>Monter dossiers BPI : <span class="amount">40 000€</span> à <span class="amount">100 000€</span></li>
                        <li>Préparer CIR/CII : <span class="amount">161 572€</span> combinés</li>
                    </ul>
                </li>
                <li><strong>Long terme (6-12 mois)</strong>
                    <ul>
                        <li>Programmes européens : <span class="amount">60 000€</span> à <span class="amount">80 000€</span></li>
                        <li>Fonds sectoriels CNC : <span class="amount">200 000€</span> potentiels</li>
                    </ul>
                </li>
            </ol>

            <h2>6. Points d'Attention</h2>
            <ul>
                <li class="medium">Cumul possible de la plupart des aides</li>
                <li class="medium">Plafonnements à respecter (notamment JEI)</li>
                <li class="hard">Anticiper les délais longs pour les gros montants</li>
                <li class="easy">Privilégier d'abord les aides "faciles"</li>
            </ul>

            <h2>7. Conclusion</h2>
            <p>
                Le potentiel total de subventions accessibles dépasse <span class="amount">1 million d'euros</span>. 
                Une approche structurée, commençant par les dispositifs les plus simples tout en préparant les dossiers plus complexes, 
                permettra d'optimiser les chances d'obtention et de maximiser les montants perçus.
            </p>
        </div>
    </div>
    """
