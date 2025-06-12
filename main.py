import tkinter as tk
from tkinter import ttk, messagebox
from urllib.parse import quote
import webbrowser
import ctypes
import os
import sys

VALID_WEAPONS = [
    "AK-47", "M4A4", "M4A1-S", "AWP", "MAG-7", "Glock-18", "Desert Eagle", "P250",
    "USP-S", "Five-SeveN", "Tec-9", "CZ75-Auto", "FAMAS", "Galil AR", "SSG 08",
    "Negev", "XM1014", "Sawed-Off", "Nova", "MP9", "MP7", "MP5-SD", "UMP-45",
    "P90", "PP-Bizon", "MAC-10", "M249", "R8 Revolver"
]

VALID_SKINS = [
    "Abyss", "Abyssal Apparition", "Acheron", "Acid Dart", "Acid Etched", "Acid Fade", "Acid Hex", "Acid Wash",
    "Aerial", "Afterimage", "Agent", "Airlock", "Akihabara Accept", "Akoben", "Allure", "Aloha", "Alpine Camo",
    "Amber Fade", "Amber Slipstream", "Analog Input", "Ancient Earth", "Ancient Lore", "Ancient Ritual",
    "Ancient Visions", "Angry Mob", "Anodized Gunmetal", "Anodized Navy", "Anolis", "Antique", "Apep's Curse",
    "Apocalypto", "Aqua Terrace", "Aquamarine Revenge", "Arctic Camo", "Arctic Tri-Tone", "Arctic Wolf",
    "Aristocrat", "Armor Core", "Army Mesh", "Army Recon", "Army Sheen", "Arsenic Spill", "Ash Wood", "Asiimov",
    "Assault", "Asterion", "Astral Jörmungandr", "Astrolabe", "Atheris", "Atlas", "Atomic Alloy", "Attack Vector",
    "Autotronic", "Autumn Thicket", "Autumn Twilly", "Avalanche", "AXIA", "Aztec", "Azure Glyph", "Azure Zebra",
    "B the Monster", "Bad Trip", "Balance", "Bamboo Forest", "Bamboo Garden", "Bamboo Print", "Bamboo Shadow",
    "Bamboozle", "Banana Cannon", "Banana Leaf", "Baroque Orange", "Baroque Purple", "Baroque Red", "Barricade",
    "Basilisk", "Basket Halftone", "Bengal Tiger", "Berries And Cherries", "Berry Gel Coat", "BI83 Spectrum",
    "Big Iron", "Bioleak", "Black & Tan", "Black Laminate", "Black Limba", "Black Lotus", "Black Nile", "Black Sand",
    "Black Tie", "Blast From the Past", "Blaze", "Blaze Orange", "Bleached", "Bleeding Edge", "Blind Spot",
    "Blizzard Marbleized", "Block-18", "Blood in the Water", "Blood Tiger", "Bloodshot", "Bloodsport", "Bloomstick",
    "Blue Blast", "Blue Fissure", "Blue Laminate", "Blue Phosphor", "Blue Ply", "Blue Spruce", "Blue Steel",
    "Blue Streak", "Blue Tac", "Blue Tire", "Blue Titanium", "Blueprint", "Blush Pour", "Bone Forged", "Bone Machine",
    "Bone Mask", "Bone Pile", "BOOM", "Boost Protocol", "BorDeux", "Boreal Forest", "Boroque Sand", "Brake Light",
    "Brass", "Bratatat", "Breaker Box", "Briar", "Briefing", "Bright Water", "Bronze Deco", "Bronzer", "Brother",
    "Buddy", "Buff Blue", "Bulkhead", "Bulldozer", "Bullet Queen", "Bullet Rain", "Bunsen Burner", "Business Class",
    "Button Masher", "Buzz Kill", "Caged Steel", "Caiman", "Calf Skin", "CaliCamo", "Canal Spray", "Candy Apple",
    "Canvas Cloud", "Capillary", "Caramel", "Carbon Fiber", "Cardiac", "Carnivore", "Cartel", "Carved Jade",
    "Case Hardened", "Cassette", "Catacombs", "CAUTION!", "Cerberus", "Chainmail", "Chalice", "Chameleon",
    "Chantico's Fire", "Charged Up", "Charter", "Chatterbox", "Check Engine", "Chemical Green", "Choppa", "Chopper",
    "Chromatic Aberration", "Chrome Cannon", "Chronos", "Cinquedea", "Circaetus", "Cirrus", "Citric Acid",
    "Classic Crate", "Clay Ambush", "Clear Polymer", "CMYK", "Co-Processor", "Coach Class", "Cobalt Core",
    "Cobalt Disruption", "Cobalt Grip", "Cobalt Halftone", "Cobalt Paisley", "Cobalt Quartz", "Cobra Strike",
    "Cocoa Rampage", "Code Red", "Cold Blooded", "Cold Cell", "Cold Fusion", "Colony", "Colony IV", "Commando Company",
    "Commemoration", "Commuter", "Condemned", "Condition Zero", "Connexion", "Conspiracy", "Constructivist",
    "Containment Breach", "Contaminant", "Contamination", "Contractor", "Contrast Spray", "Control", "Control Panel",
    "Converter", "Coolant", "Copper", "Copper Borre", "Copper Coated", "Copper Fiber", "Copper Galaxy",
    "Copper Oxide", "Copperflage", "Copperhead", "Coral Bloom", "Coral Halftone", "Core Breach", "Corinthian",
    "Corporal", "Cortex", "Corticera", "Counter Terrace", "Cracked Opal", "Crakow!", "Crime Scene",
    "Crimson Blossom", "Crimson Foil", "Crimson Kimono", "Crimson Tsunami", "Crimson Web", "Crossfade", "Crypsis",
    "Curse", "Cut Out", "Cyanospatter", "Cyber Security", "Cyber Shell", "Cyberforce", "Cyrex", "Daedalus",
    "Damascus Steel", "Danger Close", "Dark Age", "Dark Blossom", "Dark Filigree", "Dark Sigil", "Dark Water",
    "Darkwing", "Dart", "Day Lily", "Daybreak", "Dazzle", "Deadly Poison", "Death by Kitty", "Death by Puppy", "Death Grip",
    "Death Rattle", "Death Strike", "Death's Head", "Decimator", "Decommissioned", "Deep Relief",
    "Delusion", "Demeter", "Demolition", "Derailment", "Desert Blossom", "Desert Brush",
    "Desert DDPAT", "Desert Halftone", "Desert Hydra", "Desert Storm", "Desert Strike",
    "Desert Tactical", "Desert Warfare", "Desert-Strike", "Desolate Space", "Destroyer", "Detour",
    "dev_texture", "Devourer", "Dezastre", "Digital Architect", "Digital Mesh", "Directive",
    "Dirt Drop", "Disco Tech", "Dispatch", "Distressed", "Djinn", "Doomkitty", "Doppler",
    "Downtown", "Dragon Lore", "Dragon Snore", "Dragon Tattoo", "Dragon Tech", "Dragonfire",
    "Dream Glade", "Drift Wood", "Drop Me", "Drought", "Dry Season", "Dualing Dragons", "Duality",
    "Duelist", "Dusk Ruins", "Echoing Sands", "Eco", "Electric Blue", "Electric Hive", "Elegant Vines",
    "Elite 1.6", "Elite Build", "Embargo", "Emerald", "Emerald Dragon", "Emerald Jörmungandr",
    "Emerald Pinstripe", "Emerald Poison Dart", "Emerald Quartz", "Emphorosaur-S", "Enforcer",
    "Ensnared", "Entombed", "Etch Lord", "Evil Daimyo", "Exchanger", "Exo", "Exoskeleton",
    "Exposure", "Eye of Athena", "Eye of Horus", "Eye of Zapems", "Facets", "Facility Dark",
    "Facility Draft", "Facility Negative", "Facility Sketch", "Fade", "Faded Zebra", "Fairy Tale",
    "Fall Hazard", "Fallout Warning", "Faulty Wiring", "Featherweight", "Fennec Fox", "Fever Dream",
    "Fire Elemental", "Fire Serpent", "Firefight", "Firestarter", "First Class", "Fizzy POP",
    "Flame Jörmungandr", "Flame Test", "Flash Out", "Flashback", "Fleet Flock", "Flora Carnivora",
    "Flux", "Food Chain", "Foresight", "Forest DDPAT", "Forest Leaves", "Forest Night", "Fowl Play",
    "Fragments", "Framework", "Franklin", "Freehand", "Freight", "Frontside Misty", "Frost Borre",
    "Fubar", "Fuel Injector", "Fuel Rod", "Full Stop", "Gamma Doppler", "Garter-9", "Gator Mesh",
    "Gauss", "Ghost Camo", "Ghost Crusader", "Gila", "Glacier Mesh", "Glitched Paint",
    "Global Offensive", "Glockingbird", "Gnarled", "Gold Arabesque", "Gold Bismuth", "Gold Brick",
    "Gold Leaf", "Golden Coil", "Golden Koi", "Goo", "Grand Prix", "Granite Marbleized", "Graphite",
    "Grassland", "Grassland Leaves", "Graven", "Green Apple", "Green Cell", "Green Ceramic",
    "Green Energy", "Green Laminate", "Green Line", "Green Marine", "Green Plaid", "Green Swirl",
    "Grey Ghost", "Grey Smoke", "Griffin", "Grim", "Grinder", "Grip", "Grotto", "Groundwater",
    "Guardian", "Guerrilla", "Gum Wall Camo", "Gungnir", "Gunsmoke", "Hades", "Half Sleeve",
    "Halftone Shift", "Halftone Wash", "Halftone Whorl", "Hand Brake", "Hand Cannon", "Handgun",
    "Hard Water", "Harvester", "Hazard", "Hazard Pay", "Head Shot", "Heat", "Heat Treated",
    "Heaven Guard", "Heavy Metal", "Heirloom", "Heist", "Hellfire", "Hellish", "Hemoglobin",
    "Hexane", "Hideout", "Hieroglyph", "High Beam", "High Roller", "High Seas", "Highwayman", "Hive",
    "Hot Rod", "Hot Shot", "Hot Snakes", "Houndstooth", "Howl", "Humidor", "Hunter", "Hunting Blind",
    "Hybrid", "Hydra", "Hydroponic", "Hyper Beast", "Hypnotic", "Icarus Fell", "Ice Cap", "Ice Coaled",
    "Imminent Danger", "Impact Drill", "Imperial", "Imperial Dragon", "Impire", "Imprint",
    "In Living Color", "Incinegator", "Indigo", "Inferno", "Infrastructure", "Inheritance", "Inlay",
    "Insomnia", "Integrale", "Interlock", "Irezumi", "Iron Clad", "Ironwork", "Irradiated Alert",
    "Isaac", "Ivory", "Jaguar", "Jambiya", "Jawbreaker", "Jet Set", "Judgement of Anubis", "Jungle",
    "Jungle Dashed", "Jungle DDPAT", "Jungle Slipstream", "Jungle Spray", "Jungle Thicket", "Jungle Tiger", "Junk Yard", "Just Smile", "Justice", "K.O. Factory",
    "Kami", "Keeping Tabs", "Kill Confirmed", "Kiss♥Love", "Kitbash", "Knight", "Koi",
    "Kumicho Dragon", "Lab Rats", "Labyrinth", "Lapis Gator", "Last Dive", "Late Night Transit",
    "Latte Rush", "Lead Conduit", "Leaded Glass", "Leafhopper", "Leather", "Leet Museo",
    "Legion of Anubis", "Lichen Dashed", "Lifted Spirits", "Light Box", "Light Rail",
    "Lightning Strike", "Lil' Pig", "Lime Hex", "Limelight", "Lionfish", "Liquidation",
    "Llama Cannon", "LongDog", "Lore", "Loudmouth", "Lumen", "Lush Ruins", "Macabre", "Magma",
    "Magna Carta", "Magnesium", "Mainframe", "Mainframe 001", "Malachite", "Man-o'-war",
    "Mandrel", "Marble Fade", "Marina", "Marsh", "Marsh Grass", "Master Piece", "Mayan Dreams",
    "Mecha Industries", "Mechanism", "Medusa", "Mehndi", "Melondrama", "Meltdown", "Memento",
    "Memorial", "Meow 36", "Metal Flowers", "Metallic DDPAT", "Metallic Squeezer", "Meteorite",
    "Midnight Laminate", "Midnight Lily", "Midnight Paintover", "Midnight Palm", "Midnight Storm",
    "Minotaur's Labyrinth", "Mint Fan", "Mint Kimono", "Mischief", "Mjölnir", "Mockingbird",
    "Modern Hunter", "Modest Threat", "Module", "Momentum", "Monkey Business", "Monkeyflage",
    "Monster Call", "Monster Mashup", "Monster Melt", "Moon in Libra", "Moonrise", "Morris",
    "Mortis", "Mosaico", "Moss Quartz", "Motherboard", "Motorized", "Mount Fuji", "Mud-Spec",
    "Mudder", "Muertos", "Mulberry", "Multi-Terrain", "Mummy's Rot", "Murky", "Music Box",
    "Mustard Gas", "Naga", "Naval Shred Camo", "Navy Murano", "Navy Sheen", "Nebula Crusader",
    "Necro Jr.", "Necropos", "Nemesis", "Neo-Noir", "Neon Kimono", "Neon Ply", "Neon Revolution",
    "Neon Rider", "Neon Squeezer", "Neoqueen", "Neural Net", "Nevermore", "New Roots", "Nexus",
    "Night", "Night Borre", "Night Camo", "Night Heist", "Night Ops", "Night Riot", "Night Stripe",
    "Night Terror", "Nightmare", "Nightshade", "Nightwish", "Nitro", "Nostalgia", "Nouveau Rouge",
    "Nuclear Garden", "Nuclear Threat", "Nuclear Waste", "NV", "O-Ranger", "O.S.I.P.R.",
    "Obsidian", "Ocean Drive", "Ocean Foam", "Ocean Topo", "Oceanic", "Off World", "Oil Change",
    "Ol' Rusty", "Old Roots", "Olive Plaid", "Olive Polycam", "Olympus", "Oni Taiji",
    "Orange Anolis", "Orange Crash", "Orange DDPAT", "Orange Filigree", "Orange Kimono",
    "Orange Murano", "Orange Peel", "Orbit Mk01", "Origami", "Orion", "Oscillator", "Osiris",
    "Ossified", "Outbreak", "Overgrowth", "Oxide Blaze", "Oxide Oasis", "Palm", "Pandora's Box",
    "Panther", "Panther Camo", "Panthera onca", "Para Green", "Parallax", "Parched",
    "Pathfinder", "PAW", "PC-GRN", "Petroglyph", "Phantom", "Phantom Disruptor", "Phobos",
    "Phoenix Blacklight", "Phoenix Chalk", "Phoenix Marker", "Phoenix Stencil", "Phosphor",
    "Photic Zone", "Pilot", "Pine", "Pink DDPAT", "Pink Pearl", "Pipe Down", "Pipsqueak",
    "Pit Viper", "Plague", "Plastique", "Player Two", "Plum Netting", "Plume", "Point Disarray",
    "Poison Dart", "Polar Camo", "Polar Mesh", "Pole Position", "Polished Malachite", "Poly Mag",
    "Polymer", "Polysoup", "POP AWP", "Popdog", "Poplar Thicket", "Poseidon", "Poultrygeist",
    "Power Loader", "Powercore", "Praetorian", "Predator", "Prey", "Primal Saber",
    "Prime Conspiracy", "Printstream", "Prism Terrace", "Propaganda", "Prototype", "Pulse", "Purple DDPAT", "Pyre", "Quick Sand",
    "Quicksilver", "Radiation Hazard", "Rain Station", "Rainbow Spoon", "Ramese's Reach",
    "Random Access", "Rangeen", "Ranger", "Rapid Eye Movement", "Rat Rod", "Raw Ceramic",
    "Re-Entry", "Re.built", "Reactor", "Rebel", "Reboot", "Red Astor", "Red DDPAT",
    "Red Filigree", "Red FragCam", "Red Jasper", "Red Laminate", "Red Leather", "Red Python",
    "Red Quartz", "Red Rock", "Red Stone", "Red Tide", "Red Tire", "Redline", "Reef Grief",
    "Remote Control", "Resupply", "Retribution", "Retrobution", "Ricochet", "Riot", "Ripple",
    "Rising Skull", "Rising Sun", "Road Rash", "Roadblock", "Robin's Egg", "Rocket Pop",
    "Roll Cage", "Rose Hex", "Rose Iron", "Rose Nacre", "Royal Baroque", "Royal Blue",
    "Royal Consorts", "Royal Guard", "Royal Legion", "Royal Paladin", "Ruby Poison Dart",
    "Run and Hide", "Run Run Run", "Runic", "Runoff", "Rust Coat", "Rust Leaf", "Sacrifice",
    "Safari Mesh", "Safety Net", "Sage Camo", "Sage Spray", "Sakkaku", "Sand Dashed", "Sand Dune",
    "Sand Mesh", "Sand Scale", "Sand Spray", "Sand Storm", "Sandstorm", "Savannah Halftone",
    "Scaffold", "ScaraB Rush", "Scavenger", "Schematic", "Scorched", "Scorpion", "Scrawl",
    "Scumbria", "Sea Calico", "Seabird", "Searing Rage", "Seasons", "Sedimentary", "See Ya Later",
    "Serenity", "Sergeant", "Serpent Strike", "Serum", "Setting Sun", "Shallow Grave",
    "Shapewood", "Shattered", "Sheet Lightning", "Shinobu", "Shipping Forecast", "Short Ochre",
    "Shred", "Shredded", "Sienna Damask", "Signal", "Silk Tiger", "Silver", "Silver Quartz",
    "Skull Crusher", "Skulls", "Sky Blue", "Slag", "Slalom", "Slashed", "Slate", "Slaughter",
    "Slide", "Slipstream", "Small Game", "Snack Attack", "Snake Camo", "Snake Pit", "Snek-9",
    "Sobek's Bite", "Solitude", "Sonar", "Sour Grapes", "Space Cat", "Space Race",
    "Spalted Wood", "Special Delivery", "Spectre", "Spectrogram", "Spider Lily", "Spirit Board",
    "Spitfire", "Splash", "Splash Jam", "Spring Twilly", "Sputnik", "Stained", "Stained Glass",
    "Stainless", "Stalker", "Starcade", "Starlight Protector", "Statics", "Steel Delta",
    "Steel Disruption", "Steel Sentinel", "Steel Work", "Stinger", "Stone Cold", "Stone Mosaico",
    "Storm", "Storm Camo", "Straight Dimes", "Stratosphere", "Strats", "Stymphalian", "Styx",
    "Submerged", "Sugar Rush", "Sun in Leo", "Sunbaked", "Sundown", "Sunset Lily",
    "Sunset Storm 壱", "Sunset Storm 弐", "Supernova", "Sure Grip", "Surfwood", "Surveillance",
    "Survivalist", "Survivor Z", "SWAG-7", "Swamp DDPAT", "Sweeper", "Sweet Little Angels",
    "Switch Board", "Syd Mead", "Syndicate", "Synth Leaf", "System Lock", "Tacticat", "Tall Grass",
    "Target Acquired", "Tatter", "Teal Blossom", "Teal Graf", "Teardown", "Teclu Burner",
    "Tempest", "Temukau", "Terrace", "Terrain", "The Battlestar", "The Bronze", "The Coalition",
    "The Emperor", "The Empress", "The Executioner", "The Fuschia Is Now", "The Kraken",
    "The Prince", "The Traitor", "Threat Detected", "Ticket to Hell", "Tiger Moth", "Tiger Pit",
    "Tiger Stencil", "Tiger Tear", "Tiger Tooth", "Tigris", "Tilted", "Titanium Bit", "Tom Cat",
    "Tooth Fairy", "Torn", "Tornado", "Torque", "Tosai", "Toxic", "Toy Soldier", "Toybox",
    "Traction", "Tranquility", "Traveler", "Tread", "Tread Plate", "Triarch", "Trigger Discipline", "Trigon", "Triqua", "Triumvirate",
    "Tropical Breeze", "Tropical Storm", "Turbo Peek", "Turf", "Turquoise Pour", "Tuxedo",
    "Twilight Galaxy", "Twin Turbo", "Twist", "Ultralight", "Ultraviolet", "Umbral Rabbit",
    "Uncharted", "Undertow", "Urban Dashed", "Urban DDPAT", "Urban Hazard", "Urban Masked",
    "Urban Perforated", "Urban Rubble", "Urban Shock", "Valence", "Vandal", "VariCamo",
    "VariCamo Blue", "VariCamo Grey", "Vault Heist", "Vendetta", "Vent Rush", "Ventilator",
    "Ventilators", "Verdant Growth", "Verdigris", "Victoria", "Vino Primo", "Violent Daimyo",
    "Violet Murano", "Virus", "Visions", "Vogue", "Vulcan", "Wall Bang", "Walnut", "Warbird",
    "Warhawk", "Wash me", "Wash me plz", "Wasteland Princess", "Wasteland Rebel", "Watchdog",
    "Water Elemental", "Water Sigil", "Waters of Nephthys", "Wave Breaker", "Wave Spray",
    "Waves Perforated", "Weasel", "Welcome to the Jungle", "Whitefish", "Whiteout",
    "Wicked Sick", "Wild Berry", "Wild Child", "Wild Lily", "Wild Lotus", "Wild Six",
    "Wildfire", "Wildwood", "Windblown", "Wings", "Wingshot", "Winter Forest", "Wintergreen",
    "Winterized", "Withered Vine", "Wood Block Camo", "Wood Fired", "Woodsman", "Worm God",
    "Wraiths", "Wurst Hölle", "X-Ray", "X-Ray (P250)", "Xiangliu", "XOXO", "Yellow Jacket",
    "Yeti Camo", "Yorick", "Yorkshire", "Zander", "Zeno", "Ziggy", "Zirka", "Zombie Offensive",
    "ZX Spectron", "龍王 (Dragon King)"
]

