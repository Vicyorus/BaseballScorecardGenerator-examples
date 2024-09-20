import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2018-05-12
# https://www.baseball-reference.com/boxes/TOR/TOR201805120.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2018/05/12/529988/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-12 16:08-19:19",
        "at": "Rogers Centre, Toronto, ON",
        "att": "37,588",
        "temp": "68F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Starting pitcher
                24: "David Price",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
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
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [28, "0"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [7, "2"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [57, 39, 22, 41, 31, 61, 37, 46, 76, 56, 32],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 25,
            "roster": {
                # Lineup
                37: "Teoscar Hernández",
                20: "Josh Donaldson",
                26: "Yangervis Solarte",
                14: "Justin Smoak",
                11: "Kevin Pillar",
                55: "Russell Martin",
                30: "Anthony Alford",
                21: "Luke Maile",
                3: "Gio Urshela",
                # Starting pitcher
                25: "Marco Estrada",
                # Bench
                7: "Richard Urena",
                13: "Lourdes Gurriel Jr.",
                18: "Curtis Granderson",
                8: "Kendrys Morales",
                # Bullpen
                62: "Aaron Loup",
                57: "Jaime García",
                31: "Joe Biagini",
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
                [20, "0"],
                [26, "4"],
                [14, "3"],
                [11, "8"],
                [55, "5"],
                [30, "7"],
                [21, "2"],
                [3, "6"],
            ],
            "bench": [
                [7, "SS"],
                [13, "LF"],
                [18, "CF"],
                [8, "DH"],
            ],
            "bullpen": [62, 57, 31, 39, 43, 41, 36, 22, 77, 52, 33],
        },
        "umpires": {
            "HP": "Ron Kulpa",
            "1B": "Jerry Meals",
            "2B": "Gabe Morales",
            "3B": "Ed Hickox",
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
# Pitching: TOR #25 Marco Estrada
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b f")
t1.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("s s")
t1.hit(1)
t1.thrown_out(2, "28 FC6-4", 3, 25)

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t1.new_ab()
t1.pitch_list("f f d 1 b b s")
t1.out("K")

# 4. BOS #28 J.D. Martinez (X - X - 16)
t1.new_ab()
t1.reach("FC6-4")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. TOR #37 Teoscar Hernández (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("G3")

# 2. TOR #20 Josh Donaldson (X - X - X)
b1.new_ab()
b1.pitch_list("b s f b b b")
b1.reach("BB")

# 3. TOR #26 Yangervis Solarte (X - X - 20)
b1.new_ab()
b1.pitch_list("c")
b1.out("L8")

# 4. TOR #14 Justin Smoak (X - X - 20)
b1.new_ab()
b1.pitch_list("c b")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #25 Marco Estrada
t2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c b s f")
t2.out("F8")

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("b f f f b f t")
t2.out("KT")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.hit(1)
t2.error(9)
t2.advance(2, "E9")

# 8. BOS #19 Jackie Bradley Jr. (X - 36 - X)
t2.new_ab()
t2.pitch_list("t c b")
t2.out("P3")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 5. TOR #11 Kevin Pillar (X - X - X)
b2.new_ab()
b2.pitch_list("c b s c")
b2.out("!K")

# 6. TOR #55 Russell Martin (X - X - X)
b2.new_ab()
b2.pitch_list("s c b c")
b2.out("!K")

# 7. TOR #30 Anthony Alford (X - X - X)
b2.new_ab()
b2.pitch_list("b b c f b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #25 Marco Estrada
t3 = game.new_inning()

# 9. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b")
t3.out("F7")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.hit(2)
t3.advance(4, "16 2B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t3.new_ab()
t3.pitch_list("b d d c")
t3.hit(2, rbis=1)
t3.advance(4, "13 HR")

# 3. BOS #13 Hanley Ramirez (X - 16 - X)
t3.new_ab()
t3.pitch_list("f")
t3.hit(4, rbis=2)

# 4. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("b c b c b b")
t3.reach("BB")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t3.new_ab()
t3.pitch_list("f d b c")
t3.out("F7")

# 6. BOS #11 Rafael Devers (X - X - 28)
t3.new_ab()
t3.pitch_list("f b t f b f f f s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 8. TOR #21 Luke Maile (X - X - X)
b3.new_ab()
b3.pitch_list("b b c b c f s")
b3.out("K")

# 9. TOR #3  Gio Urshela (X - X - X)
b3.new_ab()
b3.pitch_list("f b")
b3.hit(1)
b3.advance(2, "37 1B")
b3.thrown_out(2, "20 DP6-4", 3, 24)

# 1. TOR #37 Teoscar Hernández (X - X - 3)
b3.new_ab()
b3.pitch_list("f")
b3.hit(1)

# 2. TOR #20 Josh Donaldson (X - 3 - 37)
b3.new_ab()
b3.pitch_list("c b f b")
b3.out("DP6-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #25 Marco Estrada
t4 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("c s")
t4.out("F8")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("b c t f f f b b f s")
t4.out("K")

# 9. BOS #7  Christian Vázquez (X - X - X)
t4.new_ab()
t4.out("F8")


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 3. TOR #26 Yangervis Solarte (X - X - X)
b4.new_ab()
b4.pitch_list("s b f")
b4.out("L7")

# 4. TOR #14 Justin Smoak (X - X - X)
b4.new_ab()
b4.pitch_list("c b b s b b")
b4.reach("BB")
b4.thrown_out(2, "11 FC6-4", 2, 24)

# 5. TOR #11 Kevin Pillar (X - X - 14)
b4.new_ab()
b4.pitch_list("f f")
b4.reach("FC6-4")
b4.advance(2, "55 BB")
b4.advance(4, "30 1B")

# 6. TOR #55 Russell Martin (X - X - 11)
b4.new_ab()
b4.pitch_list("c b b f d b")
b4.reach("BB")
b4.advance(2, "30 1B")

# 7. TOR #30 Anthony Alford (X - 11 - 55)
b4.new_ab()
b4.pitch_list("b b")
b4.hit(1, rbis=1)

# 8. TOR #21 Luke Maile (X - 55 - 30)
b4.new_ab()
b4.pitch_list("b c s b f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #25 Marco Estrada
t5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("b f")
t5.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("c b f")
t5.out("G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t5.new_ab()
t5.out("F9")


# Bot 5th
# Pitching: BOS #24 David Price
b5 = game.new_inning()

# 9. TOR #3  Gio Urshela (X - X - X)
b5.new_ab()
b5.pitch_list("b s c b s")
b5.out("K")

# 1. TOR #37 Teoscar Hernández (X - X - X)
b5.new_ab()
b5.hit(2)
b5.advance(3, "20 G1-3")

# 2. TOR #20 Josh Donaldson (X - 37 - X)
b5.new_ab()
b5.out("G1-3")

# 3. TOR #26 Yangervis Solarte (37 - X - X)
b5.new_ab()
b5.pitch_list("f b b")
b5.out("P6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #25 Marco Estrada
t6 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("c f b b s")
t6.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("c b c")
t6.hit(2)
t6.advance(4, "11 1B")

# 6. BOS #11 Rafael Devers (X - 2 - X)
t6.new_ab()
t6.hit(1, rbis=1)

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t6.new_ab()
t6.pitch_list("f")
t6.out("P3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 11)
t6.new_ab()
t6.out("F9")


# Bot 6th
# Pitching: BOS #24 David Price
b6 = game.new_inning()

# 4. TOR #14 Justin Smoak (X - X - X)
b6.new_ab()
b6.pitch_list("f b b f f")
b6.hit(4)

# 5. TOR #11 Kevin Pillar (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("(F)P3")

# Pitching change (BOS): #39 Carson Smith replaces #24 David Price
b6.pitching_substitution(39)

# 6. TOR #55 Russell Martin (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b f")
b6.out("G5-3")

# 7. TOR #30 Anthony Alford (X - X - X)
b6.new_ab()
b6.error(5)
b6.reach("E5", end_base=2)

# 8. TOR #21 Luke Maile (X - 30 - X)
b6.new_ab()
b6.pitch_list("c b b c s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #39 Jake Petricka
t7 = game.new_inning()

# Pitching change (TOR): #39 Jake Petricka replaces #25 Marco Estrada
t7.pitching_substitution(39)

# 9. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("c c b")
t7.hit(1)
t7.advance(2, "50 1B")
t7.thrown_out(3, "16 CS", 1, 62)

# 1. BOS #50 Mookie Betts (X - X - 7)
t7.new_ab()
t7.pitch_list("c f b")
t7.hit(1)
t7.advance(2, "16 CS")

# Pitching change (TOR): #62 Aaron Loup replaces #39 Jake Petricka
t7.pitching_substitution(62)

# 2. BOS #16 Andrew Benintendi (X - 7 - 50)
t7.new_ab()
t7.pitch_list("b c b f s")
t7.out("K")

# Pitching change (TOR): #22 Seunghwan Oh replaces #62 Aaron Loup
t7.pitching_substitution(22)

# 3. BOS #13 Hanley Ramirez (X - 50 - X)
t7.new_ab()
t7.pitch_list("b c")
t7.out("P6")


# Bot 7th
# Pitching: BOS #76 Hector Velázquez
b7 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #39 Carson Smith
b7.pitching_substitution(76)

# Offensive change (TOR): Pinch-hitter #7 Richard Urena replaces #3 Gio Urshela, batting 9th
b7.offensive_substitution(9, 7, "PH")

# 9. TOR #7  Richard Urena (X - X - X)
b7.new_ab()
b7.pitch_list("b f s")
b7.hit(1)
b7.thrown_out(2, "37 DP6-4-3", 1, 76)

# 1. TOR #37 Teoscar Hernández (X - X - 7)
b7.new_ab()
b7.out("DP6-4-3")

# 2. TOR #20 Josh Donaldson (X - X - X)
b7.new_ab()
b7.out("G3-1")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #22 Seunghwan Oh
t8 = game.new_inning()

# Defensive switch (TOR): #7 Richard Urena moves to SS
t8.defensive_switch(7, "6")

# 4. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("f b b f f s")
t8.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("c b b")
t8.out("F7")

# 6. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.pitch_list("s")
t8.hit(1)

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t8.new_ab()
t8.pitch_list("f s s")
t8.out("K")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #76 Hector Velázquez
b8.pitching_substitution(56)

# 3. TOR #26 Yangervis Solarte (X - X - X)
b8.new_ab()
b8.pitch_list("c f b s")
b8.out("K")

# 4. TOR #14 Justin Smoak (X - X - X)
b8.new_ab()
b8.pitch_list("c s b b b s")
b8.out("K")

# 5. TOR #11 Kevin Pillar (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)
b8.advance(2, "55 SB")

# 6. TOR #55 Russell Martin (X - X - 11)
b8.new_ab()
b8.pitch_list("b c c d b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #52 Ryan Tepera
t9 = game.new_inning()

# Pitching change (TOR): #52 Ryan Tepera replaces #22 Seunghwan Oh
t9.pitching_substitution(52)

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("c c b b s")
t9.out("K")

# 9. BOS #7  Christian Vázquez (X - X - X)
t9.new_ab()
t9.pitch_list("c b f f s")
t9.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("s b b b c")
t9.hit(2)
t9.advance(4, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t9.new_ab()
t9.hit(1, rbis=1)

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t9.new_ab()
t9.pitch_list("1 s s 1 b c")
t9.out("!K")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
b9.pitching_substitution(46)

# Offensive change (TOR): Pinch-hitter #18 Curtis Granderson replaces #30 Anthony Alford, batting 7th
b9.offensive_substitution(7, 18, "PH")

# 7. TOR #18 Curtis Granderson (X - X - X)
b9.new_ab()
b9.pitch_list("c c")
b9.out("G1-3")

# 8. TOR #21 Luke Maile (X - X - X)
b9.new_ab()
b9.pitch_list("b s s s")
b9.out("K")

# 9. TOR #7  Richard Urena (X - X - X)
b9.new_ab()
b9.pitch_list("c s s")
b9.out("K")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: TOR
# LP: TOR #25 Marco Estrada
game.losing_pitcher(25)

# print(game)
game.generate_scorecard()
