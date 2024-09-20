import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2018-07-14
# https://www.baseball-reference.com/boxes/BOS/BOS201807140.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2018/07/14/530839/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-14 13:07-16:39",
        "at": "Fenway Park, Boston, MA",
        "att": "36,390",
        "temp": "74F, Partly Cloudy",
        "wind": "14mph, In From RF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 43,
            "roster": {
                # Lineup
                13: "Lourdes Gurriel Jr.",
                26: "Yangervis Solarte",
                37: "Teoscar Hernández",
                14: "Justin Smoak",
                8: "Kendrys Morales",
                11: "Kevin Pillar",
                15: "Randal Grichuk",
                1: "Aledmys Díaz",
                21: "Luke Maile",
                # Starting pitcher
                43: "Sam Gaviglio",
                # Bench
                55: "Russell Martin",
                29: "Devon Travis",
                27: "Dwight Smith Jr.",
                18: "Curtis Granderson",
                # Bullpen
                62: "Aaron Loup",
                31: "Joe Biagini",
                58: "Tim Mayza",
                47: "Chris Rowley",
                71: "Luis Santos",
                39: "Jake Petricka",
                36: "Tyler Clippard",
                22: "Seunghwan Oh",
                6: "Marcus Stroman",
                77: "John Axford",
                33: "J.A. Happ",
            },
            "lefties": [62, 58, 33],
            "lineup": [
                [13, "4"],
                [26, "5"],
                [37, "7"],
                [14, "3"],
                [8, "0"],
                [11, "8"],
                [15, "9"],
                [1, "6"],
                [21, "2"],
            ],
            "bench": [
                [55, "C"],
                [29, "2B"],
                [27, "LF"],
                [18, "CF"],
            ],
            "bullpen": [62, 31, 58, 47, 71, 39, 36, 22, 6, 77, 33],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                12: "Brock Holt",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                19: "Jackie Bradley Jr.",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                3: "Sandy León",
                5: "Tzu-Wei Lin",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                25: "Steve Pearce",
                18: "Mitch Moreland",
                59: "Sam Travis",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 66, 24],
            "lineup": [
                [50, "9"],
                [12, "4"],
                [28, "7"],
                [2, "6"],
                [19, "8"],
                [36, "0"],
                [23, "3"],
                [3, "2"],
                [5, "5"],
            ],
            "bench": [
                [25, "1B"],
                [18, "1B"],
                [59, "1B"],
            ],
            "bullpen": [47, 44, 22, 41, 66, 37, 24, 46, 76, 70, 56, 32],
        },
        "umpires": {
            "HP": "Mike Muchlinski",
            "1B": "Adrian Johnson",
            "2B": "Tripp Gibson",
            "3B": "Brian Gorman",
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

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t1.new_ab()
t1.pitch_list("b b c t f")
t1.hit(1)

# 2. TOR #26 Yangervis Solarte (X - X - 13)
t1.new_ab()
t1.pitch_list("f b f f c")
t1.out("!K")

# 3. TOR #37 Teoscar Hernández (X - X - 13)
t1.new_ab()
t1.pitch_list("c b b b s s")
t1.out("K")

# 4. TOR #14 Justin Smoak (X - X - 13)
t1.new_ab()
t1.pitch_list("d")
t1.out("G4-3")


# Bot 1st
# Pitching: TOR #43 Sam Gaviglio
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b c b f")
b1.hit(1)
b1.thrown_out(2, "12 DP6-4-3", 1, 43)

# 2. BOS #12 Brock Holt (X - X - 50)
b1.new_ab()
b1.out("DP6-4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c b s b b")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 5. TOR #8  Kendrys Morales (X - X - X)
t2.new_ab()
t2.pitch_list("s b")
t2.hit(1)
t2.thrown_out(2, "11 FC5-4", 1, 57)

# 6. TOR #11 Kevin Pillar (X - X - 8)
t2.new_ab()
t2.pitch_list("b f f b")
t2.reach("FC5-4")
t2.advance(3, "15 1B")

# 7. TOR #15 Randal Grichuk (X - X - 11)
t2.new_ab()
t2.hit(1)
t2.thrown_out(2, "7-4", 2, 57)

# 8. TOR #1  Aledmys Díaz (11 - X - X)
t2.new_ab()
t2.pitch_list("b b f c f s")
t2.out("K")


# Bot 2nd
# Pitching: TOR #43 Sam Gaviglio
b2 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("c b b s c")
b2.out("!K")

# 5. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("b c s b s")
b2.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)

