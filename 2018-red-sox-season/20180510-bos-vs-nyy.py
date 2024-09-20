import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2018-05-10
# https://www.baseball-reference.com/boxes/NYA/NYA201805100.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2018/05/10/529963/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-10 19:09-23:25 (0:55 delay)",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "46,899",
        "temp": "62F, Partly Cloudy",
        "wind": "9mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Bullpen
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 24],
            "lineup": [
                [50, "8"],
                [16, "7"],
                [13, "0"],
                [28, "9"],
                [2, "6"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [7, "2"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [19, "CF"],
                [3, "C"],
            ],
            "bullpen": [39, 22, 41, 31, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 52,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                99: "Aaron Judge",
                18: "Didi Gregorius",
                27: "Giancarlo Stanton",
                24: "Gary Sánchez",
                26: "Tyler Austin",
                41: "Miguel Andujar",
                25: "Gleyber Torres",
                74: "Ronald Torreyes",
                # Starting pitcher
                52: "CC Sabathia",
                # Bench
                28: "Austin Romine",
                31: "Aaron Hicks",
                14: "Neil Walker",
                # Bullpen
                67: "A.J. Cole",
                68: "Dellin Betances",
                40: "Luis Severino",
                45: "Chasen Shreve",
                65: "Domingo Germán",
                55: "Sonny Gray",
                56: "Jonathan Holder",
                19: "Masahiro Tanaka",
                57: "Chad Green",
                61: "David Hale",
                30: "David Robertson",
                54: "Aroldis Chapman",
            },
            "lefties": [52, 45, 54],
            "lineup": [
                [11, "8"],
                [99, "9"],
                [18, "6"],
                [27, "7"],
                [24, "2"],
                [26, "3"],
                [41, "0"],
                [25, "4"],
                [74, "5"],
            ],
            "bench": [
                [28, "C"],
                [31, "RF"],
                [14, "2B"],
            ],
            "bullpen": [67, 68, 40, 45, 65, 55, 56, 19, 57, 61, 30, 54],
        },
        "umpires": {
            "HP": "Stu Scheurwater",
            "1B": "Eric Cooper",
            "2B": "Gary Cederstrom",
            "3B": "Cory Blaser",
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
# Pitching: NYY #52 CC Sabathia
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b f")
t1.hit(2)
t1.advance(3, "16 G3")
t1.advance(4, "13 G6-3")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t1.new_ab()
t1.out("G3")

# 3. BOS #13 Hanley Ramirez (50 - X - X)
t1.new_ab()
t1.pitch_list("b b s")
t1.out("G6-3", rbis=1)

# 4. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("b s f b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #57 Eduardo Rodriguez
b1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.out("F7")

# 2. NYY #99 Aaron Judge (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c b")
b1.reach("BB")

# 3. NYY #18 Didi Gregorius (X - X - 99)
b1.new_ab()
b1.pitch_list("b b f b")
b1.out("F7")

# 4. NYY #27 Giancarlo Stanton (X - X - 99)
b1.new_ab()
b1.pitch_list("b c b s b f f")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #52 CC Sabathia
t2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c s s")
t2.out("K")

# 6. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("b f s b f s")
t2.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.hit(1)
t2.advance(2, "11 1B")

# 8. BOS #11 Rafael Devers (X - X - 36)
t2.new_ab()
t2.pitch_list("s c")
t2.hit(1)

# 9. BOS #7  Christian Vázquez (X - 36 - 11)
t2.new_ab()
t2.pitch_list("b c b")
t2.out("G5-3")


# Bot 2nd
# Pitching: BOS #57 Eduardo Rodriguez
b2 = game.new_inning()

# 5. NYY #24 Gary Sánchez (X - X - X)
b2.new_ab()
b2.pitch_list("b c b")
b2.out("G6-3")

# 6. NYY #26 Tyler Austin (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b f c")
b2.out("!K")

# 7. NYY #41 Miguel Andujar (X - X - X)
b2.new_ab()
b2.pitch_list("b c s c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #52 CC Sabathia
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b c f")
t3.hit(1)
t3.advance(3, "16 2B")
t3.advance(4, "13 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t3.new_ab()
t3.pitch_list("f f")
t3.hit(2)
t3.advance(3, "13 1B")
t3.advance(4, "28 FC4-6")

# 3. BOS #13 Hanley Ramirez (50 - 16 - X)
t3.new_ab()
t3.pitch_list("f b f b b")
t3.hit(1, rbis=1)
t3.thrown_out(2, "28 FC4-6", 1, 52)

# 4. BOS #28 J.D. Martinez (16 - X - 13)
t3.new_ab()
t3.pitch_list("s b s b f f f")
t3.reach("FC4-6", rbis=1)
t3.advance(2, "2 1B")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t3.new_ab()
t3.pitch_list("c")
t3.hit(1)
t3.thrown_out(2, "36 FC6", 3, 52)

# 6. BOS #18 Mitch Moreland (X - 28 - 2)
t3.new_ab()
t3.pitch_list("t b c s")
t3.out("K")

# 7. BOS #36 Eduardo Núñez (X - 28 - 2)
t3.new_ab()
t3.reach("FC6")


# Bot 3rd
# Pitching: BOS #57 Eduardo Rodriguez
b3 = game.new_inning()

# 8. NYY #25 Gleyber Torres (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c f c")
b3.out("!K")

# 9. NYY #74 Ronald Torreyes (X - X - X)
b3.new_ab()
b3.pitch_list("c f s")
b3.out("K")

# 1. NYY #11 Brett Gardner (X - X - X)
b3.new_ab()
b3.pitch_list("c b b c c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #52 CC Sabathia
t4 = game.new_inning()

# 8. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("s")
t4.out("G4-3")

# 9. BOS #7  Christian Vázquez (X - X - X)
t4.new_ab()
t4.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)
t4.advance(2, "16 SB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t4.new_ab()
t4.pitch_list("b 1 c s f b b s")
t4.out("K")


# Bot 4th
# Pitching: BOS #57 Eduardo Rodriguez
b4 = game.new_inning()

# 2. NYY #99 Aaron Judge (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c b")
b4.reach("BB")
b4.advance(2, "27 1B")
b4.advance(3, "24 BB")

# 3. NYY #18 Didi Gregorius (X - X - 99)
b4.new_ab()
b4.pitch_list("b b f f")
b4.out("P4")

# 4. NYY #27 Giancarlo Stanton (X - X - 99)
b4.new_ab()
b4.hit(1)
b4.advance(2, "24 BB")

# 5. NYY #24 Gary Sánchez (X - 99 - 27)
b4.new_ab()
b4.pitch_list("f c b b b f b")
b4.reach("BB")

# 6. NYY #26 Tyler Austin (99 - 27 - 24)
b4.new_ab()
b4.pitch_list("b d s s c")
b4.out("!K")

# 7. NYY #41 Miguel Andujar (99 - 27 - 24)
b4.new_ab()
b4.pitch_list("f f f")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #52 CC Sabathia
t5 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
t5.new_ab()
t5.pitch_list("c f f b b")
t5.hit(4)

# Pitching change (NYY): #56 Jonathan Holder replaces #52 CC Sabathia
t5.pitching_substitution(56)

# 4. BOS #28 J.D. Martinez (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("b c f c")
t5.out("!K")

# 6. BOS #18 Mitch Moreland (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G1-3")


# Bot 5th
# Pitching: BOS #57 Eduardo Rodriguez
b5 = game.new_inning()

# 8. NYY #25 Gleyber Torres (X - X - X)
b5.new_ab()
b5.pitch_list("b s f b f c")
b5.out("!K")

# 9. NYY #74 Ronald Torreyes (X - X - X)
b5.new_ab()
b5.pitch_list("c b c b b f s")
b5.out("K")

# 1. NYY #11 Brett Gardner (X - X - X)
b5.new_ab()
b5.pitch_list("c s")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #56 Jonathan Holder
t6 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("c s")
t6.out("F9")

# 8. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("c s b t")
t6.out("KT")

# 9. BOS #7  Christian Vázquez (X - X - X)
t6.new_ab()
t6.pitch_list("s f")
t6.out("F8")


# Bot 6th
# Pitching: BOS #32 Matt Barnes
b6 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #57 Eduardo Rodriguez
b6.pitching_substitution(32)

# 2. NYY #99 Aaron Judge (X - X - X)
b6.new_ab()
b6.pitch_list("c b b f b b")
b6.reach("BB")

# 3. NYY #18 Didi Gregorius (X - X - 99)
b6.new_ab()
b6.pitch_list("b")
b6.out("L7")

# 4. NYY #27 Giancarlo Stanton (X - X - 99)
b6.new_ab()
b6.pitch_list("b")
b6.out("P6")

# 5. NYY #24 Gary Sánchez (X - X - 99)
b6.new_ab()
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #68 Dellin Betances
t7 = game.new_inning()

# Pitching change (NYY): #68 Dellin Betances replaces #56 Jonathan Holder
t7.pitching_substitution(68)

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.out("(F)F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("s b c")
t7.out("G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t7.new_ab()
t7.pitch_list("b c f f c")
t7.out("!K")


# Bot 7th
# Pitching: BOS #37 Heath Hembree
b7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #32 Matt Barnes
b7.pitching_substitution(37)

# 6. NYY #26 Tyler Austin (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F9")

# 7. NYY #41 Miguel Andujar (X - X - X)
b7.new_ab()
b7.hit(1)
b7.advance(3, "25 1B")
b7.advance(4, "11 BB")

# 8. NYY #25 Gleyber Torres (X - X - 41)
b7.new_ab()
b7.pitch_list("s s f b f")
b7.hit(1)
b7.advance(2, "14 BB")
b7.advance(3, "11 BB")
b7.advance(4, "99 1B")

# Offensive change (NYY): Pinch-hitter #14 Neil Walker replaces #74 Ronald Torreyes, batting 9th
b7.offensive_substitution(9, 14, "PH")

# 9. NYY #14 Neil Walker (41 - X - 25)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.advance(2, "11 BB")
b7.advance(3, "99 1B")
b7.advance(4, "18 FC4-6")

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
b7.pitching_substitution(56)

# 1. NYY #11 Brett Gardner (41 - 25 - 14)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB", rbis=1)
b7.advance(2, "99 1B")
b7.advance(3, "18 FC4-6")
b7.advance(4, "27 WP")

# 2. NYY #99 Aaron Judge (25 - 14 - 11)
b7.new_ab()
b7.pitch_list("b")
b7.hit(1, rbis=1)
b7.thrown_out(2, "18 FC4-6", 2, 56)

# 3. NYY #18 Didi Gregorius (14 - 11 - 99)
b7.new_ab()
b7.reach("FC4-6", rbis=1)
b7.advance(2, "27 WP")

# 4. NYY #27 Giancarlo Stanton (11 - X - 18)
b7.new_ab()
b7.pitch_list("b")
b7.wp()
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #68 Dellin Betances
t8 = game.new_inning()

# Defensive switch (NYY): #14 Neil Walker moves to 3B
t8.defensive_switch(14, "5")

# 4. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(4)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("b b s b c f f s")
t8.out("K")

# 6. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("b c f b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# 5. NYY #24 Gary Sánchez (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c b")
b8.reach("BB")
b8.advance(2, "25 1B")

# 6. NYY #26 Tyler Austin (X - X - 24)
b8.new_ab()
b8.out("F7")

# 7. NYY #41 Miguel Andujar (X - X - 24)
b8.new_ab()
b8.pitch_list("b f 1 f s")
b8.out("K")

# 8. NYY #25 Gleyber Torres (X - X - 24)
b8.new_ab()
b8.pitch_list("c 1")
b8.hit(1)

# 9. NYY #14 Neil Walker (X - 24 - 25)
b8.new_ab()
b8.pitch_list("c f b d f c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #45 Chasen Shreve
t9 = game.new_inning()

# Pitching change (NYY): #45 Chasen Shreve replaces #68 Dellin Betances
t9.pitching_substitution(45)

# 8. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("s f f b")
t9.out("L7")

# 9. BOS #7  Christian Vázquez (X - X - X)
t9.new_ab()
t9.pitch_list("c f b")
t9.out("G5-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("b b c b b")
t9.reach("BB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t9.new_ab()
t9.pitch_list("b b 1 t 1 s s")
t9.out("K")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
b9.pitching_substitution(46)

# 1. NYY #11 Brett Gardner (X - X - X)
b9.new_ab()
b9.pitch_list("b c b s b s")
b9.out("K")

# 2. NYY #99 Aaron Judge (X - X - X)
b9.new_ab()
b9.pitch_list("b b c s")
b9.out("F8")

# 3. NYY #18 Didi Gregorius (X - X - X)
b9.new_ab()
b9.pitch_list("f")
b9.out("G1-3")

# Winning team: BOS
# WP: BOS #56 Joe Kelly
game.winning_pitcher(56, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: NYY
# LP: NYY #68 Dellin Betances
game.losing_pitcher(68)

# print(game)
game.generate_scorecard()
