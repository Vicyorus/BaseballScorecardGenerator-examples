import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2018-05-30
# https://www.baseball-reference.com/boxes/BOS/BOS201805300.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2018/05/30/530242/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-30 13:07-15:59",
        "at": "Fenway Park, Boston, MA",
        "att": "33,451",
        "temp": "65F, Partly Cloudy",
        "wind": "13mph, R To L",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 43,
            "roster": {
                # Lineup
                37: "Teoscar Hernández",
                11: "Kevin Pillar",
                26: "Yangervis Solarte",
                14: "Justin Smoak",
                8: "Kendrys Morales",
                29: "Devon Travis",
                18: "Curtis Granderson",
                21: "Luke Maile",
                3: "Gio Urshela",
                # Starting pitcher
                43: "Sam Gaviglio",
                # Bench
                55: "Russell Martin",
                27: "Dwight Smith Jr.",
                # Bullpen
                41: "Aaron Sanchez",
                62: "Aaron Loup",
                36: "Tyler Clippard",
                22: "Seunghwan Oh",
                57: "Jaime García",
                31: "Joe Biagini",
                24: "Danny Barnes",
                25: "Marco Estrada",
                39: "Jake Petricka",
                77: "John Axford",
                52: "Ryan Tepera",
                33: "J.A. Happ",
            },
            "lefties": [62, 57, 33],
            "lineup": [
                [37, "9"],
                [11, "8"],
                [26, "6"],
                [14, "3"],
                [8, "0"],
                [29, "4"],
                [18, "7"],
                [21, "2"],
                [3, "5"],
            ],
            "bench": [
                [55, "C"],
                [27, "LF"],
            ],
            "bullpen": [41, 62, 36, 22, 57, 31, 24, 25, 39, 77, 52, 33],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                18: "Mitch Moreland",
                3: "Sandy León",
                # Bullpen
                35: "Steven Wright",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                22: "Rick Porcello",
                41: "Chris Sale",
                56: "Joe Kelly",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [57, 24, 41, 31, 61],
            "lineup": [
                [16, "8"],
                [2, "6"],
                [28, "7"],
                [11, "5"],
                [36, "0"],
                [12, "4"],
                [23, "3"],
                [7, "2"],
                [19, "9"],
            ],
            "bench": [
                [18, "1B"],
                [3, "C"],
            ],
            "bullpen": [35, 24, 46, 76, 22, 41, 56, 31, 61, 32, 37],
        },
        "umpires": {
            "HP": "Jerry Layne",
            "1B": "Jansen Visconti",
            "2B": "Jordan Baker",
            "3B": "Vic Carapazza",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: BOS #57 Eduardo Rodriguez
t1 = game.new_inning()

# 1. TOR #37 Teoscar Hernández (X - X - X)
t1.new_ab()
t1.pitch_list("c s s")
t1.out("K")

# 2. TOR #11 Kevin Pillar (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("L9")

# 3. TOR #26 Yangervis Solarte (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.out("L4")


# Bot 1st
# Pitching: TOR #43 Sam Gaviglio
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("f")
b1.out("G3")

# 2. BOS #2  Xander Bogaerts (X - X - X)
b1.new_ab()
b1.pitch_list("b c b")
b1.out("G5-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c b c")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 4. TOR #14 Justin Smoak (X - X - X)
t2.new_ab()
t2.pitch_list("b c s")
t2.out("G6-3")

# 5. TOR #8  Kendrys Morales (X - X - X)
t2.new_ab()
t2.pitch_list("c c f b b")
t2.out("G6-3")

# 6. TOR #29 Devon Travis (X - X - X)
t2.new_ab()
t2.pitch_list("f f b b")
t2.out("F7")


# Bot 2nd
# Pitching: TOR #43 Sam Gaviglio
b2 = game.new_inning()

# 4. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("c f b c")
b2.out("!K")

# 5. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b b s f f")
b2.out("G6-3")

# 6. BOS #12 Brock Holt (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 7. TOR #18 Curtis Granderson (X - X - X)
t3.new_ab()
t3.pitch_list("s b s c")
t3.out("!K")

# 8. TOR #21 Luke Maile (X - X - X)
t3.new_ab()
t3.pitch_list("t s t")
t3.out("KT")

# 9. TOR #3  Gio Urshela (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b")
t3.out("G6-3")


# Bot 3rd
# Pitching: TOR #43 Sam Gaviglio
b3 = game.new_inning()

# 7. BOS #23 Blake Swihart (X - X - X)
b3.new_ab()
b3.pitch_list("s")
b3.hit(1)
b3.advance(2, "7 G5-3")
b3.advance(4, "19 2B")

# 8. BOS #7  Christian Vázquez (X - X - 23)
b3.new_ab()
b3.pitch_list("1 1 1")
b3.out("G5-3")

# 9. BOS #19 Jackie Bradley Jr. (X - 23 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b c s d b")
b3.hit(2, rbis=1)
b3.advance(3, "16 1B")
b3.thrown_out(4, "2 2-4-2-1", 3, 43)

# 1. BOS #16 Andrew Benintendi (X - 19 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b f b")
b3.hit(1)
b3.thrown_out(2, "2 CS", 2, 43)

# 2. BOS #2  Xander Bogaerts (19 - X - 16)
b3.new_ab(is_risp=True)
b3.pitch_list("1 c f b f d")
b3.no_ab("2-4-2-1")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 1. TOR #37 Teoscar Hernández (X - X - X)
t4.new_ab()
t4.pitch_list("f b c f s")
t4.out("K")

# 2. TOR #11 Kevin Pillar (X - X - X)
t4.new_ab()
t4.out("L9")

# 3. TOR #26 Yangervis Solarte (X - X - X)
t4.new_ab()
t4.pitch_list("c b b")
t4.out("G6-3")


# Bot 4th
# Pitching: TOR #43 Sam Gaviglio
b4 = game.new_inning()

# 2. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("c b f s")
b4.out("K")

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("f b s b s")
b4.out("K")

# 4. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #57 Eduardo Rodriguez
t5 = game.new_inning()

# 4. TOR #14 Justin Smoak (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G4-3")

# 5. TOR #8  Kendrys Morales (X - X - X)
t5.new_ab()
t5.pitch_list("c b b b f f")
t5.hit(1)
t5.thrown_out(2, "29 CS", 3, 57)

# 6. TOR #29 Devon Travis (X - X - 8)
t5.new_ab()
t5.pitch_list("f s b f b b c")
t5.out("KDP2-4")


# Bot 5th
# Pitching: TOR #43 Sam Gaviglio
b5 = game.new_inning()

# 5. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(4)

# 6. BOS #12 Brock Holt (X - X - X)
b5.new_ab()
b5.pitch_list("b b c")
b5.out("L9")

# 7. BOS #23 Blake Swihart (X - X - X)
b5.new_ab()
b5.pitch_list("b b f s")
b5.hit(1)

# 8. BOS #7  Christian Vázquez (X - X - 23)
b5.new_ab()
b5.pitch_list("b 1 f p b")
b5.out("P4")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 23)
b5.new_ab()
b5.pitch_list("s")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #57 Eduardo Rodriguez
t6 = game.new_inning()