# 7. BOS #23 Blake Swihart (X - X - 36)
b2.new_ab()
b2.pitch_list("c d b c")
b2.out("P5")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 9. TOR #21 Luke Maile (X - X - X)
t3.new_ab()
t3.pitch_list("b f")
t3.out("F9")

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c c b c")
t3.out("!K")

# 2. TOR #26 Yangervis Solarte (X - X - X)
t3.new_ab()
t3.out("G5-3")


# Bot 3rd
# Pitching: TOR #43 Sam Gaviglio
b3 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("b c b b f")
b3.out("F9")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b3.new_ab()
b3.pitch_list("b b f b b")
b3.reach("BB")
b3.advance(2, "50 1B")
b3.thrown_out(2, "12 DP8-4", 3, 43)

# 1. BOS #50 Mookie Betts (X - X - 5)
b3.new_ab()
b3.pitch_list("b c 1")
b3.hit(1)

# 2. BOS #12 Brock Holt (X - 5 - 50)
b3.new_ab()
b3.pitch_list("c")
b3.out("DP8-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 3. TOR #37 Teoscar Hernández (X - X - X)
t4.new_ab()
t4.pitch_list("b t t f")
t4.out("F8")

# 4. TOR #14 Justin Smoak (X - X - X)
t4.new_ab()
t4.pitch_list("b c c")
t4.out("G3")

# 5. TOR #8  Kendrys Morales (X - X - X)
t4.new_ab()
t4.pitch_list("b f")
t4.out("G6-3")


# Bot 4th
# Pitching: TOR #43 Sam Gaviglio
b4 = game.new_inning()

# Defensive change (TOR): #27 Dwight Smith Jr. replaces #11 Kevin Pillar (CF), playing RF, batting 6th
b4.defensive_substitution(6, 27, "9")

# Defensive switch (TOR): #15 Randal Grichuk moves to CF
b4.defensive_switch(15, "8")

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("s b b c b")
b4.hit(4)

# 4. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("b c b f")
b4.out("F9")

# Pitching change (TOR): #58 Tim Mayza replaces #43 Sam Gaviglio
b4.pitching_substitution(58)

# 5. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("c b s f s")
b4.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("P4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #57 Eduardo Rodriguez
t5 = game.new_inning()

# 6. TOR #27 Dwight Smith Jr. (X - X - X)
t5.new_ab()
t5.out("B1-3")

# 7. TOR #15 Randal Grichuk (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("P3")

# 8. TOR #1  Aledmys Díaz (X - X - X)
t5.new_ab()
t5.pitch_list("f c")
t5.out("G4-3")


# Bot 5th
# Pitching: TOR #58 Tim Mayza
b5 = game.new_inning()

# 7. BOS #23 Blake Swihart (X - X - X)
b5.new_ab()
b5.pitch_list("c f b b")
b5.out("L9")

# 8. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("b c b s f b s")
b5.out("K")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b5.new_ab()
b5.pitch_list("c s b")
b5.hit(1)
b5.advance(2, "50 IBB")

# 1. BOS #50 Mookie Betts (X - X - 5)
b5.new_ab()
b5.pitch_list("b b b v")
b5.reach("IBB")

# 2. BOS #12 Brock Holt (X - 5 - 50)
b5.new_ab()
b5.pitch_list("c b f d b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #57 Eduardo Rodriguez
t6 = game.new_inning()

# 9. TOR #21 Luke Maile (X - X - X)
t6.new_ab()
t6.pitch_list("f b b b f c")
t6.out("!K")

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t6.new_ab()
t6.hit(1)
t6.advance(2, "26 G3")

# Pitching change (BOS): #37 Heath Hembree replaces #57 Eduardo Rodriguez
t6.pitching_substitution(37)

# 2. TOR #26 Yangervis Solarte (X - X - 13)
t6.new_ab()
t6.pitch_list("1 b f s")
t6.out("G3")

# 3. TOR #37 Teoscar Hernández (X - 13 - X)
t6.new_ab()
t6.pitch_list("b b c f b b")
t6.reach("BB")

# 4. TOR #14 Justin Smoak (X - 13 - 37)
t6.new_ab()
t6.out("F8")


# Bot 6th
# Pitching: TOR #71 Luis Santos
b6 = game.new_inning()

# Pitching change (TOR): #71 Luis Santos replaces #58 Tim Mayza
b6.pitching_substitution(71)

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("c s s")
b6.out("K")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("b c b")
b6.out("G5-3")

# 5. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("f b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #56 Joe Kelly
t7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
t7.pitching_substitution(56)

# 5. TOR #8  Kendrys Morales (X - X - X)
t7.new_ab()
t7.pitch_list("b b c c")
t7.hit(1)
t7.advance(3, "27 2B")
t7.advance(4, "1 G6-3")

# 6. TOR #27 Dwight Smith Jr. (X - X - 8)
t7.new_ab()
t7.pitch_list("b c b")
t7.hit(2)
t7.advance(3, "1 G6-3")
t7.advance(4, "13 1B")

# 7. TOR #15 Randal Grichuk (8 - 27 - X)
t7.new_ab()
t7.pitch_list("b d c")
t7.out("G5-3")

# 8. TOR #1  Aledmys Díaz (8 - 27 - X)
t7.new_ab()
t7.out("G6-3", rbis=1)

# 9. TOR #21 Luke Maile (27 - X - X)
t7.new_ab()
t7.pitch_list("b b b b")
t7.reach("BB")
t7.advance(3, "13 1B")

# Pitching change (BOS): #32 Matt Barnes replaces #56 Joe Kelly
t7.pitching_substitution(32)

# 1. TOR #13 Lourdes Gurriel Jr. (27 - X - 21)
t7.new_ab()
t7.pitch_list("s b")
t7.hit(1, rbis=1)

# 2. TOR #26 Yangervis Solarte (21 - X - 13)
t7.new_ab()
t7.pitch_list("c b d f s")
t7.out("K")


# Bot 7th
# Pitching: TOR #71 Luis Santos
b7 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.out("F7")

# 7. BOS #23 Blake Swihart (X - X - X)
b7.new_ab()
b7.hit(1)
b7.thrown_out(1, "3 DP7-3", 3, 71)

# 8. BOS #3  Sandy León (X - X - 23)
b7.new_ab()
b7.pitch_list("c d f")
b7.out("DP7-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# 3. TOR #37 Teoscar Hernández (X - X - X)
t8.new_ab()
t8.pitch_list("b c s b b f f")
t8.out("F7")

# 4. TOR #14 Justin Smoak (X - X - X)
t8.new_ab()
t8.pitch_list("c b s b b s")
t8.out("K")

# 5. TOR #8  Kendrys Morales (X - X - X)
t8.new_ab()
t8.pitch_list("b s b s b b")
t8.reach("BB")
t8.advance(2, "27 BB")
# Offensive change (TOR): Pinch-runner #18 Curtis Granderson replaces #8 Kendrys Morales
t8.offensive_substitution(5, 18, "PR")
t8.atbase("PR")

# 6. TOR #27 Dwight Smith Jr. (X - X - 8)
t8.new_ab()
t8.pitch_list("c c b f d b b")
t8.reach("BB")

# 7. TOR #15 Randal Grichuk (X - 8 - 27)
t8.new_ab()
t8.pitch_list("c s c")
t8.out("!K")


# Bot 8th
# Pitching: TOR #31 Joe Biagini
b8 = game.new_inning()

# Pitching change (TOR): #31 Joe Biagini replaces #71 Luis Santos
b8.pitching_substitution(31)

# Defensive switch (TOR): #18 Curtis Granderson moves to DH
b8.defensive_switch(18, "0")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b8.new_ab()
b8.pitch_list("c s s")
b8.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("c b b b")
b8.hit(1)
b8.error(5)
b8.advance(2, "E5")
b8.advance(3, "12 SB")

# 2. BOS #12 Brock Holt (X - 50 - X)
b8.new_ab()
b8.pitch_list("d c s b")
b8.out("G4-3")

# 3. BOS #28 J.D. Martinez (50 - X - X)
b8.new_ab()
b8.pitch_list("f f b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #44 Brandon Workman
t9 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #32 Matt Barnes
t9.pitching_substitution(44)

# 8. TOR #1  Aledmys Díaz (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("G5-3")

# 9. TOR #21 Luke Maile (X - X - X)
t9.new_ab()
t9.pitch_list("c f f b s")
t9.out("K")

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("s s b b t")
t9.out("KT")


# Bot 9th
# Pitching: TOR #36 Tyler Clippard
b9 = game.new_inning()

# Pitching change (TOR): #36 Tyler Clippard replaces #31 Joe Biagini
b9.pitching_substitution(36)

# 4. BOS #2  Xander Bogaerts (X - X - X)
b9.new_ab()
b9.pitch_list("c b f b")
b9.hit(2)
b9.advance(4, "19 2B")

# 5. BOS #19 Jackie Bradley Jr. (X - 2 - X)
b9.new_ab()
b9.pitch_list("l")
b9.hit(2, rbis=1)

# 6. BOS #36 Eduardo Núñez (X - 19 - X)
b9.new_ab()
b9.pitch_list("f b b s f d f s")
b9.out("K")

# 7. BOS #23 Blake Swihart (X - 19 - X)
b9.new_ab()
b9.pitch_list("c d f f f d b")
b9.out("F8")

# 8. BOS #3  Sandy León (X - 19 - X)
b9.new_ab()
b9.pitch_list("c b")
b9.out("G5-3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #46 Craig Kimbrel
t10 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #44 Brandon Workman
t10.pitching_substitution(46)

# 2. TOR #26 Yangervis Solarte (X - X - X)
t10.new_ab()
t10.pitch_list("f b f f b s")
t10.out("K")

# 3. TOR #37 Teoscar Hernández (X - X - X)
t10.new_ab()
t10.pitch_list("c s b b s")
t10.out("K")

# 4. TOR #14 Justin Smoak (X - X - X)
t10.new_ab()
t10.pitch_list("f c b b b f b")
t10.reach("BB")
# Offensive change (TOR): Pinch-runner #29 Devon Travis replaces #14 Justin Smoak
t10.offensive_substitution(4, 29, "PR")
t10.atbase("PR")

# 5. TOR #18 Curtis Granderson (X - X - 14)
t10.new_ab()
t10.pitch_list("c")
t10.out("L9")


# Bot 10th
# Pitching: TOR #47 Chris Rowley
b10 = game.new_inning()

# Pitching change (TOR): #47 Chris Rowley replaces #36 Tyler Clippard
b10.pitching_substitution(47)

# Defensive switch (TOR): #13 Lourdes Gurriel Jr. moves to SS
b10.defensive_switch(13, "6")

# Defensive switch (TOR): #26 Yangervis Solarte moves to 1B
b10.defensive_switch(26, "3")

# Defensive switch (TOR): #29 Devon Travis moves to 2B
b10.defensive_switch(29, "4")

# Defensive switch (TOR): #1 Aledmys Díaz moves to 3B
b10.defensive_switch(1, "5")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b10.new_ab()
b10.pitch_list("l")
b10.out("G3")

# 1. BOS #50 Mookie Betts (X - X - X)
b10.new_ab()
b10.pitch_list("b")
b10.error(6)
b10.reach("E6")
b10.advance(3, "12 1B")
b10.advance("U", "2 HR")

# 2. BOS #12 Brock Holt (X - X - 50)
b10.new_ab()
b10.pitch_list("b b c")
b10.hit(1)
b10.advance(2, "28 IBB")
b10.advance(4, "2 HR")

# 3. BOS #28 J.D. Martinez (50 - X - 12)
b10.new_ab()
b10.pitch_list("v v v v")
b10.reach("IBB")
b10.advance(4, "2 HR")

# 4. BOS #2  Xander Bogaerts (50 - 12 - 28)
b10.new_ab()
b10.pitch_list("b b")
b10.hit(4, rbis=4)

# Winning team: BOS
# WP: BOS #46 Craig Kimbrel
game.winning_pitcher(46)

# Loser team: TOR
# LP: TOR #47 Chris Rowley
game.losing_pitcher(47, is_away_team=True)

# print(game)
game.generate_scorecard()
