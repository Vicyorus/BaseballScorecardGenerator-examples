import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2018-09-19
# https://www.baseball-reference.com/boxes/NYA/NYA201809190.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2018/09/19/531676/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-19 19:09-22:26",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "43,297",
        "temp": "78F, Partly Cloudy",
        "wind": "8mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                12: "Brock Holt",
                59: "Sam Travis",
                11: "Rafael Devers",
                23: "Blake Swihart",
                0: "Brandon Phillips",
                7: "Christian Vázquez",
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
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 31, 61, 66, 63],
            "lineup": [
                [50, "0"],
                [16, "7"],
                [28, "9"],
                [2, "6"],
                [18, "3"],
                [5, "4"],
                [36, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [12, "2B"],
                [59, "1B"],
                [11, "3B"],
                [23, "C"],
                [0, "2B"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 41, 31, 61, 66, 37, 63, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 40,
            "roster": {
                # Lineup
                26: "Andrew McCutchen",
                99: "Aaron Judge",
                31: "Aaron Hicks",
                27: "Giancarlo Stanton",
                18: "Didi Gregorius",
                41: "Miguel Andujar",
                24: "Gary Sánchez",
                45: "Luke Voit",
                25: "Gleyber Torres",
                # Starting pitcher
                40: "Luis Severino",
                # Bench
                28: "Austin Romine",
                33: "Greg Bird",
                66: "Kyle Higashioka",
                29: "Adeiny Hechavarría",
                11: "Brett Gardner",
                12: "Tyler Wade",
                74: "Ronald Torreyes",
                14: "Neil Walker",
                # Bullpen
                67: "A.J. Cole",
                68: "Dellin Betances",
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
                34: "J.A. Happ",
                30: "David Robertson",
                61: "Justus Sheffield",
                54: "Aroldis Chapman",
            },
            "lefties": [52, 53, 71, 34, 61, 54],
            "lineup": [
                [26, "7"],
                [99, "0"],
                [31, "8"],
                [27, "9"],
                [18, "6"],
                [41, "5"],
                [24, "2"],
                [45, "3"],
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
                [14, "2B"],
            ],
            "bullpen": [67, 68, 65, 36, 43, 38, 55, 56, 52, 53, 19, 57, 48, 85, 71, 34, 30, 61, 54],
        },
        "umpires": {
            "HP": "Chris Guccione",
            "1B": "Kerwin Danley",
            "2B": "Mike Estabrook",
            "3B": "Chad Fairchild",
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
# Pitching: NYY #40 Luis Severino
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")
t1.advance(3, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t1.new_ab()
t1.pitch_list("b 1 b s s")
t1.out("L8")

# 3. BOS #28 J.D. Martinez (X - X - 50)
t1.new_ab()
t1.pitch_list("c 1 b")
t1.hit(1)
t1.advance(2, "2 WP")

# 4. BOS #2  Xander Bogaerts (50 - X - 28)
t1.new_ab(is_risp=True)
t1.pitch_list("c s b")
t1.wp()
t1.out("P6")

# 5. BOS #18 Mitch Moreland (50 - 28 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b b s")
t1.out("G1-3")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. NYY #26 Andrew McCutchen (X - X - X)
b1.new_ab()
b1.pitch_list("b b b b")
b1.reach("BB")
b1.advance(2, "31 G5-3")

# 2. NYY #99 Aaron Judge (X - X - 26)
b1.new_ab()
b1.pitch_list("c b c b f")
b1.out("L4")

# 3. NYY #31 Aaron Hicks (X - X - 26)
b1.new_ab()
b1.out("G5-3")

# 4. NYY #27 Giancarlo Stanton (X - 26 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b c f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #40 Luis Severino
t2 = game.new_inning()

# 6. BOS #5  Ian Kinsler (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("P4")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.out("L6")

# 8. BOS #3  Sandy León (X - X - X)
t2.new_ab()
t2.pitch_list("c c s")
t2.out("K2-3")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 5. NYY #18 Didi Gregorius (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("F7")

# 6. NYY #41 Miguel Andujar (X - X - X)
b2.new_ab()
b2.pitch_list("c b f")
b2.hit(4)

# 7. NYY #24 Gary Sánchez (X - X - X)
b2.new_ab()
b2.pitch_list("b c b s b b")
b2.reach("BB")
b2.advance(2, "45 1B")
b2.advance(3, "26 BB")
b2.advance("U", "99 E5")

# 8. NYY #45 Luke Voit (X - X - 24)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.advance(2, "26 BB")
b2.advance("U", "99 E5")

# 9. NYY #25 Gleyber Torres (X - 24 - 45)
b2.new_ab(is_risp=True)
b2.pitch_list("c f s")
b2.out("K")

# 1. NYY #26 Andrew McCutchen (X - 24 - 45)
b2.new_ab(is_risp=True)
b2.pitch_list("c b b b b")
b2.reach("BB")
b2.advance(3, "99 E5")

# 2. NYY #99 Aaron Judge (24 - 45 - 26)
b2.new_ab(is_risp=True)
b2.error(5)
b2.reach("E5", end_base=2)

# 3. NYY #31 Aaron Hicks (26 - 99 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b t f b f")
b2.out("L9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #40 Luis Severino
t3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c f s")
t3.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c b s b b f")
t3.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("b b c")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 4. NYY #27 Giancarlo Stanton (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G5-3")

# 5. NYY #18 Didi Gregorius (X - X - X)
b3.new_ab()
b3.pitch_list("c b b f b")
b3.out("P5")

# 6. NYY #41 Miguel Andujar (X - X - X)
b3.new_ab()
b3.hit(2)

# 7. NYY #24 Gary Sánchez (X - 41 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c f f")
b3.out("L8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #40 Luis Severino
t4 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("b b")
t4.hit(1)

# 4. BOS #2  Xander Bogaerts (X - X - 28)
t4.new_ab()
t4.pitch_list("d")
t4.out("P6")

# 5. BOS #18 Mitch Moreland (X - X - 28)
t4.new_ab()
t4.pitch_list("b c b f b s")
t4.out("K")

# 6. BOS #5  Ian Kinsler (X - X - 28)
t4.new_ab()
t4.pitch_list("1")
t4.out("P4")


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 8. NYY #45 Luke Voit (X - X - X)
b4.new_ab()
b4.pitch_list("s f")
b4.hit(4)

# 9. NYY #25 Gleyber Torres (X - X - X)
b4.new_ab()
b4.out("F9")

# 1. NYY #26 Andrew McCutchen (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.out("G5-3")

# 2. NYY #99 Aaron Judge (X - X - X)
b4.new_ab()
b4.pitch_list("f s b")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #40 Luis Severino
t5 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(2)
t5.advance(4, "3 1B")

# 8. BOS #3  Sandy León (X - 36 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b f")
t5.hit(1, rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
t5.new_ab()
t5.pitch_list("c")
t5.out("L7")

# 1. BOS #50 Mookie Betts (X - X - 3)
t5.new_ab()
t5.pitch_list("c b d f b s")
t5.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - 3)
t5.new_ab()
t5.out("G3-1")


# Bot 5th
# Pitching: BOS #24 David Price
b5 = game.new_inning()

# 3. NYY #31 Aaron Hicks (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("L7")

# 4. NYY #27 Giancarlo Stanton (X - X - X)
b5.new_ab()
b5.pitch_list("f c f")
b5.out("P3")

# 5. NYY #18 Didi Gregorius (X - X - X)
b5.new_ab()
b5.pitch_list("b f f")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #40 Luis Severino
t6 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("f")
t6.hit(1)

# 4. BOS #2  Xander Bogaerts (X - X - 28)
t6.new_ab()
t6.pitch_list("b c b f f")
t6.out("(F)P5")

# 5. BOS #18 Mitch Moreland (X - X - 28)
t6.new_ab()
t6.pitch_list("c t f d d d s")
t6.out("K")

# 6. BOS #5  Ian Kinsler (X - X - 28)
t6.new_ab()
t6.pitch_list("c s f d d")
t6.out("P5")


# Bot 6th
# Pitching: BOS #24 David Price
b6 = game.new_inning()

# 6. NYY #41 Miguel Andujar (X - X - X)
b6.new_ab()
b6.pitch_list("f b")
b6.out("F7")

# 7. NYY #24 Gary Sánchez (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c b")
b6.reach("BB")
b6.advance(4, "45 HR")

# 8. NYY #45 Luke Voit (X - X - 24)
b6.new_ab()
b6.pitch_list("c s b f d")
b6.hit(4, rbis=2)

# Pitching change (BOS): #56 Joe Kelly replaces #24 David Price
b6.pitching_substitution(56)

# 9. NYY #25 Gleyber Torres (X - X - X)
b6.new_ab()
b6.pitch_list("f b s f b b")
b6.out("G5-3")

# 1. NYY #26 Andrew McCutchen (X - X - X)
b6.new_ab()
b6.pitch_list("c f f")
b6.hit(1)
b6.advance(3, "99 1B")
b6.advance(4, "31 3B")

# 2. NYY #99 Aaron Judge (X - X - 26)
b6.new_ab()
b6.pitch_list("s f b")
b6.hit(1)
b6.advance(4, "31 3B")

# 3. NYY #31 Aaron Hicks (26 - X - 99)
b6.new_ab(is_risp=True)
b6.pitch_list("b c b f")
b6.hit(3, rbis=2)

# Pitching change (BOS): #76 Hector Velázquez replaces #56 Joe Kelly
b6.pitching_substitution(76)

# 4. NYY #27 Giancarlo Stanton (31 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("s b s s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #40 Luis Severino
t7 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t7.new_ab()
t7.pitch_list("b b c b")
t7.out("L8")

# 8. BOS #3  Sandy León (X - X - X)
t7.new_ab()
t7.pitch_list("f b f b")
t7.out("(F)P5")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("f b b b")
t7.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 19)
t7.new_ab()
t7.pitch_list("c d f d f f c")
t7.out("!K")


# Bot 7th
# Pitching: BOS #76 Hector Velázquez
b7 = game.new_inning()

# Defensive change (BOS): #59 Sam Travis replaces #5 Ian Kinsler (2B), playing LF, batting 6th
b7.defensive_substitution(6, 59, "7")

# Defensive change (BOS): #23 Blake Swihart replaces #16 Andrew Benintendi (LF), playing RF, batting 2nd
b7.defensive_substitution(2, 23, "9")

# Defensive change (BOS): #30 Tzu-Wei Lin replaces #2 Xander Bogaerts (SS), playing SS, batting 4th
b7.defensive_substitution(4, 30, "6")

# Defensive change (BOS): #0 Brandon Phillips replaces #28 J.D. Martinez (RF), playing 2B, batting 3rd
b7.defensive_substitution(3, 0, "4")

# 5. NYY #18 Didi Gregorius (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("L8")

# 6. NYY #41 Miguel Andujar (X - X - X)
b7.new_ab()
b7.pitch_list("c f b f")
b7.out("F7")

# 7. NYY #24 Gary Sánchez (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #56 Jonathan Holder
t8 = game.new_inning()

# Pitching change (NYY): #56 Jonathan Holder replaces #40 Luis Severino
t8.pitching_substitution(56)

# 2. BOS #23 Blake Swihart (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.hit(1)

# 3. BOS #0  Brandon Phillips (X - X - 23)
t8.new_ab()
t8.pitch_list("s f d")
t8.out("P4")

# 4. BOS #30 Tzu-Wei Lin (X - X - 23)
t8.new_ab()
t8.pitch_list("c f b c")
t8.out("!K")

# 5. BOS #18 Mitch Moreland (X - X - 23)
t8.new_ab()
t8.pitch_list("f s b")
t8.out("F8")


# Bot 8th
# Pitching: BOS #67 William Cuevas
b8 = game.new_inning()

# Pitching change (BOS): #67 William Cuevas replaces #76 Hector Velázquez
b8.pitching_substitution(67)

# Defensive change (BOS): #12 Brock Holt replaces #59 Sam Travis (LF), playing LF, batting 6th
b8.defensive_substitution(6, 12, "7")

# 8. NYY #45 Luke Voit (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(1)
b8.advance(2, "25 1B")
b8.advance(3, "26 G1-3")
b8.advance(4, "33 G1-3")

# 9. NYY #25 Gleyber Torres (X - X - 45)
b8.new_ab()
b8.pitch_list("c b")
b8.hit(1)
b8.advance(2, "26 G1-3")
b8.advance(3, "33 G1-3")
b8.advance(4, "31 1B")

# 1. NYY #26 Andrew McCutchen (X - 45 - 25)
b8.new_ab(is_risp=True)
b8.out("G1-3")

# Offensive change (NYY): Pinch-hitter #33 Greg Bird replaces #99 Aaron Judge, batting 2nd
b8.offensive_substitution(2, 33, "PH")

# 2. NYY #33 Greg Bird (45 - 25 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c f")
b8.out("G1-3", rbis=1)

# 3. NYY #31 Aaron Hicks (25 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b c")
b8.hit(1, rbis=1)

# 4. NYY #27 Giancarlo Stanton (X - X - 31)
b8.new_ab()
b8.pitch_list("c b b b c c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #61 Justus Sheffield
t9 = game.new_inning()

# Pitching change (NYY): #61 Justus Sheffield replaces #56 Jonathan Holder
t9.pitching_substitution(61)

# Defensive switch (NYY): #33 Greg Bird moves to DH
t9.defensive_switch(33, "0")

# Defensive change (NYY): #12 Tyler Wade replaces #27 Giancarlo Stanton (RF), playing RF, batting 4th
t9.defensive_substitution(4, 12, "9")

# Defensive change (NYY): #74 Ronald Torreyes replaces #25 Gleyber Torres (2B), playing 2B, batting 9th
t9.defensive_substitution(9, 74, "4")

# 6. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("b b c b")
t9.hit(1)
t9.advance(2, "36 1B")
t9.advance(3, "19 BB")

# 7. BOS #36 Eduardo Núñez (X - X - 12)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)
# Offensive change (BOS): Pinch-runner #7 Christian Vázquez replaces #36 Eduardo Núñez
t9.offensive_substitution(7, 7, "PR")
t9.atbase("PR")
t9.advance(2, "19 BB")

# 8. BOS #3  Sandy León (X - 12 - 36)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.out("IF4")

# 9. BOS #19 Jackie Bradley Jr. (X - 12 - 7)
t9.new_ab(is_risp=True)
t9.pitch_list("c b c d b b")
t9.reach("BB")
t9.thrown_out(2, "50 DP6-4-3", 2, 61)

# 1. BOS #50 Mookie Betts (12 - 7 - 19)
t9.new_ab(is_risp=True)
t9.pitch_list("b b c b f")
t9.out("DP6-4-3")

# Winning team: NYY
# WP: NYY #40 Luis Severino
game.winning_pitcher(40)

# Loser team: BOS
# LP: BOS #24 David Price
game.losing_pitcher(24, is_away_team=True)

# print(game)
game.generate_scorecard()
