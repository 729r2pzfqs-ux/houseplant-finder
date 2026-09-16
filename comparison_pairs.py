#!/usr/bin/env python3
"""Curated plant-vs-plant pairs for the static comparison pages.

Each entry is (plant_a_id, plant_b_id, tell_them_apart_note).
The note is the hand-written bit a database diff cannot produce: how the two
plants actually differ in the hand, and which one people usually mean.
Order matters -- it fixes the canonical URL (a-vs-b) and the page title.
"""

# Short, search-friendly slug fragments. Anything not listed falls back to a
# slugified plant name.
SLUG_OVERRIDES = {
    "pothos-golden": "pothos",
    "monstera-deliciosa": "monstera",
    "dracaena-marginata": "dragon-tree",
    "philodendron-heartleaf": "heartleaf-philodendron",
    "succulent-echeveria": "echeveria",
    "orchid-phalaenopsis": "moth-orchid",
    "bromeliad-guzmania": "bromeliad",
    "haworthia-zebra": "zebra-haworthia",
    "rhaphidophora-tetrasperma": "mini-monstera",
    "peperomia-obtusifolia": "baby-rubber-plant",
    "schefflera-arboricola": "dwarf-umbrella-tree",
    "pilea-peperomioides": "chinese-money-plant",
    "dracaena-corn-plant": "corn-plant",
    "calathea-rattlesnake": "rattlesnake-plant",
    "sedum-burrito": "burros-tail",
    "sedum-rubrotinctum": "jelly-bean-plant",
    "hoya-carnosa": "hoya",
}