# 7. TOR #18 Curtis Granderson (X - X - X)
t6.new_ab()
t6.pitch_list("c b f f f b f c")
t6.out("!K")

# 8. TOR #21 Luke Maile (X - X - X)
t6.new_ab()
t6.out("L9")

# 9. TOR #3  Gio Urshela (X - X - X)
t6.new_ab()
t6.pitch_list("c f b f f b b b")
t6.reach("BB")
t6.advance(4, "37 HR")

# 1. TOR #37 Teoscar Hernández (X - X - 3)
t6.new_ab()
t6.pitch_list("b d")
t6.hit(4, rbis=2)

# 2. TOR #11 Kevin Pillar (X - X - X)
t6.new_ab()
t6.pitch_list("c f f f b f s")
t6.out("K")


# Bot 6th
# Pitching: TOR #43 Sam Gaviglio
b6 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.advance(4, "28 HR")

# 2. BOS #2  Xander Bogaerts (X - X - 16)
b6.new_ab()
b6.out("(F)B2")

# 3. BOS #28 J.D. Martinez (X - X - 16)
b6.new_ab()
b6.pitch_list("1 d b")
b6.hit(4, rbis=2)

# 4. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("s f b b b f s")
b6.out("K")

# 5. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #57 Eduardo Rodriguez
t7 = game.new_inning()

# 3. TOR #26 Yangervis Solarte (X - X - X)
t7.new_ab()
t7.out("P6")

# 4. TOR #14 Justin Smoak (X - X - X)
t7.new_ab()
t7.pitch_list("b c c f b b f")
t7.hit(1)
t7.advance(3, "29 E3")

# 5. TOR #8  Kendrys Morales (X - X - 14)
t7.new_ab()
t7.pitch_list("b c")
t7.out("P6")

# Pitching change (BOS): #32 Matt Barnes replaces #57 Eduardo Rodriguez
t7.pitching_substitution(32)

# 6. TOR #29 Devon Travis (X - X - 14)
t7.new_ab()
t7.pitch_list("c c")
t7.error(3)
t7.reach("E3")