VALID_CONDITIONS = [
    "Factory New", "Minimal Wear", "Field-Tested", "Well-Worn", "Battle-Scarred"
]

UV_COLOR = "#7F00FF"
BG_COLOR = "#1a1a1a"
FG_COLOR = "#e0e0e0"

def create_steam_market_url(weapon, skin_name, condition=None, stat_track=False, souvenir=False):
    prefix = ""
    if stat_track:
        prefix += "StatTrak™ "
    if souvenir:
        prefix += "Souvenir "
    
    item_name = f"{prefix}{weapon} | {skin_name}"
    if condition:
        item_name += f" ({condition})"
    
    encoded_item_name = quote(item_name)
    return "https://steamcommunity.com/market/listings/730/" + encoded_item_name

def open_url_in_new_window(root, url):
    win = tk.Toplevel(root)
    win.title("Resulting URL")
    win.geometry("500x150")
    win.configure(bg=BG_COLOR)

    tk.Label(win, text="Resulting URL:", bg=BG_COLOR, fg=UV_COLOR, font=("Arial", 12, "bold")).pack(pady=5)
    url_text = tk.Text(win, height=3, wrap="word", bg="#2a2a2a", fg=FG_COLOR, relief="flat")
    url_text.pack(fill=tk.BOTH, padx=10)
    url_text.insert(tk.END, url)
    url_text.config(state='disabled')

    def open_in_browser():
        webbrowser.open(url)

    open_btn = tk.Button(win, text="Go to Site", command=open_in_browser, bg=UV_COLOR, fg=BG_COLOR,
                          relief="flat", font=("Arial", 11, "bold"))
    open_btn.pack(pady=10)

