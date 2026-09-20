#!/usr/bin/env python3
"""Generate Spanish article pages for PlantFinder"""

import os

BASE_DIR = os.path.expanduser("~/clawd/houseplant-finder")
GA_ID = "G-J2JW25BZPF"

def get_header(lang_code, current_article):
    return f'''<!DOCTYPE html>
<html lang="es">
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
                <a href="/es/" class="flex items-center gap-2">
                    <svg class="w-8 h-8 text-emerald-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/></svg>
                    <span class="font-bold text-xl bg-gradient-to-r from-emerald-600 to-teal-600 bg-clip-text text-transparent">PlantFinder</span>
                </a>
                <nav class="flex items-center gap-6">
                    <a href="/es/search/" class="text-slate-600 hover:text-emerald-700 font-medium hidden sm:block">Buscar</a>
                    <a href="/es/quiz/" class="text-slate-600 hover:text-emerald-700 font-medium hidden sm:block">Quiz</a>
                    <a href="/es/articles/" class="text-emerald-700 font-medium hidden sm:block">Guías</a>'''

def get_lang_selector(article_slug):
    return f'''
                    <div class="relative group">
                        <button class="flex items-center gap-1 text-slate-600 hover:text-emerald-700 py-2">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                            <span>ES</span>
                        </button>
                        <div class="absolute right-0 top-full bg-white border border-slate-200 rounded-xl shadow-xl hidden group-hover:block min-w-[140px] py-2 z-50">
                            <a href="/articles/{article_slug}/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">English</a>
                            <a href="/es/articles/{article_slug}/" class="block px-4 py-2 hover:bg-slate-100 font-semibold text-emerald-700">Español</a>
                            <a href="/de/articles/{article_slug}/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">Deutsch</a>
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
                    <a href="/es/search/" class="hover:text-white transition">Buscar</a>
                    <a href="/es/quiz/" class="hover:text-white transition">Quiz</a>
                    <a href="/es/compare/" class="hover:text-white transition">Comparar</a>
                    <a href="/es/articles/" class="hover:text-white transition">Guías</a>
                    <a href="/es/about/" class="hover:text-white transition">Acerca de</a>
                </nav>
            </div>
            <div class="border-t border-slate-800 mt-8 pt-8 text-center text-sm">
                <p>© 2026 PlantFinder. Hecho con 🌿 para amantes de las plantas.</p>
            </div>
        </div>
    </footer>
    <script defer src="https://unpkg.com/lucide@1.47.0/dist/umd/lucide.min.js"></script>
    <script>document.addEventListener('DOMContentLoaded', () => lucide.createIcons());</script>
</body>
</html>'''