PAIRS = [
    # --- the six the tool already promoted -------------------------------
    ("pothos-golden", "philodendron-heartleaf",
     "Look at the leaf and the stem. Pothos leaves are thick, waxy and slightly "
     "puckered, and the stem swells into a visible groove where it meets the leaf. "
     "Heartleaf philodendron leaves are thinner, softer and matte, with a longer, "
     "narrower point and a smooth stem. New philodendron leaves unfurl from a "
     "papery sheath; new pothos leaves simply unroll out of the previous leaf."),

    ("snake-plant", "zz-plant",
     "Both are stiff, upright and nearly unkillable, so the real split is light. "
     "The ZZ plant is the one that genuinely grows in a dark corner; the snake "
     "plant tolerates low light but gets leggy and pale there. Snake plant leaves "
     "are flat, banded blades from a rosette; ZZ leaves are glossy oval leaflets "
     "lined along a thick, arching stalk."),

    ("monstera-deliciosa", "fiddle-leaf-fig",
     "This is a forgiveness comparison, not a looks comparison. A monstera shrugs "
     "off a missed watering, a move across the room and a week of gloom. A fiddle "
     "leaf fig drops leaves over any of the three. If this is your first big floor "
     "plant, the monstera is the one that survives the learning curve."),

    ("peace-lily", "spider-plant",
     "The peace lily tells you when it is thirsty -- it wilts dramatically, then "
     "recovers within hours of a drink -- which makes it oddly good for people who "
     "water on instinct. The spider plant never signals; it just keeps producing "
     "plantlets on arching stems that you can snip off and root in water."),

    ("rubber-plant", "dracaena-marginata",
     "Two easy indoor trees with opposite silhouettes. The rubber plant is broad "
     "and solid -- big glossy paddle leaves on an upright trunk, and it fills a "
     "corner visually. The dragon tree is airy and vertical -- thin spiky leaves "
     "in tufts on slim canes -- so it fits a narrow space the rubber plant would "
     "overwhelm."),

    ("calathea-medallion", "boston-fern",
     "Both want damp air, but they fail differently. A calathea protests dry air "
     "and tap-water minerals with crispy leaf edges and needs filtered or rested "
     "water. A Boston fern simply sheds -- it drops fronds and litters the floor "
     "when the air is dry, but recovers fast once you raise humidity."),

    # --- monstera family --------------------------------------------------
    ("monstera-deliciosa", "monstera-adansonii",
     "Same genus, different habit. Deliciosa gets large and architectural, with "
     "leaves that split at the edges as the plant matures. Adansonii stays vining "
     "and small-leaved, with holes fully enclosed inside the leaf rather than cut "
     "in from the margin. Adansonii is the one for a hanging basket or a pole on a "
     "shelf."),

    ("monstera-deliciosa", "rhaphidophora-tetrasperma",
     "The 'mini monstera' is not a monstera at all. Rhaphidophora tetrasperma "
     "splits its leaves from day one on a fast, thin vine and stays apartment-sized. "
     "Monstera deliciosa needs years and a sturdy pole before it fenestrates, then "
     "it keeps getting bigger. Buy the rhaphidophora if you want the look without "
     "the floor space."),

    ("monstera-adansonii", "rhaphidophora-tetrasperma",
     "The clearest tell is the hole. Adansonii leaves have holes sealed inside the "
     "leaf blade; tetrasperma leaves are cut through to the edge, like a tiny "
     "deliciosa. Tetrasperma also grows noticeably faster and wants a little more "
     "light."),

    ("monstera-deliciosa", "philodendron-selloum",
     "The confusion is old -- monstera was sold as 'split-leaf philodendron' for "
     "decades. Monstera leaves have holes as well as splits and the plant climbs; "
     "selloum leaves are deeply lobed but solid, and the plant spreads outward from "
     "a low trunk instead of climbing. Selloum needs much more floor width."),

    # --- pothos varieties -------------------------------------------------
    ("pothos-golden", "pothos-marble-queen",
     "Same plant, different amount of white. Marble Queen carries far more "
     "variegation, which means less chlorophyll, which means it grows noticeably "
     "slower and wants brighter indirect light to hold its pattern. Golden pothos "
     "is the faster, more forgiving of the two."),

    ("pothos-golden", "pothos-neon",
     "Neon pothos is solid chartreuse rather than variegated, so it keeps golden "
     "pothos' speed and toughness while reading as a much brighter plant in a dim "
     "room. Give neon medium light -- in deep shade the colour dulls toward "
     "ordinary green."),

    ("pothos-marble-queen", "pothos-njoy",
     "N'Joy has crisp, well-separated blocks of white and green on smaller leaves; "
     "Marble Queen's variegation is speckled and streaky on larger ones. N'Joy is "
     "the slowest pothos in the range, so it stays tidy on a shelf for a long time."),

    ("pothos-golden", "satin-pothos",
     "Satin pothos (Scindapsus pictus) is a different genus wearing the pothos "
     "name. Its leaves are matte, slightly thick and dusted with silver, and it "
     "tolerates a little more humidity and slightly more light than golden pothos. "
     "Care is otherwise nearly identical."),

    # --- philodendrons ----------------------------------------------------
    ("philodendron-heartleaf", "philodendron-brasil",
     "Brasil is a variegated sport of heartleaf -- same vine, same care, with a "
     "lime-and-cream stripe down the centre of each leaf. Give Brasil brighter "
     "indirect light or the stripe fades back to plain green."),

    ("philodendron-heartleaf", "philodendron-micans",
     "Micans is the velvet one. Its leaves have a suede texture and a bronze-to-"
     "purple flush in good light, where heartleaf is glossy green. Micans wants "
     "slightly more humidity and slightly more consistent moisture."),

    ("philodendron-birkin", "philodendron-pink-princess",
     "Both are self-heading, slow and variegated, and both can revert. Birkin's "
     "white pinstripes are stable and it is much cheaper. Pink Princess needs "
     "genuinely bright indirect light to keep producing pink, and needs pruning "
     "back to a variegated node when it reverts."),

    # --- tough / low-light ------------------------------------------------
    ("snake-plant", "pothos-golden",
     "The classic beginner fork: upright or trailing. The snake plant wants less "
     "water than almost anything else in the house and stands still in a corner. "
     "Pothos grows fast enough to be satisfying and can be cut back and rooted "
     "endlessly. Both are toxic to pets."),

    ("snake-plant", "cast-iron-plant",
     "The cast iron plant handles genuine darkness better than the snake plant and "
     "is safe around cats and dogs, which the snake plant is not. The trade is "
     "speed -- the cast iron plant is one of the slowest houseplants sold."),

    ("zz-plant", "cast-iron-plant",
     "Both are dark-corner specialists. The ZZ stores water in potato-like rhizomes "
     "and would rather be forgotten entirely; the cast iron plant wants a little "
     "more regular moisture. If pets chew leaves, the cast iron plant is the safe "
     "one."),

    ("snake-plant", "whale-fin-snake-plant",
     "The whale fin is a single enormous mottled paddle rather than a clump of "
     "blades, usually sold as one or two leaves. Care is identical, but it grows "
     "even more slowly and takes up much more visual space per leaf."),

    ("snake-plant", "bird-nest-snake-plant",
     "Same plant, shrunk. The bird's nest form stays under about 30 cm in a tight "
     "rosette, so it works on a desk or shelf where the full-size snake plant needs "
     "floor space. Care is unchanged."),

    # --- succulents -------------------------------------------------------
    ("aloe-vera", "haworthia-zebra",
     "Zebra haworthia is the small, safe stand-in for aloe. It has raised white "
     "bands on dark leaves, stays under 15 cm, tolerates less light, and is "
     "non-toxic to pets. Aloe is bigger, needs more sun, and carries gel you can "
     "actually use on a burn."),

    ("aloe-vera", "jade-plant",
     "Both are sun-loving and drought-proof, but jade is a woody shrub that thickens "
     "into a miniature tree over years, while aloe stays a rosette and offsets into "
     "pups. Jade is the one to buy if you want something you can shape."),

    ("jade-plant", "succulent-echeveria",
     "Jade grows tall and branching; echeveria stays a flat, symmetrical rosette. "
     "Echeveria needs more light -- it stretches and loses its shape fast indoors -- "
     "and unlike jade it is not toxic to pets."),

    ("haworthia-zebra", "haworthia-cooperi",
     "Zebra haworthia has firm, pointed leaves with white ridges. Cooperi has "
     "swollen, translucent leaf tips -- 'windows' that let light into the plant -- "
     "and looks like a cluster of green bubbles. Cooperi is more sensitive to "
     "overwatering."),

    ("string-of-pearls", "string-of-bananas",
     "String of bananas is the easier one. Its curved, elongated beads hold more "
     "water and it grows noticeably faster, where string of pearls' round beads "
     "shrivel and drop at the first mistake. Neither is safe for pets."),

    ("string-of-pearls", "string-of-dolphins",
     "Dolphins is a hybrid with curved leaves that look like leaping fins. It is "
     "slower and fussier than pearls about light, and the dolphin shape only forms "
     "properly in bright conditions -- in low light it grows out flat and plain."),

    ("string-of-hearts", "string-of-turtles",
     "String of hearts trails metres from a shelf and grows fast; string of turtles "
     "creeps slowly and stays short, so it is a tabletop plant rather than a hanging "
     "one. Both are pet-safe. Turtles wants a little more humidity."),

    ("sedum-burrito", "string-of-bananas",
     "Burro's tail has plump, tightly packed beads that fall off the moment you "
     "brush past, so hang it where nobody walks. String of bananas is far more "
     "robust to handling and grows faster, but is toxic to pets where burro's tail "
     "is not."),

    # --- ferns ------------------------------------------------------------
    ("boston-fern", "maidenhair-fern",
     "The maidenhair is the hard one. It dies if the soil dries out even once, "
     "which makes it a terrarium or bathroom plant rather than a shelf plant. A "
     "Boston fern forgives a missed watering and just drops a few fronds. Both are "
     "pet-safe."),

    ("boston-fern", "lemon-button-fern",
     "The lemon button is a compact Boston fern relative with small round pinnae "
     "and a faint lemon scent when brushed. It stays small, grows slowly and is far "
     "less messy indoors -- the sensible fern for a bookshelf."),

    ("blue-star-fern", "kangaroo-fern",
     "Both are epiphytic ferns with leathery fronds that cope with ordinary room "
     "humidity better than most, and both are pet-safe. Blue star has blue-green, "
     "finger-lobed fronds; kangaroo fern's are glossier and more deeply cut. Blue "
     "star resents soggy soil the most of the two."),

    ("birds-nest-fern", "staghorn-fern",
     "The bird's nest grows in a pot as a rosette of wavy, undivided fronds. The "
     "staghorn is an epiphyte usually mounted on a board, watered by soaking, and "
     "hung on a wall. Choose by how you want to mount it, not by care."),

    ("boston-fern", "asparagus-fern",
     "The asparagus fern is not a fern and not pet-safe -- it is a lily relative "
     "with needle-like foliage, thorns on older stems, and berries that are toxic "
     "to cats and dogs. It is tougher and faster than a Boston fern, but the Boston "
     "fern is the one for a home with animals."),

    # --- palms ------------------------------------------------------------
    ("areca-palm", "majesty-palm",
     "Both want light and water, but the majesty palm is the one that browns out in "
     "a normal living room -- it really wants greenhouse humidity and constant "
     "moisture. The areca is the realistic indoor choice, and both are safe around "
     "cats and dogs."),

    ("kentia-palm", "parlor-palm",
     "Same low-light tolerance, very different scale and price. The parlor palm is "
     "cheap, tabletop-sized and a little short-lived indoors. The kentia is an "
     "expensive, slow-growing floor palm that will still look good in ten years. "
     "Both are pet-safe."),

    ("bamboo-palm", "lady-palm",
     "The lady palm is the more refined and more expensive of the two, with stiff, "
     "fan-shaped leaflets and a very slow, dense habit. The bamboo palm is softer, "
     "feathery and cheaper, and fills a corner faster. Both tolerate low light and "
     "both are pet-safe."),

    ("areca-palm", "cat-palm",
     "The areca is taller and more upright with golden stems; the cat palm is "
     "shorter, bushier and clumps at the base. The cat palm also wants more "
     "consistent moisture -- it browns faster than the areca if the soil dries out."),

    ("parlor-palm", "bamboo-palm",
     "Both tolerate dim rooms and both are pet-safe. The parlor palm stays small "
     "enough for a table; the bamboo palm grows into a genuine screen and is the "
     "one to buy if you want to block a view or fill a corner."),

    # --- prayer plant family ---------------------------------------------
    ("calathea-medallion", "calathea-orbifolia",
     "Orbifolia has large, round, silver-striped leaves and is the fussier of the "
     "two about water quality and humidity. Medallion's leaves are oval with "
     "purple undersides and it recovers from a dry spell a little more willingly. "
     "Both need filtered or rested water."),

    ("calathea-medallion", "prayer-plant",
     "The prayer plant (maranta) is the forgiving entry point to this family. It "
     "tolerates ordinary room humidity and average tap water far better than a "
     "calathea, trails rather than standing upright, and stays small. Both fold "
     "their leaves up at night and both are pet-safe."),

    ("calathea-medallion", "calathea-rattlesnake",
     "The rattlesnake is the toughest common calathea -- narrower, wavy leaves with "
     "dark blotches, and noticeably more tolerant of a dry afternoon than the "
     "medallion. If you have killed a calathea before, start here."),

    ("calathea-white-fusion", "stromanthe-triostar",
     "Both are white-and-green and both are difficult, but the failure mode differs. "
     "White Fusion scorches and crisps the moment humidity drops. Triostar is "
     "slightly hardier and adds pink to the mix, but it drops lower leaves if you "
     "let it dry out. Neither is a beginner plant."),

    ("prayer-plant", "stromanthe-triostar",
     "The maranta is the easier plant by a wide margin -- ordinary humidity, "
     "ordinary water, small footprint. The stromanthe is taller, showier and much "
     "more demanding about damp air. Both are pet-safe and both move their leaves "
     "on a daily rhythm."),

    # --- alocasia ---------------------------------------------------------
    ("alocasia-polly", "alocasia-zebrina",
     "Polly is grown for the leaf -- arrow-shaped, hard, deeply veined in white. "
     "Zebrina is grown for the stem, which is striped like a zebra's leg under a "
     "plainer shield-shaped leaf. Zebrina needs the brighter spot of the two to "
     "keep its stems short and upright."),

    ("alocasia-polly", "alocasia-frydek",
     "Frydek has velvet, matte-green leaves with bright white veins and is the "
     "softer-looking of the two; Polly's are glossy, stiff and more sharply lobed. "
     "Frydek is marginally more forgiving, but both go dormant and drop everything "
     "if they get cold or dry."),

    # --- ficus / trees ----------------------------------------------------
    ("fiddle-leaf-fig", "rubber-plant",
     "If you want a big-leaved indoor tree and you do not want drama, buy the rubber "
     "plant. It takes less light, less water and far more neglect than a fiddle leaf "
     "fig, which drops leaves whenever anything changes. The fiddle's leaves are "
     "bigger and more sculptural -- that is what you are paying for."),

    ("fiddle-leaf-fig", "ficus-audrey",
     "Ficus Audrey is the fiddle leaf fig's easygoing cousin: smaller, softer, "
     "velvety leaves with pale veins, and a much higher tolerance for imperfect "
     "light and inconsistent watering. It is the ficus to buy if the fiddle already "
     "beat you once."),

    ("rubber-plant", "ficus-tineke",
     "Tineke is a variegated rubber plant -- cream, green and pink on the same leaf, "
     "with a pink midrib. Care is the same, but Tineke needs brighter indirect light "
     "to hold the variegation and grows a little more slowly than the plain green "
     "form."),

    # --- flowering --------------------------------------------------------
    ("peace-lily", "anthurium",
     "Both throw a spathe around a spadix, but the anthurium's is a waxy red or pink "
     "heart that lasts for weeks, while the peace lily's is a white hood that fades "
     "to green. The peace lily flowers in much lower light; the anthurium needs a "
     "bright spot to rebloom at all."),

    ("chinese-evergreen", "dieffenbachia",
     "These are shop lookalikes. Chinese evergreen leaves are narrower, often "
     "silver or red-splashed, and the plant stays lower and tolerates deeper shade. "
     "Dieffenbachia leaves are broader and it grows faster into a cane. "
     "Dieffenbachia's sap is the more irritating of the two -- it is the one called "
     "dumb cane for a reason."),

    ("peace-lily", "chinese-evergreen",
     "Both are low-light standards. The peace lily flowers and wilts visibly when "
     "thirsty; the Chinese evergreen does neither but handles dry air and neglect "
     "better and comes in silver, red and pink forms. Both are toxic to pets."),

    ("money-tree", "pilea-peperomioides",
     "Two different plants both sold as 'money plant'. The money tree (Pachira) is a "
     "braided-trunk floor tree with palmate leaves. The Chinese money plant (Pilea) "
     "is a small tabletop plant with round, coin-like leaves on thin stalks that "
     "pups constantly. Both are pet-safe."),

    ("orchid-phalaenopsis", "anthurium",
     "The moth orchid flowers for months and then needs a rest and a cool trigger to "
     "rebloom; it grows in bark, not soil. The anthurium flowers on and off all year "
     "in an ordinary pot given enough light. The orchid is the longer show, the "
     "anthurium the steadier one."),

    ("african-violet", "cyclamen",
     "The African violet blooms indoors year-round in modest light and lives for "
     "years. The cyclamen is a winter plant that goes fully dormant in summer and is "
     "usually treated as seasonal. Cyclamen tubers are toxic to pets; African violets "
     "are not."),

    ("bromeliad-guzmania", "anthurium",
     "The guzmania's colour is a bract that lasts for months, then the mother plant "
     "dies and leaves pups behind -- it is a one-show plant that replaces itself. The "
     "anthurium keeps producing new flowers from the same plant for years. Both are "
     "easy; only the guzmania is pet-safe."),

    ("christmas-cactus", "kalanchoe",
     "The Christmas cactus is a jungle cactus -- it wants indirect light, regular "
     "water, and a cool dark autumn to set buds, and it is safe for pets. The "
     "kalanchoe is a true succulent that needs direct sun, very little water, and is "
     "toxic to cats and dogs."),

    # --- cacti ------------------------------------------------------------
    ("bunny-ears-cactus", "prickly-pear-cactus",
     "Same genus, different scale. Bunny ears stays small with paired pads and no "
     "large spines -- but it is covered in glochids, the barbed hairs that are far "
     "worse to get out of skin than a spine. The prickly pear grows large and armed, "
     "and can fruit."),

    ("golden-barrel-cactus", "old-man-cactus",
     "The golden barrel is a ribbed globe with yellow spines; the old man is a "
     "column wrapped in white hair. Both want full sun and almost no water in "
     "winter. The old man's hair mats and yellows if you water it from above -- "
     "water the soil only."),

    # --- lookalikes and odds ---------------------------------------------
    ("dracaena-marginata", "yucca",
     "Both are spiky, upright and drought-tolerant, but the yucca's leaves are stiff "
     "and sharp-tipped and it needs real sun, where the dragon tree's are soft and "
     "it copes with medium light. In a room with one bright window, the yucca takes "
     "it and the dragon tree goes elsewhere."),

    ("dracaena-marginata", "dracaena-corn-plant",
     "The dragon tree has thin, arching, red-edged blades; the corn plant has wide, "
     "strappy leaves with a pale central stripe on thicker canes. The corn plant "
     "handles low light better and gets bigger; the dragon tree stays narrower."),

    ("dracaena-lemon-lime", "dracaena-janet-craig",
     "Lemon Lime is the same plant with chartreuse-and-cream striped leaves; Janet "
     "Craig is solid dark green. Janet Craig is the better low-light performer of "
     "the two -- Lemon Lime needs medium light to keep its stripes bright."),

    ("ponytail-palm", "yucca",
     "Neither is a palm. The ponytail is a succulent with a swollen water-storing "
     "base and soft, curling leaves, and it is pet-safe. The yucca has a plain woody "
     "trunk, rigid sharp leaves, and is toxic to cats and dogs. The ponytail forgives "
     "far more neglect."),

    ("schefflera-arboricola", "schefflera-amate",
     "Same family, two scales. The dwarf umbrella tree has small leaflets and is "
     "easy to keep bushy at shelf height. Amate has large, glossy leaflets and grows "
     "into a proper indoor tree -- it needs more light and much more room."),

    ("croton", "ti-plant",
     "Both are colour plants that go dull in poor light. The croton needs the "
     "brightest spot you have and drops every leaf when it is moved; the ti plant "
     "tolerates slightly less light but is sensitive to fluoride in tap water and "
     "browns at the tips. Both are toxic to pets."),

    ("nerve-plant", "polka-dot-plant",
     "The nerve plant (fittonia) has fine white or pink veining and collapses "
     "theatrically when dry -- then recovers within an hour of water. The polka dot "
     "plant is speckled rather than veined, grows faster, and gets leggy unless you "
     "pinch it back. Both are pet-safe and both want humidity."),

    ("rex-begonia", "polka-dot-begonia",
     "Rex begonias are grown for the leaf -- spiralled, metallic, endlessly patterned "
     "-- and they are rhizomatous and prone to rot. The polka dot (maculata) is a "
     "cane begonia: tall, silver-spotted, red-backed, faster, and much easier to "
     "keep alive."),

    ("peperomia-watermelon", "peperomia-rosso",
     "Watermelon peperomia has round, silver-striped leaves on red stalks; Rosso has "
     "narrow, deeply corrugated dark leaves with wine-red undersides. Both are "
     "semi-succulent, pet-safe and happiest when you underwater rather than over."),

    ("peperomia-watermelon", "aluminum-plant",
     "Both are small plants with silver markings, but the patterns differ: the "
     "watermelon peperomia's silver runs in clean stripes from the stalk, the "
     "aluminum plant's is a quilted splash between the veins. The aluminum plant "
     "grows faster, wants steadier moisture and needs pinching to stay bushy."),

    ("peperomia-obtusifolia", "rubber-plant",
     "The baby rubber plant is not a small rubber plant -- it is a peperomia with "
     "thick, rounded, glossy leaves that stays on a shelf, and it is safe for pets. "
     "The real rubber plant (Ficus elastica) becomes a floor tree and is toxic to "
     "cats and dogs."),

    ("hoya-carnosa", "hoya-kerrii",
     "Carnosa is the vining hoya that eventually flowers in porcelain-like clusters. "
     "Kerrii is the heart-shaped one -- and the single leaf sold at Valentine's "
     "usually has no node, so it will sit there for years and never vine. Buy a "
     "kerrii with a stem if you want a plant rather than an ornament."),

    ("syngonium", "philodendron-brasil",
     "Syngonium leaves are arrow-shaped and change form as the plant matures, from "
     "compact rosette to climbing vine. Philodendron Brasil keeps its heart shape and "
     "trails from the start. Syngonium comes in pink and white forms that need "
     "brighter light to hold colour."),

    ("spider-plant", "boston-fern",
     "Two pet-safe hanging plants with different demands. The spider plant copes with "
     "dry air, missed waterings and a bright window, and hands you free babies. The "
     "Boston fern wants damp air and steady moisture, and sheds when it does not get "
     "them."),

    ("pothos-golden", "english-ivy",
     "Pothos is the indoor plant; English ivy really wants cool, bright, humid "
     "conditions and attracts spider mites in a warm dry room. Ivy clings and climbs "
     "on its own, pothos needs tying to a support. Both are toxic to pets."),

    ("spider-plant", "pothos-golden",
     "The spider plant is the pet-safe option and the one that makes babies you can "
     "root for free. Pothos tolerates darker corners and trails longer, but it is "
     "toxic to cats and dogs. For a bright kitchen with animals, take the spider "
     "plant."),

    ("bird-of-paradise", "majesty-palm",
     "Both are big, thirsty and light-hungry. The bird of paradise has broad paddle "
     "leaves that split naturally with age and needs the single brightest spot in the "
     "house. The majesty palm is feathery and pet-safe but browns badly in dry indoor "
     "air. Neither is a low-light corner plant."),

    ("lucky-bamboo", "money-tree",
     "Lucky bamboo is a dracaena grown in water or pebbles, usually on a desk, and it "
     "is toxic to pets. The money tree is a braided-trunk floor plant in soil and is "
     "pet-safe. Both are sold as luck charms; only one of them is a real tree."),

    ("hoya-carnosa", "peperomia-hope",
     "Peperomia Hope is the smaller, faster, tidier of the two, with round trailing "
     "leaves in threes. Hoya carnosa is slower and woodier but eventually flowers. "
     "Both are semi-succulent, pet-safe and prefer to dry out between waterings."),

    ("tradescantia-zebrina", "tradescantia-nanouk",
     "Zebrina is the purple-and-silver striped classic -- fast, cheap and easy to "
     "root from a cutting. Nanouk is a stockier pink-and-green cultivar with thicker "
     "leaves that holds its shape better on a shelf and needs brighter light to keep "
     "the pink."),
]