def filter_combobox(event, combo, valid_values):
    value = combo.get().lower()
    filtered = [v for v in valid_values if value in v.lower()]
    combo['values'] = filtered

def bind_keypress_to_open(event, combo):
    if event.keysym == 'Return':
        combo.event_generate('<Down>')

def create_combobox(frame, label_text, valid_values, row):
    tk.Label(frame, text=label_text, bg=BG_COLOR, fg=UV_COLOR, font=("Arial", 12, "bold")).grid(row=row*2, column=0, sticky="w", pady=5)
    combo = ttk.Combobox(frame, values=valid_values, font=("Arial", 11))
    combo.grid(row=row*2+1, column=0, sticky="ew", pady=2)
    combo.bind('<KeyRelease>', lambda e: filter_combobox(e, combo, valid_values))
    combo.bind('<KeyPress>', lambda e: bind_keypress_to_open(e, combo))
    return combo


def resource_path(relative_path):
    # PyInstaller exe içindeyken doğru yolu bulmak için
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('CS2SS')

root = tk.Tk()
root.iconbitmap(resource_path("logo.ico"))
root.title("Steam Shop URL Creater")
root.geometry("410x210")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

left_frame = tk.Frame(root, bg=BG_COLOR)
left_frame.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
left_frame.grid_columnconfigure(0, weight=1)

