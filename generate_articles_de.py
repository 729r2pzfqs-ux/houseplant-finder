#!/usr/bin/env python3
"""Generate German article pages for PlantFinder"""

import os

BASE_DIR = os.path.expanduser("~/clawd/houseplant-finder")
GA_ID = "G-J2JW25BZPF"

def get_header(lang_code, current_article):
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","{GA_ID}");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">'''

def get_nav():
    return '''
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4">
            <div class="flex items-center justify-between">
                <a href="/de/" class="flex items-center gap-2">
                    <svg class="w-8 h-8 text-emerald-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/></svg>
                    <span class="font-bold text-xl bg-gradient-to-r from-emerald-600 to-teal-600 bg-clip-text text-transparent">PlantFinder</span>
                </a>
                <nav class="flex items-center gap-6">
                    <a href="/de/search/" class="text-slate-600 hover:text-emerald-700 font-medium hidden sm:block">Durchsuchen</a>
                    <a href="/de/quiz/" class="text-slate-600 hover:text-emerald-700 font-medium hidden sm:block">Quiz</a>
                    <a href="/de/articles/" class="text-emerald-700 font-medium hidden sm:block">Ratgeber</a>'''

def get_lang_selector(article_slug):
    return f'''
                    <div class="relative group">
                        <button class="flex items-center gap-1 text-slate-600 hover:text-emerald-700 py-2">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                            <span>DE</span>
                        </button>
                        <div class="absolute right-0 top-full bg-white border border-slate-200 rounded-xl shadow-xl hidden group-hover:block min-w-[140px] py-2 z-50">
                            <a href="/articles/{article_slug}/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">English</a>
                            <a href="/es/articles/{article_slug}/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">Español</a>
                            <a href="/de/articles/{article_slug}/" class="block px-4 py-2 hover:bg-slate-100 font-semibold text-emerald-700">Deutsch</a>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    </header>'''

def get_footer():
    return '''
    <footer class="bg-slate-900 text-slate-400 py-12 px-4 mt-12">
        <div class="max-w-6xl mx-auto">
            <div class="flex flex-col md:flex-row items-center justify-between gap-6">
                <div class="flex items-center gap-2">
                    <svg class="w-8 h-8 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/></svg>
                    <span class="font-semibold text-white">PlantFinder</span>
                </div>
                <nav class="flex flex-wrap justify-center gap-6 text-sm">
                    <a href="/de/search/" class="hover:text-white transition">Durchsuchen</a>
                    <a href="/de/quiz/" class="hover:text-white transition">Quiz</a>
                    <a href="/de/compare/" class="hover:text-white transition">Vergleichen</a>
                    <a href="/de/articles/" class="hover:text-white transition">Ratgeber</a>
                    <a href="/de/about/" class="hover:text-white transition">Über uns</a>
                </nav>
            </div>
            <div class="border-t border-slate-800 mt-8 pt-8 text-center text-sm">
                <p>© 2026 PlantFinder. Mit 🌿 für Pflanzenliebhaber gemacht.</p>
            </div>
        </div>
    </footer>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script>lucide.createIcons();</script>
