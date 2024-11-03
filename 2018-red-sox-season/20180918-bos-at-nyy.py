import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2018-09-18
# https://www.baseball-reference.com/boxes/NYA/NYA201809180.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2018/09/18/531661/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-18 19:08-22:21",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "38,695",
        "temp": "72F, Cloudy",
        "wind": "5mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 17,
            "roster": {
                # Lineup
                5: "Ian Kinsler",
                25: "Steve Pearce",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                0: "Brandon Phillips",
                12: "Brock Holt",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                17: "Nathan Eovaldi",
                # Bench
                30: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                59: "Sam Travis",
                11: "Rafael Devers",
                23: "Blake Swihart",
                16: "Andrew Benintendi",
                50: "Mookie Betts",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 66, 63, 24],
            "lineup": [
                [5, "4"],
                [25, "3"],
                [28, "9"],
                [2, "6"],
                [36, "0"],
                [0, "5"],
                [12, "7"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [30, "OF"],
                [18, "1B"],
                [59, "1B"],
                [11, "3B"],
                [23, "C"],
                [16, "LF"],
                [50, "SS"],
                [3, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 41, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 32],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 34,
            "roster": {
                # Lineup
                26: "Andrew McCutchen",
                99: "Aaron Judge",
                18: "Didi Gregorius",
                27: "Giancarlo Stanton",
                31: "Aaron Hicks",
                41: "Miguel Andujar",
                24: "Gary Sánchez",
                14: "Neil Walker",
                25: "Gleyber Torres",
                # Starting pitcher
                34: "J.A. Happ",
                # Bench
                28: "Austin Romine",
                33: "Greg Bird",
                66: "Kyle Higashioka",
                29: "Adeiny Hechavarría",
                11: "Brett Gardner",
                12: "Tyler Wade",
                74: "Ronald Torreyes",
                45: "Luke Voit",
                # Bullpen
                67: "A.J. Cole",
                68: "Dellin Betances",
                40: "Luis Severino",
                65: "Domingo Germán",
                36: "Lance Lynn",
                43: "Chance Adams",
                38: "Jonathan Loáisiga",
                55: "Sonny Gray",
                56: "Jonathan Holder",
                52: "CC Sabathia",
                53: "Zack Britton",
                19: "Masahiro Tanaka",
                57: "Chad Green",
                48: "Tommy Kahnle",
                85: "Luis Cessa",
                71: "Stephen Tarpley",
                30: "David Robertson",
                61: "Justus Sheffield",
            },
            "lefties": [34, 52, 53, 71, 61],
            "lineup": [
                [26, "7"],
                [99, "9"],
                [18, "6"],
                [27, "0"],
                [31, "8"],
                [41, "5"],
                [24, "2"],
                [14, "3"],
                [25, "4"],
            ],
            "bench": [
                [28, "C"],
                [33, "1B"],
                [66, "C"],
                [29, "2B"],
                [11, "LF"],
                [12, "3B"],
                [74, "SS"],
                [45, "1B"],
            ],
            "bullpen": [67, 68, 40, 65, 36, 43, 38, 55, 56, 52, 53, 19, 57, 48, 85, 71, 30, 61],
        },
        "umpires": {
            "HP": "Chad Fairchild",
            "1B": "Chris Guccione",
            "2B": "Kerwin Danley",
            "3B": "Mike Estabrook",
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
# Pitching: NYY #34 J.A. Happ
t1 = game.new_inning()

# 1. BOS #5  Ian Kinsler (X - X - X)
t1.new_ab()
t1.out("F8")

# 2. BOS #25 Steve Pearce (X - X - X)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")

# 3. BOS #28 J.D. Martinez (X - X - 25)
t1.new_ab()
t1.pitch_list("b c")
t1.out("F9")

# 4. BOS #2  Xander Bogaerts (X - X - 25)
t1.new_ab()
t1.pitch_list("b c f s")
t1.out("K")


# Bot 1st
# Pitching: BOS #17 Nathan Eovaldi
b1 = game.new_inning()

# 1. NYY #26 Andrew McCutchen (X - X - X)
b1.new_ab()
b1.pitch_list("c b b f s")
b1.out("K")

# 2. NYY #99 Aaron Judge (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("L9")

# 3. NYY #18 Didi Gregorius (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #34 J.A. Happ
t2 = game.new_inning()

# 5. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b f f f s")
t2.out("K")

# 6. BOS #0  Brandon Phillips (X - X - X)
t2.new_ab()
t2.pitch_list("c b s b s")
t2.out("K")

# 7. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("c s b b")
t2.hit(1)
t2.advance(2, "7 BB")

# 8. BOS #7  Christian Vázquez (X - X - 12)
t2.new_ab()
t2.pitch_list("1 f b b b s b")
t2.reach("BB")

# 9. BOS #19 Jackie Bradley Jr. (X - 12 - 7)
t2.new_ab(is_risp=True)
t2.pitch_list("s b")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #17 Nathan Eovaldi
b2 = game.new_inning()

# 4. NYY #27 Giancarlo Stanton (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.out("G1-3")

# 5. NYY #31 Aaron Hicks (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)

# 6. NYY #41 Miguel Andujar (X - X - 31)
b2.new_ab()
b2.out("F9")

# 7. NYY #24 Gary Sánchez (X - X - 31)
b2.new_ab()
b2.pitch_list("c b b f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #34 J.A. Happ
t3 = game.new_inning()

# 1. BOS #5  Ian Kinsler (X - X - X)
t3.new_ab()
t3.pitch_list("c b f f f")
t3.hit(1)
t3.advance(2, "25 BLK")
t3.advance(3, "28 PB")
t3.advance("U", "28 SF9")

# 2. BOS #25 Steve Pearce (X - X - 5)
t3.new_ab(is_risp=True)
t3.pitch_list("n b f b f b b")
t3.balk()
t3.reach("BB")
t3.advance(2, "28 PB")
t3.advance(3, "28 SF9")

# 3. BOS #28 J.D. Martinez (X - 5 - 25)
t3.new_ab(is_risp=True)
t3.pitch_list("f b b")
t3.pb()
t3.out("SF9", rbis=1)

# 4. BOS #2  Xander Bogaerts (25 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f")
t3.out("F8")

# 5. BOS #36 Eduardo Núñez (25 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f b")
t3.out("F8")


# Bot 3rd
# Pitching: BOS #17 Nathan Eovaldi
b3 = game.new_inning()

# 8. NYY #14 Neil Walker (X - X - X)
b3.new_ab()
b3.pitch_list("b c b b b")
b3.reach("BB")
b3.advance(2, "26 BB")

# 9. NYY #25 Gleyber Torres (X - X - 14)
b3.new_ab()
b3.pitch_list("b c b s f f b f")
b3.out("F7")

# 1. NYY #26 Andrew McCutchen (X - X - 14)
b3.new_ab()
b3.pitch_list("b b d c c f f f b")
b3.reach("BB")
b3.thrown_out(2, "99 DP6-4-3", 2, 17)

# 2. NYY #99 Aaron Judge (X - 14 - 26)
b3.new_ab(is_risp=True)
b3.out("DP6-4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #34 J.A. Happ
t4 = game.new_inning()

# 6. BOS #0  Brandon Phillips (X - X - X)
t4.new_ab()
t4.pitch_list("b b s f s")
t4.out("K")

# 7. BOS #12 Brock Holt (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("L9")

# 8. BOS #7  Christian Vázquez (X - X - X)
t4.new_ab()
t4.pitch_list("b b f f")
t4.out("(F)P3")


# Bot 4th
# Pitching: BOS #17 Nathan Eovaldi
b4 = game.new_inning()

# 3. NYY #18 Didi Gregorius (X - X - X)
b4.new_ab()
b4.pitch_list("b f s s")
b4.out("K")

# 4. NYY #27 Giancarlo Stanton (X - X - X)
b4.new_ab()
b4.pitch_list("s b")
b4.out("G6-3")

# 5. NYY #31 Aaron Hicks (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("L5")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #34 J.A. Happ
t5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("f s f s")
t5.out("K")

# 1. BOS #5  Ian Kinsler (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("L8")

# 2. BOS #25 Steve Pearce (X - X - X)
t5.new_ab()
t5.pitch_list("c s f")
t5.out("P5")


# Bot 5th
# Pitching: BOS #17 Nathan Eovaldi
b5 = game.new_inning()

# 6. NYY #41 Miguel Andujar (X - X - X)
b5.new_ab()
b5.pitch_list("c c b b f")
b5.out("P3")

# 7. NYY #24 Gary Sánchez (X - X - X)
b5.new_ab()
b5.out("G1-3")

# 8. NYY #14 Neil Walker (X - X - X)
b5.new_ab()
b5.pitch_list("c f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #34 J.A. Happ
t6 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("P4")

# 4. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("c b c f b b")
t6.hit(2)
t6.advance(3, "36 1B")

# 5. BOS #36 Eduardo Núñez (X - 2 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b f f b f f")
t6.hit(1)

# 6. BOS #0  Brandon Phillips (2 - X - 36)
t6.new_ab(is_risp=True)
t6.pitch_list("b b")
t6.out("P4")

# 7. BOS #12 Brock Holt (2 - X - 36)
t6.new_ab(is_risp=True)
t6.pitch_list("c s s")
t6.out("K")


# Bot 6th
# Pitching: BOS #17 Nathan Eovaldi
b6 = game.new_inning()

# 9. NYY #25 Gleyber Torres (X - X - X)
b6.new_ab()
b6.pitch_list("b f b")
b6.hit(2)
b6.advance(3, "99 F9")

# 1. NYY #26 Andrew McCutchen (X - 25 - X)
b6.new_ab(is_risp=True)
b6.out("L8")

# 2. NYY #99 Aaron Judge (X - 25 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("s")
b6.out("F9")

# 3. NYY #18 Didi Gregorius (25 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b b c s f")
b6.reach("HBP")

# 4. NYY #27 Giancarlo Stanton (25 - X - 18)
b6.new_ab(is_risp=True)
b6.pitch_list("b b f s b f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #57 Chad Green
t7 = game.new_inning()

# Pitching change (NYY): #57 Chad Green replaces #34 J.A. Happ
t7.pitching_substitution(57)

# 8. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("b c b f")
t7.out("L8")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.out("F9")

# 1. BOS #5  Ian Kinsler (X - X - X)
t7.new_ab()
t7.pitch_list("c b b")
t7.out("G4-3")


# Bot 7th
# Pitching: BOS #44 Brandon Workman
b7 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #17 Nathan Eovaldi
b7.pitching_substitution(44)

# 5. NYY #31 Aaron Hicks (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c d")
b7.reach("BB")
b7.advance(2, "24 SB")
b7.advance(4, "14 HR")

# 6. NYY #41 Miguel Andujar (X - X - 31)
b7.new_ab()
b7.pitch_list("1 f d b 1 b")
b7.out("(F)P3")

# 7. NYY #24 Gary Sánchez (X - X - 31)
b7.new_ab(is_risp=True)
b7.pitch_list("1 b c s b b d")
b7.reach("BB")
b7.advance(4, "14 HR")

# Pitching change (BOS): #70 Ryan Brasier replaces #44 Brandon Workman
b7.pitching_substitution(70)

# 8. NYY #14 Neil Walker (X - 31 - 24)
b7.new_ab(is_risp=True)
b7.pitch_list("f b b b c")
b7.hit(4, rbis=3)

# 9. NYY #25 Gleyber Torres (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("(F)P3")

# 1. NYY #26 Andrew McCutchen (X - X - X)
b7.new_ab()
b7.pitch_list("b c b s")
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #30 David Robertson
t8 = game.new_inning()

# Pitching change (NYY): #30 David Robertson replaces #57 Chad Green
t8.pitching_substitution(30)

# Offensive change (BOS): Pinch-hitter #16 Andrew Benintendi replaces #25 Steve Pearce, batting 2nd
t8.offensive_substitution(2, 16, "PH")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("b b c b")
t8.out("G3-1")

# 3. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("s")
t8.hit(3)

# 4. BOS #2  Xander Bogaerts (28 - X - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c b")
t8.out("P3")

# 5. BOS #36 Eduardo Núñez (28 - X - X)
t8.new_ab(is_risp=True)
t8.pitch_list("d f")
t8.out("F7")


# Bot 8th
# Pitching: BOS #67 William Cuevas
b8 = game.new_inning()

# Pitching change (BOS): #67 William Cuevas replaces #70 Ryan Brasier
b8.pitching_substitution(67)

# Defensive switch (BOS): #16 Andrew Benintendi moves to LF
b8.defensive_switch(16, "7")

# Defensive switch (BOS): #12 Brock Holt moves to 1B
b8.defensive_switch(12, "3")

# 2. NYY #99 Aaron Judge (X - X - X)
b8.new_ab()
b8.pitch_list("b c b s b s")
b8.out("K")

# 3. NYY #18 Didi Gregorius (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.reach("HBP")

# 4. NYY #27 Giancarlo Stanton (X - X - 18)
b8.new_ab()
b8.pitch_list("b b t 1 f b f")
b8.out("F9")

# 5. NYY #31 Aaron Hicks (X - X - 18)
b8.new_ab()
b8.pitch_list("b f f b f t")
b8.out("KT")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #53 Zack Britton
t9 = game.new_inning()

# Pitching change (NYY): #53 Zack Britton replaces #30 David Robertson
t9.pitching_substitution(53)

# Defensive change (NYY): #29 Adeiny Hechavarría replaces #41 Miguel Andujar (3B), playing 3B, batting 6th
t9.defensive_substitution(6, 29, "5")

# 6. BOS #0  Brandon Phillips (X - X - X)
t9.new_ab()
t9.pitch_list("c f s")
t9.out("K2-3")

# 7. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b b")
t9.reach("BB")
t9.error(4)
t9.advance(2, "7 FC5")
t9.advance(3, "7 E4")
t9.advance("U", "59 E1")

# 8. BOS #7  Christian Vázquez (X - X - 12)
t9.new_ab()
t9.pitch_list("c d")
t9.reach("FC5")
# Offensive change (BOS): Pinch-runner #30 Tzu-Wei Lin replaces #7 Christian Vázquez
t9.offensive_substitution(8, 30, "PR")
t9.atbase("PR")
t9.advance(2, "59 E1")

# Offensive change (BOS): Pinch-hitter #59 Sam Travis replaces #19 Jackie Bradley Jr., batting 9th
t9.offensive_substitution(9, 59, "PH")

# 9. BOS #59 Sam Travis (12 - X - 7)
t9.new_ab(is_risp=True)
t9.pitch_list("b b f c d f")
t9.error(1)
t9.reach("E1", rbis=1)
# Offensive change (BOS): Pinch-runner #23 Blake Swihart replaces #59 Sam Travis
t9.offensive_substitution(9, 23, "PR")
t9.atbase("PR")
t9.thrown_out(2, "5 DP1-4-3", 2, 53)

# 1. BOS #5  Ian Kinsler (X - 30 - 59)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.out("DP1-4-3")

# Winning team: NYY
# WP: NYY #57 Chad Green
game.winning_pitcher(57)
# SV: NYY #53 Zack Britton
game.save_pitcher(53)

# Loser team: BOS
# LP: BOS #44 Brandon Workman
game.losing_pitcher(44, is_away_team=True)

# print(game)
game.generate_scorecard()
