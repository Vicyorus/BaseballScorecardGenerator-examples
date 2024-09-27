import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2018-09-28
# https://www.baseball-reference.com/boxes/BOS/BOS201809280.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2018/09/28/531801/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-28 19:11-22:38",
        "at": "Fenway Park, Boston, MA",
        "att": "36,779",
        "temp": "60F, Cloudy",
        "wind": "5mph, In From RF",
        "away": {
            "team": "New York Yankees",
            "starter": 34,
            "roster": {
                # Lineup
                26: "Andrew McCutchen",
                99: "Aaron Judge",
                31: "Aaron Hicks",
                27: "Giancarlo Stanton",
                45: "Luke Voit",
                18: "Didi Gregorius",
                41: "Miguel Andujar",
                24: "Gary Sánchez",
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
                14: "Neil Walker",
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
                54: "Aroldis Chapman",
            },
            "lefties": [34, 52, 53, 71, 61, 54],
            "lineup": [
                [26, "7"],
                [99, "9"],
                [31, "8"],
                [27, "0"],
                [45, "3"],
                [18, "6"],
                [41, "5"],
                [24, "2"],
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
            "bullpen": [67, 68, 40, 65, 36, 43, 38, 55, 56, 52, 53, 19, 57, 48, 85, 71, 30, 61, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 61,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                25: "Steve Pearce",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                5: "Ian Kinsler",
                23: "Blake Swihart",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                30: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                12: "Brock Holt",
                59: "Sam Travis",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
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
            "lefties": [61, 57, 41, 31, 66, 63, 24],
            "lineup": [
                [50, "8"],
                [16, "7"],
                [28, "9"],
                [2, "6"],
                [25, "3"],
                [11, "5"],
                [36, "0"],
                [5, "4"],
                [23, "2"],
            ],
            "bench": [
                [30, "OF"],
                [18, "1B"],
                [12, "2B"],
                [59, "1B"],
                [19, "CF"],
                [3, "C"],
                [0, "2B"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 41, 31, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Laz Diaz",
            "1B": "Manny Gonzalez",
            "2B": "Andy Fletcher",
            "3B": "Jeff Nelson",
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
# Pitching: BOS #61 Brian Johnson
t1 = game.new_inning()

# 1. NYY #26 Andrew McCutchen (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("L5")

# 2. NYY #99 Aaron Judge (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("F9")

# 3. NYY #31 Aaron Hicks (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.out("P3")


# Bot 1st
# Pitching: NYY #34 J.A. Happ
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c c f c")
b1.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b s b c s")
b1.out("K")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #61 Brian Johnson
t2 = game.new_inning()

# 4. NYY #27 Giancarlo Stanton (X - X - X)
t2.new_ab()
t2.pitch_list("f b b f")
t2.out("F8")

# 5. NYY #45 Luke Voit (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c b")
t2.reach("BB")
t2.thrown_out(2, "18 FC4-6", 2, 61)

# 6. NYY #18 Didi Gregorius (X - X - 45)
t2.new_ab()
t2.pitch_list("b f f f d f f b")
t2.reach("FC4-6")

# 7. NYY #41 Miguel Andujar (X - X - 18)
t2.new_ab()
t2.pitch_list("b 1 b f s 1")
t2.out("L9")


# Bot 2nd
# Pitching: NYY #34 J.A. Happ
b2 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("c b c b f")
b2.out("F8")

# 5. BOS #25 Steve Pearce (X - X - X)
b2.new_ab()
b2.pitch_list("s s f c")
b2.out("!K")

# 6. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #61 Brian Johnson
t3 = game.new_inning()

# 8. NYY #24 Gary Sánchez (X - X - X)
t3.new_ab()
t3.pitch_list("b b")
t3.hit(4)

# 9. NYY #25 Gleyber Torres (X - X - X)
t3.new_ab()
t3.pitch_list("c b c s")
t3.out("K")

# 1. NYY #26 Andrew McCutchen (X - X - X)
t3.new_ab()
t3.pitch_list("b b c c b s")
t3.out("K")

# 2. NYY #99 Aaron Judge (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c s b")
t3.reach("BB")
t3.advance(2, "31 1B")
t3.advance(4, "27 1B")

# 3. NYY #31 Aaron Hicks (X - X - 99)
t3.new_ab()
t3.pitch_list("c f 1 1 d")
t3.hit(1)
t3.advance(3, "27 1B")

# 4. NYY #27 Giancarlo Stanton (X - 99 - 31)
t3.new_ab()
t3.pitch_list("s b f")
t3.hit(1, rbis=1)

# 5. NYY #45 Luke Voit (31 - X - 27)
t3.new_ab()
t3.pitch_list("b c c d b f")
t3.out("F9")


# Bot 3rd
# Pitching: NYY #34 J.A. Happ
b3 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b3.new_ab()
b3.pitch_list("b s f b f")
b3.out("G4-3")

# 8. BOS #5  Ian Kinsler (X - X - X)
b3.new_ab()
b3.pitch_list("f b")
b3.out("L7")

# 9. BOS #23 Blake Swihart (X - X - X)
b3.new_ab()
b3.pitch_list("c b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #67 William Cuevas
t4 = game.new_inning()

# Pitching change (BOS): #67 William Cuevas replaces #61 Brian Johnson
t4.pitching_substitution(67)

# 6. NYY #18 Didi Gregorius (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c")
t4.out("L8")

# 7. NYY #41 Miguel Andujar (X - X - X)
t4.new_ab()
t4.pitch_list("c f")
t4.hit(2)
t4.advance(4, "25 2B")

# 8. NYY #24 Gary Sánchez (X - 41 - X)
t4.new_ab()
t4.pitch_list("s b b b c b")
t4.reach("BB")
t4.advance(4, "25 2B")

# 9. NYY #25 Gleyber Torres (X - 41 - 24)
t4.new_ab()
t4.pitch_list("b s f")
t4.hit(2, rbis=2)
t4.advance(4, "26 1B")

# 1. NYY #26 Andrew McCutchen (X - 25 - X)
t4.new_ab()
t4.pitch_list("c c b f b")
t4.hit(1, rbis=1)
t4.advance(2, "99 1B")
t4.advance(4, "31 HR")

# 2. NYY #99 Aaron Judge (X - X - 26)
t4.new_ab()
t4.pitch_list("b c c")
t4.hit(1)
t4.advance(4, "31 HR")

# 3. NYY #31 Aaron Hicks (X - 26 - 99)
t4.new_ab()
t4.pitch_list("d")
t4.hit(4, rbis=3)

# 4. NYY #27 Giancarlo Stanton (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)

# Pitching change (BOS): #37 Heath Hembree replaces #67 William Cuevas
t4.pitching_substitution(37)

# 5. NYY #45 Luke Voit (X - X - 27)
t4.new_ab()
t4.out("F9")

# 6. NYY #18 Didi Gregorius (X - X - 27)
t4.new_ab()
t4.pitch_list("f d b")
t4.out("F9")


# Bot 4th
# Pitching: NYY #34 J.A. Happ
b4 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b b")
b4.reach("BB")
b4.advance(3, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.thrown_out(2, "25 FC6-4", 3, 34)

# 3. BOS #28 J.D. Martinez (50 - X - 16)
b4.new_ab()
b4.pitch_list("f")
b4.out("(F)F9")

# 4. BOS #2  Xander Bogaerts (50 - X - 16)
b4.new_ab()
b4.pitch_list("c f s")
b4.out("K")

# 5. BOS #25 Steve Pearce (50 - X - 16)
b4.new_ab()
b4.pitch_list("b c b")
b4.reach("FC6-4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Drew Pomeranz
t5 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #37 Heath Hembree
t5.pitching_substitution(31)

# 7. NYY #41 Miguel Andujar (X - X - X)
t5.new_ab()
t5.pitch_list("b c b f b")
t5.out("L3")

# 8. NYY #24 Gary Sánchez (X - X - X)
t5.new_ab()
t5.pitch_list("c s f s")
t5.out("K")

# 9. NYY #25 Gleyber Torres (X - X - X)
t5.new_ab()
t5.pitch_list("b b s c")
t5.out("G6-3")


# Bot 5th
# Pitching: NYY #34 J.A. Happ
b5 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.pitch_list("b s")
b5.out("G6-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.out("G3")

# 8. BOS #5  Ian Kinsler (X - X - X)
b5.new_ab()
b5.pitch_list("c b b b f f f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Drew Pomeranz
t6 = game.new_inning()

# 1. NYY #26 Andrew McCutchen (X - X - X)
t6.new_ab()
t6.out("G5-3")

# 2. NYY #99 Aaron Judge (X - X - X)
t6.new_ab()
t6.pitch_list("c b f c")
t6.out("!K")

# 3. NYY #31 Aaron Hicks (X - X - X)
t6.new_ab()
t6.pitch_list("b c c f c")
t6.out("!K")


# Bot 6th
# Pitching: NYY #34 J.A. Happ
b6 = game.new_inning()

# 9. BOS #23 Blake Swihart (X - X - X)
b6.new_ab()
b6.pitch_list("c f b s")
b6.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("c b b c")
b6.hit(1)
b6.advance(3, "16 2B")
b6.advance(4, "25 HR")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b6.new_ab()
b6.hit(2)
b6.advance(4, "25 HR")

# 3. BOS #28 J.D. Martinez (50 - 16 - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("(F)P3")

# 4. BOS #2  Xander Bogaerts (50 - 16 - X)
b6.new_ab()
b6.pitch_list("b d b b")
b6.reach("BB")
b6.advance(4, "25 HR")

# 5. BOS #25 Steve Pearce (50 - 16 - 2)
b6.new_ab()
b6.hit(4, rbis=4)

# 6. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("c b f")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #31 Drew Pomeranz
t7 = game.new_inning()

# 4. NYY #27 Giancarlo Stanton (X - X - X)
t7.new_ab()
t7.pitch_list("c c b b s")
t7.out("K")

# 5. NYY #45 Luke Voit (X - X - X)
t7.new_ab()
t7.hit(4)

# 6. NYY #18 Didi Gregorius (X - X - X)
t7.new_ab()
t7.pitch_list("c b s b")
t7.hit(1)
t7.advance(2, "41 BB")
t7.error(6)
t7.advance(3, "24 FC6")
t7.advance("U", "24 E6")

# 7. NYY #41 Miguel Andujar (X - X - 18)
t7.new_ab()
t7.pitch_list("c b f f f d b b")
t7.reach("BB")
t7.advance(3, "24 E6")

# Pitching change (BOS): #56 Joe Kelly replaces #31 Drew Pomeranz
t7.pitching_substitution(56)

# 8. NYY #24 Gary Sánchez (X - 18 - 41)
t7.new_ab()
t7.pitch_list("b b b c")
t7.reach("FC6")
t7.thrown_out(2, "26 FC4-6", 3, 56)

# 9. NYY #25 Gleyber Torres (41 - X - 24)
t7.new_ab()
t7.pitch_list("b s d c c")
t7.out("!K")

# 1. NYY #26 Andrew McCutchen (41 - X - 24)
t7.new_ab()
t7.pitch_list("b b s c")
t7.reach("FC4-6")


# Bot 7th
# Pitching: NYY #57 Chad Green
b7 = game.new_inning()

# Pitching change (NYY): #57 Chad Green replaces #34 J.A. Happ
b7.pitching_substitution(57)

# 7. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("c b b")
b7.out("L8")

# 8. BOS #5  Ian Kinsler (X - X - X)
b7.new_ab()
b7.pitch_list("f f f b f f f")
b7.out("F9")

# 9. BOS #23 Blake Swihart (X - X - X)
b7.new_ab()
b7.pitch_list("s f b b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #66 Bobby Poyner
t8 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #56 Joe Kelly
t8.pitching_substitution(66)

# 2. NYY #99 Aaron Judge (X - X - X)
t8.new_ab()
t8.hit(4)

# 3. NYY #31 Aaron Hicks (X - X - X)
t8.new_ab()
t8.out("F9")

# 4. NYY #27 Giancarlo Stanton (X - X - X)
t8.new_ab()
t8.pitch_list("c b s f f f")
t8.out("F9")

# 5. NYY #45 Luke Voit (X - X - X)
t8.new_ab()
t8.pitch_list("s b b c f f f b s")
t8.out("K")


# Bot 8th
# Pitching: NYY #68 Dellin Betances
b8 = game.new_inning()

# Pitching change (NYY): #68 Dellin Betances replaces #57 Chad Green
b8.pitching_substitution(68)

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("c b c b b b")
b8.reach("BB")
b8.advance(2, "28 1B")
b8.advance(4, "25 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b8.new_ab()
b8.pitch_list("c f f s")
b8.out("K")

# 3. BOS #28 J.D. Martinez (X - X - 50)
b8.new_ab()
b8.pitch_list("c s")
b8.hit(1)
b8.advance(2, "25 1B")
b8.advance(3, "11 BB")

# 4. BOS #2  Xander Bogaerts (X - 50 - 28)
b8.new_ab()
b8.pitch_list("b c b f")
b8.out("IF5")

# 5. BOS #25 Steve Pearce (X - 50 - 28)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1, rbis=1)
b8.advance(2, "11 BB")

# 6. BOS #11 Rafael Devers (X - 28 - 25)
b8.new_ab()
b8.pitch_list("b b b c b")
b8.reach("BB")

# 7. BOS #36 Eduardo Núñez (28 - 25 - 11)
b8.new_ab()
b8.pitch_list("f f b f")
b8.out("L4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #66 Bobby Poyner
t9 = game.new_inning()

# Defensive switch (BOS): #50 Mookie Betts moves to RF
t9.defensive_switch(50, "9")

# Defensive change (BOS): #30 Tzu-Wei Lin replaces #28 J.D. Martinez (RF), playing CF, batting 3rd
t9.defensive_substitution(3, 30, "8")

# 6. NYY #18 Didi Gregorius (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.out("L9")

# 7. NYY #41 Miguel Andujar (X - X - X)
t9.new_ab()
t9.pitch_list("f b")
t9.out("P3")

# 8. NYY #24 Gary Sánchez (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.hit(2)

# 9. NYY #25 Gleyber Torres (X - 24 - X)
t9.new_ab()
t9.pitch_list("f f s")
t9.out("K")


# Bot 9th
# Pitching: NYY #53 Zack Britton
b9 = game.new_inning()

# Pitching change (NYY): #53 Zack Britton replaces #68 Dellin Betances
b9.pitching_substitution(53)

# 8. BOS #5  Ian Kinsler (X - X - X)
b9.new_ab()
b9.pitch_list("b b b b")
b9.reach("BB")
b9.thrown_out(2, "59 FC5-4", 1, 53)

# Offensive change (BOS): Pinch-hitter #59 Sam Travis replaces #23 Blake Swihart, batting 9th
b9.offensive_substitution(9, 59, "PH")

# 9. BOS #59 Sam Travis (X - X - 5)
b9.new_ab()
b9.pitch_list("d c d")
b9.reach("FC5-4")
b9.error(6)
b9.advance(2, "50 FC6")
b9.advance(3, "50 E6")
b9.advance("U", "2 BB")

# 1. BOS #50 Mookie Betts (X - X - 59)
b9.new_ab()
b9.pitch_list("c d")
b9.reach("FC6")
b9.advance(2, "E6")
b9.advance(3, "2 BB")

# 2. BOS #16 Andrew Benintendi (59 - 50 - X)
b9.new_ab()
b9.pitch_list("f")
b9.out("L6")

# Offensive change (BOS): Pinch-hitter #7 Christian Vázquez replaces #30 Tzu-Wei Lin, batting 3rd
b9.offensive_substitution(3, 7, "PH")

# 3. BOS #7  Christian Vázquez (59 - 50 - X)
b9.new_ab()
b9.pitch_list("b b b c c d")
b9.reach("BB")
b9.advance(2, "2 BB")

# 4. BOS #2  Xander Bogaerts (59 - 50 - 7)
b9.new_ab()
b9.pitch_list("b b c b b")
b9.reach("BB", rbis=1)

# 5. BOS #25 Steve Pearce (50 - 7 - 2)
b9.new_ab()
b9.pitch_list("b d c d c")
b9.out("G5-3")

# Winning team: NYY
# WP: NYY #34 J.A. Happ
game.winning_pitcher(34, is_away_team=True)

# Loser team: BOS
# LP: BOS #61 Brian Johnson
game.losing_pitcher(61)

# print(game)
game.generate_scorecard()
