import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2018-05-28
# https://www.baseball-reference.com/boxes/BOS/BOS201805280.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2018/05/28/530212/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-28 13:07-16:01",
        "at": "Fenway Park, Boston, MA",
        "att": "34,700",
        "temp": "53F, Cloudy",
        "wind": "7mph, In From CF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 41,
            "roster": {
                # Lineup
                37: "Teoscar Hernández",
                20: "Josh Donaldson",
                14: "Justin Smoak",
                26: "Yangervis Solarte",
                11: "Kevin Pillar",
                55: "Russell Martin",
                8: "Kendrys Morales",
                21: "Luke Maile",
                29: "Devon Travis",
                # Starting pitcher
                41: "Aaron Sanchez",
                # Bench
                3: "Gio Urshela",
                27: "Dwight Smith Jr.",
                18: "Curtis Granderson",
                # Bullpen
                62: "Aaron Loup",
                57: "Jaime García",
                31: "Joe Biagini",
                24: "Danny Barnes",
                25: "Marco Estrada",
                39: "Jake Petricka",
                43: "Sam Gaviglio",
                36: "Tyler Clippard",
                22: "Seunghwan Oh",
                77: "John Axford",
                52: "Ryan Tepera",
                33: "J.A. Happ",
            },
            "lefties": [62, 57, 33],
            "lineup": [
                [37, "9"],
                [20, "5"],
                [14, "3"],
                [26, "6"],
                [11, "8"],
                [55, "7"],
                [8, "0"],
                [21, "2"],
                [29, "4"],
            ],
            "bench": [
                [3, "3B"],
                [27, "LF"],
                [18, "CF"],
            ],
            "bullpen": [62, 57, 31, 24, 25, 39, 43, 36, 22, 77, 52, 33],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                23: "Blake Swihart",
                50: "Mookie Betts",
                15: "Dustin Pedroia",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 31, 61],
            "lineup": [
                [16, "7"],
                [2, "6"],
                [18, "3"],
                [28, "0"],
                [11, "5"],
                [36, "4"],
                [12, "9"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [23, "C"],
                [50, "SS"],
                [15, "2B"],
                [3, "C"],
            ],
            "bullpen": [57, 35, 22, 41, 31, 61, 37, 46, 76, 56, 32],
        },
        "umpires": {
            "HP": "Jordan Baker",
            "1B": "Vic Carapazza",
            "2B": "Jerry Layne",
            "3B": "Jansen Visconti",
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
# Pitching: BOS #24 David Price
t1 = game.new_inning()

# 1. TOR #37 Teoscar Hernández (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.out("P4")

# 2. TOR #20 Josh Donaldson (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b")
t1.hit(1)

# 3. TOR #14 Justin Smoak (X - X - 20)
t1.new_ab()
t1.pitch_list("c b s f b s")
t1.out("K")

# 4. TOR #26 Yangervis Solarte (X - X - 20)
t1.new_ab()
t1.out("L1-3")


# Bot 1st
# Pitching: TOR #41 Aaron Sanchez
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c b c b f b")
b1.out("G3")

# 2. BOS #2  Xander Bogaerts (X - X - X)
b1.new_ab()
b1.pitch_list("c b c b f")
b1.hit(1)
b1.advance(3, "18 1B")
b1.advance(4, "28 FC6-4")

# 3. BOS #18 Mitch Moreland (X - X - 2)
b1.new_ab()
b1.pitch_list("b d")
b1.hit(1)
b1.thrown_out(2, "28 FC6-4", 2, 41)

# 4. BOS #28 J.D. Martinez (2 - X - 18)
b1.new_ab()
b1.pitch_list("c")
b1.reach("FC6-4", rbis=1)

# 5. BOS #11 Rafael Devers (X - X - 28)
b1.new_ab()
b1.pitch_list("s")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 5. TOR #11 Kevin Pillar (X - X - X)
t2.new_ab()
t2.pitch_list("b b f f f f f f b b")
t2.reach("BB")
t2.advance(2, "55 SB")
t2.advance(3, "8 F9")

# 6. TOR #55 Russell Martin (X - X - 11)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")

# 7. TOR #8  Kendrys Morales (X - 11 - 55)
t2.new_ab()
t2.pitch_list("f b c b b")
t2.out("F9")

# 8. TOR #21 Luke Maile (11 - X - 55)
t2.new_ab()
t2.pitch_list("b b b c s")
t2.out("(F)P3")

# 9. TOR #29 Devon Travis (11 - X - 55)
t2.new_ab()
t2.pitch_list("b b c s f b f s")
t2.out("K")


# Bot 2nd
# Pitching: TOR #41 Aaron Sanchez
b2 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f s")
b2.out("K")

# 7. BOS #12 Brock Holt (X - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")

# 8. BOS #7  Christian Vázquez (X - X - 12)
b2.new_ab()
b2.pitch_list("f b 1")
b2.out("F9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 12)
b2.new_ab()
b2.pitch_list("b")
b2.out("L8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 1. TOR #37 Teoscar Hernández (X - X - X)
t3.new_ab()
t3.pitch_list("f f b")
t3.out("F9")

# 2. TOR #20 Josh Donaldson (X - X - X)
t3.new_ab()
t3.pitch_list("b b c b f b")
t3.reach("BB")

# 3. TOR #14 Justin Smoak (X - X - 20)
t3.new_ab()
t3.pitch_list("f d f c")
t3.out("!K")

# 4. TOR #26 Yangervis Solarte (X - X - 20)
t3.new_ab()
t3.pitch_list("b")
t3.out("P6")


# Bot 3rd
# Pitching: TOR #41 Aaron Sanchez
b3 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("c c f b")
b3.hit(1)
b3.thrown_out(2, "18 FC1-6", 2, 41)

# 2. BOS #2  Xander Bogaerts (X - X - 16)
b3.new_ab()
b3.pitch_list("c 1 c s")
b3.out("K")

# 3. BOS #18 Mitch Moreland (X - X - 16)
b3.new_ab()
b3.pitch_list("b 1")
b3.reach("FC1-6")

# 4. BOS #28 J.D. Martinez (X - X - 18)
b3.new_ab()
b3.out("L8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 5. TOR #11 Kevin Pillar (X - X - X)
t4.new_ab()
t4.hit(2)
t4.advance(3, "55 G6-3")
t4.advance(4, "8 1B")

# 6. TOR #55 Russell Martin (X - 11 - X)
t4.new_ab()
t4.pitch_list("b c")
t4.out("G6-3")

# 7. TOR #8  Kendrys Morales (11 - X - X)
t4.new_ab()
t4.pitch_list("b s")
t4.hit(1, rbis=1)

# 8. TOR #21 Luke Maile (X - X - 8)
t4.new_ab()
t4.out("F8")

# 9. TOR #29 Devon Travis (X - X - 8)
t4.new_ab()
t4.pitch_list("f b f f b")
t4.out("L8")


# Bot 4th
# Pitching: TOR #41 Aaron Sanchez
b4 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("b f")
b4.hit(1)
b4.advance(2, "36 1B")
b4.advance(3, "12 PB")
b4.advance(4, "12 SF7")

# 6. BOS #36 Eduardo Núñez (X - X - 11)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1)
b4.advance(2, "12 PB")
b4.advance(3, "7 1B")
b4.advance(4, "19 2B")

# 7. BOS #12 Brock Holt (X - 11 - 36)
b4.new_ab()
b4.pitch_list("s")
b4.pb()
b4.out("SF7", rbis=1)

# 8. BOS #7  Christian Vázquez (X - 36 - X)
b4.new_ab()
b4.hit(1)
b4.advance(3, "19 2B")
b4.advance(4, "16 HR")

# 9. BOS #19 Jackie Bradley Jr. (36 - X - 7)
b4.new_ab()
b4.pitch_list("b b")
b4.hit(2, rbis=1)
b4.advance(4, "16 HR")

# 1. BOS #16 Andrew Benintendi (7 - 19 - X)
b4.new_ab()
b4.pitch_list("s b")
b4.hit(4, rbis=3)

# 2. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("c f s")
b4.out("K")

# 3. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("c b f b b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 1. TOR #37 Teoscar Hernández (X - X - X)
t5.new_ab()
t5.pitch_list("c f f")
t5.out("L9")

# 2. TOR #20 Josh Donaldson (X - X - X)
t5.new_ab()
t5.pitch_list("b b c b b")
t5.reach("BB")
t5.advance(3, "14 2B")
# Offensive change (TOR): Pinch-runner #3 Gio Urshela replaces #20 Josh Donaldson
t5.offensive_substitution(2, 3, "PR")
t5.atbase("PR")
t5.advance(4, "26 SF9")

# 3. TOR #14 Justin Smoak (X - X - 20)
t5.new_ab()
t5.pitch_list("f")
t5.hit(2)

# 4. TOR #26 Yangervis Solarte (20 - 14 - X)
t5.new_ab()
t5.out("SF9", rbis=1)

# 5. TOR #11 Kevin Pillar (X - 14 - X)
t5.new_ab()
t5.pitch_list("c f b s")
t5.out("K")


# Bot 5th
# Pitching: TOR #41 Aaron Sanchez
b5 = game.new_inning()

# Defensive switch (TOR): #3 Gio Urshela moves to 3B
b5.defensive_switch(3, "5")

# 4. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("s f")
b5.hit(4, rbis=1)

# 5. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.pitch_list("f f b f")
b5.out("P3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("G3")

# 7. BOS #12 Brock Holt (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #37 Heath Hembree
t6 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #24 David Price
t6.pitching_substitution(37)

# 6. TOR #55 Russell Martin (X - X - X)
t6.new_ab()
t6.pitch_list("c b c s")
t6.out("K")

# 7. TOR #8  Kendrys Morales (X - X - X)
t6.new_ab()
t6.pitch_list("b f b f")
t6.out("F8")

# 8. TOR #21 Luke Maile (X - X - X)
t6.new_ab()
t6.pitch_list("c b t b s")
t6.out("K")


# Bot 6th
# Pitching: TOR #24 Danny Barnes
b6 = game.new_inning()

# Pitching change (TOR): #24 Danny Barnes replaces #41 Aaron Sanchez
b6.pitching_substitution(24)

# 8. BOS #7  Christian Vázquez (X - X - X)
b6.new_ab()
b6.pitch_list("b f")
b6.out("G4-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c b")
b6.reach("BB")
b6.error(2)
b6.advance(2, "16 SB")
b6.advance(3, "16 E2")
b6.advance(4, "16 3B")

# 1. BOS #16 Andrew Benintendi (X - X - 19)
b6.new_ab()
b6.pitch_list("s c")
b6.hit(3, rbis=1)

# 2. BOS #2  Xander Bogaerts (16 - X - X)
b6.new_ab()
b6.out("F8")

# 3. BOS #18 Mitch Moreland (16 - X - X)
b6.new_ab()
b6.pitch_list("d")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Heath Hembree
t7 = game.new_inning()

# 9. TOR #29 Devon Travis (X - X - X)
t7.new_ab()
t7.pitch_list("b c c f b")
t7.hit(3)
t7.advance(4, "37 3B")

# 1. TOR #37 Teoscar Hernández (29 - X - X)
t7.new_ab()
t7.pitch_list("c b b")
t7.hit(3, rbis=1)

# 2. TOR #3  Gio Urshela (37 - X - X)
t7.new_ab()
t7.pitch_list("f f t")
t7.out("KT")

# 3. TOR #14 Justin Smoak (37 - X - X)
t7.new_ab()
t7.pitch_list("b b d b")
t7.reach("BB")
t7.thrown_out(2, "26 DP3-6-3", 2, 37)

# 4. TOR #26 Yangervis Solarte (37 - X - 14)
t7.new_ab()
t7.pitch_list("d")
t7.out("DP3-6-3")


# Bot 7th
# Pitching: TOR #77 John Axford
b7 = game.new_inning()

# Pitching change (TOR): #77 John Axford replaces #24 Danny Barnes
b7.pitching_substitution(77)

# 4. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("b b b f f b")
b7.reach("BB")
b7.advance(2, "11 1B")
b7.advance(3, "36 DP6-4-3")

# 5. BOS #11 Rafael Devers (X - X - 28)
b7.new_ab()
b7.pitch_list("f b")
b7.hit(1)
b7.thrown_out(2, "36 DP6-4-3", 1, 77)

# 6. BOS #36 Eduardo Núñez (X - 28 - 11)
b7.new_ab()
b7.pitch_list("d")
b7.out("DP6-4-3")

# 7. BOS #12 Brock Holt (28 - X - X)
b7.new_ab()
b7.pitch_list("b b b c b")
b7.reach("BB")

# 8. BOS #7  Christian Vázquez (28 - X - 12)
b7.new_ab()
b7.pitch_list("d b f")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #35 Steven Wright
t8 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #37 Heath Hembree
t8.pitching_substitution(35)

# 5. TOR #11 Kevin Pillar (X - X - X)
t8.new_ab()
t8.pitch_list("b c f s")
t8.out("K")

# 6. TOR #55 Russell Martin (X - X - X)
t8.new_ab()
t8.pitch_list("c c")
t8.out("G5-3")

# 7. TOR #8  Kendrys Morales (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G6-3")


# Bot 8th
# Pitching: TOR #39 Jake Petricka
b8 = game.new_inning()

# Pitching change (TOR): #39 Jake Petricka replaces #77 John Axford
b8.pitching_substitution(39)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G4-3")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("F7")

# 2. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #35 Steven Wright
t9 = game.new_inning()

# 8. TOR #21 Luke Maile (X - X - X)
t9.new_ab()
t9.out("G5-3")

# 9. TOR #29 Devon Travis (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G6-3")

# 1. TOR #37 Teoscar Hernández (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(2)

# 2. TOR #3  Gio Urshela (X - 37 - X)
t9.new_ab()
t9.pitch_list("c c f b b s")
t9.out("K")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24)

# Loser team: TOR
# LP: TOR #41 Aaron Sanchez
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