articles = {
    "beginner-houseplants": {
        "title": "Las 10 Mejores Plantas de Interior para Principiantes (Guía 2026)",
        "description": "Descubre las plantas de interior más fáciles de cultivar. Estas 10 plantas para principiantes sobreviven al descuido y al riego irregular.",
        "badge": "🌱 Guía para Principiantes",
        "h1": "Las 10 Mejores Plantas para Principiantes",
        "intro": "Comienza tu aventura como padre de plantas con estas variedades casi indestructibles que prosperan con el descuido.",
        "breadcrumb": "Plantas para Principiantes",
        "plants": [
            {"name": "Pothos (Hiedra del Diablo)", "id": "pothos-golden", "desc": "La planta definitiva para principiantes. Tolera poca luz, riego irregular, y te avisa cuando tiene sed al marchitarse ligeramente.", "tags": [("Poca Luz OK", "amber"), ("Poco Riego", "blue")]},
            {"name": "Sansevieria (Lengua de Suegra)", "id": "snake-plant", "desc": "Sobrevive semanas sin agua. Tolera cualquier nivel de luz. Prácticamente prospera con el descuido y purifica el aire.", "tags": [("Cualquier Luz", "amber"), ("Purifica Aire", "green")]},
            {"name": "ZZ Plant (Zamioculcas)", "id": "zz-plant", "desc": "Riega una vez al mes—¡sí, en serio! Maneja la poca luz muy bien. Hojas brillantes y verde oscuro siempre lucen impresionantes.", "tags": [("Poca Luz OK", "amber"), ("Riego Mensual", "blue")]},
            {"name": "Planta Araña", "id": "spider-plant", "desc": "Difícil de matar y produce adorables plantas bebé que puedes compartir. ¡Genial para ganar confianza!", "tags": [("Segura para Mascotas 🐾", "pink"), ("Produce Bebés", "purple")]},
            {"name": "Planta de Caucho", "id": "rubber-plant", "desc": "Hojas grandes y brillantes hacen una declaración. Sorprendentemente fácil a pesar de su apariencia dramática.", "tags": [("Planta Decorativa", "emerald"), ("Fácil Cuidado", "blue")]},
            {"name": "Lirio de la Paz", "id": "peace-lily", "desc": "Hermosas flores blancas y excelente purificación del aire. ¡Se marchita dramáticamente cuando tiene sed—luego se recupera!", "tags": [("Floración 🌸", "white"), ("Purifica Aire", "green")]},
            {"name": "Filodendro Hoja de Corazón", "id": "philodendron-heartleaf", "desc": "Hojas en forma de corazón en enredaderas colgantes. Crece rápido, perdona el descuido, y luce hermoso en cestas colgantes.", "tags": [("Poca Luz OK", "amber"), ("Colgante", "purple")]},
            {"name": "Aloe Vera", "id": "aloe-vera", "desc": "¡Útil Y fácil! El gel alivia quemaduras. Riega con moderación y dale luz brillante. Casi imposible de matar.", "tags": [("Medicinal", "orange"), ("Tolerante a Sequía", "blue")]},
            {"name": "Aglaonema (Siempreverde Chino)", "id": "chinese-evergreen", "desc": "Hermosas hojas con patrones en varios colores. Prospera en poca luz donde otras plantas luchan. Muy indulgente.", "tags": [("Poca Luz OK", "amber"), ("Decorativa", "emerald")]},
            {"name": "Dracaena", "id": "dracaena", "desc": "Belleza arquitectónica sorprendentemente fácil. Muchas variedades para elegir. Tolera poca luz y riego infrecuente.", "tags": [("Purifica Aire", "green"), ("Planta Decorativa", "emerald")]}
        ],
        "tips": [
            {"icon": "💧", "title": "Riega Menos, No Más", "text": "La mayoría de las plantas de interior mueren por exceso de riego. En caso de duda, espera un día más."},
            {"icon": "👆", "title": "La Prueba del Dedo", "text": "Introduce tu dedo 2-3 cm en la tierra. Solo riega si se siente seca."},
            {"icon": "🌤️", "title": "Empieza con Plantas de Poca Luz", "text": "Son más indulgentes y se adaptan a la mayoría de condiciones interiores."},
            {"icon": "🏺", "title": "No Trasplantes Inmediatamente", "text": "Deja que las plantas nuevas se adapten unas semanas antes de molestar sus raíces."}
        ],
        "mistakes": [
            {"title": "Exceso de riego", "text": "El asesino #1 de plantas de interior. ¡Las raíces también necesitan aire!"},
            {"title": "Demasiado sol directo", "text": "La mayoría de las plantas de interior prefieren luz indirecta"},
            {"title": "Ignorar el drenaje", "text": "Siempre usa macetas con agujeros de drenaje"},
            {"title": "Mover plantas constantemente", "text": "Necesitan tiempo para adaptarse a su lugar"}
        ]
    },
    "air-purifying-plants": {
        "title": "Las 10 Mejores Plantas Purificadoras de Aire (Estudio NASA)",
        "description": "Plantas estudiadas por la NASA que limpian el aire interior. Elimina toxinas como formaldehído y benceno naturalmente.",
        "badge": "🌬️ Calidad del Aire",
        "h1": "Mejores Plantas Purificadoras de Aire",
        "intro": "Estas plantas no solo lucen hermosas—activamente limpian el aire de tu hogar eliminando toxinas comunes.",
        "breadcrumb": "Plantas Purificadoras",
        "plants": [
            {"name": "Sansevieria", "id": "snake-plant", "desc": "Campeona en filtrar formaldehído, benceno y otros compuestos. Libera oxígeno de noche, perfecta para dormitorios.", "tags": [("Estudio NASA", "green"), ("Nocturna", "purple")]},
            {"name": "Pothos", "id": "pothos-golden", "desc": "Elimina formaldehído, xileno y tolueno. Una de las más efectivas según el estudio de NASA.", "tags": [("Fácil Cuidado", "emerald"), ("Purifica Aire", "green")]},
            {"name": "Lirio de la Paz", "id": "peace-lily", "desc": "Elimina amoníaco, benceno, formaldehído y tricloroetileno. Bonus: hermosas flores blancas.", "tags": [("Floración", "white"), ("Top NASA", "green")]},
            {"name": "Planta Araña", "id": "spider-plant", "desc": "Excelente para eliminar monóxido de carbono y xileno. Segura para mascotas y fácil de propagar.", "tags": [("Segura Mascotas 🐾", "pink"), ("CO Remover", "blue")]},
            {"name": "Ficus Robusta", "id": "rubber-plant", "desc": "Hojas grandes absorben contaminantes eficientemente. Especialmente buena para formaldehído.", "tags": [("Hojas Grandes", "emerald"), ("Formaldehído", "green")]},
            {"name": "Helecho de Boston", "id": "boston-fern", "desc": "Actúa como humidificador natural mientras elimina formaldehído y xileno del aire.", "tags": [("Humidificador", "cyan"), ("NASA Estudio", "green")]},
            {"name": "Dracaena", "id": "dracaena", "desc": "Múltiples variedades, todas excelentes purificadoras. Elimina benceno, formaldehído y tricloroetileno.", "tags": [("Versátil", "purple"), ("Multi-Toxina", "green")]},
            {"name": "Palma Bambú", "id": "areca-palm", "desc": "Natural humidificador y purificador. Elimina benceno, formaldehído y tricloroetileno.", "tags": [("Humidificador", "cyan"), ("Tropical", "emerald")]},
            {"name": "Aglaonema", "id": "chinese-evergreen", "desc": "Elimina benceno y formaldehído efectivamente. Perfecta para espacios con poca luz.", "tags": [("Poca Luz", "amber"), ("Benceno", "green")]},
            {"name": "Aloe Vera", "id": "aloe-vera", "desc": "Elimina formaldehído y benceno. Bonus: gel medicinal para quemaduras.", "tags": [("Medicinal", "orange"), ("Dual Propósito", "emerald")]}
        ],
        "tips": [
            {"icon": "📏", "title": "Una Planta por 10m²", "text": "Para purificación efectiva, coloca al menos una planta mediana por cada 10 metros cuadrados."},
            {"icon": "🍃", "title": "Limpia las Hojas", "text": "El polvo reduce la capacidad de purificación. Limpia las hojas mensualmente."},
            {"icon": "🏠", "title": "Variedad es Clave", "text": "Diferentes plantas eliminan diferentes toxinas. Usa varias especies."},
            {"icon": "🛏️", "title": "Plantas de Dormitorio", "text": "Sansevieria y Aloe liberan oxígeno de noche, ideales junto a la cama."}
        ],
        "mistakes": [
            {"title": "Pocas plantas", "text": "Una sola planta no purifica una habitación entera"},
            {"title": "Hojas polvorientas", "text": "El polvo bloquea los estomas y reduce la purificación"},
            {"title": "Ignorar la ventilación", "text": "Las plantas complementan, no reemplazan, la buena ventilación"},
            {"title": "Ubicación incorrecta", "text": "Coloca plantas donde pasas más tiempo"}
        ]
    },
    "best-low-light-plants": {
        "title": "Las 10 Mejores Plantas para Poca Luz (Guía 2026)",
        "description": "Plantas de interior que prosperan en espacios oscuros. Perfectas para oficinas, baños y habitaciones con pocas ventanas.",
        "badge": "🌙 Poca Luz",
        "h1": "Mejores Plantas para Poca Luz",
        "intro": "¿Sin ventanas grandes? No hay problema. Estas plantas prosperan en las condiciones más oscuras de tu hogar.",
        "breadcrumb": "Plantas Poca Luz",
        "plants": [
            {"name": "ZZ Plant", "id": "zz-plant", "desc": "La reina de la poca luz. Sobrevive prácticamente en la oscuridad. Hojas brillantes sin necesidad de sol.", "tags": [("Tolerante Oscuridad", "slate"), ("Brillante", "emerald")]},
            {"name": "Sansevieria", "id": "snake-plant", "desc": "Prospera desde esquinas oscuras hasta sol brillante. La planta más versátil en cuanto a luz.", "tags": [("Super Versátil", "purple"), ("Indestructible", "emerald")]},
            {"name": "Pothos", "id": "pothos-golden", "desc": "Crece bien en oficinas sin ventanas. Las variedades verdes toleran mejor la poca luz que las variegadas.", "tags": [("Oficina Perfecta", "blue"), ("Colgante", "purple")]},
            {"name": "Aglaonema", "id": "chinese-evergreen", "desc": "Diseñada para la sombra. Los patrones coloridos brillan incluso en poca luz.", "tags": [("Colorida", "pink"), ("Sombra Amante", "slate")]},
            {"name": "Aspidistra (Planta de Hierro)", "id": "cast-iron-plant", "desc": "Llamada así porque sobrevive casi todo, incluyendo esquinas muy oscuras.", "tags": [("Indestructible", "slate"), ("Victorian Fave", "amber")]},
            {"name": "Dracaena", "id": "dracaena", "desc": "Muchas variedades toleran poca luz. Los tipos verdes sólidos mejor que los variegados.", "tags": [("Arquitectónica", "emerald"), ("Adaptable", "blue")]},
            {"name": "Filodendro Hoja de Corazón", "id": "philodendron-heartleaf", "desc": "Enredadera perfecta para estantes en esquinas oscuras. Crece más lento en poca luz pero sobrevive.", "tags": [("Colgante", "purple"), ("Romántica", "pink")]},
            {"name": "Palma de Salón", "id": "parlor-palm", "desc": "Palma clásica de interior que prefiere luz filtrada. Popular desde la era Victoriana.", "tags": [("Tropical", "emerald"), ("Elegante", "amber")]},
            {"name": "Helecho Nido de Ave", "id": "birds-nest-fern", "desc": "Prefiere sombra húmeda. Perfecto para baños con poca luz natural.", "tags": [("Baño Ideal", "cyan"), ("Humedad Amante", "blue")]},
            {"name": "Dieffenbachia", "id": "dieffenbachia", "desc": "Hojas grandes y llamativas prosperan en luz indirecta baja a media.", "tags": [("Hojas Grandes", "emerald"), ("Tropical", "green")]}
        ],
        "tips": [
            {"icon": "💡", "title": "Luz Artificial Cuenta", "text": "Las luces fluorescentes de oficina pueden mantener vivas muchas plantas de poca luz."},
            {"icon": "🔄", "title": "Rota Ocasionalmente", "text": "Gira las plantas cada pocas semanas para crecimiento uniforme."},
            {"icon": "💧", "title": "Menos Agua Necesaria", "text": "Plantas en poca luz crecen más lento y necesitan menos agua."},
            {"icon": "🌿", "title": "Elige Verde Sólido", "text": "Las plantas variegadas necesitan más luz que las de hojas verdes sólidas."}
        ],
        "mistakes": [
            {"title": "Regar igual que plantas de sol", "text": "Poca luz = crecimiento lento = menos agua necesaria"},
            {"title": "Esperar crecimiento rápido", "text": "Las plantas crecen más lento en poca luz, es normal"},
            {"title": "Elegir plantas variegadas", "text": "Las hojas blancas/amarillas necesitan más luz"},
            {"title": "Olvidar limpiar hojas", "text": "Las hojas limpias capturan más de la poca luz disponible"}
        ]
    },
    "pet-safe-plants": {
        "title": "Las 10 Mejores Plantas Seguras para Mascotas (Guía 2026)",
        "description": "Plantas de interior no tóxicas seguras para gatos y perros. Crea un hogar verde sin preocuparte por tus mascotas.",
        "badge": "🐾 Segura para Mascotas",
        "h1": "Mejores Plantas Seguras para Mascotas",
        "intro": "Ama las plantas Y a tus mascotas? Estas bellezas no tóxicas te permiten tener ambos sin preocupaciones.",
        "breadcrumb": "Plantas Pet-Safe",
        "plants": [
            {"name": "Planta Araña", "id": "spider-plant", "desc": "Completamente segura para gatos y perros. Bonus: a muchos gatos les encanta jugar con las hojas colgantes.", "tags": [("100% Segura", "green"), ("Gatos Aman", "pink")]},
            {"name": "Helecho de Boston", "id": "boston-fern", "desc": "No tóxico y agrega humedad al aire. Perfecto para hogares con mascotas alérgicas.", "tags": [("No Tóxico", "green"), ("Humidificador", "cyan")]},
            {"name": "Palma Areca", "id": "areca-palm", "desc": "Palma tropical segura que es completamente no tóxica. Añade un toque de paraíso sin riesgo.", "tags": [("Tropical", "emerald"), ("Segura", "green")]},
            {"name": "Calathea", "id": "calathea-medallion", "desc": "Patrones impresionantes y completamente segura. Las hojas se mueven durante el día—¡entretenimiento para gatos!", "tags": [("Patrones", "purple"), ("Movimiento", "pink")]},
            {"name": "Peperomia", "id": "peperomia-watermelon", "desc": "Pequeña, linda y 100% segura. Muchas variedades con texturas y colores únicos.", "tags": [("Compacta", "blue"), ("Variedad", "purple")]},
            {"name": "Violeta Africana", "id": "african-violet", "desc": "Flores coloridas sin toxicidad. Perfecta para alféizares donde las mascotas curiosean.", "tags": [("Floración", "violet"), ("Segura", "green")]},
            {"name": "Planta de Oración", "id": "prayer-plant", "desc": "Hojas que se pliegan de noche fascinan a humanos y son seguras para mascotas.", "tags": [("Interactiva", "purple"), ("No Tóxica", "green")]},
            {"name": "Pilea (Planta del Dinero China)", "id": "pilea-peperomioides", "desc": "De moda, fácil de propagar, y completamente segura para todos los miembros peludos.", "tags": [("Trendy", "emerald"), ("Propaga Fácil", "blue")]},
            {"name": "Palma de Salón", "id": "parlor-palm", "desc": "Elegancia victoriana sin preocupaciones. Completamente no tóxica para gatos y perros.", "tags": [("Elegante", "amber"), ("Clásica", "slate")]},
            {"name": "Haworthia", "id": "haworthia-zebra", "desc": "Suculenta pequeña y segura. A diferencia del Aloe, es completamente no tóxica.", "tags": [("Suculenta Segura", "green"), ("Compacta", "blue")]}
        ],
        "tips": [
            {"icon": "📍", "title": "Ubicación Alta", "text": "Incluso plantas seguras pueden causar malestar estomacal si se comen en exceso. Mantén fuera del alcance fácil."},
            {"icon": "🔍", "title": "Verifica Siempre", "text": "Consulta la base de datos ASPCA antes de comprar cualquier planta nueva."},
            {"icon": "🌿", "title": "Ofrece Alternativas", "text": "Cultiva hierba gatera o hierba de trigo para que tus mascotas mastiquen en lugar de tus plantas."},
            {"icon": "👀", "title": "Observa el Comportamiento", "text": "Algunos animales son más propensos a masticar plantas. Conoce a tu mascota."}
        ],
        "mistakes": [
            {"title": "Asumir que todas las plantas son seguras", "text": "Muchas plantas populares son tóxicas—siempre verifica"},
            {"title": "Ignorar fertilizantes", "text": "Algunos fertilizantes son tóxicos incluso si la planta no lo es"},
            {"title": "Olvidar el agua estancada", "text": "El agua de los platos puede contener bacterias dañinas"},
            {"title": "No asegurar macetas", "text": "Las macetas que caen pueden lastimar a mascotas curiosas"}
        ]
    },
    "watering-guide": {
        "title": "Guía de Riego para Plantas de Interior (2026)",
        "description": "Aprende exactamente cuándo y cómo regar tus plantas de interior. Evita el error más común que mata plantas.",
        "badge": "💧 Cuidado Esencial",
        "h1": "Guía Completa de Riego",
        "intro": "El riego incorrecto mata más plantas de interior que cualquier otra cosa. Aprende a hacerlo bien.",
        "breadcrumb": "Guía de Riego",
        "plants": [
            {"name": "Suculentas y Cactus", "id": "jade-plant", "desc": "Riega profundamente pero con poca frecuencia. Deja secar completamente entre riegos. En invierno, casi nada.", "tags": [("Cada 2-3 Semanas", "amber"), ("Secar Totalmente", "orange")]},
            {"name": "Pothos y Filodendros", "id": "pothos-golden", "desc": "Riega cuando los 2-3 cm superiores estén secos. Toleran algo de sequía pero no encharcamiento.", "tags": [("Semanal", "blue"), ("Flexible", "emerald")]},
            {"name": "Helechos", "id": "boston-fern", "desc": "Mantén consistentemente húmedo pero no empapado. Nunca dejes secar completamente.", "tags": [("2-3 Días", "cyan"), ("Humedad Alta", "blue")]},
            {"name": "Sansevieria y ZZ", "id": "snake-plant", "desc": "Las plantas más tolerantes a sequía. Riega cada 2-4 semanas, menos en invierno.", "tags": [("Cada 2-4 Semanas", "amber"), ("Olvídalas", "emerald")]},
            {"name": "Calatheas y Marantas", "id": "calathea-medallion", "desc": "Necesitan humedad constante. Usa agua filtrada—son sensibles al cloro.", "tags": [("Cada 5-7 Días", "blue"), ("Agua Filtrada", "cyan")]},
            {"name": "Ficus (Caucho, Lyrata)", "id": "rubber-plant", "desc": "Riega cuando la pulgada superior esté seca. No les gusta estar empapados ni completamente secos.", "tags": [("Semanal", "blue"), ("Equilibrado", "emerald")]},
            {"name": "Palmas", "id": "areca-palm", "desc": "Mantén tierra ligeramente húmeda. Más agua en verano, menos en invierno.", "tags": [("Cada 5-7 Días", "blue"), ("Estacional", "amber")]},
            {"name": "Orquídeas", "id": "moth-orchid", "desc": "Riega semanalmente sumergiendo las raíces. Deja drenar completamente antes de volver a la maceta.", "tags": [("Semanal Inmersión", "purple"), ("Drenar Bien", "blue")]},
            {"name": "Lirio de la Paz", "id": "peace-lily", "desc": "Te avisa cuando tiene sed marchitándose. Riega cuando las hojas empiecen a caer.", "tags": [("Cuando Se Marchita", "green"), ("Auto-Aviso", "emerald")]},
            {"name": "Monstera", "id": "monstera-deliciosa", "desc": "Riega cuando los 5 cm superiores estén secos. Menos frecuente que muchas tropicales.", "tags": [("Cada 1-2 Semanas", "blue"), ("Deja Secar", "amber")]}
        ],
        "tips": [
            {"icon": "👆", "title": "La Prueba del Dedo", "text": "Introduce tu dedo 2-5 cm en la tierra. Si está seco, riega. Si húmedo, espera."},
            {"icon": "⚖️", "title": "Prueba del Peso", "text": "Levanta la maceta. Las plantas secas son notablemente más ligeras que las recién regadas."},
            {"icon": "🕐", "title": "Riega por la Mañana", "text": "Las plantas usan agua durante el día. Regar de noche puede causar pudrición."},
            {"icon": "🚰", "title": "Drenar es Clave", "text": "Siempre usa macetas con agujeros. Vacía los platos después de 30 minutos."}
        ],
        "mistakes": [
            {"title": "Regar en horario fijo", "text": "Las necesidades cambian con estaciones, luz y temperatura"},
            {"title": "Regar poco y frecuente", "text": "Mejor riego profundo y poco frecuente que poquito cada día"},
            {"title": "Ignorar el tipo de maceta", "text": "Terracota seca más rápido que plástico o cerámica"},
            {"title": "Usar agua muy fría", "text": "El agua a temperatura ambiente es mejor para las raíces"}
        ]
    }
}

