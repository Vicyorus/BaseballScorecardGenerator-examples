import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TBR @ BOS, 2018-08-19
# https://www.baseball-reference.com/boxes/BOS/BOS201808190.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2018/08/19/531277/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-19 13:06-15:53",
        "at": "Fenway Park, Boston, MA",
        "att": "37,242",
        "temp": "71F, Cloudy",
        "wind": "16mph, In From CF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 63,
            "roster": {
                # Lineup
                0: "Mallex Smith",
                5: "Matt Duffy",
                9: "Jake Bauers",
                29: "Tommy Pham",
                18: "Joey Wendle",
                44: "C.J. Cron",
                26: "Ji Man Choi",
                35: "Brandon Lowe",
                45: "Jesús Sucre",
                # Starting pitcher
                63: "Diego Castillo",
                # Bench
                39: "Kevin Kiermaier",
                27: "Carlos Gómez",
                43: "Michael Pérez",
                1: "Willy Adames",
                # Bullpen
                46: "José Alvarado",
                20: "Tyler Glasnow",
                61: "Hunter Wood",
                48: "Ryan Yarbrough",
                68: "Jalen Beeks",
                56: "Adam Kolarek",
                52: "Chaz Roe",
                55: "Ryne Stanek",
                42: "Blake Snell",
                72: "Yonny Chirinos",
                54: "Sergio Romo",
            },
            "lefties": [46, 48, 68, 56, 42],
            "lineup": [
                [0, "9"],
                [5, "5"],
                [9, "7"],
                [29, "8"],
                [18, "6"],
                [44, "3"],
                [26, "0"],
                [35, "4"],
                [45, "2"],
            ],
            "bench": [
                [39, "CF"],
                [27, "CF"],
                [43, "C"],
                [1, "SS"],
            ],
            "bullpen": [46, 20, 61, 48, 68, 56, 52, 55, 42, 72, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 76,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                25: "Steve Pearce",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                76: "Hector Velázquez",
                # Bench
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [25, "3"],
                [28, "0"],
                [2, "6"],
                [36, "5"],
                [12, "4"],
                [23, "2"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [5, "2B"],
                [3, "C"],
            ],
            "bullpen": [47, 44, 22, 31, 61, 37, 24, 46, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "John Tumpane",
            "1B": "Jim Reynolds",
            "2B": "Chad Whitson",
            "3B": "Mark Wegner",
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
# Pitching: BOS #76 Hector Velázquez
t1 = game.new_inning()

# 1. TBR #0  Mallex Smith (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("G4-3")

# 2. TBR #5  Matt Duffy (X - X - X)
t1.new_ab()
t1.pitch_list("c f b")
t1.out("G6-3")

# 3. TBR #9  Jake Bauers (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c b")
t1.reach("BB")

# 4. TBR #29 Tommy Pham (X - X - 9)
t1.new_ab()
t1.pitch_list("b f s b f s")
t1.out("K")


# Bot 1st
# Pitching: TBR #63 Diego Castillo
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.out("G4-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G3")

# 3. BOS #25 Steve Pearce (X - X - X)
b1.new_ab()
b1.pitch_list("b c b b c")
b1.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #76 Hector Velázquez
t2 = game.new_inning()

# 5. TBR #18 Joey Wendle (X - X - X)
t2.new_ab()
t2.pitch_list("b b c")
t2.hit(4, rbis=1)

# 6. TBR #44 C.J. Cron (X - X - X)
t2.new_ab()
t2.out("G6-3")

# 7. TBR #26 Ji Man Choi (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(1)
t2.advance(2, "35 HBP")

# 8. TBR #35 Brandon Lowe (X - X - 26)
t2.new_ab()
t2.pitch_list("b 1 s f b")
t2.reach("HBP")
t2.thrown_out(2, "45 DP6-4-3", 2, 76)

# 9. TBR #45 Jesús Sucre (X - 26 - 35)
t2.new_ab()
t2.pitch_list("b f b b")
t2.out("DP6-4-3")


# Bot 2nd
# Pitching: TBR #63 Diego Castillo
b2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("P3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.hit(2)
b2.advance(3, "36 G4-3")

# 6. BOS #36 Eduardo Núñez (X - 2 - X)
b2.new_ab()
b2.pitch_list("c c")
b2.out("G4-3")

# Pitching change (TBR): #68 Jalen Beeks replaces #63 Diego Castillo
b2.pitching_substitution(68)

# 7. BOS #12 Brock Holt (2 - X - X)
b2.new_ab()
b2.pitch_list("d c f b b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #76 Hector Velázquez
t3 = game.new_inning()

# 1. TBR #0  Mallex Smith (X - X - X)
t3.new_ab()
t3.out("G3")

# 2. TBR #5  Matt Duffy (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(1)

# 3. TBR #9  Jake Bauers (X - X - 5)
t3.new_ab()
t3.out("F7")

# 4. TBR #29 Tommy Pham (X - X - 5)
t3.new_ab()
t3.pitch_list("c 1")
t3.out("G4-3")


# Bot 3rd
# Pitching: TBR #68 Jalen Beeks
b3 = game.new_inning()

# 8. BOS #23 Blake Swihart (X - X - X)
b3.new_ab()
b3.pitch_list("b f b f s")
b3.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("f b b f f")
b3.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("P4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #76 Hector Velázquez
t4 = game.new_inning()

# 5. TBR #18 Joey Wendle (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G4-3")

# 6. TBR #44 C.J. Cron (X - X - X)
t4.new_ab()
t4.pitch_list("b c f f f b f f")
t4.out("L9")

# 7. TBR #26 Ji Man Choi (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c f b")
t4.reach("BB")
t4.advance(2, "35 BB")

# 8. TBR #35 Brandon Lowe (X - X - 26)
t4.new_ab()
t4.pitch_list("b s c f b b b")
t4.reach("BB")

# 9. TBR #45 Jesús Sucre (X - 26 - 35)
t4.new_ab()
t4.pitch_list("c f f d f c")
t4.out("!K")


# Bot 4th
# Pitching: TBR #68 Jalen Beeks
b4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(2, "25 BB")
b4.advance(3, "28 DP6-4-3")

# 3. BOS #25 Steve Pearce (X - X - 16)
b4.new_ab()
b4.pitch_list("b c b b f b")
b4.reach("BB")
b4.thrown_out(2, "28 DP6-4-3", 1, 68)

# 4. BOS #28 J.D. Martinez (X - 16 - 25)
b4.new_ab()
b4.pitch_list("b s s d b f f")
b4.out("DP6-4-3")

# 5. BOS #2  Xander Bogaerts (16 - X - X)
b4.new_ab()
b4.pitch_list("c b b f d f f b")
b4.reach("BB")

# 6. BOS #36 Eduardo Núñez (16 - X - 2)
b4.new_ab()
b4.out("L7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #44 Brandon Workman
t5 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #76 Hector Velázquez
t5.pitching_substitution(44)

# 1. TBR #0  Mallex Smith (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G4-3")

# 2. TBR #5  Matt Duffy (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("L9")

# 3. TBR #9  Jake Bauers (X - X - X)
t5.new_ab()
t5.pitch_list("f c s")
t5.out("K")


# Bot 5th
# Pitching: TBR #68 Jalen Beeks
b5 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
b5.new_ab()
b5.pitch_list("c b c")
b5.error(6)
b5.reach("E6")
b5.thrown_out(2, "23 DP6-4-3", 1, 68)

# 8. BOS #23 Blake Swihart (X - X - 12)
b5.new_ab()
b5.out("DP6-4-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("c s b f f b b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #44 Brandon Workman
t6 = game.new_inning()

# 4. TBR #29 Tommy Pham (X - X - X)
t6.new_ab()
t6.out("G5-3")

# 5. TBR #18 Joey Wendle (X - X - X)
t6.new_ab()
t6.pitch_list("b c b")
t6.out("G4-3")

# 6. TBR #44 C.J. Cron (X - X - X)
t6.new_ab()
t6.out("G5-3")


# Bot 6th
# Pitching: TBR #68 Jalen Beeks
b6 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("c s f")
b6.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("c f b b f b")
b6.out("G4-3")

# Pitching change (TBR): #52 Chaz Roe replaces #68 Jalen Beeks
b6.pitching_substitution(52)

# 3. BOS #25 Steve Pearce (X - X - X)
b6.new_ab()
b6.pitch_list("c s b b b")
b6.out("P4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #56 Joe Kelly
t7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #44 Brandon Workman
t7.pitching_substitution(56)

# 7. TBR #26 Ji Man Choi (X - X - X)
t7.new_ab()
t7.pitch_list("b c b")
t7.out("L8")

# 8. TBR #35 Brandon Lowe (X - X - X)
t7.new_ab()
t7.pitch_list("s c f b s")
t7.out("K")

# 9. TBR #45 Jesús Sucre (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("F9")


# Bot 7th
# Pitching: TBR #52 Chaz Roe
b7 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("c c f b b b s")
b7.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("b c b f")
b7.out("G3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("c b f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #37 Heath Hembree
t8 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #56 Joe Kelly
t8.pitching_substitution(37)

# 1. TBR #0  Mallex Smith (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b")
t8.out("L9")

# 2. TBR #5  Matt Duffy (X - X - X)
t8.new_ab()
t8.pitch_list("b s f b")
t8.out("L8")

# 3. TBR #9  Jake Bauers (X - X - X)
t8.new_ab()
t8.pitch_list("b c b b f b")
t8.reach("BB")
# Offensive change (TBR): Pinch-runner #39 Kevin Kiermaier replaces #9 Jake Bauers
t8.offensive_substitution(3, 39, "PR")
t8.atbase("PR")

# 4. TBR #29 Tommy Pham (X - X - 9)
t8.new_ab()
t8.pitch_list("1 s c b")
t8.out("L9")


# Bot 8th
# Pitching: TBR #46 José Alvarado
b8 = game.new_inning()

# Pitching change (TBR): #46 José Alvarado replaces #52 Chaz Roe
b8.pitching_substitution(46)

# Defensive switch (TBR): #39 Kevin Kiermaier moves to CF
b8.defensive_switch(39, "8")

# Defensive switch (TBR): #29 Tommy Pham moves to LF
b8.defensive_switch(29, "7")

# Offensive change (BOS): Pinch-hitter #5 Ian Kinsler replaces #12 Brock Holt, batting 7th
b8.offensive_substitution(7, 5, "PH")

# 7. BOS #5  Ian Kinsler (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c f s")
b8.out("K")

# 8. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("b c s s")
b8.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("c c b f b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #32 Matt Barnes
t9 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #37 Heath Hembree
t9.pitching_substitution(32)

# Defensive switch (BOS): #5 Ian Kinsler moves to 2B
t9.defensive_switch(5, "4")

# 5. TBR #18 Joey Wendle (X - X - X)
t9.new_ab()
t9.pitch_list("l b b f b s")
t9.out("K")

# 6. TBR #44 C.J. Cron (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.hit(4, rbis=1)

# 7. TBR #26 Ji Man Choi (X - X - X)
t9.new_ab()
t9.pitch_list("b b b b")
t9.reach("BB")
t9.advance(2, "35 SB")

# 8. TBR #35 Brandon Lowe (X - X - 26)
t9.new_ab()
t9.pitch_list("b s b s b s")
t9.out("K")

# 9. TBR #45 Jesús Sucre (X - 26 - X)
t9.new_ab()
t9.pitch_list("c s s")
t9.out("K")


# Bot 9th
# Pitching: TBR #54 Sergio Romo
b9 = game.new_inning()

# Pitching change (TBR): #54 Sergio Romo replaces #46 José Alvarado
b9.pitching_substitution(54)

# 1. BOS #50 Mookie Betts (X - X - X)
b9.new_ab()
b9.pitch_list("c f b b s")
b9.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b9.new_ab()
b9.pitch_list("f b b")
b9.out("L6")

# Offensive change (BOS): Pinch-hitter #18 Mitch Moreland replaces #25 Steve Pearce, batting 3rd
b9.offensive_substitution(3, 18, "PH")

# 3. BOS #18 Mitch Moreland (X - X - X)
b9.new_ab()
b9.pitch_list("b b s f s")
b9.out("K")

# Winning team: TBR
# WP: TBR #68 Jalen Beeks
game.winning_pitcher(68, is_away_team=True)
# SV: TBR #54 Sergio Romo
game.save_pitcher(54, is_away_team=True)

# Loser team: BOS
# LP: BOS #76 Hector Velázquez
game.losing_pitcher(76)

# print(game)
game.generate_scorecard()