# Hand-written meta description for every pair, keyed by (plant_a, plant_b).
# Answer-first: the first clause is the answer to the query, not a restatement
# of it. One per page, never templated -- a generated description would put the
# same sentence on twenty pages, which is the problem these pages exist to fix.
DESCRIPTIONS = {
    ("pothos-golden", "philodendron-heartleaf"):
        "Pothos has thicker, waxy leaves and takes darker corners; philodendron's are "
        "softer and want a bit more light. Both easy, both toxic to pets.",
    ("snake-plant", "zz-plant"):
        "The ZZ plant is the one that truly grows in a dark corner; the snake plant "
        "needs some light or it goes leggy. Both want water barely twice a month.",
    ("monstera-deliciosa", "fiddle-leaf-fig"):
        "Buy the monstera. It is rated easy and forgives neglect; the fiddle leaf fig "
        "is rated hard and drops leaves over light, draughts or a missed watering.",
    ("peace-lily", "spider-plant"):
        "The spider plant is the pet-safe one and shrugs off dry air. The peace lily "
        "flowers in lower light but is toxic to cats and dogs.",
    ("rubber-plant", "dracaena-marginata"):
        "The dragon tree is narrower and takes medium light; the rubber plant is broad, "
        "wants a brighter spot and fills a corner. Both easy, both toxic to pets.",
    ("calathea-medallion", "boston-fern"):
        "The Boston fern is the easier of the two and only sheds when the air is dry. "
        "The calathea is rated hard and crisps without filtered water and humidity.",
    ("monstera-deliciosa", "monstera-adansonii"):
        "Deliciosa grows large with split edges; adansonii stays a small-leaved vine "
        "with holes inside the leaf. Adansonii is the one for a hanging basket.",
    ("monstera-deliciosa", "rhaphidophora-tetrasperma"):
        "Rhaphidophora tetrasperma splits its leaves immediately and stays "
        "apartment-sized. Monstera deliciosa needs years, a pole and far more floor space.",
    ("monstera-adansonii", "rhaphidophora-tetrasperma"):
        "Adansonii's holes are sealed inside the leaf; tetrasperma's are cut through to "
        "the edge. Tetrasperma grows faster and wants slightly brighter light.",
    ("monstera-deliciosa", "philodendron-selloum"):
        "Monstera climbs and its leaves have holes as well as splits. Selloum spreads "
        "outward from a low trunk with solid lobed leaves and needs far more width.",
    ("pothos-golden", "pothos-marble-queen"):
        "Marble Queen carries much more white, so it grows slower and needs brighter "
        "indirect light. Golden pothos is the faster, darker-corner-tolerant one.",
    ("pothos-golden", "pothos-neon"):
        "Neon pothos is solid chartreuse rather than variegated, so it keeps golden "
        "pothos' speed but wants medium light to stay bright rather than dull green.",
    ("pothos-marble-queen", "pothos-njoy"):
        "N'Joy has crisp blocks of white on small leaves and is the slowest pothos; "
        "Marble Queen is speckled, larger-leaved and grows noticeably faster.",
    ("pothos-golden", "satin-pothos"):
        "Satin pothos is a Scindapsus, not a pothos: matte silver-dusted leaves, a "
        "little more humidity wanted. Care is otherwise the same easy, low-water routine.",
    ("philodendron-heartleaf", "philodendron-brasil"):
        "Brasil is a variegated heartleaf - identical care, plus a lime stripe that "
        "fades to plain green unless you give it brighter indirect light.",
    ("philodendron-heartleaf", "philodendron-micans"):
        "Micans is the velvet one, with bronze-purple leaves and a thirstier, more "
        "humidity-hungry habit. Heartleaf is glossy and the easier of the two.",
    ("philodendron-birkin", "philodendron-pink-princess"):
        "Identical care; Birkin's white pinstripes are stable and cheap, while Pink "
        "Princess needs bright indirect light and pruning to keep producing pink.",
    ("snake-plant", "pothos-golden"):
        "Snake plant if the corner is dark and you water rarely; pothos if you want "
        "fast trailing growth and free cuttings. Both are toxic to cats and dogs.",
    ("snake-plant", "cast-iron-plant"):
        "The cast iron plant is pet-safe and handles genuine darkness better; the snake "
        "plant is faster to establish but toxic to cats and dogs.",
    ("zz-plant", "cast-iron-plant"):
        "Both thrive in dark corners. The ZZ wants to be forgotten between waterings; "
        "the cast iron plant needs a little more moisture but is safe around pets.",
    ("snake-plant", "whale-fin-snake-plant"):
        "Same care, different scale: the whale fin is one enormous mottled paddle "
        "instead of a clump of blades, and it takes far longer to fill a pot.",
    ("snake-plant", "bird-nest-snake-plant"):
        "The bird's nest form is the same plant shrunk to a 30 cm rosette - desk-sized, "
        "identical care. Take the full-size snake plant if you want floor presence.",
    ("aloe-vera", "haworthia-zebra"):
        "Zebra haworthia is the pet-safe, shelf-sized stand-in: white-banded leaves, "
        "less light needed. Aloe is bigger, wants more sun and is toxic to pets.",
    ("aloe-vera", "jade-plant"):
        "Same sun and near-zero watering; jade becomes a woody miniature tree you can "
        "shape, aloe stays a rosette and pups. Both are toxic to cats and dogs.",
    ("jade-plant", "succulent-echeveria"):
        "Echeveria is pet-safe and stays a flat rosette but stretches without strong "
        "light. Jade grows into a branching shrub and is toxic to cats and dogs.",
    ("haworthia-zebra", "haworthia-cooperi"):
        "Care is identical. Zebra has firm pointed leaves with white ridges; Cooperi is "
        "a cluster of translucent green bubbles and rots faster if overwatered.",
    ("string-of-pearls", "string-of-bananas"):
        "String of bananas is the easier one - its beads hold more water and it grows "
        "faster. String of pearls shrivels at the first watering mistake.",
    ("string-of-pearls", "string-of-dolphins"):
        "Same care; dolphins is slower and only forms its curved fins in bright light, "
        "where pearls grows faster and rounder. Both are toxic to pets.",
    ("string-of-hearts", "string-of-turtles"):
        "String of hearts trails metres and grows fast; string of turtles creeps slowly "
        "and stays a tabletop plant. Both pet-safe; turtles wants more humidity.",
    ("sedum-burrito", "string-of-bananas"):
        "Burro's tail is pet-safe but drops beads if you brush it; string of bananas "
        "handles handling and grows faster, but is toxic to cats and dogs.",
    ("boston-fern", "maidenhair-fern"):
        "The Boston fern forgives a missed watering; the maidenhair dies if the soil "
        "dries once, so it is a bathroom or terrarium plant. Both are pet-safe.",
    ("boston-fern", "lemon-button-fern"):
        "The lemon button fern is the tidy one: small, slow, far less shedding, and "
        "rated easy. The Boston fern gets big and litters the floor with fronds.",
    ("blue-star-fern", "kangaroo-fern"):
        "Identical care and both pet-safe. Blue star has blue-green finger-lobed fronds "
        "and hates soggy soil; kangaroo fern's are glossier and more deeply cut.",
    ("birds-nest-fern", "staghorn-fern"):
        "Choose by mounting, not care: the bird's nest sits in a pot as a rosette, the "
        "staghorn hangs on a board and is watered by soaking. Both are pet-safe.",
    ("boston-fern", "asparagus-fern"):
        "The asparagus fern is not a fern and is toxic to cats and dogs - it has thorns "
        "and toxic berries. For a home with animals, take the Boston fern.",
    ("areca-palm", "majesty-palm"):
        "The areca is the realistic indoor palm - rated medium where the majesty is "
        "hard and browns in dry room air. Both are safe around cats and dogs.",
    ("kentia-palm", "parlor-palm"):
        "Both take low light and both are pet-safe. The parlor palm is cheap and "
        "tabletop-sized; the kentia is a slow, expensive floor palm that lasts decades.",
    ("bamboo-palm", "lady-palm"):
        "Identical care, both pet-safe, both fine in low light. The lady palm is "
        "slower, stiffer and pricier; the bamboo palm fills a corner faster.",
    ("areca-palm", "cat-palm"):
        "The cat palm is shorter, bushier and takes slightly less light, but browns "
        "faster when dry. The areca is taller and more upright. Both are pet-safe.",
    ("parlor-palm", "bamboo-palm"):
        "Same care, both pet-safe, both fine in low light. The parlor palm stays "
        "table-sized; the bamboo palm grows into a screen for blocking a view.",
    ("calathea-medallion", "calathea-orbifolia"):
        "Both are rated hard with identical needs. Orbifolia's big silver-striped "
        "leaves are fussier about water quality; medallion recovers from a dry spell better.",
    ("calathea-medallion", "prayer-plant"):
        "The prayer plant is the forgiving one - medium not hard, fine in ordinary room "
        "humidity and tap water. The calathea crisps without filtered water.",
    ("calathea-medallion", "calathea-rattlesnake"):
        "The rattlesnake plant is the toughest common calathea, rated medium where the "
        "medallion is hard. Start here if a calathea has beaten you before.",
    ("calathea-white-fusion", "stromanthe-triostar"):
        "Identical demands, different failure: White Fusion scorches when humidity "
        "drops, Triostar drops lower leaves when dry. Neither is a beginner plant.",
    ("prayer-plant", "stromanthe-triostar"):
        "The prayer plant wins on ease - medium, small, fine in normal humidity. The "
        "stromanthe is taller and showier but rated hard. Both are pet-safe.",
    ("alocasia-polly", "alocasia-zebrina"):
        "Same care. Polly is grown for its hard, white-veined arrow leaves; zebrina for "
        "its striped stems. Zebrina needs the brighter spot to stay upright.",
    ("alocasia-polly", "alocasia-frydek"):
        "Frydek is the slightly more forgiving one - velvet leaves, rated medium where "
        "Polly is hard. Both go dormant and drop everything if cold or dry.",
    ("fiddle-leaf-fig", "rubber-plant"):
        "Take the rubber plant: rated easy, less light, less water, far more neglect "
        "tolerated. The fiddle leaf fig is rated hard and drops leaves over anything.",
    ("fiddle-leaf-fig", "ficus-audrey"):
        "Ficus Audrey is the easier fiddle leaf: velvety leaves, rated medium not hard, "
        "and much more tolerant of imperfect light and inconsistent watering.",
    ("rubber-plant", "ficus-tineke"):
        "Care is the same; Tineke is the variegated rubber plant with cream and pink "
        "leaves, and it needs brighter indirect light to hold that colour.",
    ("peace-lily", "anthurium"):
        "The peace lily is easier and flowers in far lower light; the anthurium's waxy "
        "red spathes last weeks but need a bright spot. Both are toxic to pets.",
    ("chinese-evergreen", "dieffenbachia"):
        "Chinese evergreen takes darker rooms and stays lower; dieffenbachia grows "
        "faster into a cane and has the more irritating sap. Both are toxic to pets.",
    ("peace-lily", "chinese-evergreen"):
        "The Chinese evergreen handles dry air and neglect better; the peace lily "
        "flowers and wilts visibly when thirsty. Both are toxic to cats and dogs.",
    ("money-tree", "pilea-peperomioides"):
        "Two plants sold as 'money plant': the Pachira is a braided floor tree, the "
        "Pilea a small coin-leaved tabletop plant that pups. Both are pet-safe.",
    ("orchid-phalaenopsis", "anthurium"):
        "The moth orchid is pet-safe and flowers for months in bark, then rests. The "
        "anthurium flowers year-round in soil but is toxic to cats and dogs.",
    ("african-violet", "cyclamen"):
        "The African violet is pet-safe and blooms indoors year-round for years. The "
        "cyclamen is a winter plant that goes dormant, and its tubers are toxic.",
    ("bromeliad-guzmania", "anthurium"):
        "The bromeliad is pet-safe but flowers once and dies, leaving pups. The "
        "anthurium reblooms for years from the same plant but is toxic to pets.",
    ("christmas-cactus", "kalanchoe"):
        "The Christmas cactus is pet-safe and wants indirect light and regular water. "
        "The kalanchoe needs full sun and almost none, and is toxic to cats and dogs.",
    ("bunny-ears-cactus", "prickly-pear-cactus"):
        "Same care, different scale. Bunny ears stays small and has no big spines - "
        "just glochids, which are worse. The prickly pear gets large, armed and fruits.",
    ("golden-barrel-cactus", "old-man-cactus"):
        "Identical care: full sun, almost no winter water. The golden barrel is a "
        "ribbed globe with yellow spines; the old man is a column wrapped in white hair.",
    ("dracaena-marginata", "yucca"):
        "The dragon tree copes with medium light and has soft leaves; the yucca needs a "
        "genuinely sunny window and has rigid, sharp tips. Both are toxic to pets.",
    ("dracaena-marginata", "dracaena-corn-plant"):
        "The corn plant handles lower light and grows bigger, with wide striped leaves; "
        "the dragon tree stays narrow with thin red-edged blades. Both are easy.",
    ("dracaena-lemon-lime", "dracaena-janet-craig"):
        "Janet Craig is the better low-light plant of the two; Lemon Lime needs medium "
        "light to keep its chartreuse stripes bright. Care is otherwise identical.",
    ("ponytail-palm", "yucca"):
        "Neither is a palm. The ponytail is pet-safe, stores water in a swollen base "
        "and forgives neglect; the yucca has sharp leaves and is toxic to pets.",
    ("schefflera-arboricola", "schefflera-amate"):
        "The dwarf umbrella tree stays shelf-sized on slightly less light; Amate has "
        "large glossy leaflets and becomes a full indoor tree. Both are toxic to pets.",
    ("croton", "ti-plant"):
        "The croton needs the brightest spot you have and drops leaves when moved; the "
        "ti plant takes less light but browns from fluoride in tap water.",
    ("nerve-plant", "polka-dot-plant"):
        "The polka dot plant is the easier one and grows faster, but needs pinching. "
        "The nerve plant collapses dramatically when dry, then recovers in an hour.",
    ("rex-begonia", "polka-dot-begonia"):
        "The polka dot (maculata) is the easier cane begonia - tall, silver-spotted, "
        "fast. The rex is a rhizomatous leaf plant, prone to rot, wanting less light.",
    ("peperomia-watermelon", "peperomia-rosso"):
        "Identical care, both pet-safe, both happier underwatered. Watermelon has round "
        "silver-striped leaves; Rosso narrow corrugated ones with wine-red backs.",
    ("peperomia-watermelon", "aluminum-plant"):
        "The peperomia's silver runs in clean stripes and it stores water in its "
        "leaves; the aluminum plant's is a quilted splash and it wants steadier moisture.",
    ("peperomia-obtusifolia", "rubber-plant"):
        "The baby rubber plant is a pet-safe shelf peperomia, not a small Ficus "
        "elastica. The real rubber plant becomes a floor tree and is toxic to pets.",
    ("hoya-carnosa", "hoya-kerrii"):
        "Same care. Carnosa vines and eventually flowers; kerrii is the heart leaf - "
        "and the single leaf sold at Valentine's has no node, so it never grows.",
    ("syngonium", "philodendron-brasil"):
        "Syngonium's arrow leaves change shape as it matures and it wants a touch more "
        "water; Brasil keeps its heart shape and trails from day one. Both toxic.",
    ("spider-plant", "boston-fern"):
        "Two pet-safe hangers: the spider plant is easier, copes with dry air and makes "
        "free babies. The Boston fern wants damp air and sheds when it dries out.",
    ("pothos-golden", "english-ivy"):
        "Pothos is the better indoor plant - it takes darker corners and warm dry "
        "rooms. English ivy wants cool humid air and gets spider mites indoors.",
    ("spider-plant", "pothos-golden"):
        "The spider plant is pet-safe and hands you free plantlets; pothos tolerates "
        "darker corners and trails longer but is toxic to cats and dogs.",
    ("bird-of-paradise", "majesty-palm"):
        "Both are big and light-hungry. The majesty palm is pet-safe but browns in dry "
        "air; the bird of paradise needs your brightest window and is toxic to pets.",
    ("lucky-bamboo", "money-tree"):
        "The money tree is pet-safe and a proper floor plant in soil. Lucky bamboo is a "
        "dracaena grown in water on a desk, and it is toxic to cats and dogs.",
    ("hoya-carnosa", "peperomia-hope"):
        "Peperomia Hope is smaller, faster and tidier; hoya carnosa is slower and "
        "woodier but eventually flowers. Both pet-safe, both happiest left to dry out.",
    ("tradescantia-zebrina", "tradescantia-nanouk"):
        "Zebrina is the fast purple-and-silver classic that roots from any cutting; "
        "Nanouk is stockier and pink but needs brighter light to keep that colour.",
}