def generate_article(slug, article):
    html = get_header("es", slug)
    
    # Meta tags
    html += f'''
    <title>{article["title"]} | PlantFinder</title>
    <meta name="description" content="{article["description"]}">
    <link rel="canonical" href="https://plantfinder.org/es/articles/{slug}/">
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
    <script src="https://analytics.ahrefs.com/analytics.js" data-key="qlbhxGtUr2oyQ7ePI+y0Qg" async></script>
</head>
<body class="bg-slate-50 text-slate-800">'''
    
    html += get_nav()
    html += get_lang_selector(slug)
    
    # Main content
    html += f'''
    <main class="max-w-4xl mx-auto px-4 py-12">
        <nav class="text-sm text-slate-500 mb-6">
            <a href="/es/" class="hover:text-emerald-600">Inicio</a><span class="mx-2">/</span>
            <a href="/es/articles/" class="hover:text-emerald-600">Guías</a><span class="mx-2">/</span>
            <span class="text-slate-700">{article["breadcrumb"]}</span>
        </nav>

        <article>
            <header class="mb-10">
                <div class="flex items-center gap-2 mb-4">
                    <span class="bg-emerald-100 text-emerald-700 px-3 py-1 rounded-full text-sm font-medium">{article["badge"]}</span>
                    <span class="text-slate-500 text-sm">Actualizado Feb 2026</span>
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
                            <h3 class="font-bold text-lg mb-1"><a href="/es/plants/{plant["id"]}/" class="text-emerald-700 hover:underline">{i}. {plant["name"]}</a></h3>
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
                Consejos Esenciales
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
                Errores Comunes a Evitar
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
                <h3 class="font-bold text-xl mb-2">🔍 Encuentra Tu Planta Perfecta</h3>
                <p class="text-emerald-100 mb-4">¿No estás seguro qué planta es perfecta para ti? ¡Haz nuestro quiz!</p>
                <div class="flex flex-wrap gap-3">
                    <a href="/es/quiz/" class="bg-white text-emerald-700 px-5 py-2 rounded-xl font-semibold hover:bg-emerald-50 transition">Hacer el Quiz</a>
                    <a href="/es/search/" class="bg-emerald-600 text-white px-5 py-2 rounded-xl font-semibold hover:bg-emerald-700 transition border border-emerald-400">Explorar Plantas</a>
                </div>
            </div>
        </article>
    </main>'''
    
    html += get_footer()
    
    return html


def main():
    for slug, article in articles.items():
        article_dir = os.path.join(BASE_DIR, f"es/articles/{slug}")
        os.makedirs(article_dir, exist_ok=True)
        
        html = generate_article(slug, article)
        
        with open(os.path.join(article_dir, "index.html"), 'w') as f:
            f.write(html)
        
        print(f"  ✓ {slug}")
    
    print(f"\n✅ Created {len(articles)} Spanish articles")


if __name__ == "__main__":
    main()
