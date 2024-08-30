import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2018-05-13
# https://www.baseball-reference.com/boxes/TOR/TOR201805130.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2018/05/13/530003/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-13 13:08-16:50",
        "at": "Rogers Centre, Toronto, ON",
        "att": "37,888",
        "temp": "59F, Sunny",
        "wind": "15mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                12: "Brock Holt",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                31: "Drew Pomeranz",
                # Bench
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                3: "Sandy León",
                13: "Hanley Ramirez",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [31, 57, 41, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [12, "4"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [36, "SS"],
                [23, "C"],
                [3, "C"],
                [13, "SS"],
            ],
            "bullpen": [57, 39, 22, 41, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 31,
            "roster": {
                # Lineup
                37: "Teoscar Hernández",
                20: "Josh Donaldson",
                14: "Justin Smoak",
                26: "Yangervis Solarte",
                11: "Kevin Pillar",
                55: "Russell Martin",
                8: "Kendrys Morales",
                30: "Anthony Alford",
                7: "Richard Urena",
                # Starting pitcher
                31: "Joe Biagini",
                # Bench
                3: "Gio Urshela",
                21: "Luke Maile",
                18: "Curtis Granderson",
                # Bullpen
                62: "Aaron Loup",
                48: "Deck McGuire",
                57: "Jaime García",
                25: "Marco Estrada",
                39: "Jake Petricka",
                43: "Sam Gaviglio",
                41: "Aaron Sanchez",
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
                [26, "4"],
                [11, "8"],
                [55, "2"],
                [8, "0"],
                [30, "7"],
                [7, "6"],
            ],
            "bench": [
                [3, "3B"],
                [21, "C"],
                [18, "CF"],
            ],
            "bullpen": [62, 48, 57, 25, 39, 43, 41, 36, 22, 77, 52, 33],
        },
        "umpires": {
            "HP": "Jerry Meals",
            "1B": "Gabe Morales",
            "2B": "Ed Hickox",
            "3B": "Ron Kulpa",
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
# Pitching: TOR #31 Joe Biagini
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b b f b c")
t1.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b b f")
t1.hit(1)
t1.advance(4, "28 HR")

# 3. BOS #28 J.D. Martinez (X - X - 16)
t1.new_ab()
t1.hit(4, rbis=2)

# 4. BOS #18 Mitch Moreland (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.out("G5-3")


# Bot 1st
# Pitching: BOS #31 Drew Pomeranz
b1 = game.new_inning()

# 1. TOR #37 Teoscar Hernández (X - X - X)
b1.new_ab()
b1.pitch_list("c b b t f f b")
b1.out("L6")

# 2. TOR #20 Josh Donaldson (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.hit(2)
b1.advance(3, "26 FC4-6")

# 3. TOR #14 Justin Smoak (X - 20 - X)
b1.new_ab()
b1.pitch_list("b b b c b")
b1.reach("BB")
b1.thrown_out(2, "26 FC4-6", 2, 31)

# 4. TOR #26 Yangervis Solarte (X - 20 - 14)
b1.new_ab()
b1.pitch_list("d c f b")
b1.reach("FC4-6")

# 5. TOR #11 Kevin Pillar (20 - X - 26)
b1.new_ab()
b1.pitch_list("c b c b b")
b1.out("G1-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #31 Joe Biagini
t2 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("f s b s")
t2.out("K")

# 7. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("b c b c t")
t2.out("KT")

# 8. BOS #7  Christian Vázquez (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("L9")


# Bot 2nd
# Pitching: BOS #31 Drew Pomeranz
b2 = game.new_inning()

# 6. TOR #55 Russell Martin (X - X - X)
b2.new_ab()
b2.hit(1)
b2.advance(2, "8 BB")

# 7. TOR #8  Kendrys Morales (X - X - 55)
b2.new_ab()
b2.pitch_list("b b d c b")
b2.reach("BB")

# 8. TOR #30 Anthony Alford (X - 55 - 8)
b2.new_ab()
b2.pitch_list("c b f c")
b2.out("!K")

# 9. TOR #7  Richard Urena (X - 55 - 8)
b2.new_ab()
b2.pitch_list("b f d b c c")
b2.out("!K")

# 1. TOR #37 Teoscar Hernández (X - 55 - 8)
b2.new_ab()
b2.pitch_list("f f")
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #31 Joe Biagini
t3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c b s f b f b b")
t3.reach("BB")
t3.advance(3, "50 1B")
t3.advance(4, "18 BB")

# 1. BOS #50 Mookie Betts (X - X - 19)
t3.new_ab()
t3.pitch_list("d c 1 c f 1 f 1 f b")
t3.hit(1)
t3.advance(2, "28 SB")
t3.advance(3, "18 BB")

# 2. BOS #16 Andrew Benintendi (19 - X - 50)
t3.new_ab()
t3.pitch_list("d c 1 f b")
t3.out("F7")

# 3. BOS #28 J.D. Martinez (19 - X - 50)
t3.new_ab()
t3.pitch_list("b c b b f b")
t3.reach("BB")
t3.advance(2, "18 BB")

# 4. BOS #18 Mitch Moreland (19 - 50 - 28)
t3.new_ab()
t3.pitch_list("b b f s f f b f f b")
t3.reach("BB", rbis=1)
t3.thrown_out(2, "2 DP6-4-3", 2, 31)

# 5. BOS #2  Xander Bogaerts (50 - 28 - 18)
t3.new_ab()
t3.pitch_list("c d c")
t3.out("DP6-4-3")


# Bot 3rd
# Pitching: BOS #31 Drew Pomeranz
b3 = game.new_inning()

# 2. TOR #20 Josh Donaldson (X - X - X)
b3.new_ab()
b3.pitch_list("b c b c s")
b3.out("K")

# 3. TOR #14 Justin Smoak (X - X - X)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")
b3.advance(2, "26 BLK")

# 4. TOR #26 Yangervis Solarte (X - X - 14)
b3.new_ab()
b3.pitch_list("n c f f d c")
b3.balk()
b3.out("!K")

# 5. TOR #11 Kevin Pillar (X - 14 - X)
b3.new_ab()
b3.pitch_list("b c b s d f f")
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #31 Joe Biagini
t4 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("f b b")
t4.out("G5-3")

# 7. BOS #12 Brock Holt (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("G6-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t4.new_ab()
t4.pitch_list("b c b")
t4.out("G4-3")


# Bot 4th
# Pitching: BOS #31 Drew Pomeranz
b4 = game.new_inning()

# 6. TOR #55 Russell Martin (X - X - X)
b4.new_ab()
b4.pitch_list("c b f c")
b4.out("!K")

# 7. TOR #8  Kendrys Morales (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c b")
b4.reach("BB")
b4.advance(2, "30 WP")

# 8. TOR #30 Anthony Alford (X - X - 8)
b4.new_ab()
b4.pitch_list("f b c b c")
b4.wp()
b4.out("!K")

# 9. TOR #7  Richard Urena (X - 8 - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #31 Joe Biagini
t5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("f b")
t5.out("G1-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(1)
t5.advance(2, "16 SB")
t5.advance(3, "16 F7")
t5.advance(4, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t5.new_ab()
t5.pitch_list("b b b c")
t5.out("F7")

# Pitching change (TOR): #77 John Axford replaces #31 Joe Biagini
t5.pitching_substitution(77)

# 3. BOS #28 J.D. Martinez (50 - X - X)
t5.new_ab()
t5.pitch_list("b c b")
t5.hit(1, rbis=1)

# 4. BOS #18 Mitch Moreland (X - X - 28)
t5.new_ab()
t5.pitch_list("s c d c")
t5.out("!K")


# Bot 5th
# Pitching: BOS #31 Drew Pomeranz
b5 = game.new_inning()

# 1. TOR #37 Teoscar Hernández (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)
b5.advance(2, "20 1B")
b5.advance(4, "14 2B")

# 2. TOR #20 Josh Donaldson (X - X - 37)
b5.new_ab()
b5.pitch_list("c c b")
b5.hit(1)
b5.advance(4, "14 2B")

# 3. TOR #14 Justin Smoak (X - 37 - 20)
b5.new_ab()
b5.pitch_list("c d f")
b5.hit(2, rbis=2)
b5.advance(4, "55 1B")

# 4. TOR #26 Yangervis Solarte (X - 14 - X)
b5.new_ab()
b5.pitch_list("f d s b f d f f b")
b5.reach("BB")
b5.advance(2, "55 1B")

# Pitching change (BOS): #76 Hector Velázquez replaces #31 Drew Pomeranz
b5.pitching_substitution(76)

# 5. TOR #11 Kevin Pillar (X - 14 - 26)
b5.new_ab()
b5.pitch_list("f b f f d f b s")
b5.out("K")

# 6. TOR #55 Russell Martin (X - 14 - 26)
b5.new_ab()
b5.hit(1, rbis=1)
b5.thrown_out(2, "8 DP1-6-3", 2, 76)

# 7. TOR #8  Kendrys Morales (X - 26 - 55)
b5.new_ab()
b5.out("DP1-6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #77 John Axford
t6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.out("F7")

# 6. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("l")
t6.out("B1-3")

# 7. BOS #12 Brock Holt (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b")
t6.out("G1-3")


# Bot 6th
# Pitching: BOS #76 Hector Velázquez
b6 = game.new_inning()

# Offensive change (TOR): Pinch-hitter #18 Curtis Granderson replaces #30 Anthony Alford, batting 8th
b6.offensive_substitution(8, 18, "PH")

# 8. TOR #18 Curtis Granderson (X - X - X)
b6.new_ab()
b6.pitch_list("c c b b f b")
b6.out("L8")

# 9. TOR #7  Richard Urena (X - X - X)
b6.new_ab()
b6.pitch_list("b f")
b6.hit(1)

# 1. TOR #37 Teoscar Hernández (X - X - 7)
b6.new_ab()
b6.pitch_list("v b s s d 1 f f")
b6.out("P6")

# 2. TOR #20 Josh Donaldson (X - X - 7)
b6.new_ab()
b6.pitch_list("f c t")
b6.out("KT")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #43 Sam Gaviglio
t7 = game.new_inning()

# Pitching change (TOR): #43 Sam Gaviglio replaces #77 John Axford
t7.pitching_substitution(43)

# Defensive switch (TOR): #18 Curtis Granderson moves to LF
t7.defensive_switch(18, "7")

# 8. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("b f b c")
t7.out("G4-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("f b f b b s")
t7.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("b c f b c")
t7.out("!K")


# Bot 7th
# Pitching: BOS #32 Matt Barnes
b7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #76 Hector Velázquez
b7.pitching_substitution(32)

# 3. TOR #14 Justin Smoak (X - X - X)
b7.new_ab()
b7.pitch_list("f b")
b7.out("F8")

# 4. TOR #26 Yangervis Solarte (X - X - X)
b7.new_ab()
b7.pitch_list("b b f")
b7.hit(1)
b7.thrown_out(4, "55 7-6-2", 3, 32)
b7.advance(3, "55 2B")

# 5. TOR #11 Kevin Pillar (X - X - 26)
b7.new_ab()
b7.pitch_list("c f f d s")
b7.out("K")

# 6. TOR #55 Russell Martin (X - X - 26)
b7.new_ab()
b7.pitch_list("b")
b7.hit(2)


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #43 Sam Gaviglio
t8 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("c b b c f f b f b")
t8.reach("BB")
t8.advance(2, "28 SB")
t8.advance(3, "18 1B")
t8.advance(4, "2 G1-3")

# 3. BOS #28 J.D. Martinez (X - X - 16)
t8.new_ab()
t8.pitch_list("b s 1 1 c b s")
t8.out("K")

# 4. BOS #18 Mitch Moreland (X - 16 - X)
t8.new_ab()
t8.pitch_list("d b")
t8.hit(1)
t8.advance(2, "2 G1-3")

# Pitching change (TOR): #36 Tyler Clippard replaces #43 Sam Gaviglio
t8.pitching_substitution(36)

# 5. BOS #2  Xander Bogaerts (16 - X - 18)
t8.new_ab()
t8.pitch_list("t d b c")
t8.out("G1-3", rbis=1)

# 6. BOS #11 Rafael Devers (X - 18 - X)
t8.new_ab()
t8.pitch_list("f")
t8.out("P6")


# Bot 8th
# Pitching: BOS #37 Heath Hembree
b8 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #32 Matt Barnes
b8.pitching_substitution(37)

# 7. TOR #8  Kendrys Morales (X - X - X)
b8.new_ab()
b8.pitch_list("b c s")
b8.hit(1)
b8.thrown_out(2, "7 FC5-4", 2, 37)

# 8. TOR #18 Curtis Granderson (X - X - 8)
b8.new_ab()
b8.pitch_list("b c s b s")
b8.out("K")

# 9. TOR #7  Richard Urena (X - X - 8)
b8.new_ab()
b8.pitch_list("b d")
b8.reach("FC5-4")

# 1. TOR #37 Teoscar Hernández (X - X - 7)
b8.new_ab()
b8.pitch_list("1 s b s t")
b8.out("KT")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #36 Tyler Clippard
t9 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.hit(2)
t9.thrown_out(3, "19 CS", 2, 36)

# 8. BOS #7  Christian Vázquez (X - 12 - X)
t9.new_ab()
t9.pitch_list("b b f f f b f f")
t9.out("P3")

# 9. BOS #19 Jackie Bradley Jr. (X - 12 - X)
t9.new_ab()
t9.pitch_list("b c s")
t9.hit(1)
t9.advance(2, "50 SB")

# 1. BOS #50 Mookie Betts (X - X - 19)
t9.new_ab()
t9.pitch_list("c d b s b b")
t9.reach("BB")

# 2. BOS #16 Andrew Benintendi (X - 19 - 50)
t9.new_ab()
t9.out("G4-3")


# Bot 9th
# Pitching: BOS #56 Joe Kelly
b9 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
b9.pitching_substitution(56)

# 2. TOR #20 Josh Donaldson (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("G3-1")

# 3. TOR #14 Justin Smoak (X - X - X)
b9.new_ab()
b9.out("F8")

# 4. TOR #26 Yangervis Solarte (X - X - X)
b9.new_ab()
b9.out("G4-3")

# Winning team: BOS
# WP: BOS #76 Hector Velázquez
game.winning_pitcher(76, is_away_team=True)
# SV: BOS #56 Joe Kelly
game.save_pitcher(56, is_away_team=True)

# Loser team: TOR
# LP: TOR #31 Joe Biagini
game.losing_pitcher(31)

# print(game)
game.generate_scorecard()
