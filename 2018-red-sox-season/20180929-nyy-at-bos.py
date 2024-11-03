import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2018-09-29
# https://www.baseball-reference.com/boxes/BOS/BOS201809290.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2018/09/29/531816/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-29 13:06-16:46",
        "at": "Fenway Park, Boston, MA",
        "att": "36,375",
        "temp": "70F, Partly Cloudy",
        "wind": "8mph, L To R",
        "away": {
            "team": "New York Yankees",
            "starter": 65,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                26: "Andrew McCutchen",
                31: "Aaron Hicks",
                27: "Giancarlo Stanton",
                18: "Didi Gregorius",
                41: "Miguel Andujar",
                33: "Greg Bird",
                28: "Austin Romine",
                25: "Gleyber Torres",
                # Starting pitcher
                65: "Domingo Germán",
                # Bench
                99: "Aaron Judge",
                66: "Kyle Higashioka",
                29: "Adeiny Hechavarría",
                12: "Tyler Wade",
                74: "Ronald Torreyes",
                45: "Luke Voit",
                24: "Gary Sánchez",
                14: "Neil Walker",
                # Bullpen
                67: "A.J. Cole",
                68: "Dellin Betances",
                40: "Luis Severino",
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
                [11, "7"],
                [26, "9"],
                [31, "8"],
                [27, "0"],
                [18, "6"],
                [41, "5"],
                [33, "3"],
                [28, "2"],
                [25, "4"],
            ],
            "bench": [
                [99, "CF"],
                [66, "C"],
                [29, "2B"],
                [12, "3B"],
                [74, "SS"],
                [45, "1B"],
                [24, "C"],
                [14, "2B"],
            ],
            "bullpen": [67, 68, 40, 36, 43, 38, 55, 56, 52, 53, 19, 57, 48, 85, 71, 34, 30, 61, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 17,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                12: "Brock Holt",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                19: "Jackie Bradley Jr.",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Starting pitcher
                17: "Nathan Eovaldi",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                59: "Sam Travis",
                50: "Mookie Betts",
                2: "Xander Bogaerts",
                3: "Sandy León",
                0: "Brandon Phillips",
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
                [16, "7"],
                [12, "6"],
                [28, "0"],
                [11, "5"],
                [18, "3"],
                [5, "4"],
                [19, "8"],
                [23, "9"],
                [7, "2"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [36, "SS"],
                [59, "1B"],
                [50, "SS"],
                [2, "2B"],
                [3, "C"],
                [0, "2B"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 41, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 32],
        },
        "umpires": {
            "HP": "Manny Gonzalez",
            "1B": "Nic Lentz",
            "2B": "Jeff Nelson",
            "3B": "Laz Diaz",
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
# Pitching: BOS #17 Nathan Eovaldi
t1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
t1.new_ab()
t1.pitch_list("c c b b b")
t1.error(5)
t1.reach("E5")
t1.advance("U", "27 2B")

# 2. NYY #26 Andrew McCutchen (X - X - 11)
t1.new_ab()
t1.pitch_list("f 1 f s")
t1.out("K")

# 3. NYY #31 Aaron Hicks (X - X - 11)
t1.new_ab()
t1.pitch_list("b b f f 1 c")
t1.out("!K")

# 4. NYY #27 Giancarlo Stanton (X - X - 11)
t1.new_ab()
t1.pitch_list("c c f b")
t1.hit(2, rbis=1)

# 5. NYY #18 Didi Gregorius (X - 27 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c f d f d s")
t1.out("K")


# Bot 1st
# Pitching: NYY #65 Domingo Germán
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b c s f f")
b1.hit(1)
b1.advance(3, "12 1B")

# 2. BOS #12 Brock Holt (X - X - 16)
b1.new_ab()
b1.pitch_list("c c b 1 b")
b1.hit(1)

# 3. BOS #28 J.D. Martinez (16 - X - 12)
b1.new_ab(is_risp=True)
b1.pitch_list("f f s")
b1.out("K")

# 4. BOS #11 Rafael Devers (16 - X - 12)
b1.new_ab(is_risp=True)
b1.pitch_list("f f f 1 c")
b1.out("!K")

# 5. BOS #18 Mitch Moreland (16 - X - 12)
b1.new_ab(is_risp=True)
b1.pitch_list("c b")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #17 Nathan Eovaldi
t2 = game.new_inning()

# 6. NYY #41 Miguel Andujar (X - X - X)
t2.new_ab()
t2.out("G4-3")

# 7. NYY #33 Greg Bird (X - X - X)
t2.new_ab()
t2.pitch_list("b b f b f")
t2.out("G4-3")

# 8. NYY #28 Austin Romine (X - X - X)
t2.new_ab()
t2.pitch_list("b s f b c")
t2.out("!K")


# Bot 2nd
# Pitching: NYY #65 Domingo Germán
b2 = game.new_inning()

# 6. BOS #5  Ian Kinsler (X - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")
b2.advance(2, "19 SB")
b2.advance(4, "19 2B")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 5)
b2.new_ab(is_risp=True)
b2.pitch_list("1 c b s f 1 b")
b2.hit(2, rbis=1)
b2.advance(3, "16 SB")

# 8. BOS #23 Blake Swihart (X - 19 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("s b f s")
b2.out("K")

# 9. BOS #7  Christian Vázquez (X - 19 - X)
b2.new_ab(is_risp=True)
b2.reach("HBP")
b2.advance(2, "16 SB")

# Pitching change (NYY): #71 Stephen Tarpley replaces #65 Domingo Germán
b2.pitching_substitution(71)

# 1. BOS #16 Andrew Benintendi (X - 19 - 7)
b2.new_ab(is_risp=True)
b2.pitch_list("t c b b b")
b2.out("F8")

# 2. BOS #12 Brock Holt (19 - 7 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b c b c f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# Pitching change (BOS): #57 Eduardo Rodriguez replaces #17 Nathan Eovaldi
t3.pitching_substitution(57)

# 9. NYY #25 Gleyber Torres (X - X - X)
t3.new_ab()
t3.pitch_list("b c b f b f b")
t3.reach("BB")
t3.advance(2, "26 1B")
t3.advance(3, "31 G1-4-3")

# 1. NYY #11 Brett Gardner (X - X - 25)
t3.new_ab()
t3.out("L7")

# 2. NYY #26 Andrew McCutchen (X - X - 25)
t3.new_ab()
t3.pitch_list("b b")
t3.hit(1)
t3.advance(2, "31 G1-4-3")

# 3. NYY #31 Aaron Hicks (X - 25 - 26)
t3.new_ab(is_risp=True)
t3.out("G1-4-3")

# 4. NYY #27 Giancarlo Stanton (25 - 26 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("s b s b c")
t3.out("!K")


# Bot 3rd
# Pitching: NYY #36 Lance Lynn
b3 = game.new_inning()

# Pitching change (NYY): #36 Lance Lynn replaces #71 Stephen Tarpley
b3.pitching_substitution(36)

# 3. BOS #28 J.D. Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("f f b c")
b3.out("!K")

# 4. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("b b f")
b3.out("G4-3")

# 5. BOS #18 Mitch Moreland (X - X - X)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")
b3.thrown_out(2, "5 FC5-4", 3, 36)

# 6. BOS #5  Ian Kinsler (X - X - 18)
b3.new_ab()
b3.pitch_list("c c f")
b3.reach("FC5-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 5. NYY #18 Didi Gregorius (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(1)
t4.advance(4, "33 2B")

# 6. NYY #41 Miguel Andujar (X - X - 18)
t4.new_ab()
t4.pitch_list("b")
t4.out("F8")

# 7. NYY #33 Greg Bird (X - X - 18)
t4.new_ab()
t4.pitch_list("s b s f f")
t4.hit(2, rbis=1)
t4.advance(3, "28 G6-3")
t4.advance(4, "25 HR")

# 8. NYY #28 Austin Romine (X - 33 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b")
t4.out("G6-3")

# 9. NYY #25 Gleyber Torres (33 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("s b")
t4.hit(4, rbis=2)

# 1. NYY #11 Brett Gardner (X - X - X)
t4.new_ab()
t4.pitch_list("c f b b f b b")
t4.reach("BB")

# 2. NYY #26 Andrew McCutchen (X - X - 11)
t4.new_ab()
t4.pitch_list("c f f s")
t4.out("K")


# Bot 4th
# Pitching: NYY #36 Lance Lynn
b4 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("c b b f b f")
b4.out("G4-3")

# 8. BOS #23 Blake Swihart (X - X - X)
b4.new_ab()
b4.hit(2)
b4.advance(4, "16 1B")

# 9. BOS #7  Christian Vázquez (X - 23 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c s b t")
b4.out("KT")

# 1. BOS #16 Andrew Benintendi (X - 23 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b f")
b4.hit(1, rbis=1)

# 2. BOS #12 Brock Holt (X - X - 16)
b4.new_ab()
b4.pitch_list("b b c s")
b4.out("P5")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #44 Brandon Workman
t5 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #57 Eduardo Rodriguez
t5.pitching_substitution(44)

# 3. NYY #31 Aaron Hicks (X - X - X)
t5.new_ab()
t5.hit(1)
# Offensive change (NYY): Pinch-runner #12 Tyler Wade replaces #31 Aaron Hicks
t5.offensive_substitution(3, 12, "PR")
t5.atbase("PR")
t5.advance(2, "27 1B")
t5.advance(3, "18 FC4-6")
t5.advance(4, "41 2B")

# 4. NYY #27 Giancarlo Stanton (X - X - 31)
t5.new_ab()
t5.pitch_list("c 1 b b")
t5.hit(1)
t5.thrown_out(2, "18 FC4-6", 1, 44)

# 5. NYY #18 Didi Gregorius (X - 12 - 27)
t5.new_ab(is_risp=True)
t5.reach("FC4-6")
t5.advance(4, "41 2B")

# 6. NYY #41 Miguel Andujar (12 - X - 18)
t5.new_ab(is_risp=True)
t5.pitch_list("b")
t5.hit(2, rbis=2)
t5.advance(4, "28 E8")

# 7. NYY #33 Greg Bird (X - 41 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b s f f s")
t5.out("K")

# 8. NYY #28 Austin Romine (X - 41 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c b")
t5.hit(1, rbis=1)
t5.error(8)
t5.advance(2, "E8")

# 9. NYY #25 Gleyber Torres (X - 28 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b f s c")
t5.out("!K")


# Bot 5th
# Pitching: NYY #36 Lance Lynn
b5 = game.new_inning()

# Defensive switch (NYY): #11 Brett Gardner moves to CF
b5.defensive_switch(11, "8")

# Defensive switch (NYY): #26 Andrew McCutchen moves to LF
b5.defensive_switch(26, "7")

# Defensive switch (NYY): #12 Tyler Wade moves to RF
b5.defensive_switch(12, "9")

# Defensive change (NYY): #29 Adeiny Hechavarría replaces #18 Didi Gregorius (SS), playing SS, batting 5th
b5.defensive_substitution(5, 29, "6")

# Defensive change (NYY): #74 Ronald Torreyes replaces #25 Gleyber Torres (2B), playing 2B, batting 9th
b5.defensive_substitution(9, 74, "4")

# Offensive change (BOS): Pinch-hitter #59 Sam Travis replaces #28 J.D. Martinez, batting 3rd
b5.offensive_substitution(3, 59, "PH")

# 3. BOS #59 Sam Travis (X - X - X)
b5.new_ab()
b5.pitch_list("c b s b b t")
b5.out("KT")

# 4. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.pitch_list("b c b f b s")
b5.out("K")

# 5. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.out("P5")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #37 Heath Hembree
t6 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #44 Brandon Workman
t6.pitching_substitution(37)

# Defensive switch (BOS): #59 Sam Travis moves to DH
t6.defensive_switch(59, "0")

# 1. NYY #11 Brett Gardner (X - X - X)
t6.new_ab()
t6.pitch_list("c c b f f f")
t6.out("F7")

# 2. NYY #26 Andrew McCutchen (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("L8")

# 3. NYY #12 Tyler Wade (X - X - X)
t6.new_ab()
t6.pitch_list("b b c f s")
t6.out("K")


# Bot 6th
# Pitching: NYY #55 Sonny Gray
b6 = game.new_inning()

# Pitching change (NYY): #55 Sonny Gray replaces #36 Lance Lynn
b6.pitching_substitution(55)

# 6. BOS #5  Ian Kinsler (X - X - X)
b6.new_ab()
b6.pitch_list("f b b f")
b6.hit(2)
b6.advance(3, "19 G4-3")

# 7. BOS #19 Jackie Bradley Jr. (X - 5 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b c d f")
b6.out("G4-3")

# 8. BOS #23 Blake Swihart (5 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c f b s")
b6.out("K")

# 9. BOS #7  Christian Vázquez (5 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("f")
b6.out("L9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #35 Steven Wright
t7 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #37 Heath Hembree
t7.pitching_substitution(35)

# Defensive change (BOS): #30 Tzu-Wei Lin replaces #16 Andrew Benintendi (LF), playing CF, batting 1st
t7.defensive_substitution(1, 30, "8")

# Defensive switch (BOS): #19 Jackie Bradley Jr. moves to RF
t7.defensive_switch(19, "9")

# Defensive switch (BOS): #23 Blake Swihart moves to LF
t7.defensive_switch(23, "7")

# 4. NYY #27 Giancarlo Stanton (X - X - X)
t7.new_ab()
t7.pitch_list("b s f b")
t7.hit(4)

# 5. NYY #29 Adeiny Hechavarría (X - X - X)
t7.new_ab()
t7.pitch_list("b c f f s")
t7.out("K2-3")

# 6. NYY #41 Miguel Andujar (X - X - X)
t7.new_ab()
t7.out("F7")

# 7. NYY #33 Greg Bird (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(1)

# 8. NYY #28 Austin Romine (X - X - 33)
t7.new_ab()
t7.pitch_list("c f t")
t7.out("KT")


# Bot 7th
# Pitching: NYY #55 Sonny Gray
b7 = game.new_inning()

# 1. BOS #30 Tzu-Wei Lin (X - X - X)
b7.new_ab()
b7.pitch_list("c b b f f")
b7.out("G4-3")

# 2. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("b b c c b c")
b7.out("!K")

# 3. BOS #59 Sam Travis (X - X - X)
b7.new_ab()
b7.pitch_list("f s c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #76 Hector Velázquez
t8 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #35 Steven Wright
t8.pitching_substitution(76)

# 9. NYY #74 Ronald Torreyes (X - X - X)
t8.new_ab()
t8.pitch_list("c f b b b f")
t8.out("G5-3")

# 1. NYY #11 Brett Gardner (X - X - X)
t8.new_ab()
t8.pitch_list("b b c f")
t8.out("G1-3")

# 2. NYY #26 Andrew McCutchen (X - X - X)
t8.new_ab()
t8.pitch_list("f")
t8.hit(1)
t8.thrown_out(2, "12 FC6", 3, 76)

# 3. NYY #12 Tyler Wade (X - X - 26)
t8.new_ab()
t8.pitch_list("b c d")
t8.reach("FC6")


# Bot 8th
# Pitching: NYY #48 Tommy Kahnle
b8 = game.new_inning()

# Pitching change (NYY): #48 Tommy Kahnle replaces #55 Sonny Gray
b8.pitching_substitution(48)

# Offensive change (BOS): Pinch-hitter #0 Brandon Phillips replaces #11 Rafael Devers, batting 4th
b8.offensive_substitution(4, 0, "PH")

# 4. BOS #0  Brandon Phillips (X - X - X)
b8.new_ab()
b8.pitch_list("b s b b b")
b8.reach("BB")
b8.advance(2, "18 1B")
b8.advance(3, "5 BB")
b8.advance(4, "23 G4-3")

# 5. BOS #18 Mitch Moreland (X - X - 0)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)
b8.advance(2, "5 BB")
b8.advance(3, "23 G4-3")

# 6. BOS #5  Ian Kinsler (X - 0 - 18)
b8.new_ab(is_risp=True)
b8.pitch_list("b b c c b b")
b8.reach("BB")
b8.advance(2, "23 G4-3")

# 7. BOS #19 Jackie Bradley Jr. (0 - 18 - 5)
b8.new_ab(is_risp=True)
b8.pitch_list("b b b c f")
b8.out("F7")

# 8. BOS #23 Blake Swihart (0 - 18 - 5)
b8.new_ab(is_risp=True)
b8.pitch_list("b c f")
b8.out("G4-3", rbis=1)

# 9. BOS #7  Christian Vázquez (18 - 5 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c b f d b")
b8.out("L1-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #76 Hector Velázquez
t9 = game.new_inning()

# Defensive switch (BOS): #0 Brandon Phillips moves to 3B
t9.defensive_switch(0, "5")

# Offensive change (NYY): Pinch-hitter #66 Kyle Higashioka replaces #27 Giancarlo Stanton, batting 4th
t9.offensive_substitution(4, 66, "PH")

# 4. NYY #66 Kyle Higashioka (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b")
t9.out("F7")

# 5. NYY #29 Adeiny Hechavarría (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("F9")

# 6. NYY #41 Miguel Andujar (X - X - X)
t9.new_ab()
t9.hit(2)

# Pitching change (BOS): #63 Robby Scott replaces #76 Hector Velázquez
t9.pitching_substitution(63)

# 7. NYY #33 Greg Bird (X - 41 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c b d b f f s")
t9.out("K")


# Bot 9th
# Pitching: NYY #56 Jonathan Holder
b9 = game.new_inning()

# Pitching change (NYY): #56 Jonathan Holder replaces #48 Tommy Kahnle
b9.pitching_substitution(56)

# Defensive switch (NYY): #66 Kyle Higashioka moves to DH
b9.defensive_switch(66, "0")

# 1. BOS #30 Tzu-Wei Lin (X - X - X)
b9.new_ab()
b9.hit(2)
b9.advance(4, "12 HR")

# 2. BOS #12 Brock Holt (X - 30 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("c b")
b9.hit(4, rbis=2)

# 3. BOS #59 Sam Travis (X - X - X)
b9.new_ab()
b9.pitch_list("s c f")
b9.hit(1)
b9.advance(2, "5 DI")

# 4. BOS #0  Brandon Phillips (X - X - 59)
b9.new_ab()
b9.pitch_list("c d t d b s")
b9.out("K")

# Pitching change (NYY): #54 Aroldis Chapman replaces #56 Jonathan Holder
b9.pitching_substitution(54)

# 5. BOS #18 Mitch Moreland (X - X - 59)
b9.new_ab()
b9.pitch_list("c s f f s")
b9.out("K")

# 6. BOS #5  Ian Kinsler (X - X - 59)
b9.new_ab(is_risp=True)
b9.pitch_list("b b b c b")
b9.reach("BB")

# 7. BOS #19 Jackie Bradley Jr. (X - 59 - 5)
b9.new_ab(is_risp=True)
b9.pitch_list("b c c d s")
b9.out("K")

# Winning team: NYY
# WP: NYY #36 Lance Lynn
game.winning_pitcher(36, is_away_team=True)
# SV: NYY #54 Aroldis Chapman
game.save_pitcher(54, is_away_team=True)

# Loser team: BOS
# LP: BOS #57 Eduardo Rodriguez
game.losing_pitcher(57)

# print(game)
game.generate_scorecard()