# 7. TOR #18 Curtis Granderson (14 - X - 29)
t7.new_ab(is_risp=True)
t7.pitch_list("b")
t7.out("F8")


# Bot 7th
# Pitching: TOR #22 Seunghwan Oh
b7 = game.new_inning()

# Pitching change (TOR): #22 Seunghwan Oh replaces #43 Sam Gaviglio
b7.pitching_substitution(22)

# 6. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("c b b s f b f b")
b7.reach("BB")
b7.advance(2, "19 1B")

# 7. BOS #23 Blake Swihart (X - X - 12)
b7.new_ab()
b7.pitch_list("b c c f c")
b7.out("!K")

# 8. BOS #7  Christian Vázquez (X - X - 12)
b7.new_ab()
b7.pitch_list("c f b f s")
b7.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 12)
b7.new_ab()
b7.hit(1)

# 1. BOS #16 Andrew Benintendi (X - 12 - 19)
b7.new_ab(is_risp=True)
b7.pitch_list("s")
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Defensive change (BOS): #18 Mitch Moreland replaces #23 Blake Swihart (1B), playing 1B, batting 7th
t8.defensive_substitution(7, 18, "3")

# 8. TOR #21 Luke Maile (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("L9")

# 9. TOR #3  Gio Urshela (X - X - X)
t8.new_ab()
t8.pitch_list("c s b b c")
t8.out("!K")

# 1. TOR #37 Teoscar Hernández (X - X - X)
t8.new_ab()
t8.pitch_list("c s s")
t8.out("K")


# Bot 8th
# Pitching: TOR #52 Ryan Tepera
b8 = game.new_inning()

# Pitching change (TOR): #52 Ryan Tepera replaces #22 Seunghwan Oh
b8.pitching_substitution(52)

# 2. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(1)
b8.error(1)
b8.advance(2, "28 E1")
b8.advance("U", "36 2B")

# 3. BOS #28 J.D. Martinez (X - X - 2)
b8.new_ab()
b8.pitch_list("c s b 1 f b")
b8.reach("FC1")
b8.advance(3, "36 2B")
b8.advance(4, "12 1B")

# 4. BOS #11 Rafael Devers (X - 2 - 28)
b8.new_ab(is_risp=True)
b8.pitch_list("l")
b8.out("IF6")

# 5. BOS #36 Eduardo Núñez (X - 2 - 28)
b8.new_ab(is_risp=True)
b8.pitch_list("c c")
b8.hit(2, rbis=1)
b8.advance(3, "12 1B")

# 6. BOS #12 Brock Holt (28 - 36 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b b c b c")
b8.hit(1, rbis=1)
b8.advance(2, "7 SB")

# 7. BOS #18 Mitch Moreland (36 - X - 12)
b8.new_ab(is_risp=True)
b8.pitch_list("s f s")
b8.out("K")

# 8. BOS #7  Christian Vázquez (36 - X - 12)
b8.new_ab(is_risp=True)
b8.pitch_list("f f b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #61 Brian Johnson
t9 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #32 Matt Barnes
t9.pitching_substitution(61)

# 2. TOR #11 Kevin Pillar (X - X - X)
t9.new_ab()
t9.hit(1)
t9.advance(3, "26 1B")
t9.advance(4, "8 2B")

# 3. TOR #26 Yangervis Solarte (X - X - 11)
t9.new_ab()
t9.pitch_list("c")
t9.hit(1)
t9.advance(2, "14 BB")
t9.advance(4, "8 2B")

# Pitching change (BOS): #46 Craig Kimbrel replaces #61 Brian Johnson
t9.pitching_substitution(46)

# 4. TOR #14 Justin Smoak (11 - X - 26)
t9.new_ab(is_risp=True)
t9.pitch_list("b f s b b b")
t9.reach("BB")
t9.advance(3, "8 2B")

# 5. TOR #8  Kendrys Morales (11 - 26 - 14)
t9.new_ab(is_risp=True)
t9.pitch_list("d")
t9.hit(2, rbis=2)
# Offensive change (TOR): Pinch-runner #27 Dwight Smith Jr. replaces #8 Kendrys Morales
t9.offensive_substitution(5, 27, "PR")
t9.atbase("PR")

# 6. TOR #29 Devon Travis (14 - 8 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("s d b")
t9.out("G5-3")

# 7. TOR #18 Curtis Granderson (14 - 27 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c b b s f t")
t9.out("KT")

# 8. TOR #21 Luke Maile (14 - 27 - X)
t9.new_ab(is_risp=True)
t9.out("G4-3")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: TOR
# LP: TOR #43 Sam Gaviglio
game.losing_pitcher(43, is_away_team=True)

# print(game)
game.generate_scorecard()