weapon_combo = create_combobox(left_frame, "Select Weapon:", VALID_WEAPONS, 0)
condition_combo = create_combobox(left_frame, "Select Condition:", VALID_CONDITIONS, 1)
skin_combo = create_combobox(left_frame, "Select Skin:", VALID_SKINS, 2)

right_frame = tk.Frame(root, bg=BG_COLOR)
right_frame.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
right_frame.grid_columnconfigure(0, weight=1)

stat_track_var = tk.BooleanVar()
souvenir_var = tk.BooleanVar()

stat_track_cb = tk.Checkbutton(right_frame, text="StatTrak™", variable=stat_track_var,
                              bg=BG_COLOR, fg=UV_COLOR, activebackground=BG_COLOR, activeforeground=UV_COLOR,
                              font=("Arial", 12, "bold"), selectcolor=BG_COLOR)
stat_track_cb.pack(anchor="w", pady=5)

souvenir_cb = tk.Checkbutton(right_frame, text="Souvenir", variable=souvenir_var,
                            bg=BG_COLOR, fg=UV_COLOR, activebackground=BG_COLOR, activeforeground=UV_COLOR,
                            font=("Arial", 12, "bold"), selectcolor=BG_COLOR)
souvenir_cb.pack(anchor="w", pady=5)

def generate_url():
    weapon = weapon_combo.get()
    if weapon not in VALID_WEAPONS:
        messagebox.showerror("Error", "Please select a valid weapon.")
        return

    condition = condition_combo.get()
    if condition not in VALID_CONDITIONS:
        messagebox.showerror("Error", "Please select a valid condition.")
        return

    skin_name = skin_combo.get().strip()
    if not skin_name:
        messagebox.showerror("Error", "Please enter the skin.")
        return

    url = create_steam_market_url(weapon, skin_name, condition,
                                  stat_track=stat_track_var.get(),
                                  souvenir=souvenir_var.get())
    open_url_in_new_window(root, url)

button_frame = tk.Frame(right_frame, bg=BG_COLOR)
button_frame.pack(fill="x", pady=25)

generate_btn = tk.Button(button_frame, text="URL Create", command=generate_url,
                          bg=UV_COLOR, fg=BG_COLOR, font=("Arial", 14, "bold"), relief="flat", padx=20, pady=10)
generate_btn.pack(anchor="center")

root.mainloop()