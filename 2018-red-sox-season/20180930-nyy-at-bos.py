import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2018-09-30
# https://www.baseball-reference.com/boxes/BOS/BOS201809300.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2018/09/30/531831/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-30 15:07-18:27",
        "at": "Fenway Park, Boston, MA",
        "att": "36,201",
        "temp": "68F, Partly Cloudy",
        "wind": "10mph, Out To RF",
        "away": {
            "team": "New York Yankees",
            "starter": 85,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                99: "Aaron Judge",
                31: "Aaron Hicks",
                41: "Miguel Andujar",
                45: "Luke Voit",
                24: "Gary Sánchez",
                25: "Gleyber Torres",
                14: "Neil Walker",
                29: "Adeiny Hechavarría",
                # Starting pitcher
                85: "Luis Cessa",
                # Bench
                28: "Austin Romine",
                33: "Greg Bird",
                26: "Andrew McCutchen",
                66: "Kyle Higashioka",
                12: "Tyler Wade",
                74: "Ronald Torreyes",
                27: "Giancarlo Stanton",
                18: "Didi Gregorius",
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
                71: "Stephen Tarpley",
                34: "J.A. Happ",
                30: "David Robertson",
                61: "Justus Sheffield",
                54: "Aroldis Chapman",
            },
            "lefties": [52, 53, 71, 34, 61, 54],
            "lineup": [
                [11, "7"],
                [99, "9"],
                [31, "8"],
                [41, "0"],
                [45, "3"],
                [24, "2"],
                [25, "4"],
                [14, "5"],
                [29, "6"],
            ],
            "bench": [
                [28, "C"],
                [33, "1B"],
                [26, "RF"],
                [66, "C"],
                [12, "3B"],
                [74, "SS"],
                [27, "DH"],
                [18, "SS"],
            ],
            "bullpen": [67, 68, 40, 65, 36, 43, 38, 55, 56, 52, 53, 19, 57, 48, 71, 34, 30, 61, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                12: "Brock Holt",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                5: "Ian Kinsler",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                59: "Sam Travis",
                11: "Rafael Devers",
                23: "Blake Swihart",
                16: "Andrew Benintendi",
                0: "Brandon Phillips",
                7: "Christian Vázquez",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
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
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 66, 63, 24],
            "lineup": [
                [50, "9"],
                [12, "7"],
                [28, "0"],
                [2, "6"],
                [18, "3"],
                [36, "5"],
                [5, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [59, "1B"],
                [11, "3B"],
                [23, "C"],
                [16, "LF"],
                [0, "2B"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 41, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Nic Lentz",
            "1B": "Jeremie Rehak",
            "2B": "Laz Diaz",
            "3B": "Manny Gonzalez",
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
# Pitching: BOS #22 Rick Porcello
t1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F9")

# 2. NYY #99 Aaron Judge (X - X - X)
t1.new_ab()
t1.pitch_list("b b c c")
t1.out("G4-3")

# 3. NYY #31 Aaron Hicks (X - X - X)
t1.new_ab()
t1.pitch_list("b c c f b b")
t1.out("G3-1")


# Bot 1st
# Pitching: NYY #85 Luis Cessa
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c c")
b1.hit(1)
b1.error(9)
b1.advance(2, "12 1B")
b1.advance(4, "12 E9")

# 2. BOS #12 Brock Holt (X - X - 50)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)
b1.advance(2, "E9")
b1.advance(3, "28 1B")
b1.advance(4, "18 2B")

# 3. BOS #28 J.D. Martinez (X - 12 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.hit(1)
b1.advance(3, "18 2B")
b1.error(1)
b1.advance(4, "36 E1")

# 4. BOS #2  Xander Bogaerts (12 - X - 28)
b1.new_ab(is_risp=True)
b1.pitch_list("c b")
b1.out("(F)P3")

# 5. BOS #18 Mitch Moreland (12 - X - 28)
b1.new_ab(is_risp=True)
b1.pitch_list("b b")
b1.hit(2, rbis=1)
b1.advance(3, "36 E1")
b1.advance("U", "5 FC6-4")

# 6. BOS #36 Eduardo Núñez (28 - 18 - X)
b1.new_ab(is_risp=True)
b1.hit(1)
b1.thrown_out(2, "5 FC6-4", 2, 30)

# Pitching change (NYY): #30 David Robertson replaces #85 Luis Cessa
b1.pitching_substitution(30)

# 7. BOS #5  Ian Kinsler (18 - X - 36)
b1.new_ab(is_risp=True)
b1.reach("FC6-4", rbis=1)

# 8. BOS #3  Sandy León (X - X - 5)
b1.new_ab()
b1.pitch_list("b s c d s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 4. NYY #41 Miguel Andujar (X - X - X)
t2.new_ab()
t2.pitch_list("c b s b b f")
t2.out("G3-1")

# 5. NYY #45 Luke Voit (X - X - X)
t2.new_ab()
t2.pitch_list("b s b s b c")
t2.out("!K")

# 6. NYY #24 Gary Sánchez (X - X - X)
t2.new_ab()
t2.pitch_list("c b s b f b f b")
t2.reach("BB")

# 7. NYY #25 Gleyber Torres (X - X - 24)
t2.new_ab()
t2.pitch_list("b s c d s")
t2.out("K")


# Bot 2nd
# Pitching: NYY #38 Jonathan Loáisiga
b2 = game.new_inning()

# Pitching change (NYY): #38 Jonathan Loáisiga replaces #30 David Robertson
b2.pitching_substitution(38)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("b s b c f b f")
b2.error(7)
b2.hit(1)
b2.advance("U", "12 2B")

# 1. BOS #50 Mookie Betts (X - X - 19)
b2.new_ab()
b2.pitch_list("c")
b2.out("P6")

# 2. BOS #12 Brock Holt (X - X - 19)
b2.new_ab()
b2.pitch_list("1 b")
b2.hit(2, rbis=1)
b2.advance("U", "2 HR")

# 3. BOS #28 J.D. Martinez (X - 12 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b f t s")
b2.out("K")

# 4. BOS #2  Xander Bogaerts (X - 12 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f")
b2.hit("U", rbis=2)

# 5. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f f f")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #56 Joe Kelly
t3 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #22 Rick Porcello
t3.pitching_substitution(56)

# Defensive change (BOS): #30 Tzu-Wei Lin replaces #50 Mookie Betts (RF), playing CF, batting 1st
t3.defensive_substitution(1, 30, "8/6")

# Defensive switch (BOS): #19 Jackie Bradley Jr. moves to RF
t3.defensive_switch(19, "9")

# 8. NYY #14 Neil Walker (X - X - X)
t3.new_ab()
t3.hit(1)
t3.advance(2, "29 BB")

# 9. NYY #29 Adeiny Hechavarría (X - X - 14)
t3.new_ab()
t3.pitch_list("c b d f b b")
t3.reach("BB")
t3.thrown_out(2, "99 DP4-3", 2, 56)

# 1. NYY #11 Brett Gardner (X - 14 - 29)
t3.new_ab(is_risp=True)
t3.pitch_list("d c b s b f s")
t3.out("K")

# 2. NYY #99 Aaron Judge (X - 14 - 29)
t3.new_ab(is_risp=True)
t3.pitch_list("b b f b t")
t3.out("DP4-3")


# Bot 3rd
# Pitching: NYY #38 Jonathan Loáisiga
b3 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.thrown_out(2, "3 DP3-5-1", 2, 38)

# 7. BOS #5  Ian Kinsler (X - X - 36)
b3.new_ab()
b3.pitch_list("c f b f b s")
b3.out("K")

# 8. BOS #3  Sandy León (X - X - 36)
b3.new_ab()
b3.pitch_list("c d b f f")
b3.out("DP3-5-1")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #66 Bobby Poyner
t4 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #56 Joe Kelly
t4.pitching_substitution(66)

# 3. NYY #31 Aaron Hicks (X - X - X)
t4.new_ab()
t4.pitch_list("f s b f")
t4.out("G1-3")

# 4. NYY #41 Miguel Andujar (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(2)
t4.advance(4, "45 HR")

# 5. NYY #45 Luke Voit (X - 41 - X)
t4.new_ab(is_risp=True)
t4.hit(4, rbis=2)

# 6. NYY #24 Gary Sánchez (X - X - X)
t4.new_ab()
t4.pitch_list("f")
t4.reach("HBP")

# 7. NYY #25 Gleyber Torres (X - X - 24)
t4.new_ab()
t4.pitch_list("b s f b s")
t4.out("K")

# 8. NYY #14 Neil Walker (X - X - 24)
t4.new_ab()
t4.pitch_list("c f b s")
t4.out("K")


# Bot 4th
# Pitching: NYY #61 Justus Sheffield
b4 = game.new_inning()

# Pitching change (NYY): #61 Justus Sheffield replaces #38 Jonathan Loáisiga
b4.pitching_substitution(61)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("c c b b")
b4.out("G4-3")

# 1. BOS #30 Tzu-Wei Lin (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c s f b")
b4.reach("BB")
b4.advance(2, "12 BB")
b4.advance(4, "28 HR")

# 2. BOS #12 Brock Holt (X - X - 30)
b4.new_ab()
b4.pitch_list("b b b b")
b4.reach("BB")
b4.advance(4, "28 HR")

# 3. BOS #28 J.D. Martinez (X - 30 - 12)
b4.new_ab(is_risp=True)
b4.pitch_list("f")
b4.hit(4, rbis=3)

# 4. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("b c c f b")
b4.hit(2)
# Offensive change (BOS): Pinch-runner #23 Blake Swihart replaces #2 Xander Bogaerts
b4.offensive_substitution(4, 23, "PR")
b4.atbase("PR")
b4.advance(3, "18 WP")

# 5. BOS #18 Mitch Moreland (X - 2 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b c f b f")
b4.wp()
b4.out("(F)P5")

# 6. BOS #36 Eduardo Núñez (23 - X - X)
b4.new_ab(is_risp=True)
b4.out("G3-1")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #57 Eduardo Rodriguez
t5 = game.new_inning()

# Pitching change (BOS): #57 Eduardo Rodriguez replaces #66 Bobby Poyner
t5.pitching_substitution(57)

# Defensive switch (BOS): #30 Tzu-Wei Lin moves to SS
t5.defensive_switch(30, "6")

# Defensive switch (BOS): #12 Brock Holt moves to RF
t5.defensive_switch(12, "9")

# Defensive switch (BOS): #23 Blake Swihart moves to LF
t5.defensive_switch(23, "7")

# Defensive switch (BOS): #19 Jackie Bradley Jr. moves to CF
t5.defensive_switch(19, "8")

# 9. NYY #29 Adeiny Hechavarría (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("(F)P3")

# 1. NYY #11 Brett Gardner (X - X - X)
t5.new_ab()
t5.pitch_list("c c b b f s")
t5.out("K")

# 2. NYY #99 Aaron Judge (X - X - X)
t5.new_ab()
t5.pitch_list("b c s b b c")
t5.out("!K")


# Bot 5th
# Pitching: NYY #71 Stephen Tarpley
b5 = game.new_inning()

# Pitching change (NYY): #71 Stephen Tarpley replaces #61 Justus Sheffield
b5.pitching_substitution(71)

# 7. BOS #5  Ian Kinsler (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G6-3")

# 8. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G5-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b f b f b b")
b5.reach("BB")

# 1. BOS #30 Tzu-Wei Lin (X - X - 19)
b5.new_ab()
b5.pitch_list("c f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #32 Matt Barnes
t6 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #57 Eduardo Rodriguez
t6.pitching_substitution(32)

# 3. NYY #31 Aaron Hicks (X - X - X)
t6.new_ab()
t6.pitch_list("s b s s")
t6.out("K")

# 4. NYY #41 Miguel Andujar (X - X - X)
t6.new_ab()
t6.out("G6-3")

# 5. NYY #45 Luke Voit (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)
t6.advance(2, "24 WP")

# 6. NYY #24 Gary Sánchez (X - X - 45)
t6.new_ab(is_risp=True)
t6.pitch_list("d b c s s")
t6.wp()
t6.out("K")


# Bot 6th
# Pitching: NYY #71 Stephen Tarpley
b6 = game.new_inning()

# Defensive switch (NYY): #11 Brett Gardner moves to CF
b6.defensive_switch(11, "8")

# Defensive change (NYY): #12 Tyler Wade replaces #31 Aaron Hicks (CF), playing RF, batting 3rd
b6.defensive_substitution(3, 12, "9")

# Defensive change (NYY): #74 Ronald Torreyes replaces #99 Aaron Judge (RF), playing SS, batting 2nd
b6.defensive_substitution(2, 74, "6")

# Defensive change (NYY): #66 Kyle Higashioka replaces #24 Gary Sánchez (C), playing C, batting 6th
b6.defensive_substitution(6, 66, "2")

# Defensive switch (NYY): #14 Neil Walker moves to LF
b6.defensive_switch(14, "7")

# Defensive switch (NYY): #29 Adeiny Hechavarría moves to 3B
b6.defensive_switch(29, "5")

# 2. BOS #12 Brock Holt (X - X - X)
b6.new_ab()
b6.pitch_list("c b f s")
b6.out("K")

# Offensive change (BOS): Pinch-hitter #0 Brandon Phillips replaces #28 J.D. Martinez, batting 3rd
b6.offensive_substitution(3, 0, "PH")

# 3. BOS #0  Brandon Phillips (X - X - X)
b6.new_ab()
b6.pitch_list("f b f s")
b6.out("K2-3")

# 4. BOS #23 Blake Swihart (X - X - X)
b6.new_ab()
b6.pitch_list("c f b b b f c")
b6.pb()
b6.reach("K")
b6.advance(2, "18 BB")
b6.advance(3, "36 BB")

# 5. BOS #18 Mitch Moreland (X - X - 23)
b6.new_ab()
b6.pitch_list("c b b b c b")
b6.reach("BB")
# Offensive change (BOS): Pinch-runner #59 Sam Travis replaces #18 Mitch Moreland
b6.offensive_substitution(5, 59, "PR")
b6.atbase("PR")
b6.advance(2, "36 BB")

# Pitching change (NYY): #67 A.J. Cole replaces #71 Stephen Tarpley
b6.pitching_substitution(67)

# 6. BOS #36 Eduardo Núñez (X - 23 - 18)
b6.new_ab(is_risp=True)
b6.pitch_list("c b b c f d d")
b6.reach("BB")
# Offensive change (BOS): Pinch-runner #11 Rafael Devers replaces #36 Eduardo Núñez
b6.offensive_substitution(6, 11, "PR")
b6.atbase("PR")

# 7. BOS #5  Ian Kinsler (23 - 59 - 36)
b6.new_ab(is_risp=True)
b6.pitch_list("t f b")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #70 Ryan Brasier
t7 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #32 Matt Barnes, batting 7th
t7.pitching_substitution(70)
t7.defensive_substitution(7, 70, "1")

# Defensive switch (BOS): #0 Brandon Phillips moves to 2B
t7.defensive_switch(0, "4")

# Defensive switch (BOS): #59 Sam Travis moves to 1B
t7.defensive_switch(59, "3")

# Defensive switch (BOS): #11 Rafael Devers moves to 3B
t7.defensive_switch(11, "5")

# 7. NYY #25 Gleyber Torres (X - X - X)
t7.new_ab()
t7.out("F7")

# 8. NYY #14 Neil Walker (X - X - X)
t7.new_ab()
t7.pitch_list("c s b f b b b")
t7.reach("BB")

# 9. NYY #29 Adeiny Hechavarría (X - X - 14)
t7.new_ab()
t7.pitch_list("b f f s")
t7.out("K")

# 1. NYY #11 Brett Gardner (X - X - 14)
t7.new_ab()
t7.pitch_list("b f c")
t7.out("L5")


# Bot 7th
# Pitching: NYY #67 A.J. Cole
b7 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("b c c f")
b7.out("F9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("c s b b f")
b7.hit(2)

# 1. BOS #30 Tzu-Wei Lin (X - 19 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c b c f s")
b7.out("K")

# 2. BOS #12 Brock Holt (X - 19 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b c c f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #31 Drew Pomeranz
t8 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #70 Ryan Brasier, batting 7th
t8.pitching_substitution(31)
t8.defensive_substitution(7, 31, "1")

# 2. NYY #74 Ronald Torreyes (X - X - X)
t8.new_ab()
t8.pitch_list("c b f s")
t8.out("K")

# 3. NYY #12 Tyler Wade (X - X - X)
t8.new_ab()
t8.pitch_list("c b c b f b")
t8.out("G6-3")

# 4. NYY #41 Miguel Andujar (X - X - X)
t8.new_ab()
t8.pitch_list("c b f t")
t8.out("KT")


# Bot 8th
# Pitching: NYY #43 Chance Adams
b8 = game.new_inning()

# Pitching change (NYY): #43 Chance Adams replaces #67 A.J. Cole
b8.pitching_substitution(43)

# 3. BOS #0  Brandon Phillips (X - X - X)
b8.new_ab()
b8.pitch_list("b f b f f")
b8.out("F8")

# 4. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("f b s b b f t")
b8.out("KT")

# 5. BOS #59 Sam Travis (X - X - X)
b8.new_ab()
b8.pitch_list("b c b b")
b8.hit(2)

# 6. BOS #11 Rafael Devers (X - 59 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b c c f b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #31 Drew Pomeranz, batting 7th
t9.pitching_substitution(46)
t9.defensive_substitution(7, 46, "1")

# 5. NYY #45 Luke Voit (X - X - X)
t9.new_ab()
t9.pitch_list("f b s f b f c")
t9.out("!K")

# 6. NYY #66 Kyle Higashioka (X - X - X)
t9.new_ab()
t9.pitch_list("c s s")
t9.out("K2-3")

# 7. NYY #25 Gleyber Torres (X - X - X)
t9.new_ab()
t9.pitch_list("c b f b f s")
t9.out("K")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57)

# Loser team: NYY
# LP: NYY #85 Luis Cessa
game.losing_pitcher(85, is_away_team=True)

# print(game)
game.generate_scorecard()
