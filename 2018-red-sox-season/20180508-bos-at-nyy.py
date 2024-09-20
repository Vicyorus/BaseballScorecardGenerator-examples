import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2018-05-08
# https://www.baseball-reference.com/boxes/NYA/NYA201805080.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2018/05/08/529935/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-08 19:11-22:40",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "45,773",
        "temp": "66F, Clear",
        "wind": "8mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
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
                31: "Drew Pomeranz",
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
            "bullpen": [57, 39, 22, 41, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 40,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                99: "Aaron Judge",
                18: "Didi Gregorius",
                27: "Giancarlo Stanton",
                24: "Gary Sánchez",
                31: "Aaron Hicks",
                41: "Miguel Andujar",
                26: "Tyler Austin",
                25: "Gleyber Torres",
                # Starting pitcher
                40: "Luis Severino",
                # Bench
                28: "Austin Romine",
                74: "Ronald Torreyes",
                14: "Neil Walker",
                # Bullpen
                67: "A.J. Cole",
                68: "Dellin Betances",
                45: "Chasen Shreve",
                65: "Domingo Germán",
                55: "Sonny Gray",
                56: "Jonathan Holder",
                52: "CC Sabathia",
                19: "Masahiro Tanaka",
                57: "Chad Green",
                61: "David Hale",
                30: "David Robertson",
                54: "Aroldis Chapman",
            },
            "lefties": [45, 52, 54],
            "lineup": [
                [11, "7"],
                [99, "9"],
                [18, "6"],
                [27, "0"],
                [24, "2"],
                [31, "8"],
                [41, "5"],
                [26, "3"],
                [25, "4"],
            ],
            "bench": [
                [28, "C"],
                [74, "SS"],
                [14, "2B"],
            ],
            "bullpen": [67, 68, 45, 65, 55, 56, 52, 19, 57, 61, 30, 54],
        },
        "umpires": {
            "HP": "Gary Cederstrom",
            "1B": "Cory Blaser",
            "2B": "Stu Scheurwater",
            "3B": "Eric Cooper",
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
t1.pitch_list("c")
t1.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("f b f f b")
t1.out("P5")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("c b b f")
t1.error(4)
t1.reach("E4")

# 4. BOS #28 J.D. Martinez (X - X - 13)
t1.new_ab()
t1.pitch_list("b f s s")
t1.out("K")


# Bot 1st
# Pitching: BOS #31 Drew Pomeranz
b1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b1.new_ab()
b1.pitch_list("b c c s")
b1.out("K")

# 2. NYY #99 Aaron Judge (X - X - X)
b1.new_ab()
b1.pitch_list("f b b b c")
b1.out("F9")

# 3. NYY #18 Didi Gregorius (X - X - X)
b1.new_ab()
b1.pitch_list("b b s b f")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #40 Luis Severino
t2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c f s")
t2.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("c b s s")
t2.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b c f b")
t2.hit(2)

# 8. BOS #19 Jackie Bradley Jr. (X - 36 - X)
t2.new_ab()
t2.pitch_list("f s f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #31 Drew Pomeranz
b2 = game.new_inning()

# 4. NYY #27 Giancarlo Stanton (X - X - X)
b2.new_ab()
b2.pitch_list("c b s b f b")
b2.hit(4)

# 5. NYY #24 Gary Sánchez (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c b")
b2.reach("BB")
b2.advance(2, "31 BB")

# 6. NYY #31 Aaron Hicks (X - X - 24)
b2.new_ab()
b2.pitch_list("b b b c b")
b2.reach("BB")

# 7. NYY #41 Miguel Andujar (X - 24 - 31)
b2.new_ab()
b2.pitch_list("c f b s")
b2.out("K")

# 8. NYY #26 Tyler Austin (X - 24 - 31)
b2.new_ab()
b2.pitch_list("f b b f b f s")
b2.out("K")

# 9. NYY #25 Gleyber Torres (X - 24 - 31)
b2.new_ab()
b2.pitch_list("c b b")
b2.out("P6")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #40 Luis Severino
t3 = game.new_inning()

# 9. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b f")
t3.hit(1)
t3.thrown_out(2, "9-6", 1, 40)

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c s s")
t3.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("f c s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #31 Drew Pomeranz
b3 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b3.new_ab()
b3.pitch_list("b c c s")
b3.out("K")

# 2. NYY #99 Aaron Judge (X - X - X)
b3.new_ab()
b3.pitch_list("c s f f s")
b3.out("K")

# 3. NYY #18 Didi Gregorius (X - X - X)
b3.new_ab()
b3.pitch_list("b f b s b f")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #40 Luis Severino
t4 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("f")
t4.out("G1-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(2)

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("F7")

# 6. BOS #11 Rafael Devers (X - 28 - X)
t4.new_ab()
t4.out("G5-3")


# Bot 4th
# Pitching: BOS #31 Drew Pomeranz
b4 = game.new_inning()

# 4. NYY #27 Giancarlo Stanton (X - X - X)
b4.new_ab()
b4.pitch_list("c b b")
b4.hit(4)

# 5. NYY #24 Gary Sánchez (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G4-3")

# 6. NYY #31 Aaron Hicks (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.out("L8")

# 7. NYY #41 Miguel Andujar (X - X - X)
b4.new_ab()
b4.pitch_list("f b b b f")
b4.hit(1)

# 8. NYY #26 Tyler Austin (X - X - 41)
b4.new_ab()
b4.pitch_list("b")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #40 Luis Severino
t5 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("b c c b f s")
t5.wp()
t5.reach("K")
t5.advance(2, "50 1B")
t5.advance(4, "16 1B")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 36)
t5.new_ab()
t5.pitch_list("b 1 s s c")
t5.out("!K")

# 9. BOS #7  Christian Vázquez (X - X - 36)
t5.new_ab()
t5.pitch_list("c f 1 b f s")
t5.out("K")

# 1. BOS #50 Mookie Betts (X - X - 36)
t5.new_ab()
t5.pitch_list("b b c")
t5.hit(1)
t5.advance(3, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - 36 - 50)
t5.new_ab()
t5.pitch_list("c f f b d b")
t5.hit(1, rbis=1)
t5.advance(2, "T")

# 3. BOS #13 Hanley Ramirez (50 - 16 - X)
t5.new_ab()
t5.pitch_list("b d d f f")
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #31 Drew Pomeranz
b5 = game.new_inning()

# 9. NYY #25 Gleyber Torres (X - X - X)
b5.new_ab()
b5.pitch_list("f b")
b5.hit(1)
b5.thrown_out(2, "11 DP6-3", 1, 31)

# 1. NYY #11 Brett Gardner (X - X - 25)
b5.new_ab()
b5.pitch_list("b")
b5.out("DP6-3")

# 2. NYY #99 Aaron Judge (X - X - X)
b5.new_ab()
b5.pitch_list("b s f b b f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #40 Luis Severino
t6 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("s c s")
t6.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("s b b b f f")
t6.out("P4")

# 6. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("f b s s")
t6.out("K")


# Bot 6th
# Pitching: BOS #31 Drew Pomeranz
b6 = game.new_inning()

# 3. NYY #18 Didi Gregorius (X - X - X)
b6.new_ab()
b6.pitch_list("c b f f f")
b6.out("G4-3")

# 4. NYY #27 Giancarlo Stanton (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G5-3")

# 5. NYY #24 Gary Sánchez (X - X - X)
b6.new_ab()
b6.pitch_list("b f c b")
b6.error(5)
b6.reach("E5", end_base=2)

# 6. NYY #31 Aaron Hicks (X - 24 - X)
b6.new_ab()
b6.out("P4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #40 Luis Severino
t7 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t7.new_ab()
t7.pitch_list("f f b f b f f f b")
t7.hit(1)
t7.advance(2, "50 SB")
t7.advance(4, "50 3B")

# Pitching change (NYY): #30 David Robertson replaces #40 Luis Severino
t7.pitching_substitution(30)

# 8. BOS #19 Jackie Bradley Jr. (X - X - 36)
t7.new_ab()
t7.pitch_list("c 1 d c 1 b 1 s")
t7.out("K")

# 9. BOS #7  Christian Vázquez (X - X - 36)
t7.new_ab()
t7.pitch_list("d f 1 f b")
t7.out("F8")

# 1. BOS #50 Mookie Betts (X - X - 36)
t7.new_ab()
t7.pitch_list("f s b f d")
t7.hit(3, rbis=1)

# 2. BOS #16 Andrew Benintendi (50 - X - X)
t7.new_ab()
t7.pitch_list("b b b c c s")
t7.out("K")


# Bot 7th
# Pitching: BOS #37 Heath Hembree
b7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #31 Drew Pomeranz
b7.pitching_substitution(37)

# 7. NYY #41 Miguel Andujar (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G6-3")

# Offensive change (NYY): Pinch-hitter #14 Neil Walker replaces #26 Tyler Austin, batting 8th
b7.offensive_substitution(8, 14, "PH")

# 8. NYY #14 Neil Walker (X - X - X)
b7.new_ab()
b7.pitch_list("b c f b b")
b7.hit(2)
b7.advance(3, "11 BLK")
b7.advance(4, "99 1B")

# 9. NYY #25 Gleyber Torres (X - 14 - X)
b7.new_ab()
b7.pitch_list("f b b s b b")
b7.reach("BB")
b7.advance(2, "11 BLK")
b7.thrown_out(4, "99 7-2", 2, 56)
b7.advance(3, "99 1B")

# 1. NYY #11 Brett Gardner (X - 14 - 25)
b7.new_ab()
b7.pitch_list("d f s b n d b")
b7.balk()
b7.reach("BB")
b7.advance(2, "99 7-2")

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
b7.pitching_substitution(56)

# 2. NYY #99 Aaron Judge (14 - 25 - 11)
b7.new_ab()
b7.pitch_list("f b")
b7.hit(1, rbis=1)

# 3. NYY #18 Didi Gregorius (X - 11 - 99)
b7.new_ab()
b7.out("G1-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #57 Chad Green
t8 = game.new_inning()

# Pitching change (NYY): #57 Chad Green replaces #30 David Robertson
t8.pitching_substitution(57)

# Defensive switch (NYY): #14 Neil Walker moves to 1B
t8.defensive_switch(14, "3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t8.new_ab()
t8.pitch_list("b f f b")
t8.hit(1)
t8.thrown_out(2, "2 DP4-6-3", 2, 57)

# 4. BOS #28 J.D. Martinez (X - X - 13)
t8.new_ab()
t8.pitch_list("b c b f")
t8.out("L8")

# 5. BOS #2  Xander Bogaerts (X - X - 13)
t8.new_ab()
t8.pitch_list("1")
t8.out("DP4-6-3")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# 4. NYY #27 Giancarlo Stanton (X - X - X)
b8.new_ab()
b8.pitch_list("c f b b b b")
b8.reach("BB")
b8.advance(2, "24 SB")
b8.advance(3, "31 WP")
b8.thrown_out(4, "31 FC3-2", 2, 56)

# 5. NYY #24 Gary Sánchez (X - X - 27)
b8.new_ab()
b8.pitch_list("c b b b s s")
b8.out("K2-3")

# 6. NYY #31 Aaron Hicks (X - 27 - X)
b8.new_ab()
b8.pitch_list("b b f b f")
b8.wp()
b8.reach("FC3-2")

# Pitching change (BOS): #39 Carson Smith replaces #56 Joe Kelly
b8.pitching_substitution(39)

# 7. NYY #41 Miguel Andujar (X - X - 31)
b8.new_ab()
b8.pitch_list("c f 1 1 1 b 1 s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #54 Aroldis Chapman
t9 = game.new_inning()

# Pitching change (NYY): #54 Aroldis Chapman replaces #57 Chad Green
t9.pitching_substitution(54)

# 6. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("f b b")
t9.out("G1-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("c b f s")
t9.out("K")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.reach("HBP")

# 9. BOS #7  Christian Vázquez (X - X - 19)
t9.new_ab()
t9.pitch_list("c d b c f 1")
t9.out("G4-3")

# Winning team: NYY
# WP: NYY #30 David Robertson
game.winning_pitcher(30)
# SV: NYY #54 Aroldis Chapman
game.save_pitcher(54)

# Loser team: BOS
# LP: BOS #37 Heath Hembree
game.losing_pitcher(37, is_away_team=True)

# print(game)
game.generate_scorecard()
