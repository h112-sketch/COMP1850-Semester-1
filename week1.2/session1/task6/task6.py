# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
database = {
    "Michael Jackson": [
        "Invincible", "Dangerous", "Thriller", "Bad",
        "Off the Wall", "History", "Blood on the Dance Floor",
        "Got to Be There", "Ben", "Forever, Michael"
    ],

    "Eminem": [
        "Music To Be Murdered By", "Revival", "Kamikaze",
        "The Marshall Mathers LP", "The Eminem Show",
        "Encore", "Relapse", "Recovery", "Infinite",
        "The Slim Shady LP", "Curtain Call: The Hits",
        "Music to Be Murdered By – Side B"
    ],

    "The Beatles": [
        "Yellow Submarine", "Twist and Shout", "Abbey Road",
        "Let It Be", "Revolver", "Rubber Soul",
        "Sgt. Pepper's Lonely Hearts Club Band",
        "The Beatles", "Magical Mystery Tour",
        "Help!", "A Hard Day's Night", "Beatles for Sale",
        "Please Please Me", "With the Beatles"
    ],

    "Taylor Swift": [
        "Taylor Swift", "Fearless", "Speak Now", "Red",
        "1989", "Reputation", "Lover", "Folklore",
        "Evermore", "Midnights", "The Tortured Poets Department",
        "Fearless (Taylor's Version)", "Red (Taylor's Version)",
        "Speak Now (Taylor's Version)", "1989 (Taylor's Version)"
    ],

    "Drake": [
        "Thank Me Later", "Take Care", "Nothing Was the Same",
        "Views", "Scorpion", "Certified Lover Boy",
        "Honestly, Nevermind", "For All the Dogs",
        "More Life", "If You're Reading This It's Too Late",
        "Dark Lane Demo Tapes", "Her Loss"
    ],

    "Kanye West": [
        "The College Dropout", "Late Registration",
        "Graduation", "808s & Heartbreak", "My Beautiful Dark Twisted Fantasy",
        "Yeezus", "The Life of Pablo", "Ye", "Jesus Is King",
        "Donda", "Vultures 1", "Vultures 2"
    ],

    "Rihanna": [
        "Music of the Sun", "A Girl Like Me", "Good Girl Gone Bad",
        "Rated R", "Loud", "Talk That Talk", "Unapologetic",
        "Anti"
    ],

    "Beyoncé": [
        "Dangerously in Love", "B'Day", "I Am... Sasha Fierce",
        "4", "Beyoncé", "Lemonade", "Renaissance",
        "Cowboy Carter"
    ],

    "Ed Sheeran": [
        "+", "x", "÷", "No.6 Collaborations Project",
        "=", "-", "Autumn Variations"
    ],

    "Adele": [
        "19", "21", "25", "30"
    ],

    "Lady Gaga": [
        "The Fame", "The Fame Monster", "Born This Way",
        "Artpop", "Joanne", "Chromatica", "Mayhem",
        "A Star Is Born"
    ],

    "Bruno Mars": [
        "Doo-Wops & Hooligans", "Unorthodox Jukebox",
        "24K Magic"
    ],

    "Justin Bieber": [
        "My World 2.0", "Under the Mistletoe", "Believe",
        "Purpose", "Changes", "Justice"
    ],

    "The Weeknd": [
        "Kiss Land", "Beauty Behind the Madness",
        "Starboy", "After Hours", "Dawn FM",
        "Trilogy", "My Dear Melancholy,"
    ],

    "Harry Styles": [
        "Harry Styles", "Fine Line", "Harry's House"
    ],

    "Billie Eilish": [
        "When We All Fall Asleep, Where Do We Go?",
        "Happier Than Ever", "Hit Me Hard and Soft"
    ],

    "Ariana Grande": [
        "Yours Truly", "My Everything", "Dangerous Woman",
        "Sweetener", "Thank U, Next", "Positions",
        "Eternal Sunshine"
    ],

    "Kendrick Lamar": [
        "Section.80", "Good Kid, M.A.A.D City",
        "To Pimp a Butterfly", "DAMN.",
        "Mr. Morale & the Big Steppers",
        "GNX"
    ],

    "Jay-Z": [
        "Reasonable Doubt", "The Blueprint", "The Black Album",
        "4:44", "Magna Carta Holy Grail", "Kingdom Come",
        "American Gangster", "Vol. 2... Hard Knock Life"
    ],

    "Nas": [
        "Illmatic", "It Was Written", "I Am...",
        "Nastradamus", "Stillmatic", "God's Son",
        "Street's Disciple", "Life Is Good", "King's Disease"
    ],

    "50 Cent": [
        "Get Rich or Die Tryin'", "The Massacre",
        "Curtis", "Before I Self Destruct",
        "Animal Ambition"
    ],

    "Snoop Dogg": [
        "Doggystyle", "Tha Doggfather", "Da Game Is to Be Sold",
        "No Limit Top Dogg", "Tha Last Meal", "BODR"
    ],

    "Dr. Dre": [
        "The Chronic", "2001", "Compton"
    ],

    "2Pac": [
        "2Pacalypse Now", "Strictly 4 My N.I.G.G.A.Z...",
        "Me Against the World", "All Eyez on Me",
        "The Don Killuminati: The 7 Day Theory",
        "Until the End of Time"
    ],

    "Notorious B.I.G.": [
        "Ready to Die", "Life After Death"
    ],

    "Queen": [
        "Queen", "Queen II", "Sheer Heart Attack",
        "A Night at the Opera", "A Day at the Races",
        "News of the World", "Jazz", "The Game",
        "Hot Space", "The Works", "A Kind of Magic",
        "The Miracle", "Innuendo", "Made in Heaven"
    ],

    "David Bowie": [
        "Space Oddity", "The Man Who Sold the World",
        "Hunky Dory", "The Rise and Fall of Ziggy Stardust",
        "Aladdin Sane", "Diamond Dogs", "Young Americans",
        "Station to Station", "Low", "Heroes",
        "Lodger", "Scary Monsters", "Let's Dance",
        "Blackstar"
    ],

    "Elvis Presley": [
        "Elvis Presley", "Elvis", "Elvis' Christmas Album",
        "From Elvis in Memphis", "That's All Right",
        "Blue Hawaii", "Aloha from Hawaii Via Satellite"
    ],

    "Bob Marley": [
        "Catch a Fire", "Burnin'", "Natty Dread",
        "Rastaman Vibration", "Exodus", "Kaya",
        "Survival", "Uprising", "Legend"
    ],

    "Nirvana": [
        "Bleach", "Nevermind", "In Utero", "MTV Unplugged in New York"
    ],

    "Metallica": [
        "Kill 'Em All", "Ride the Lightning",
        "Master of Puppets", "...And Justice for All",
        "Metallica", "Load", "Reload", "Death Magnetic",
        "Hardwired... to Self-Destruct", "72 Seasons"
    ],

    "Pink Floyd": [
        "The Piper at the Gates of Dawn", "A Saucerful of Secrets",
        "Meddle", "The Dark Side of the Moon",
        "Wish You Were Here", "Animals", "The Wall",
        "The Final Cut", "A Momentary Lapse of Reason",
        "The Division Bell", "The Endless River"
    ],

    "Led Zeppelin": [
        "Led Zeppelin", "Led Zeppelin II", "Led Zeppelin III",
        "Led Zeppelin IV", "Houses of the Holy",
        "Physical Graffiti", "Presence", "In Through the Out Door",
        "Coda"
    ],

    "AC/DC": [
        "High Voltage", "T.N.T.", "Dirty Deeds Done Dirt Cheap",
        "Let There Be Rock", "Powerage", "Highway to Hell",
        "Back in Black", "For Those About to Rock",
        "The Razors Edge", "Black Ice", "Power Up"
    ],

    "The Rolling Stones": [
        "The Rolling Stones", "Let It Bleed", "Sticky Fingers",
        "Exile on Main St.", "Goats Head Soup",
        "It's Only Rock 'n Roll", "Some Girls",
        "Tattoo You", "Steel Wheels", "Hackney Diamonds"
    ],

    "Coldplay": [
        "Parachutes", "A Rush of Blood to the Head",
        "X&Y", "Viva la Vida or Death and All His Friends",
        "Mylo Xyloto", "Ghost Stories", "A Head Full of Dreams",
        "Everyday Life", "Music of the Spheres"
    ],

    "Maroon 5": [
        "Songs About Jane", "It Won't Be Soon Before Long",
        "Hands All Over", "Overexposed", "V",
        "Red Pill Blues", "Jordi"
    ],

    "Linkin Park": [
        "Hybrid Theory", "Meteora", "Minutes to Midnight",
        "A Thousand Suns", "Living Things", "The Hunting Party",
        "One More Light", "From Zero"
    ],

    "Green Day": [
        "39/Smooth", "Kerplunk", "Dookie", "Insomniac",
        "Nimrod", "Warning", "American Idiot",
        "21st Century Breakdown", "Revolution Radio",
        "Father of All Motherfuckers", "Saviors"
    ],

    "Arctic Monkeys": [
        "Whatever People Say I Am, That's What I'm Not",
        "Favourite Worst Nightmare", "Humbug",
        "Suck It and See", "AM", "Tranquility Base Hotel & Casino",
        "The Car"
    ]
}
# (keys are artist names, values are lists of album names)

# Pretty-print the data structure
pprint(database)

# Display details of one album recorded by a specific artist
albums = database["Michael Jackson"]
print(albums[0])