#!/usr/bin/env python3
"""Generate translated articles for PlantFinder"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Article translations
ARTICLES = {
    "beginner-houseplants": {
        "en": {
            "title": "Best Houseplants for Beginners",
            "desc": "Easy-to-grow houseplants perfect for beginners",
            "emoji": "🌱",
            "short": "10 forgiving plants for new plant parents"
        },
        "es": {
            "title": "Mejores Plantas de Interior para Principiantes",
            "desc": "Plantas de interior fáciles de cultivar perfectas para principiantes",
            "emoji": "🌱",
            "short": "10 plantas tolerantes para nuevos padres de plantas"
        },
        "de": {
            "title": "Beste Zimmerpflanzen für Anfänger",
            "desc": "Pflegeleichte Zimmerpflanzen perfekt für Anfänger",
            "emoji": "🌱",
            "short": "10 pflegeleichte Pflanzen für Einsteiger"
        }
    },
    "best-low-light-plants": {
        "en": {
            "title": "Best Low Light Houseplants",
            "desc": "Houseplants that thrive in low light conditions",
            "emoji": "🌑",
            "short": "15 plants for dark corners and offices"
        },
        "es": {
            "title": "Mejores Plantas para Poca Luz",
            "desc": "Plantas de interior que prosperan con poca luz",
            "emoji": "🌑",
            "short": "15 plantas para esquinas oscuras y oficinas"
        },
        "de": {
            "title": "Beste Zimmerpflanzen für wenig Licht",
            "desc": "Zimmerpflanzen die bei wenig Licht gedeihen",
            "emoji": "🌑",
            "short": "15 Pflanzen für dunkle Ecken und Büros"
        }
    },
    "pet-safe-plants": {
        "en": {
            "title": "Pet-Safe Houseplants",
            "desc": "Beautiful houseplants safe for cats and dogs",
            "emoji": "🐾",
            "short": "20 non-toxic plants for pet owners"
        },
        "es": {
            "title": "Plantas Seguras para Mascotas",
            "desc": "Hermosas plantas de interior seguras para gatos y perros",
            "emoji": "🐾",
            "short": "20 plantas no tóxicas para dueños de mascotas"
        },
        "de": {
            "title": "Haustierfreundliche Zimmerpflanzen",
            "desc": "Schöne Zimmerpflanzen sicher für Katzen und Hunde",
            "emoji": "🐾",
            "short": "20 ungiftige Pflanzen für Haustierbesitzer"
        }
    },
    "air-purifying-plants": {
        "en": {
            "title": "Best Air Purifying Plants",
            "desc": "Houseplants that clean and purify indoor air",
            "emoji": "🌬️",
            "short": "12 plants that improve air quality"
        },
        "es": {
            "title": "Mejores Plantas Purificadoras de Aire",
            "desc": "Plantas de interior que limpian y purifican el aire",
            "emoji": "🌬️",
            "short": "12 plantas que mejoran la calidad del aire"
        },
        "de": {
            "title": "Beste Luftreinigende Pflanzen",
            "desc": "Zimmerpflanzen die Luft reinigen und verbessern",
            "emoji": "🌬️",
            "short": "12 Pflanzen die Luftqualität verbessern"
        }
    },
    "watering-guide": {
        "en": {
            "title": "Complete Watering Guide",
            "desc": "How to water your houseplants correctly",
            "emoji": "💧",
            "short": "Never over or underwater again"
        },
        "es": {
            "title": "Guía Completa de Riego",
            "desc": "Cómo regar tus plantas de interior correctamente",
            "emoji": "💧",
            "short": "Nunca más riegues de más o de menos"
        },
        "de": {
            "title": "Kompletter Gieß-Ratgeber",
            "desc": "So gießen Sie Ihre Zimmerpflanzen richtig",
            "emoji": "💧",
            "short": "Nie wieder über- oder untergießen"
        }
    }
}

# Full article content translations
ARTICLE_CONTENT = {
    "beginner-houseplants": {
        "es": """
        <p>¿Nuevo en el mundo de las plantas? Estas variedades son tolerantes a los errores y prosperan con mínima atención. Perfectas para ganar confianza antes de pasar a plantas más desafiantes.</p>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Las Plantas "Inmortales" para Empezar</h2>
        <div class="space-y-4">
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/pothos-golden/" class="text-emerald-700 underline">1. Pothos</a></h3>
                <p class="text-slate-600">La planta definitiva para principiantes. Tolera poca luz, riego irregular, y te avisa cuando tiene sed al ponerse un poco caída. Crecimiento rápido y gratificante.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/snake-plant/" class="text-emerald-700 underline">2. Lengua de Suegra</a></h3>
                <p class="text-slate-600">Sobrevive semanas sin agua. Tolera cualquier nivel de luz. Prácticamente prospera con el descuido.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/zz-plant/" class="text-emerald-700 underline">3. Planta ZZ</a></h3>
                <p class="text-slate-600">Riega una vez al mes (sí, de verdad). Soporta poca luz. Las hojas brillantes siempre lucen bien.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/spider-plant/" class="text-emerald-700 underline">4. Planta Araña</a></h3>
                <p class="text-slate-600">Difícil de matar y produce hijuelos que puedes compartir. Excelente para ganar confianza.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/rubber-plant/" class="text-emerald-700 underline">5. Árbol del Caucho</a></h3>
                <p class="text-slate-600">Planta llamativa que es sorprendentemente fácil. Tolera algo de descuido.</p>
            </div>
        </div>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Consejos para Principiantes</h2>
        <ul class="list-disc pl-6 space-y-2 text-slate-600">
            <li><strong>Riega de menos en lugar de más</strong> - La mayoría de plantas mueren por exceso de riego</li>
            <li><strong>Revisa la tierra antes de regar</strong> - Mete el dedo 2cm; riega solo si está seco</li>
            <li><strong>Empieza con plantas de poca luz</strong> - Generalmente son más tolerantes</li>
            <li><strong>No trasplantes inmediatamente</strong> - Deja que las plantas nuevas se adapten primero</li>
            <li><strong>Aprende las necesidades de una planta antes de añadir más</strong></li>
        </ul>
        """,
        "de": """
        <p>Neu bei Zimmerpflanzen? Diese anfängerfreundlichen Sorten verzeihen Fehler und gedeihen mit minimaler Aufmerksamkeit. Perfekt um Vertrauen aufzubauen, bevor Sie sich an anspruchsvollere Pflanzen wagen.</p>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Die "Unkaputtbaren" Starter-Pflanzen</h2>
        <div class="space-y-4">
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/pothos-golden/" class="text-emerald-700 underline">1. Efeutute</a></h3>
                <p class="text-slate-600">Die ultimative Anfängerpflanze. Toleriert wenig Licht, unregelmäßiges Gießen und zeigt Durst durch leichtes Hängen. Schnellwachsend und belohnend.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/snake-plant/" class="text-emerald-700 underline">2. Bogenhanf</a></h3>
                <p class="text-slate-600">Überlebt Wochen ohne Wasser. Toleriert jede Lichtstärke. Gedeiht praktisch bei Vernachlässigung.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/zz-plant/" class="text-emerald-700 underline">3. Zamioculcas</a></h3>
                <p class="text-slate-600">Einmal im Monat gießen (ja, wirklich). Verträgt wenig Licht. Glänzende Blätter sehen immer gut aus.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/spider-plant/" class="text-emerald-700 underline">4. Grünlilie</a></h3>
                <p class="text-slate-600">Schwer zu töten und produziert Ableger zum Teilen. Toll um Vertrauen aufzubauen.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/rubber-plant/" class="text-emerald-700 underline">5. Gummibaum</a></h3>
                <p class="text-slate-600">Ausdrucksstarke Pflanze die überraschend einfach ist. Toleriert etwas Vernachlässigung.</p>
            </div>
        </div>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Anfänger-Tipps</h2>
        <ul class="list-disc pl-6 space-y-2 text-slate-600">
            <li><strong>Lieber zu wenig als zu viel gießen</strong> - Die meisten Pflanzen sterben durch Übergießen</li>
            <li><strong>Erde vor dem Gießen prüfen</strong> - Finger 2cm tief; nur gießen wenn trocken</li>
            <li><strong>Mit Schattenliebhabern anfangen</strong> - Sie sind generell toleranter</li>
            <li><strong>Nicht sofort umtopfen</strong> - Neue Pflanzen erst akklimatisieren lassen</li>
            <li><strong>Erst eine Pflanze kennenlernen, dann weitere hinzufügen</strong></li>
        </ul>
        """
    },
    "pet-safe-plants": {
        "es": """
        <p>¿Tienes gatos o perros curiosos? Estas hermosas plantas son completamente seguras si tu mascota decide probarlas.</p>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Las Mejores Plantas Seguras para Mascotas</h2>
        <div class="space-y-4">
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/spider-plant/" class="text-emerald-700 underline">Planta Araña</a></h3>
                <p class="text-slate-600">Totalmente segura y ¡a los gatos les encanta jugar con ella!</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/boston-fern/" class="text-emerald-700 underline">Helecho de Boston</a></h3>
                <p class="text-slate-600">Frondas exuberantes, completamente no tóxica.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/calathea-medallion/" class="text-emerald-700 underline">Calathea</a></h3>
                <p class="text-slate-600">Patrones hermosos y segura para mascotas.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/parlor-palm/" class="text-emerald-700 underline">Palmera de Salón</a></h3>
                <p class="text-slate-600">Elegante palmera que es segura para todos.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/peperomia-hope/" class="text-emerald-700 underline">Peperomia</a></h3>
                <p class="text-slate-600">Compacta, linda y no tóxica.</p>
            </div>
        </div>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Plantas a Evitar con Mascotas</h2>
        <ul class="list-disc pl-6 space-y-2 text-slate-600">
            <li><strong>Pothos</strong> - Tóxico si se ingiere</li>
            <li><strong>Monstera</strong> - Causa irritación oral</li>
            <li><strong>Lirio de la Paz</strong> - Tóxico para gatos y perros</li>
            <li><strong>Aloe Vera</strong> - Puede causar malestar digestivo</li>
        </ul>
        """,
        "de": """
        <p>Haben Sie neugierige Katzen oder Hunde? Diese schönen Pflanzen sind völlig sicher, falls Ihr Haustier sie probieren möchte.</p>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Die Besten Haustierfreundlichen Pflanzen</h2>
        <div class="space-y-4">
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/spider-plant/" class="text-emerald-700 underline">Grünlilie</a></h3>
                <p class="text-slate-600">Völlig sicher und Katzen lieben es damit zu spielen!</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/boston-fern/" class="text-emerald-700 underline">Schwertfarn</a></h3>
                <p class="text-slate-600">Üppige Wedel, komplett ungiftig.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/calathea-medallion/" class="text-emerald-700 underline">Calathea</a></h3>
                <p class="text-slate-600">Schöne Muster und sicher für Haustiere.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/parlor-palm/" class="text-emerald-700 underline">Bergpalme</a></h3>
                <p class="text-slate-600">Elegante Palme die für alle sicher ist.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/peperomia-hope/" class="text-emerald-700 underline">Peperomie</a></h3>
                <p class="text-slate-600">Kompakt, süß und ungiftig.</p>
            </div>
        </div>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Pflanzen die Haustierbesitzer Meiden Sollten</h2>
        <ul class="list-disc pl-6 space-y-2 text-slate-600">
            <li><strong>Efeutute</strong> - Giftig wenn verschluckt</li>
            <li><strong>Monstera</strong> - Verursacht Mundreizungen</li>
            <li><strong>Einblatt</strong> - Giftig für Katzen und Hunde</li>
            <li><strong>Aloe Vera</strong> - Kann Verdauungsbeschwerden verursachen</li>
        </ul>
        """
    },
    "best-low-light-plants": {
        "es": """
        <p>¿Tu espacio carece de luz solar directa? Estas plantas prosperan en esquinas sombrías, oficinas y habitaciones con ventanas pequeñas.</p>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Campeones de Poca Luz</h2>
        <div class="space-y-4">
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/zz-plant/" class="text-emerald-700 underline">Planta ZZ</a></h3>
                <p class="text-slate-600">La reina de la poca luz. Prospera en oficinas sin ventanas.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/snake-plant/" class="text-emerald-700 underline">Lengua de Suegra</a></h3>
                <p class="text-slate-600">Tolera cualquier condición de luz.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/pothos-golden/" class="text-emerald-700 underline">Pothos</a></h3>
                <p class="text-slate-600">Se adapta fácilmente a luz baja (crecerá más lento).</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/peace-lily/" class="text-emerald-700 underline">Lirio de la Paz</a></h3>
                <p class="text-slate-600">Una de las pocas plantas que florece con poca luz.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/cast-iron-plant/" class="text-emerald-700 underline">Aspidistra</a></h3>
                <p class="text-slate-600">Prácticamente indestructible en las condiciones más oscuras.</p>
            </div>
        </div>
        """,
        "de": """
        <p>Hat Ihr Raum wenig direktes Sonnenlicht? Diese Pflanzen gedeihen in schattigen Ecken, Büros und Zimmern mit kleinen Fenstern.</p>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Schattenliebhaber Champions</h2>
        <div class="space-y-4">
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/zz-plant/" class="text-emerald-700 underline">Zamioculcas</a></h3>
                <p class="text-slate-600">Die Königin des Schattens. Gedeiht in fensterlosen Büros.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/snake-plant/" class="text-emerald-700 underline">Bogenhanf</a></h3>
                <p class="text-slate-600">Toleriert jede Lichtsituation.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/pothos-golden/" class="text-emerald-700 underline">Efeutute</a></h3>
                <p class="text-slate-600">Passt sich leicht an wenig Licht an (wächst langsamer).</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/peace-lily/" class="text-emerald-700 underline">Einblatt</a></h3>
                <p class="text-slate-600">Eine der wenigen Pflanzen die bei wenig Licht blüht.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/cast-iron-plant/" class="text-emerald-700 underline">Schusterpalme</a></h3>
                <p class="text-slate-600">Praktisch unzerstörbar unter dunkelsten Bedingungen.</p>
            </div>
        </div>
        """
    },
    "air-purifying-plants": {
        "es": """
        <p>La investigación de la NASA identificó estas plantas como efectivas para eliminar contaminantes interiores comunes.</p>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Las Mejores Purificadoras de Aire</h2>
        <div class="space-y-4">
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/snake-plant/" class="text-emerald-700 underline">Lengua de Suegra</a></h3>
                <p class="text-slate-600">Convierte CO2 en oxígeno por la noche. Perfecta para dormitorios.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/pothos-golden/" class="text-emerald-700 underline">Pothos</a></h3>
                <p class="text-slate-600">Elimina formaldehído y otros VOCs.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/peace-lily/" class="text-emerald-700 underline">Lirio de la Paz</a></h3>
                <p class="text-slate-600">Elimina amoníaco, benceno y formaldehído.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/spider-plant/" class="text-emerald-700 underline">Planta Araña</a></h3>
                <p class="text-slate-600">Excelente para eliminar monóxido de carbono.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/es/plants/rubber-plant/" class="text-emerald-700 underline">Árbol del Caucho</a></h3>
                <p class="text-slate-600">Sus hojas grandes son muy efectivas limpiando el aire.</p>
            </div>
        </div>
        """,
        "de": """
        <p>NASA-Forschung identifizierte diese Pflanzen als wirksam bei der Entfernung häufiger Innenraumschadstoffe.</p>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Die Besten Luftreiniger</h2>
        <div class="space-y-4">
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/snake-plant/" class="text-emerald-700 underline">Bogenhanf</a></h3>
                <p class="text-slate-600">Wandelt nachts CO2 in Sauerstoff um. Perfekt fürs Schlafzimmer.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/pothos-golden/" class="text-emerald-700 underline">Efeutute</a></h3>
                <p class="text-slate-600">Entfernt Formaldehyd und andere flüchtige organische Verbindungen.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/peace-lily/" class="text-emerald-700 underline">Einblatt</a></h3>
                <p class="text-slate-600">Entfernt Ammoniak, Benzol und Formaldehyd.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/spider-plant/" class="text-emerald-700 underline">Grünlilie</a></h3>
                <p class="text-slate-600">Exzellent bei der Entfernung von Kohlenmonoxid.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2"><a href="/de/plants/rubber-plant/" class="text-emerald-700 underline">Gummibaum</a></h3>
                <p class="text-slate-600">Große Blätter sind sehr effektiv bei der Luftreinigung.</p>
            </div>
        </div>
        """
    },
    "watering-guide": {
        "es": """
        <p>El riego excesivo es la causa número uno de muerte de plantas. Aprende cómo hacerlo bien.</p>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">La Regla de Oro</h2>
        <div class="bg-white rounded-xl p-6 border border-slate-200 mb-6">
            <p class="text-lg text-slate-700"><strong>Siempre revisa la tierra antes de regar.</strong> Mete el dedo 2-3cm en la tierra. Si está seco, riega. Si está húmedo, espera.</p>
        </div>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Necesidades por Tipo de Planta</h2>
        <div class="space-y-4">
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2">🌵 Suculentas y Cactus</h3>
                <p class="text-slate-600">Riega cada 2-3 semanas. Deja secar completamente entre riegos.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2">🌿 Plantas Tropicales</h3>
                <p class="text-slate-600">Mantén la tierra ligeramente húmeda. Riega cuando la pulgada superior esté seca.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2">🌴 Palmeras</h3>
                <p class="text-slate-600">Riega cuando las 2 pulgadas superiores estén secas. No dejes encharcada.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2">🌸 Helechos</h3>
                <p class="text-slate-600">Mantén constantemente húmedo pero no empapado. Rocía regularmente.</p>
            </div>
        </div>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Señales de Problemas de Riego</h2>
        <ul class="list-disc pl-6 space-y-2 text-slate-600">
            <li><strong>Hojas amarillas blandas</strong> = Exceso de riego</li>
            <li><strong>Hojas marrones crujientes</strong> = Falta de riego</li>
            <li><strong>Hojas caídas</strong> = Puede ser cualquiera; revisa la tierra</li>
        </ul>
        """,
        "de": """
        <p>Übergießen ist die häufigste Todesursache bei Pflanzen. Lernen Sie es richtig zu machen.</p>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Die Goldene Regel</h2>
        <div class="bg-white rounded-xl p-6 border border-slate-200 mb-6">
            <p class="text-lg text-slate-700"><strong>Immer die Erde prüfen vor dem Gießen.</strong> Finger 2-3cm tief in die Erde stecken. Wenn trocken, gießen. Wenn feucht, warten.</p>
        </div>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Bedarf nach Pflanzentyp</h2>
        <div class="space-y-4">
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2">🌵 Sukkulenten & Kakteen</h3>
                <p class="text-slate-600">Alle 2-3 Wochen gießen. Komplett austrocknen lassen zwischen dem Gießen.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2">🌿 Tropische Pflanzen</h3>
                <p class="text-slate-600">Erde leicht feucht halten. Gießen wenn der obere Zentimeter trocken ist.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2">🌴 Palmen</h3>
                <p class="text-slate-600">Gießen wenn die oberen 5cm trocken sind. Nicht im Wasser stehen lassen.</p>
            </div>
            <div class="bg-white rounded-xl p-6 border border-slate-200">
                <h3 class="font-bold text-lg mb-2">🌸 Farne</h3>
                <p class="text-slate-600">Konstant feucht aber nicht nass halten. Regelmäßig besprühen.</p>
            </div>
        </div>

        <h2 class="text-2xl font-bold text-slate-800 mt-8 mb-4">Anzeichen für Gießprobleme</h2>
        <ul class="list-disc pl-6 space-y-2 text-slate-600">
            <li><strong>Gelbe weiche Blätter</strong> = Übergießen</li>
            <li><strong>Braune knusprige Blätter</strong> = Untergießen</li>
            <li><strong>Hängende Blätter</strong> = Kann beides sein; Erde prüfen</li>
        </ul>
        """
    }
}

def generate_article_page(slug, lang):
    """Generate translated article page"""
    info = ARTICLES[slug][lang]
    en_info = ARTICLES[slug]["en"]
    
    # Language-specific text
    if lang == "es":
        guides_text = "Guías"
        back_text = "Volver a guías"
        browse_text = "Explorar todas las plantas fáciles"
        lang_label = "Seleccionar idioma"
    elif lang == "de":
        guides_text = "Ratgeber"
        back_text = "Zurück zu Ratgebern"
        browse_text = "Alle pflegeleichten Pflanzen ansehen"
        lang_label = "Sprache wählen"
    else:
        guides_text = "Guides"
        back_text = "Back to guides"
        browse_text = "Browse all easy-care plants"
        lang_label = "Select language"
    
    content = ARTICLE_CONTENT.get(slug, {}).get(lang, "")
    if not content:
        # Fall back to a placeholder
        content = f"<p>Content coming soon...</p>"
    
    lang_prefix = f"/{lang}" if lang != "en" else ""
    
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta name="google-site-verification" content="_6B659H6pJiEc-n-JpbJOzbFOC9-IVr9OAmN5TTVh74">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{info["title"]} | PlantFinder</title>
    <meta name="description" content="{info["desc"]}">
    <link rel="canonical" href="https://plantfinder.org{lang_prefix}/articles/{slug}/">
    <link rel="alternate" hreflang="en" href="https://plantfinder.org/articles/{slug}/">
    <link rel="alternate" hreflang="es" href="https://plantfinder.org/es/articles/{slug}/">
    <link rel="alternate" hreflang="de" href="https://plantfinder.org/de/articles/{slug}/">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <script src="https://cdn.tailwindcss.com"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-J2JW25BZPF"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-J2JW25BZPF");</script>
    <script src="https://analytics.ahrefs.com/analytics.js" data-key="qlbhxGtUr2oyQ7ePI+y0Qg" async></script>
</head>
<body class="bg-slate-50 min-h-screen">
    <header class="bg-white border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="{lang_prefix}/" class="flex items-center gap-2"><span class="text-2xl">🌿</span><span class="text-xl font-bold text-emerald-700">PlantFinder</span></a>
            <nav class="flex gap-6 text-sm">
                <a href="{lang_prefix}/search/" class="text-slate-600 hover:text-emerald-700">{"Buscar" if lang == "es" else "Suchen" if lang == "de" else "Browse"}</a>
                <a href="{lang_prefix}/articles/" class="text-emerald-700 font-medium">{guides_text}</a>
            </nav>
        </div>
    </header>

    <main class="max-w-3xl mx-auto px-4 py-12">
        <nav class="text-sm text-slate-600 mb-6"><a href="{lang_prefix}/articles/" class="hover:text-emerald-700">{guides_text}</a> → {info["title"].split()[0]}</nav>
        <h1 class="text-4xl font-bold text-slate-800 mb-4">{info["title"]}</h1>
        <p class="text-xl text-slate-600 mb-8">{info["short"]}</p>

        <div class="prose prose-lg max-w-none">
            {content}
        </div>

        <div class="mt-12 p-6 bg-emerald-50 rounded-2xl border border-emerald-200">
            <p class="font-medium text-emerald-800">🔍 <a href="{lang_prefix}/search/?difficulty=easy" class="underline">{browse_text}</a></p>
        </div>
    </main>

    <footer class="bg-slate-900 text-slate-400 py-12 px-4 mt-12">
        <div class="max-w-6xl mx-auto text-center"><p class="text-sm">© 2026 PlantFinder</p></div>
    </footer>

    <div style="position:fixed;top:80px;right:20px;z-index:50;">
        <select onchange="window.location.href=this.value" class="bg-white border border-slate-300 rounded-lg px-3 py-2 text-sm shadow-lg" aria-label="{lang_label}">
            <option value="/articles/{slug}/" {"selected" if lang == "en" else ""}>🇬🇧 English</option>
            <option value="/es/articles/{slug}/" {"selected" if lang == "es" else ""}>🇪🇸 Español</option>
            <option value="/de/articles/{slug}/" {"selected" if lang == "de" else ""}>🇩🇪 Deutsch</option>
        </select>
    </div>
</body>
</html>'''
    return html

def generate_articles_index(lang):
    """Generate articles index page"""
    if lang == "es":
        title = "Guías de Plantas"
        subtitle = "Consejos expertos para cuidar tus plantas de interior"
    elif lang == "de":
        title = "Pflanzen-Ratgeber"
        subtitle = "Expertentipps für die Pflege Ihrer Zimmerpflanzen"
    else:
        title = "Plant Guides"
        subtitle = "Expert advice for caring for your houseplants"
    
    lang_prefix = f"/{lang}" if lang != "en" else ""
    
    cards = ""
    for slug, info in ARTICLES.items():
        article_info = info[lang]
        cards += f'''
        <a href="{lang_prefix}/articles/{slug}/" class="bg-white rounded-xl p-6 shadow-sm hover:shadow-md transition border border-slate-100">
            <span class="text-4xl">{article_info["emoji"]}</span>
            <h2 class="font-bold text-slate-900 text-lg mt-4 mb-2">{article_info["title"]}</h2>
            <p class="text-slate-600">{article_info["short"]}</p>
        </a>'''
    
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta name="google-site-verification" content="_6B659H6pJiEc-n-JpbJOzbFOC9-IVr9OAmN5TTVh74">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | PlantFinder</title>
    <meta name="description" content="{subtitle}">
    <link rel="canonical" href="https://plantfinder.org{lang_prefix}/articles/">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <script src="https://cdn.tailwindcss.com"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-J2JW25BZPF"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-J2JW25BZPF");</script>
    <script src="https://analytics.ahrefs.com/analytics.js" data-key="qlbhxGtUr2oyQ7ePI+y0Qg" async></script>
</head>
<body class="bg-slate-50 min-h-screen">
    <header class="bg-white border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="{lang_prefix}/" class="flex items-center gap-2"><span class="text-2xl">🌿</span><span class="text-xl font-bold text-emerald-700">PlantFinder</span></a>
            <nav class="flex gap-6 text-sm">
                <a href="{lang_prefix}/search/" class="text-slate-600 hover:text-emerald-700">{"Buscar" if lang == "es" else "Suchen" if lang == "de" else "Browse"}</a>
                <a href="{lang_prefix}/articles/" class="text-emerald-700 font-medium">{"Guías" if lang == "es" else "Ratgeber" if lang == "de" else "Guides"}</a>
            </nav>
        </div>
    </header>

    <main class="max-w-6xl mx-auto px-4 py-12">
        <h1 class="text-4xl font-bold text-slate-800 mb-2">{title}</h1>
        <p class="text-xl text-slate-600 mb-8">{subtitle}</p>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {cards}
        </div>
    </main>

    <footer class="bg-slate-900 text-slate-400 py-12 px-4 mt-12">
        <div class="max-w-6xl mx-auto text-center"><p class="text-sm">© 2026 PlantFinder</p></div>
    </footer>

    <div style="position:fixed;top:80px;right:20px;z-index:50;">
        <select onchange="window.location.href=this.value" class="bg-white border border-slate-300 rounded-lg px-3 py-2 text-sm shadow-lg" aria-label="Select language">
            <option value="/articles/" {"selected" if lang == "en" else ""}>🇬🇧 English</option>
            <option value="/es/articles/" {"selected" if lang == "es" else ""}>🇪🇸 Español</option>
            <option value="/de/articles/" {"selected" if lang == "de" else ""}>🇩🇪 Deutsch</option>
        </select>
    </div>
</body>
</html>'''
    return html


def main():
    print("Generating translated articles...\\n")
    
    for lang in ["es", "de"]:
        # Create articles directory
        articles_dir = BASE_DIR / lang / "articles"
        articles_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate index
        with open(articles_dir / "index.html", "w") as f:
            f.write(generate_articles_index(lang))
        print(f"  ✓ {lang}/articles/index.html")
        
        # Generate each article
        for slug in ARTICLES:
            article_dir = articles_dir / slug
            article_dir.mkdir(exist_ok=True)
            with open(article_dir / "index.html", "w") as f:
                f.write(generate_article_page(slug, lang))
            print(f"  ✓ {lang}/articles/{slug}/")
    
    # Also update English articles index with language selector
    with open(BASE_DIR / "articles" / "index.html", "w") as f:
        f.write(generate_articles_index("en"))
    print(f"  ✓ articles/index.html (updated)")
    
    print("\\n✅ All articles translated!")

if __name__ == "__main__":
    main()