</body>
</html>'''

articles = {
    "beginner-houseplants": {
        "title": "Die 10 Besten Zimmerpflanzen für Anfänger (Ratgeber 2026)",
        "description": "Entdecke die einfachsten Zimmerpflanzen. Diese 10 anfängerfreundlichen Pflanzen überleben Vernachlässigung und unregelmäßiges Gießen.",
        "badge": "🌱 Anfänger-Ratgeber",
        "h1": "Die 10 Besten Pflanzen für Anfänger",
        "intro": "Starte deine Pflanzenpflege-Reise mit diesen nahezu unzerstörbaren Sorten, die bei Vernachlässigung gedeihen.",
        "breadcrumb": "Anfänger-Pflanzen",
        "plants": [
            {"name": "Efeutute (Pothos)", "id": "pothos-golden", "desc": "Die ultimative Anfängerpflanze. Verträgt wenig Licht, unregelmäßiges Gießen und zeigt dir, wenn sie Durst hat, indem sie leicht welkt.", "tags": [("Wenig Licht OK", "amber"), ("Wenig Wasser", "blue")]},
            {"name": "Bogenhanf (Sansevieria)", "id": "snake-plant", "desc": "Überlebt Wochen ohne Wasser. Verträgt jede Lichtstärke. Gedeiht praktisch bei Vernachlässigung und reinigt die Luft.", "tags": [("Jedes Licht", "amber"), ("Luftreiniger", "green")]},
            {"name": "ZZ-Pflanze (Zamioculcas)", "id": "zz-plant", "desc": "Einmal im Monat gießen—ja, wirklich! Kommt mit wenig Licht gut zurecht. Glänzende, dunkelgrüne Blätter sehen immer toll aus.", "tags": [("Wenig Licht OK", "amber"), ("Monatlich Gießen", "blue")]},
            {"name": "Grünlilie", "id": "spider-plant", "desc": "Kaum totzukriegen und produziert süße Babypflanzen zum Teilen. Perfekt um Selbstvertrauen aufzubauen!", "tags": [("Haustierfreundlich 🐾", "pink"), ("Macht Ableger", "purple")]},
            {"name": "Gummibaum", "id": "rubber-plant", "desc": "Große, glänzende Blätter machen einen starken Eindruck. Überraschend pflegeleicht trotz dramatischem Aussehen.", "tags": [("Statement-Pflanze", "emerald"), ("Pflegeleicht", "blue")]},
            {"name": "Einblatt (Friedenslilie)", "id": "peace-lily", "desc": "Schöne weiße Blüten und ausgezeichnete Luftreinigung. Welkt dramatisch bei Durst—erholt sich dann schnell!", "tags": [("Blühend 🌸", "white"), ("Luftreiniger", "green")]},
            {"name": "Herzblatt-Philodendron", "id": "philodendron-heartleaf", "desc": "Herzförmige Blätter an hängenden Ranken. Wächst schnell, verzeiht Vernachlässigung und sieht toll in Ampeln aus.", "tags": [("Wenig Licht OK", "amber"), ("Hängend", "purple")]},
            {"name": "Aloe Vera", "id": "aloe-vera", "desc": "Nützlich UND pflegeleicht! Das Gel lindert Verbrennungen. Sparsam gießen und helles Licht geben. Fast unmöglich zu töten.", "tags": [("Heilpflanze", "orange"), ("Trockenheitsresistent", "blue")]},
            {"name": "Kolbenfaden (Aglaonema)", "id": "chinese-evergreen", "desc": "Wunderschöne gemusterte Blätter in verschiedenen Farben. Gedeiht bei wenig Licht, wo andere Pflanzen kämpfen. Sehr nachsichtig.", "tags": [("Wenig Licht OK", "amber"), ("Dekorativ", "emerald")]},
            {"name": "Dracaena", "id": "dracaena", "desc": "Architektonische Schönheit, überraschend pflegeleicht. Viele Sorten zur Auswahl. Verträgt wenig Licht und seltenes Gießen.", "tags": [("Luftreiniger", "green"), ("Statement-Pflanze", "emerald")]}
        ],
        "tips": [
            {"icon": "💧", "title": "Weniger Gießen, Nicht Mehr", "text": "Die meisten Zimmerpflanzen sterben durch Überwässerung. Im Zweifel noch einen Tag warten."},
            {"icon": "👆", "title": "Der Fingertest", "text": "Steck deinen Finger 2-3 cm in die Erde. Nur gießen, wenn sie sich trocken anfühlt."},
            {"icon": "🌤️", "title": "Mit Schattenpflanzen Anfangen", "text": "Sie sind nachsichtiger und passen sich an die meisten Innenbedingungen an."},
            {"icon": "🏺", "title": "Nicht Sofort Umtopfen", "text": "Lass neue Pflanzen ein paar Wochen eingewöhnen, bevor du ihre Wurzeln störst."}
        ],
        "mistakes": [
            {"title": "Überwässerung", "text": "Der #1 Pflanzenkiller. Wurzeln brauchen auch Luft!"},
            {"title": "Zu viel direkte Sonne", "text": "Die meisten Zimmerpflanzen bevorzugen indirektes Licht"},
            {"title": "Drainage ignorieren", "text": "Immer Töpfe mit Abflusslöchern verwenden"},
            {"title": "Pflanzen ständig umstellen", "text": "Sie brauchen Zeit, sich an ihren Platz zu gewöhnen"}
        ]
    },
    "air-purifying-plants": {
        "title": "Die 10 Besten Luftreinigenden Zimmerpflanzen (NASA-Studie)",
        "description": "Von der NASA untersuchte Pflanzen, die die Raumluft reinigen. Entferne Giftstoffe wie Formaldehyd und Benzol auf natürliche Weise.",
        "badge": "🌬️ Luftqualität",
        "h1": "Beste Luftreinigende Zimmerpflanzen",
        "intro": "Diese Pflanzen sehen nicht nur schön aus—sie reinigen aktiv die Luft in deinem Zuhause, indem sie häufige Giftstoffe entfernen.",
        "breadcrumb": "Luftreinigende Pflanzen",
        "plants": [
            {"name": "Bogenhanf", "id": "snake-plant", "desc": "Champion beim Filtern von Formaldehyd, Benzol und anderen Verbindungen. Gibt nachts Sauerstoff ab, perfekt fürs Schlafzimmer.", "tags": [("NASA-Studie", "green"), ("Nacht-Aktiv", "purple")]},
            {"name": "Efeutute", "id": "pothos-golden", "desc": "Entfernt Formaldehyd, Xylol und Toluol. Eine der effektivsten laut NASA-Studie.", "tags": [("Pflegeleicht", "emerald"), ("Luftreiniger", "green")]},
            {"name": "Einblatt", "id": "peace-lily", "desc": "Entfernt Ammoniak, Benzol, Formaldehyd und Trichlorethylen. Bonus: schöne weiße Blüten.", "tags": [("Blühend", "white"), ("NASA Top", "green")]},
            {"name": "Grünlilie", "id": "spider-plant", "desc": "Ausgezeichnet beim Entfernen von Kohlenmonoxid und Xylol. Haustierfreundlich und leicht zu vermehren.", "tags": [("Haustierfreundlich 🐾", "pink"), ("CO-Entferner", "blue")]},
            {"name": "Gummibaum", "id": "rubber-plant", "desc": "Große Blätter absorbieren Schadstoffe effizient. Besonders gut bei Formaldehyd.", "tags": [("Große Blätter", "emerald"), ("Formaldehyd", "green")]},
            {"name": "Boston-Farn", "id": "boston-fern", "desc": "Wirkt als natürlicher Luftbefeuchter und entfernt gleichzeitig Formaldehyd und Xylol aus der Luft.", "tags": [("Luftbefeuchter", "cyan"), ("NASA-Studie", "green")]},
            {"name": "Dracaena", "id": "dracaena", "desc": "Mehrere Sorten, alle ausgezeichnete Luftreiniger. Entfernt Benzol, Formaldehyd und Trichlorethylen.", "tags": [("Vielseitig", "purple"), ("Multi-Toxin", "green")]},
            {"name": "Goldfruchtpalme", "id": "areca-palm", "desc": "Natürlicher Luftbefeuchter und Reiniger. Entfernt Benzol, Formaldehyd und Trichlorethylen.", "tags": [("Luftbefeuchter", "cyan"), ("Tropisch", "emerald")]},
            {"name": "Kolbenfaden", "id": "chinese-evergreen", "desc": "Entfernt Benzol und Formaldehyd effektiv. Perfekt für Räume mit wenig Licht.", "tags": [("Wenig Licht", "amber"), ("Benzol", "green")]},
            {"name": "Aloe Vera", "id": "aloe-vera", "desc": "Entfernt Formaldehyd und Benzol. Bonus: Heilendes Gel für Verbrennungen.", "tags": [("Heilpflanze", "orange"), ("Doppelter Nutzen", "emerald")]}
        ],
        "tips": [
            {"icon": "📏", "title": "Eine Pflanze pro 10m²", "text": "Für effektive Reinigung mindestens eine mittelgroße Pflanze pro 10 Quadratmeter."},
            {"icon": "🍃", "title": "Blätter Sauber Halten", "text": "Staub reduziert die Reinigungskapazität. Blätter monatlich abwischen."},
            {"icon": "🏠", "title": "Vielfalt ist Wichtig", "text": "Verschiedene Pflanzen entfernen verschiedene Giftstoffe. Mehrere Arten verwenden."},
            {"icon": "🛏️", "title": "Schlafzimmer-Pflanzen", "text": "Bogenhanf und Aloe geben nachts Sauerstoff ab, ideal neben dem Bett."}
        ],
        "mistakes": [
            {"title": "Zu wenige Pflanzen", "text": "Eine einzelne Pflanze reinigt keinen ganzen Raum"},
            {"title": "Staubige Blätter", "text": "Staub blockiert die Spaltöffnungen und reduziert die Reinigung"},
            {"title": "Lüftung ignorieren", "text": "Pflanzen ergänzen, ersetzen aber keine gute Belüftung"},
            {"title": "Falsche Platzierung", "text": "Pflanzen dort aufstellen, wo du die meiste Zeit verbringst"}
        ]
    },
    "best-low-light-plants": {
        "title": "Die 10 Besten Pflanzen für Wenig Licht (Ratgeber 2026)",
        "description": "Zimmerpflanzen, die in dunklen Räumen gedeihen. Perfekt für Büros, Badezimmer und Räume mit wenig Fenstern.",
        "badge": "🌙 Wenig Licht",
        "h1": "Beste Pflanzen für Wenig Licht",
        "intro": "Keine großen Fenster? Kein Problem. Diese Pflanzen gedeihen in den dunkelsten Ecken deines Zuhauses.",
        "breadcrumb": "Schattenpflanzen",
        "plants": [
            {"name": "ZZ-Pflanze", "id": "zz-plant", "desc": "Die Königin des wenigen Lichts. Überlebt praktisch im Dunkeln. Glänzende Blätter ohne Sonne.", "tags": [("Dunkelheits-Tolerant", "slate"), ("Glänzend", "emerald")]},
            {"name": "Bogenhanf", "id": "snake-plant", "desc": "Gedeiht von dunklen Ecken bis zu hellem Sonnenlicht. Die vielseitigste Pflanze in Bezug auf Licht.", "tags": [("Super Vielseitig", "purple"), ("Unzerstörbar", "emerald")]},
            {"name": "Efeutute", "id": "pothos-golden", "desc": "Wächst gut in fensterlosen Büros. Grüne Sorten vertragen weniger Licht besser als bunte.", "tags": [("Büro-Perfekt", "blue"), ("Hängend", "purple")]},
            {"name": "Kolbenfaden", "id": "chinese-evergreen", "desc": "Für den Schatten gemacht. Die bunten Muster leuchten auch bei wenig Licht.", "tags": [("Bunt", "pink"), ("Schatten-Liebend", "slate")]},
            {"name": "Schusterpalme", "id": "cast-iron-plant", "desc": "So genannt, weil sie fast alles überlebt, einschließlich sehr dunkler Ecken.", "tags": [("Unzerstörbar", "slate"), ("Viktorianisch", "amber")]},
            {"name": "Dracaena", "id": "dracaena", "desc": "Viele Sorten vertragen wenig Licht. Einfarbig grüne besser als bunte.", "tags": [("Architektonisch", "emerald"), ("Anpassungsfähig", "blue")]},
            {"name": "Herzblatt-Philodendron", "id": "philodendron-heartleaf", "desc": "Perfekte Rankpflanze für Regale in dunklen Ecken. Wächst langsamer bei wenig Licht, überlebt aber.", "tags": [("Hängend", "purple"), ("Romantisch", "pink")]},
            {"name": "Bergpalme", "id": "parlor-palm", "desc": "Klassische Zimmerpalme, die gefiltertes Licht bevorzugt. Beliebt seit der viktorianischen Ära.", "tags": [("Tropisch", "emerald"), ("Elegant", "amber")]},
            {"name": "Nestfarn", "id": "birds-nest-fern", "desc": "Bevorzugt feuchten Schatten. Perfekt für Badezimmer mit wenig natürlichem Licht.", "tags": [("Bad-Ideal", "cyan"), ("Feuchtigkeitsliebend", "blue")]},
            {"name": "Dieffenbachie", "id": "dieffenbachia", "desc": "Große, auffällige Blätter gedeihen bei niedrigem bis mittlerem indirektem Licht.", "tags": [("Große Blätter", "emerald"), ("Tropisch", "green")]}
        ],
        "tips": [
            {"icon": "💡", "title": "Kunstlicht Zählt", "text": "Büro-Leuchtstofflampen können viele Schattenpflanzen am Leben halten."},
            {"icon": "🔄", "title": "Gelegentlich Drehen", "text": "Pflanzen alle paar Wochen drehen für gleichmäßiges Wachstum."},
            {"icon": "💧", "title": "Weniger Wasser Nötig", "text": "Pflanzen bei wenig Licht wachsen langsamer und brauchen weniger Wasser."},
            {"icon": "🌿", "title": "Einfarbig Grün Wählen", "text": "Bunte Pflanzen brauchen mehr Licht als einfarbig grüne."}
        ],
        "mistakes": [
            {"title": "Genauso gießen wie Sonnenpflanzen", "text": "Wenig Licht = langsames Wachstum = weniger Wasser nötig"},
            {"title": "Schnelles Wachstum erwarten", "text": "Pflanzen wachsen bei wenig Licht langsamer, das ist normal"},
            {"title": "Bunte Pflanzen wählen", "text": "Weiße/gelbe Blätter brauchen mehr Licht"},
            {"title": "Blätter nicht reinigen", "text": "Saubere Blätter fangen mehr vom wenigen Licht ein"}
        ]
    },
    "pet-safe-plants": {
        "title": "Die 10 Besten Haustierfreundlichen Pflanzen (Ratgeber 2026)",
        "description": "Ungiftige Zimmerpflanzen, sicher für Katzen und Hunde. Schaffe ein grünes Zuhause ohne dir um deine Haustiere Sorgen zu machen.",
        "badge": "🐾 Haustierfreundlich",
        "h1": "Beste Haustierfreundliche Pflanzen",
        "intro": "Du liebst Pflanzen UND deine Haustiere? Diese ungiftigen Schönheiten ermöglichen beides ohne Sorgen.",
        "breadcrumb": "Haustierfreundlich",
        "plants": [
            {"name": "Grünlilie", "id": "spider-plant", "desc": "Komplett sicher für Katzen und Hunde. Bonus: Viele Katzen lieben es, mit den hängenden Blättern zu spielen.", "tags": [("100% Sicher", "green"), ("Katzen Lieben", "pink")]},
            {"name": "Boston-Farn", "id": "boston-fern", "desc": "Ungiftig und erhöht die Luftfeuchtigkeit. Perfekt für Haushalte mit allergischen Haustieren.", "tags": [("Ungiftig", "green"), ("Luftbefeuchter", "cyan")]},
            {"name": "Goldfruchtpalme", "id": "areca-palm", "desc": "Tropische Palme, die komplett ungiftig ist. Bringt Paradiesesflair ohne Risiko.", "tags": [("Tropisch", "emerald"), ("Sicher", "green")]},
            {"name": "Korbmarante", "id": "calathea-medallion", "desc": "Beeindruckende Muster und komplett sicher. Die Blätter bewegen sich tagsüber—Unterhaltung für Katzen!", "tags": [("Muster", "purple"), ("Bewegung", "pink")]},
            {"name": "Peperomie", "id": "peperomia-watermelon", "desc": "Klein, süß und 100% sicher. Viele Sorten mit einzigartigen Texturen und Farben.", "tags": [("Kompakt", "blue"), ("Vielfalt", "purple")]},
            {"name": "Usambaraveilchen", "id": "african-violet", "desc": "Bunte Blüten ohne Giftigkeit. Perfekt für Fensterbänke, an denen neugierige Haustiere schnüffeln.", "tags": [("Blühend", "violet"), ("Sicher", "green")]},
            {"name": "Gebetspflanze", "id": "prayer-plant", "desc": "Blätter, die sich nachts falten, faszinieren Menschen und sind sicher für Haustiere.", "tags": [("Interaktiv", "purple"), ("Ungiftig", "green")]},
            {"name": "Ufopflanze (Pilea)", "id": "pilea-peperomioides", "desc": "Trendig, leicht zu vermehren und komplett sicher für alle pelzigen Familienmitglieder.", "tags": [("Trendy", "emerald"), ("Leicht Vermehrbar", "blue")]},
            {"name": "Bergpalme", "id": "parlor-palm", "desc": "Viktorianische Eleganz ohne Sorgen. Komplett ungiftig für Katzen und Hunde.", "tags": [("Elegant", "amber"), ("Klassisch", "slate")]},
            {"name": "Haworthia", "id": "haworthia-zebra", "desc": "Kleine, sichere Sukkulente. Im Gegensatz zu Aloe komplett ungiftig.", "tags": [("Sichere Sukkulente", "green"), ("Kompakt", "blue")]}
        ],
        "tips": [
            {"icon": "📍", "title": "Höher Platzieren", "text": "Auch sichere Pflanzen können Bauchschmerzen verursachen, wenn zu viel gefressen wird. Außer Reichweite halten."},
            {"icon": "🔍", "title": "Immer Prüfen", "text": "Die ASPCA-Datenbank konsultieren, bevor du neue Pflanzen kaufst."},
            {"icon": "🌿", "title": "Alternativen Anbieten", "text": "Katzengras oder Weizengras anbauen, damit Haustiere daran kauen statt an deinen Pflanzen."},
            {"icon": "👀", "title": "Verhalten Beobachten", "text": "Manche Tiere kauen mehr an Pflanzen als andere. Kenne dein Haustier."}
        ],
        "mistakes": [
            {"title": "Annehmen, alle Pflanzen sind sicher", "text": "Viele beliebte Pflanzen sind giftig—immer prüfen"},
            {"title": "Dünger ignorieren", "text": "Manche Dünger sind giftig, auch wenn die Pflanze es nicht ist"},
            {"title": "Stehendes Wasser vergessen", "text": "Wasser in Untersetzern kann schädliche Bakterien enthalten"},
            {"title": "Töpfe nicht sichern", "text": "Umfallende Töpfe können neugierige Haustiere verletzen"}
        ]
    },
    "watering-guide": {
        "title": "Gießanleitung für Zimmerpflanzen (2026)",
        "description": "Lerne genau, wann und wie du deine Zimmerpflanzen gießen sollst. Vermeide den häufigsten Fehler, der Pflanzen tötet.",
        "badge": "💧 Wichtige Pflege",
        "h1": "Vollständige Gießanleitung",
        "intro": "Falsches Gießen tötet mehr Zimmerpflanzen als alles andere. Lerne, es richtig zu machen.",
        "breadcrumb": "Gießanleitung",
        "plants": [
            {"name": "Sukkulenten & Kakteen", "id": "jade-plant", "desc": "Tief gießen, aber selten. Zwischen dem Gießen komplett austrocknen lassen. Im Winter fast gar nicht.", "tags": [("Alle 2-3 Wochen", "amber"), ("Komplett Trocknen", "orange")]},
            {"name": "Efeutute & Philodendren", "id": "pothos-golden", "desc": "Gießen, wenn die oberen 2-3 cm trocken sind. Vertragen etwas Trockenheit, aber keine Staunässe.", "tags": [("Wöchentlich", "blue"), ("Flexibel", "emerald")]},
            {"name": "Farne", "id": "boston-fern", "desc": "Gleichmäßig feucht halten, aber nicht nass. Niemals komplett austrocknen lassen.", "tags": [("Alle 2-3 Tage", "cyan"), ("Hohe Feuchtigkeit", "blue")]},
            {"name": "Bogenhanf & ZZ", "id": "snake-plant", "desc": "Die trockenheitsresistentesten Pflanzen. Alle 2-4 Wochen gießen, im Winter weniger.", "tags": [("Alle 2-4 Wochen", "amber"), ("Vergiss Sie", "emerald")]},
            {"name": "Korbmaranten & Marantas", "id": "calathea-medallion", "desc": "Brauchen konstante Feuchtigkeit. Gefiltertes Wasser verwenden—sie sind chlorempfindlich.", "tags": [("Alle 5-7 Tage", "blue"), ("Gefiltertes Wasser", "cyan")]},
            {"name": "Ficus (Gummibaum, Geigenfeige)", "id": "rubber-plant", "desc": "Gießen, wenn der oberste Zentimeter trocken ist. Mögen weder Staunässe noch völlige Trockenheit.", "tags": [("Wöchentlich", "blue"), ("Ausgewogen", "emerald")]},
            {"name": "Palmen", "id": "areca-palm", "desc": "Erde leicht feucht halten. Mehr Wasser im Sommer, weniger im Winter.", "tags": [("Alle 5-7 Tage", "blue"), ("Saisonal", "amber")]},
            {"name": "Orchideen", "id": "moth-orchid", "desc": "Wöchentlich gießen durch Eintauchen der Wurzeln. Komplett abtropfen lassen vor dem Zurückstellen.", "tags": [("Wöchentlich Tauchen", "purple"), ("Gut Abtropfen", "blue")]},
            {"name": "Einblatt", "id": "peace-lily", "desc": "Zeigt dir, wenn es Durst hat, indem es welkt. Gießen, wenn die Blätter anfangen zu hängen.", "tags": [("Wenn Es Welkt", "green"), ("Selbst-Meldend", "emerald")]},
            {"name": "Monstera", "id": "monstera-deliciosa", "desc": "Gießen, wenn die oberen 5 cm trocken sind. Seltener als viele andere Tropenpflanzen.", "tags": [("Alle 1-2 Wochen", "blue"), ("Trocknen Lassen", "amber")]}
        ],
        "tips": [
            {"icon": "👆", "title": "Der Fingertest", "text": "Steck deinen Finger 2-5 cm in die Erde. Wenn trocken, gießen. Wenn feucht, warten."},
            {"icon": "⚖️", "title": "Gewichtstest", "text": "Heb den Topf hoch. Trockene Pflanzen sind deutlich leichter als frisch gegossene."},
            {"icon": "🕐", "title": "Morgens Gießen", "text": "Pflanzen nutzen Wasser tagsüber. Abends gießen kann zu Fäulnis führen."},
            {"icon": "🚰", "title": "Drainage ist Entscheidend", "text": "Immer Töpfe mit Löchern verwenden. Untersetzer nach 30 Minuten leeren."}
        ],
        "mistakes": [
            {"title": "Nach Zeitplan gießen", "text": "Bedürfnisse ändern sich mit Jahreszeit, Licht und Temperatur"},
            {"title": "Wenig und oft gießen", "text": "Besser tief und selten als täglich ein bisschen"},
            {"title": "Topfart ignorieren", "text": "Terrakotta trocknet schneller als Plastik oder Keramik"},
            {"title": "Zu kaltes Wasser", "text": "Zimmerwarmes Wasser ist besser für die Wurzeln"}
        ]
    }
}

def generate_article(slug, article):
    html = get_header("de", slug)
    
    # Meta tags
    html += f'''
    <title>{article["title"]} | PlantFinder</title>
    <meta name="description" content="{article["description"]}">
    <link rel="canonical" href="https://plantfinder.org/de/articles/{slug}/">
    <link rel="alternate" hreflang="en" href="https://plantfinder.org/articles/{slug}/">
    <link rel="alternate" hreflang="es" href="https://plantfinder.org/es/articles/{slug}/">
    <link rel="alternate" hreflang="de" href="https://plantfinder.org/de/articles/{slug}/">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script>tailwind.config={{theme:{{extend:{{fontFamily:{{sans:['Plus Jakarta Sans','sans-serif']}}}}}}}}</script>
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{article["title"]}",
        "description": "{article["description"]}",
        "author": {{"@type": "Organization", "name": "PlantFinder"}},
        "publisher": {{"@type": "Organization", "name": "PlantFinder"}},
        "datePublished": "2026-01-15",
        "dateModified": "2026-02-23"
    }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800">'''
    
    html += get_nav()
    html += get_lang_selector(slug)
    
    # Main content
    html += f'''
    <main class="max-w-4xl mx-auto px-4 py-12">
        <nav class="text-sm text-slate-500 mb-6">
            <a href="/de/" class="hover:text-emerald-600">Startseite</a><span class="mx-2">/</span>
            <a href="/de/articles/" class="hover:text-emerald-600">Ratgeber</a><span class="mx-2">/</span>
            <span class="text-slate-700">{article["breadcrumb"]}</span>
        </nav>

        <article>
            <header class="mb-10">
                <div class="flex items-center gap-2 mb-4">
                    <span class="bg-emerald-100 text-emerald-700 px-3 py-1 rounded-full text-sm font-medium">{article["badge"]}</span>
                    <span class="text-slate-500 text-sm">Aktualisiert Feb 2026</span>
                </div>
                <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 mb-4">{article["h1"]}</h1>
                <p class="text-xl text-slate-600 leading-relaxed">{article["intro"]}</p>
            </header>

            <div class="space-y-4 mb-12">'''
    
    # Plant cards
    for i, plant in enumerate(article["plants"], 1):
        tags_html = ""
        for tag_text, tag_color in plant["tags"]:
            tags_html += f'<span class="text-xs bg-{tag_color}-100 text-{tag_color}-700 px-2 py-1 rounded-full">{tag_text}</span>'
        
        html += f'''
                <div class="bg-white rounded-2xl p-6 border border-slate-200 hover:border-emerald-300 transition">
                    <div class="flex gap-4">
                        <div class="w-20 h-20 bg-gradient-to-br from-emerald-100 to-teal-100 rounded-xl flex items-center justify-center flex-shrink-0">
                            <img src="/images/plants/{plant["id"]}.webp" alt="{plant["name"]}" class="w-16 h-16 object-contain">
                        </div>
                        <div>
                            <h3 class="font-bold text-lg mb-1"><a href="/de/plants/{plant["id"]}/" class="text-emerald-700 hover:underline">{i}. {plant["name"]}</a></h3>
                            <p class="text-slate-600 text-sm mb-2">{plant["desc"]}</p>
                            <div class="flex flex-wrap gap-2">{tags_html}</div>
                        </div>
                    </div>
                </div>'''
    
    # Tips section
    html += '''
            </div>

            <h2 class="text-2xl font-bold text-slate-900 mt-12 mb-6 flex items-center gap-2">
                <span class="bg-blue-100 w-10 h-10 rounded-xl flex items-center justify-center">💡</span>
                Wichtige Tipps
            </h2>
            <div class="grid md:grid-cols-2 gap-4 mb-12">'''
    
    for tip in article["tips"]:
        html += f'''
                <div class="bg-white rounded-xl p-5 border border-slate-200">
                    <div class="font-bold text-slate-900 mb-2">{tip["icon"]} {tip["title"]}</div>
                    <p class="text-slate-600 text-sm">{tip["text"]}</p>
                </div>'''
    
    # Mistakes section
    html += '''
            </div>

            <h2 class="text-2xl font-bold text-slate-900 mt-12 mb-6 flex items-center gap-2">
                <span class="bg-red-100 w-10 h-10 rounded-xl flex items-center justify-center">⚠️</span>
                Häufige Fehler Vermeiden
            </h2>
            <div class="bg-red-50 rounded-2xl p-6 border border-red-200 mb-12">
                <ul class="space-y-3 text-slate-700">'''
    
    for mistake in article["mistakes"]:
        html += f'''
                    <li class="flex items-start gap-2"><span class="text-red-500">✗</span><span><strong>{mistake["title"]}</strong> - {mistake["text"]}</span></li>'''
    
    # CTA section
    html += '''
                </ul>
            </div>

            <div class="mt-12 p-6 bg-gradient-to-r from-emerald-500 to-teal-600 rounded-2xl text-white">
                <h3 class="font-bold text-xl mb-2">🔍 Finde Deine Perfekte Pflanze</h3>
                <p class="text-emerald-100 mb-4">Nicht sicher, welche Pflanze perfekt für dich ist? Mach unser Quiz!</p>
                <div class="flex flex-wrap gap-3">
                    <a href="/de/quiz/" class="bg-white text-emerald-700 px-5 py-2 rounded-xl font-semibold hover:bg-emerald-50 transition">Quiz Machen</a>
                    <a href="/de/search/" class="bg-emerald-600 text-white px-5 py-2 rounded-xl font-semibold hover:bg-emerald-700 transition border border-emerald-400">Pflanzen Durchsuchen</a>
                </div>
            </div>
        </article>
    </main>'''
    
    html += get_footer()
    
    return html


def main():
    for slug, article in articles.items():
        article_dir = os.path.join(BASE_DIR, f"de/articles/{slug}")
        os.makedirs(article_dir, exist_ok=True)
        
        html = generate_article(slug, article)
        
        with open(os.path.join(article_dir, "index.html"), 'w') as f:
            f.write(html)
        
        print(f"  ✓ {slug}")
    
    print(f"\n✅ Created {len(articles)} German articles")


if __name__ == "__main__":
    main()
